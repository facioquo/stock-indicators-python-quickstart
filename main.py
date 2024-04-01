"""Hello indicators!"""
import csv
from datetime import datetime
from itertools import islice
from stock_indicators import indicators, Quote

# import csv file into interable list
with open('quotes.csv', 'r', newline='', encoding="utf-8") as file:
    rows = list(csv.reader(file))
    file.close()

# parse rows into quotes
quotes = []
for row in rows[1:]: # skipping CSV file header row
    quotes.append(Quote(
        datetime.strptime(row[0], '%Y-%m-%d'), # date
        row[1], # open
        row[2], # high
        row[3], # low
        row[4], # close
        row[5], # volume
    ))

# calculate 5-period simple moving average
results = indicators.get_sma(quotes, 5)

# show the first 30 results, for brevity
print("Date        SMA")
for r in islice(results, 0, 30):
    print(f"{r.date:%Y-%m-%d}  {r.sma or ''}")
