import FreeSimpleGUI as sg
from datetime import datetime

date_format="%d/%m/%Y"

class FinanceInterface:
    def __init__(self,tracker):
        self.tracker=tracker
        sg.theme("DarkBlue3")
        self.window=self.create_main_window()
    
    def create_main_window(self):
        table_headings=["Date","Title","Category","Type","Amount"]
        layout=[
            [sg.Text("Personal finance tracker", font=("Arial",16))],
            [
                sg.Text("Start date"),
                sg.Input(key="-START_DATE-",size=(12,1)),
                sg.Text("End date"),
                sg.Input(key="-END_DATE-",size=(12,1)),
                sg.Button("Filter")
            ],
            [
                sg.Table(
                    values=[],
                    headings=table_headings,
                    key="-TABLE-",
                    auto_size_columns=True,
                    expand_x=True,
                    expand_y=True,
                    justification="Center"
                )
            ],
            [
                sg.Button("Add category"),
                sg.Button("Add expense"),
                sg.Button("Add income"),
                sg.Button("Export CSV"),
                sg.Button("Exit")
            ]
        ]
        return sg.Window(
            "Personal finance tracker",
            layout,
            resizable=True,
            finalize=True
        )
    
    def category_window(self):
        layout=[
            [sg.Text("Category name")],
            [sg.Input(key="-CATEGORY_NAME-")],
            [sg.Text("Color")],
            [
                sg.Input(key="-CATEGORY_COLOR-",size=(10,1)),
                sg.ColorChooserButton("Choose color",target="-CATEGORY_COLOR-")
            ],
            [
                sg.Button("Save"),
                sg.Button("Cancel")
            ]
        ]
        return sg.Window(
            "Add category",
            layout,
            modal=True
        )
    
    def movement_window(self,movement_type):
        categories=[c.name for c in self.tracker.categories]
        layout=[
            [sg.Text(f"Add {movement_type}")],
            [sg.Text("Title")],
            [sg.Input(key="-TITLE-")],
            [sg.Text("Amount")],
            [sg.Input(key="-AMOUNT-")],
            [sg.Text("Category")],
            [
                sg.Combo(
                    categories,
                    key="-CATEGORY-",
                    readonly=True
                )
            ],
            [sg.Text("Date (dd/mm/yyyy)")],
            [sg.Input(key="-DATE-")],
            [
                sg.Button("Save"),
                sg.Button("Cancel")
            ]
        ]
        return sg.Window(
            f"Add {movement_type}",
            layout,
            modal=True
        )
    
    def update_table(self,movement):
        data=[]
        for m in movement:
            data.append([
                m.date.strftime(date_format),
                m.title,
                m.category.name,
                m.type,
                m.amount
            ])
        self.window["-TABLE-"].update(values=data)

    def validate_date(self, date_string):
        try:
            date=datetime.strptime(date_string,date_format)
            if date>datetime.now():
                sg.popup_error("Date cannot be in the future.")
                return None
            return date
        except ValueError:
            sg.popup_error("Invalid date format, please use dd/mm/yyyy")
            return None
    
    def run(self):
        while True:
            event,values=self.window.read()
            if event in (sg.WIN_CLOSED,"Exit"):
                break
            if event=="Add category":
                self.handle_add_category()
            elif event=="Add expense":
                self.handle_add_movement("Expense")
            elif event=="Add income":
                self.handle_add_movement("Income")
            elif event=="Filter":
                self.handle_filter(values)
            elif event=="Export CSV":
                self.tracker.export_csv()
    
    def handle_add_category(self):
        window=self.category_window()
        while True:
            event,values=window.read()
            if event in (sg.WIN_CLOSED,"Cancel"):
                break
            if event=="Save":
                name=values["-CATEGORY_NAME-"]
                color=values["-CATEGORY_COLOR-"]
                if not name:
                    sg.popup_error("Category name required")
                    continue
                self.tracker.add_category(name,color)
                break
        window.close()
    
    def handle_add_movement(self,movement_type):
        if not self.tracker.categories:
            sg.popup_error("You must create a category first")
            return
        window=self.movement_window(movement_type)
        while True:
            event,values=window.read()
            if event in (sg.WIN_CLOSED,"Cancel"):
                break
            if event=="Save":
                title=values["-TITLE-"]
                amount=values["-AMOUNT-"]
                category=values["-CATEGORY-"]
                date_str=values["-DATE-"]
                date=self.validate_date(date_str)
                if not date:
                    continue
                try:
                    amount=float(amount)
                except ValueError:
                    sg.popup_error("Amount must be a number")
                    continue
                self.tracker.add_movement(
                    title,
                    amount,
                    category,
                    movement_type,
                    date
                )
                self.update_table(self.tracker.movements)
                break
        window.close()
    
    def handle_filter(self,values):
        start=self.validate_date(values["-START_DATE-"])
        end=self.validate_date(values["-END_DATE-"])
        if not start or not end:
            return
        movements=self.tracker.filter_by_date(start,end)
        self.update_table(movements)