from datetime import datetime
from persistence import export_to_csv,load_from_csv,append_to_csv,initialize_csv

date_format="%d/%m/%Y"

class Category:
    def __init__(self,name,color):
        self.name=name
        self.color=color
    
    def __repr__(self):
        return f"Category({self.name})"

class Movement:
    def __init__(self,title,amount,category,movement_type,date):
        self.title=title
        self.amount=amount
        self.category=category
        self.movement_type=movement_type
        self.date=date
    
    def to_dict(self):
        return{
            "date":self.date.strftime(date_format),
            "title":self.title,
            "category":self.category.name,
            "type":self.movement_type,
            "amount":self.amount
        }
    
    def __repr__(self):
        return f"{self.movement_type} | {self.title} | {self.amount}"

class FinanceTracker:
    def __init__(self):
        initialize_csv()
        self.categories=[]
        self.movements=[]
        self.load_existing_data()
    
    def load_existing_data(self):
        rows=load_from_csv()
        for row in rows:
            category_name=row["category"].strip()
            category=self.get_category(category_name)
            if not category:
                category=self.add_category(category_name,"#CCCCCC")
            movement=Movement(
                row["title"],
                row["amount"],
                category,
                row["type"],
                row["date"]
            )
            self.movements.append(movement)

    def calculate_totals(self):
        return{"income":self.total_income(),"expenses":self.total_expenses()}
    
    def add_category(self,name,color):
        if self.get_category(name):
            raise ValueError("Category already exists")
        category=Category(name,color)
        self.categories.append(category)
        return category
    
    def get_category(self,name):
        for c in self.categories:
            if c.name.lower()==name.lower():
                return c
        return None
    
    def add_movement(self,title,amount,category_name,movement_type,date):
        if movement_type not in ["income","expenses"]:
            raise ValueError("Invalid movement")
        if isinstance(date,str):
            date=datetime.strptime(date,date_format)
        category=self.get_category(category_name)
        if not category:
            raise ValueError("Invalid category")
        movement=Movement(title,amount,category,movement_type,date)
        self.movements.append(movement)
        append_to_csv(movement)
        return movement
    
    def filter_by_date(self,start_date,end_date):
        filtered=[]
        for m in self.movements:
            if start_date<=m.date<=end_date:
                filtered.append(m)
        return filtered
    
    def total_income(self):
        total=0
        for m in self.movements:
            if m.movement_type=="income":
                total+=m.amount
        return total
    
    def total_expenses(self):
        total=0
        for m in self.movements:
            if m.movement_type=="expenses":
                total+=m.amount
        return total
    
    def balance(self):
        return self.total_income()-self.total_expenses()
    
    def export_csv(self):
        totals={
            "income":self.total_income(),
            "expenses":self.total_expenses(),
            "balance":self.balance()
        }
        export_to_csv(self.movements,totals)




