from dotenv import load_dotenv

load_dotenv()

from app import app, db
from app.models import (
    Employee,
    Menu,
    MenuItem,
    MenuItemType,
    Table,
    Order,
    OrderDetail,
)

with app.app_context():
    db.drop_all()
    db.create_all()

    employees = [
        Employee(name="Margo", employee_number=1234, password="password"),
        Employee(name="Mal", employee_number=1235, password="password1"),
    ]
    beverages = MenuItemType(name="Beverages")
    entrees = MenuItemType(name="Entrees")
    sides = MenuItemType(name="Sides")

    dinner = Menu(name="Dinner")

    fries = MenuItem(name="French fries", price=3.50, type=sides, menu=dinner)
    drp = MenuItem(name="Dr. Pepper", price=1.0, type=beverages, menu=dinner)
    jambalaya = MenuItem(
        name="Jambalaya",
        price=21.98,
        type=entrees,
        menu=dinner,
    )

    tables = list()
    for i in range(10):
        tables.append(Table(id=i, number=i, capacity=i + 2))
    orders = list()
    orderDetails = list()
    for i in range(3):
        orders.append(Order(id=i, table_id=i, server_id=1, finished=False))
        orderDetails.append(OrderDetail(id=i, order_id=i, menu_item_id=i + 1))

    db.session.add_all(employees)
    db.session.add(dinner)
    db.session.add_all(tables)
    db.session.add_all(orders)
    db.session.add_all(orderDetails)

    db.session.commit()
