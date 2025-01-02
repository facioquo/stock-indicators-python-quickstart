"""Hello indicators!"""  # calculate a Simple Moving Average (SMA)

# Import what we need from stock-indicators package
import csv
from datetime import datetime
from itertools import islice
from stock_indicators import indicators, Quote

# Step 1: Get price history data from CSV file
with open("quotes.csv", "r", newline="", encoding="utf-8") as file:
    rows = list(csv.reader(file))

# Convert rows into Quote objects that stock-indicators understands
# CSV returns strings, but Quote needs numbers for prices and volume
quotes = []
for row in rows[1:]:  # skip header row
    quotes.append(
        Quote(
            datetime.strptime(row[0], "%Y-%m-%d"),  # date
            row[1],  # open
            row[2],  # high
            row[3],  # low
            row[4],  # close
            row[5],  # volume
        )
    )

# Step 2: Calculate 5-period Simple Moving Average
results = indicators.get_sma(quotes, 5)

# Step 3: Show the results
print("Date        SMA")
print("-" * 20)
for r in islice(results, 0, 30):  # show first 30 days
    sma = f"{r.sma:.3f}" if r.sma else ""
    print(f"{r.date:%Y-%m-%d}  {sma}")

# Try other indicators at:
# https://python.stockindicators.dev/indicators
