from flask import Blueprint, render_template
from flask_login import login_required
from ..forms import AssignTableForm
from ..models import Employee, Table, Order

bp = Blueprint("orders", __name__, url_prefix="")


@bp.route("/")
@login_required
def index():
    form = AssignTableForm()

    # Assign Table form queries
    tables = Table.query.order_by(Table.number).all()
    servers = Employee.query.order_by(Employee.employee_number).all()
    open_orders = Order.query.filter(Order.finished is False)

    busy_table_ids = [order.table_id for order in open_orders]

    open_tables = [table for table in tables if table.id not in busy_table_ids]

    form.tables.choices = [(t.id, f"Table {t.number}") for t in open_tables]
    form.servers.choices = [(s.employee_number, f"{s.name}") for s in servers]

    return render_template("orders.html", form=form)


@bp.route("/assign", methods=["POST"])
def assign():
    form = AssignTableForm()
    tables = Table.query.order_by(Table.number).all()
    open_orders = Order.query.filter(Order.finished is False)

    busy_table_ids = [order.table_id for order in open_orders]

    open_tables = [table for table in tables if table.id not in busy_table_ids]

    form.tables.choices = [(t.id, f"Table {t.number}") for t in open_tables]
