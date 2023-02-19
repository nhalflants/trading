closing_price_sum = 0

def get_moving_average(days: float):
    with open("data/spy.csv") as f:
        content = f.readlines()[-days:]
        for line in content:
            close = float(line.split(",")[4])
            closing_price_sum += close

    return closing_price_sum / days