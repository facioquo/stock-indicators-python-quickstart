# QuickStart for Stock Indicators for Python

These are the steps to setup a Python project and to run your first finanical market price analysis with the [Stock Indicators for Python](https://python.stock.indicators).  We're following the guidance for the [Visual Studio Code Python Tutorial](https://code.visualstudio.com/docs/python/python-tutorial).

## Install prerequisite software

Our baseline environment and tools that we've installed:

- Windows 11 OS
- [Download and install Git for Windows](https://git-scm.com/download/win) (optional)

> [!TIP]
> Don't sweat the OS.  These instructions are the same for Mac users; however, you'll have to download the right versions of tools and installers from the links provided.  Overally, Python and our library will work on Windows, Linux, and Mac operating system.

### Install Python v3

- [Download and install Python](https://www.python.org/downloads)

   > We installed `v3.12.2` with Administrative privileges for all users and chose to add Python to the PATH variables.

   ```bash
   # test with Git Bash terminal command
   $ python --version
   Python 3.12.2
   ```

### Install the .NET SDK

- [Download and nstall .NET SDK](https://dotnet.microsoft.com/en-us/download/visual-studio-sdks)

   > We installed `v8.0.202`.  We support v6.x or newer.  We _do not_ support Mono.
   
   ```bash
   # test with Git Bash terminal command
   $ dotnet --version
   8.0.202
   ```

### Install the Visual Studio Code IDE

- [Download and install VS Code](https://code.visualstudio.com/download)

Recommended extensions:

- [Python Extension Pack](https://marketplace.visualstudio.com/items?itemName=donjayamanne.python-extension-pack) (includes primary Python extension)
- [Pylance](https://marketplace.visualstudio.com/items?itemName=ms-python.vscode-pylance)
- [Python Debugger](https://marketplace.visualstudio.com/items?itemName=ms-python.debugpy)

## Setup your project

1. Create a new project folder
2. _Optional:_ Initialize git with `git init` and a add [`.gitignore`](.gitignore) file.
3. Initialize Python workspace with `python -m venv .venv`

   > You can also use VSCode command: **Python: Create Environment ...** and then **Python: Select Interpreter** to pick your just created **venv** instance.  When done correctly, you should have a `.venv` file in your folder.

4. Install the [`stock-indicators`](https://pypi.org/project/stock-indicators) package from PyPI

   ```bash
   # git bash command
   pip install stock-indicators
   ```

   > We're using `v1.2.1`.  To verify, you should see these subfolders under `.venv/Lib/site-packages`:
   > - clr_loader
   > - pycparser
   > - pythonnet
   > - stock_indicators
   > - and others

## Write the code

It's time to start writing some code.

1. To start, add a [`quotes.csv`](quotes.csv) file containing historical financial market prices in OHLCV format.  Use the one in this repo.  You can worry about all the available [stock quote sources](https://github.com/DaveSkender/Stock.Indicators/discussions/579) later.

2. Create a file `main.py` and import the utilities we'll be using at the top.

   ```python
   import csv
   from datetime import datetime
   from itertools import islice
   from stock_indicators import indicators, Quote
   ```

3. Import the data from the CSV file and convert it to an iterable list of Quotes.

   ```python
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
   ```

   > For a quickstart that includes converting quotes from Pandas DataFrame, see our online ReplIt code example: [Williams Fractal indicator](https://replit.com/@daveskender/Stock-Indicators-for-Python-Williams-Fractal).

4. Calculate an indicator from the quotes

   ```python
   # calculate 5-period simple moving average
   results = indicators.get_sma(quotes, 5)
   ```

5. Print the `results` to console

   ```python
   # show the first 30 periods, for brevity
   print("Date        SMA")
   for r in islice(results, 0, 30):
      print(f"{r.date:%Y-%m-%d}  {r.sma or ''}")
   ```

## Run the code

6. Click the _**Run Python File in Terminal**_ &#9658; play button in the top-right side of the editor to run the code or execute `python main.py` from your bash terminal commandline.

   ```bash
   # output
   Date        SMA
   2017-01-03
   2017-01-04
   2017-01-05
   2017-01-06
   2017-01-09  213.87199999999999
   2017-01-10  214.102
   2017-01-11  214.2
   2017-01-12  214.22599999999997
   2017-01-13  214.196
   2017-01-17  214.156
   2017-01-18  214.20999999999998
   2017-01-19  213.98600000000002
   2017-01-20  214.02400000000003
   ...
   ```

   > The slight rounding errors shown on these raw results are normal for double floating point precision data types.  Developers will usually truncate our round to fewer significant digits when displaying.

## Still having trouble getting started?

If you get stuck, ask a question in our [open community discussions](https://github.com/DaveSkender/Stock.Indicators/discussions).
