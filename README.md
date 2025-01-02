<!-- markdownlint-disable MD029 -->
# Stock Indicators for Python: QuickStart Guide

A beginner's guide to setting up and using the [Stock Indicators for Python](https://python.stockindicators.dev) library for financial market analysis.

## Quick Start

For the impatient, run these commands to get started immediately:

```bash
git clone https://github.com/facioquo/stock-indicators-python-quickstart.git
cd stock-indicators-python-quickstart
python -m venv .venv
source .venv/bin/activate  # On Windows use: .venv\Scripts\activate
pip install stock-indicators
python main.py
```

## Prerequisites

Required software versions:

- [Python](https://www.python.org/downloads) ≥ 3.8
- [.NET SDK](https://dotnet.microsoft.com/download) ≥ 6.0
- [Git](https://git-scm.com/download) (any recent version)
- [VS Code](https://code.visualstudio.com/download) (recommended)

VS Code Extensions:

- [Python Extension Pack](https://marketplace.visualstudio.com/items?itemName=donjayamanne.python-extension-pack) (includes primary Python extension)
- [Pylance](https://marketplace.visualstudio.com/items?itemName=ms-python.vscode-pylance)
- [Python Debugger](https://marketplace.visualstudio.com/items?itemName=ms-python.debugpy)

## Step-by-Step Setup

0. **Install Prerequisites**

   ```bash
   # Verify installations
   python --version   # Should be ≥ 3.8
   dotnet --version   # Should be ≥ 6.0
   ```

1. **Create a new project folder.**
2. **Optional: initialize a *git repository* in this folder with `git init` bash command and add a Python flavored [`.gitignore`](.gitignore) file.**  I found this one in [the *gitignore* templates repo](https://github.com/github/gitignore/blob/4488915eec0b3a45b5c63ead28f286819c0917de/Python.gitignore).
3. **Initialize Python workspace with a [virtual environment](https://docs.python.org/3/tutorial/venv.html#creating-virtual-environments) (a cached instance):**

   ```bash
   # create environment
   python -m venv .venv

   # then activate it
   source .venv/bin/activate  # On Windows use: .venv\Scripts\activate
   ```

   > You can also use VSCode command: **Python: Create Environment ...** and then **Python: Select Interpreter** to pick your just created **venv** instance.  The comparable MacOS command is `source venv/bin/activate`.
   >
   > When done correctly, you should have a `.venv` folder in the root of your project folder.  There are other ways to initialize in a global environment; however, this is the recommended approach from [the Python tutorial](https://code.visualstudio.com/docs/python/python-tutorial) I'd mentioned above.

4. **Install the [`stock-indicators`](https://pypi.org/project/stock-indicators) package from PyPI**

   ```bash
   # bash terminal command
   pip install stock-indicators
   ```

   > I'm using `v1.3.1`, the latest version.  You should see it installed in `.venv/Lib/site-packages`.

   ```bash
   # test with bash terminal command
   pip freeze --local
   ```

   ```console
   ...
   clr-loader==0.2.7
   pycparser==2.22
   pythonnet==3.0.5
   stock-indicators==1.3.1
   typing_extensions==4.12.2
   ...
   ```

## Write the code

It's time to start writing some code.

5. **To start, add a [`quotes.csv`](quotes.csv) file containing historical financial market prices in OHLCV format.**  Use the one I put in this repo.  You can worry about all the available [stock quote sources](https://github.com/DaveSkender/Stock.Indicators/discussions/579) later.

6. **Create a [`main.py`](main.py) file and import the utilities we'll be using at the top of it.**

   ```python
   import csv
   from datetime import datetime
   from itertools import islice
   from stock_indicators import indicators, Quote
   ```

7. **Import the data from [the CSV file](quotes.csv) and convert it into an iterable list of the `Quote` class.**

   ```python
   # Get price history data from CSV file
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
   ```

   > These `quotes` can now be used by the `stock-indicators` library.  For a quickstart that uses **pandas.DataFrame**, see our online *ReplIt* code example for the [Williams Fractal indicator](https://replit.com/@daveskender/Stock-Indicators-for-Python-Williams-Fractal).

8. **Calculate [an indicator](https://python.stockindicators.dev/indicators/) from the `quotes`**

   ```python
   # Calculate 5-period Simple Moving Average
   results = indicators.get_sma(quotes, 5)
   ```

9. **Configure `results` for console output**

   ```python
   # Show the results
   print("Date        SMA")
   for r in islice(results, 0, 30):  # show first 30 days
      sma = f"{r.sma:.3f}" if r.sma else ""
      print(f"{r.date:%Y-%m-%d}  {sma}")
   ```

## Run the code

10. **Click the ***Run Python File in Terminal*** (&#9658;) play button in the top-right side of the VS Code editor to run the code, or execute from the commandline in your bash terminal.**  The SMA indicator output will print to the console.

   ```bash
   # from CLI (optional)
   python main.py
   ```

   ```console
   Date        SMA
   --------------------
   2017-01-03
   2017-01-04
   2017-01-05
   2017-01-06
   2017-01-09  213.872
   2017-01-10  214.102
   2017-01-11  214.200
   2017-01-12  214.226
   2017-01-13  214.196
   2017-01-17  214.156
   2017-01-18  214.210
   2017-01-19  213.986
   2017-01-20  214.024
   ...
   ```

   > The small deviations shown in these raw results are normal for `double` floating point precision data types.  They're not *programming errors*.  Developers will usually truncate or round to fewer significant digits when displaying.  We're showing 3 decimal places here.

**You've done it!**  That's the end of this QuickStart guide.

---

## Common Issues

- **Import Errors**: Ensure you've activated the virtual environment
- **Runtime Errors**: Verify .NET SDK installation
- **.NET Loading Issues**: On Linux/MacOS, you may need additional dependencies

## Next Steps

- Explore [all available indicators](https://python.stockindicators.dev/indicators/)
- Learn about [data sources](https://github.com/DaveSkender/Stock.Indicators/discussions/579)
- Join our [community discussions](https://github.com/DaveSkender/Stock.Indicators/discussions)

## Getting Help

Having trouble? Try these resources:

1. [Documentation](https://python.stockindicators.dev)
2. [GitHub Discussions](https://github.com/DaveSkender/Stock.Indicators/discussions)
3. [Stack Overflow](https://stackoverflow.com/questions/tagged/stock-indicators)

## Share Your Work

Built something cool? [Share it](https://github.com/DaveSkender/Stock.Indicators/discussions/categories/show-and-tell) with the community!

-- @DaveSkender, January 2025
