import sys

def main():
    tickers = []
    action = ""
    fromDate = ""
    toDate = ""

    if len(sys.argv) > 1:
        for arg in sys.argv:
            if "ticker" in arg:
                tickers = parseCSVs(arg)
            if "action" in arg:
                action = arg[arg.find("=") + 1:]
            if "from" in arg:
                fromDate = arg[arg.find("="):]
            if "toDate" in arg:
                toDate = arg[arg.find("="):]
    print("ACTION: ", action)
    print("TICKERS: ", tickers)
    print("FROM: ", fromDate)
    print("TO: ", toDate)


# tickers=GOOG,F,CGC
def parseCSVs(arg):
    return arg[arg.find("=") + 1:].split(',')

main()