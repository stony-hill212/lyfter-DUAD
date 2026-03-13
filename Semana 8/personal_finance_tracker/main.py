from interfaces import FinanceInterface
from persistence import initialize_csv
from logic import FinanceTracker


def main():
    initialize_csv()
    tracker=FinanceTracker()
    app=FinanceInterface(tracker)
    app.run()

if __name__=="__main__":
    main()

