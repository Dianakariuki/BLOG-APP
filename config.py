import os 

class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY")
    SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://diana:access@localhost/blog"
    UPLOADED_PHOTOS_DEST = "app/static/photos"

    # email configurations
    MAIL_SERVER = "smtp.gmail.com"
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")

class ProdConfig(Config):
    
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")

class TestConfig(Config):
    
    SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://pxlzdvfgdqaacy:d1854c827a7960d0734226abed26a58ee9059c1e03e6c29d8d7f990d3c6ee479@ec2-44-195-169-163.compute-1.amazonaws.com:5432/d5vfmr5fgvjli4"

class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://pxlzdvfgdqaacy:d1854c827a7960d0734226abed26a58ee9059c1e03e6c29d8d7f990d3c6ee479@ec2-44-195-169-163.compute-1.amazonaws.com:5432/d5vfmr5fgvjli4"
    DEBUG = True


config_options = {
    "development": DevConfig,
    "production": ProdConfig,
    "test": TestConfig
}