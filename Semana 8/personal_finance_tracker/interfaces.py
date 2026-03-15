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
                sg.Button("Add expenses"),
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
            [sg.Text("title")],
            [sg.Input(key="-TITLE-")],
            [sg.Text("Amount")],
            [sg.Input(key="-AMOUNT-")],
            [sg.Text("category")],
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
                m.movement_type,
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
        self.update_table(self.tracker.movements)
        while True:
            event,values=self.window.read()
            if event in (sg.WIN_CLOSED,"Exit"):
                break
            if event=="Add category":
                self.handle_add_category()
            elif event=="Add expenses":
                self.handle_add_movement("expenses")
            elif event=="Add income":
                self.handle_add_movement("income")
            elif event=="Filter":
                self.handle_filter(values)
            elif event=="Export CSV":
                self.tracker.export_csv()
        self.window.close()
    
    def handle_add_category(self):
        window=self.category_window()
        while True:
            event,values=window.read()
            if event in (sg.WIN_CLOSED,"Cancel"):
                break
            if event=="Save":
                name=values["-CATEGORY_NAME-"].strip()
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
                title=values["-TITLE-"].strip()
                amount_text=values["-AMOUNT-"].strip()
                date_text=values["-DATE-"].strip()
                category=values["-CATEGORY-"]
                if not title:
                    sg.popup_error("Title cannot be empty.")
                    continue
                if not amount_text:
                    sg.popup_error("Amount cannot be empty.")
                    continue
                try:
                    amount=float(amount_text)
                except ValueError:
                    sg.popup_error("Amount must be a number.")
                    continue
                if amount<=0:
                    sg.popup_error("Amount must be greater than 0.")
                    continue
                try:
                    date=datetime.strptime(date_text,date_format)
                except ValueError:
                    sg.popup_error("Date must be dd/mm/yyyy.")
                    continue
                if date>datetime.now():
                    sg.popup_error("Date cannot be in future.")
                    continue
                if not category:
                    sg.popup_error("Please select a category.")
                    continue
                self.tracker.add_movement(title,amount,category,movement_type,date)
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

