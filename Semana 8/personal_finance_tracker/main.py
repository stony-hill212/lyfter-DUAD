from interfaces import FinanceInterface
from logic import FinanceTracker

def main():
    tracker=FinanceTracker()
    app=FinanceInterface(tracker)
    app.run()

if __name__=="__main__":
    main()

