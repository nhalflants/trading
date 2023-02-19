import models
import yahooquery as yq
from schemas import StockRequest
from database import engine, SessionLocal, get_db
from fastapi import FastAPI, Request, Depends, BackgroundTasks
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

templates = Jinja2Templates(directory="templates")

@app.get("/")
def home(request: Request, forward_pe = None, dividend_yield = None, ma50 = None, ma200 = None, db: Session = Depends(get_db)):
    """
    show all stocks in the database and button to add more
    button next to each stock to delete from database
    filters to filter this list of stocks
    button next to each to add a note or save for later
    """
    
    stocks = db.query(models.Stock)
    if forward_pe:
        stocks = stocks.filter(models.Stock.forward_pe < forward_pe)

    if dividend_yield:
        stocks = stocks.filter(models.Stock.dividend_yield > dividend_yield)
    
    if ma50:
        stocks = stocks.filter(models.Stock.price > models.Stock.ma50)
    
    if ma200:
        stocks = stocks.filter(models.Stock.price > models.Stock.ma200)
    
    stocks = stocks.all()
    print(stocks)

    return templates.TemplateResponse("home.html", {
        "request": request,
        "stocks": stocks, 
        "dividend_yield": dividend_yield,
        "forward_pe": forward_pe,
        "ma200": ma200,
        "ma50": ma50
    })


def fetch_stock_data(id: int):
    db = SessionLocal()
    stock = db.query(models.Stock).filter(models.Stock.id == id).first()
    
    yahoo_data = yq.Ticker(stock.symbol)
    stock_summary = yahoo_data.summary_detail[stock.symbol]
    print(stock_summary)

    stock.ma200 = stock_summary['twoHundredDayAverage']
    stock.ma50 = stock_summary['fiftyDayAverage']
    stock.price = stock_summary['previousClose']
    stock.forward_pe = stock_summary['forwardPE']
    stock.forward_eps = yahoo_data.key_stats[stock.symbol]['forwardEps']
    if stock_summary['dividendYield'] != None:
        stock.dividend_yield = stock_summary['dividendYield'] * 100


    db.add(stock)
    db.commit()

@app.post("/stock")
async def create_stock(stock_request: StockRequest, background_tasks: BackgroundTasks, db: Session = Depends(get_db)):
    print(stock_request.dict())
    stock = models.Stock(symbol=stock_request.symbol)

    db.add(stock)
    db.commit()

    background_tasks.add_task(fetch_stock_data, stock.id)

    return stock_request.dict()