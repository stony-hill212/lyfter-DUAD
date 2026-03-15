import pytest
from datetime import datetime
from logic import FinanceTracker

date_format="%d/%m/%Y"

@pytest.fixture
def tracker():
    tracker=FinanceTracker()
    tracker.categories=[]
    tracker.movements=[]
    return tracker

def test_add_category(tracker: FinanceTracker):
    tracker.add_category("Food","#FF0000")
    assert len(tracker.categories)==1
    assert tracker.categories[0].name=="Food"

def test_duplicate_category(tracker: FinanceTracker):
    tracker.add_category("Food","#4800FF")
    with pytest.raises(ValueError):
        tracker.add_category("Food","#325432")

def test_add_expense(tracker: FinanceTracker):
    tracker.add_category("Food","#FF0000")
    tracker.add_movement(
        "Lunch",
        10,
        "Food",
        "expenses",
        datetime.strptime("09/03/2026",date_format)
    )
    assert len(tracker.movements)==1
    assert tracker.movements[0].movement_type=="expenses"

def test_add_income(tracker: FinanceTracker):
    tracker.add_category("Salary","#00FF00")
    tracker.add_movement(
        "Salary",
        2000,
        "Salary",
        "income",
        datetime.strptime("01/03/2026",date_format)
    )
    assert tracker.movements[0].movement_type=="income"

def test_invalid_movement_type(tracker: FinanceTracker):
    tracker.add_category("Food","#FF0000")
    with pytest.raises(ValueError):
        tracker.add_movement(
            "Lunch",
            10,
            "Food",
            "invalid",
            datetime.strptime("01/03/2026",date_format)
        )

def test_filter_movements(tracker: FinanceTracker):
    tracker.add_category("Food","#FF0000")
    tracker.add_movement(
        "Lunch",
        10,
        "Food",
        "expenses",
        datetime.strptime("01/03/2026",date_format)
    )
    results=tracker.filter_by_date(
        datetime.strptime("28/02/2026",date_format),
        datetime.strptime("02/03/2026",date_format)
    )
    assert len(results)==1

def test_totals(tracker: FinanceTracker):
    tracker.add_category("Food","#FF0000")
    tracker.add_movement(
        "Lunch",
        10,
        "Food",
        "expenses",
        datetime.strptime("01/03/2026",date_format)
    )
    tracker.add_movement(
        "job",
        50,
        "Food",
        "income",
        datetime.strptime("01/03/2026",date_format)
    )
    totals=tracker.calculate_totals()
    assert totals["income"]==50
    assert totals["expenses"]==10

def test_movement_storage(tracker: FinanceTracker):
    tracker.add_category("Transport","#0000FF")
    tracker.add_movement(
        "Uber",
        3,
        "Transport",
        "expenses",
        datetime.strptime("03/03/2026",date_format)
    )
    movement=tracker.movements[0]
    assert movement.title=="Uber"
    assert movement.amount==3
