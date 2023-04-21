from dotenv import load_dotenv

load_dotenv()

from app import app, db
from app.models import Employee, Menu, MenuItem, MenuItemType, Table

with app.app_context():
    db.drop_all()
    db.create_all()

    employee = Employee(name="Margo", employee_number=1234, password="password")
    beverages = MenuItemType(name="Beverages")
    entrees = MenuItemType(name="Entrees")
    sides = MenuItemType(name="Sides")

    dinner = Menu(name="Dinner")

    fries = MenuItem(name="French fries", price=3.50, type=sides, menu=dinner)
    drp = MenuItem(name="Dr. Pepper", price=1.0, type=beverages, menu=dinner)
    jambalaya = MenuItem(name="Jambalaya", price=21.98, type=entrees, menu=dinner)

    tables = list()
    for i in range(10):
        tables.append(Table(id=i, number=i, capacity=i + 2))

    db.session.add(employee)
    db.session.add(dinner)
    db.session.add_all(tables)
    db.session.commit()
