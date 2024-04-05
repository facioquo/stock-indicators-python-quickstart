# Stock Indicators for Python: QuickStart guide

These are the detailed steps to setup a Python project and to run your first finanical market price analysis with the [Stock Indicators for Python](https://python.stockindicators.dev) PyPI library package.  This guide is partly derived from the more detailed [Visual Studio Code Python Tutorial](https://code.visualstudio.com/docs/python/python-tutorial).

> [!TIP]
> If you just want to run the example code without building it yourself, [fork this repo](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/fork-a-repo) and skip the [_Write the code_](#write-the-code) section (steps 5-9) entirely.

## Install prerequisite software

My baseline environment and the tools that I've already installed:

- Windows 11 OS
- [Download and install Git for Windows](https://git-scm.com/download/win) for _git_ and bash terminal CLI

> [!NOTE]
> Don't sweat the OS.  These instructions are the same for Mac and Linux users; however, you'll have to download a different version of tools installers from the links provided.  Overall, Python and our library are designed to work everywhere -- on Windows, Linux, and Mac operating systems.

### Install Python v3

- [Download and install Python](https://www.python.org/downloads)

   > I installed `v3.12.2`, the latest LTS version, using _administrative privileges_, for all users, and chose to add Python to my environment PATH variables.  We support `v3.8` or newer.

   ```bash
   # test with bash terminal command
   python --version
   > Python 3.12.2
   ```

### Install the .NET SDK

- [Download and install .NET SDK](https://dotnet.microsoft.com/en-us/download/visual-studio-sdks)

   > I installed `v8.0.202`, the latest LTS version.  We support `v6` or newer.  We _do not_ support Mono.

   ```bash
   # test with bash terminal command
   dotnet --version
   > 8.0.202
   ```

### Install the Visual Studio Code IDE

- [Download and install VS Code](https://code.visualstudio.com/download)

I also installed these recommended extensions:

- [Python Extension Pack](https://marketplace.visualstudio.com/items?itemName=donjayamanne.python-extension-pack) (includes primary Python extension)
- [Pylance](https://marketplace.visualstudio.com/items?itemName=ms-python.vscode-pylance)
- [Python Debugger](https://marketplace.visualstudio.com/items?itemName=ms-python.debugpy)

## Setup your project

1. Create a new project folder.
2. Initialize git in this folder with `git init` bash command.  Also add a Python flavored [`.gitignore`](.gitignore) file; I found this one in [the _gitignore_ templates repo](https://github.com/github/gitignore/blob/4488915eec0b3a45b5c63ead28f286819c0917de/Python.gitignore).  This step is _optional_ and is only needed if you intend to store your work in a git repository.
3. Initialize Python workspace with a [virtual environment](https://docs.python.org/3/tutorial/venv.html#creating-virtual-environments) (a cached instance):

   ```bash
   # git bash commands
   # create environment
   python -m venv .venv

   # then activate it
   .venv\Scripts\activate
   ```

   > You can also use VSCode command: **Python: Create Environment ...** and then **Python: Select Interpreter** to pick your just created **venv** instance.  When done correctly, you should have a `.venv` folder in the root of your project folder.  There are other ways to initialize in a global environment; however, this is the recommended approach from [the Python tutorial](https://code.visualstudio.com/docs/python/python-tutorial) I'd mentioned above.

4. Install the [`stock-indicators`](https://pypi.org/project/stock-indicators) package from PyPI

   ```bash
   # bash terminal command
   pip install stock-indicators
   ```

   > I'm using `v1.2.1`, the latest version.  To verify, you should see these subfolders under `.venv/Lib/site-packages`:
   > - clr_loader
   > - pycparser
   > - pythonnet
   > - stock_indicators
   > - and others

## Write the code

It's time to start writing some code.

5. To start, add a [`quotes.csv`](quotes.csv) file containing historical financial market prices in OHLCV format.  Use the one I put in this repo.  You can worry about all the available [stock quote sources](https://github.com/DaveSkender/Stock.Indicators/discussions/579) later.

6. Create a [`main.py`](main.py) file and import the utilities we'll be using at the top of it.

   ```python
   import csv
   from datetime import datetime
   from itertools import islice
   from stock_indicators import indicators, Quote
   ```

7. Import the data from [the CSV file](quotes.csv) and convert it into an iterable list of the `Quote` class.

   ```python
   # import each row of the csv file into a raw iterable string list
   with open('quotes.csv', 'r', newline='', encoding="utf-8") as file:
      rows = list(csv.reader(file))
      file.close()

   # parse each row into proper `Quote` format
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

   > These `quotes` can now be used by the `stock-indicators` library.  For a quickstart that uses **pandas.DataFrame**, see our online _ReplIt_ code example for the [Williams Fractal indicator](https://replit.com/@daveskender/Stock-Indicators-for-Python-Williams-Fractal).

8. Calculate [an indicator](https://python.stockindicators.dev/indicators) from the `quotes`

   ```python
   # calculate 5-period simple moving average
   results = indicators.get_sma(quotes, 5)
   ```

9. Configure `results` for console output

   ```python
   # show the first 30 periods, for brevity
   print("Date        SMA")
   for r in islice(results, 0, 30):
      print(f"{r.date:%Y-%m-%d}  {r.sma or ''}")
   ```

## Run the code

10. Click the _**Run Python File in Terminal**_ (&#9658;) play button in the top-right side of the VS Code editor to run the code, or execute `python main.py` from your bash terminal.

    ```console
    # console output
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

    > The small deviations shown in these raw results are normal for `double` floating point precision data types.  They're not _programming errors_.  Developers will usually truncate or round to fewer significant digits when displaying.

**You've done it!**  That's the end of this QuickStart guide.

## Still having trouble getting started?

Ask a question in our [open community help and support discussions](https://github.com/DaveSkender/Stock.Indicators/discussions/categories/help-and-support).

And if you end up building something wonderful, come back and [share it with us](https://github.com/DaveSkender/Stock.Indicators/discussions/categories/show-and-tell).  We love &#128150; to see all the creative ways people are using the library.

Good luck &#127808; and have fun in building your systems!

-- @DaveSkender
