
## Step 1: Build FastAPI app, Stub out the API endpoints

* Create and document some basic API endpoint

Install dependencies `pip install -r requirements.txt`
Run app `uvicorn main:app --reload`


## Step 2: Mock the UI with Semantic UI and Jinja2 Templates

* Define application layout and look and feel using Semantic UI.Including CSS and JavaScript from the CDN

## Step 3: Database Design

* Design SQLite database by creating SQLAlchemy models
    * Check db schema by running `sqlite3 stocks.db` to enter db sqlite cli then `.schema`
    * `SELECT * FROM stocks;` to check stocks records
* See what yfinance provides 
* forwardPE, forwardEps, dividendYield, 50 Day, 200 Day, Close
* SQLAlchemy create_all

## Step 4: Add a stock endpoint

* Background task to fetch info and add to db also
* Use Insomnia to test it

## Step 5: Wire home screen

* Show added stocks in a table

## Step 6: Filters to filter table

* Filter boxes on UI
* Use SQLALchemy to filter in db
* Use query parameters to filter
 
## Step 7: Modal to add stock tickers via UI

## Youtube Links

Part 1 : https://www.youtube.com/watch?v=5GorMC2lPpk&ab_channel=PartTimeLarry