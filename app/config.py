import os


class Configuration:
    SECRET_KEY = os.environ.get("SECRET_KEY")
    SQLALCHEMY_DATABASE_URI = (
        os.environ.get("DATABASE_URL")
        # or "postgresql://oder_up:9uCxydbt@localhost/order_up_dv"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
