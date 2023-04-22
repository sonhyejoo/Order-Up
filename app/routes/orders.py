from flask import Blueprint, render_template, redirect, url_for, request
from flask_login import login_required, current_user
from ..forms import AssignTableForm, CloseTableForm, AddToOrderForm
from ..models import Employee, Table, Order, MenuItem, MenuItemType, db


bp = Blueprint("orders", __name__, url_prefix="/orders")


@bp.route("/", methods=["POST", "GET"])
@login_required
def index():
    assign_form = AssignTableForm()
    close_form = CloseTableForm()
    add_order_form = AddToOrderForm()

    # Assign Table form queries
    tables = Table.query.order_by(Table.number).all()
    servers = Employee.query.order_by(Employee.employee_number).all()
    open_orders = Order.query.filter(Order.finished == False).all()

    busy_table_ids = [order.table_id for order in open_orders]

    open_tables = [table for table in tables if table.id not in busy_table_ids]

    assign_form.tables.choices = [(t.id, f"Table {t.number}") for t in open_tables]
    assign_form.servers.choices = [(s.id, f"{s.name}") for s in servers]

    # your_open_orders
    your_open_orders = Order.query.filter(
        Order.server_id == current_user.id,
        Order.finished == False,
    ).all()

    # menu items
    menu_items_list = (
        MenuItem.query.join(MenuItemType)
        .group_by(MenuItemType.name, MenuItem.id)
        .order_by(
            MenuItemType.name,
            MenuItem.name,
        )
        .all()
    )
    add_order_form.menu_item_ids.choices = [
        (item.id, item.name) for item in MenuItem.query.all()
    ]
    print(add_order_form.menu_item_ids.choices)

    # menu_items_list_entrees = [
    #     item for item in menu_items_list if item.type.name == "Entrees"
    # ]
    # print(menu_items_list_entrees)

    if assign_form.validate_on_submit():
        table_id = assign_form.tables.data
        server_id = assign_form.servers.data
        new_order = Order(
            table_id=table_id,
            server_id=server_id,
            finished=False,
        )
        db.session.add(new_order)
        db.session.commit()
        redirect(url_for(".index"))

    return render_template(
        "orders.html",
        assign_form=assign_form,
        your_open_orders=your_open_orders,
        close_form=close_form,
        # menu_items=menu_items_list,
        add_order_form=add_order_form,
    )


@bp.route("/<int:order_id>/close", methods=["POST"])
@login_required
def close(order_id):
    order_to_close = Order.query.get(order_id)
    order_to_close.finished = True
    db.session.commit()
    return redirect(url_for(".index"))


@bp.route("/<int:order_id>", methods=["POST"])
@login_required
def add_order(order_id):
    print(request.data)
    data = request.form.to_dict()
    print(data)
    return redirect(url_for(".index"))
