import os
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY", "dev-secret")
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL", "sqlite:///" + os.path.join(BASE_DIR, "csr_system.db"))
    #SQLALCHEMY_TRACKING_MODIFICATIONS = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
