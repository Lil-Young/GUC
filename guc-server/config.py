import os
from dotenv import load_dotenv

BASEDIR = os.path.abspath(os.path.dirname(__file__))
APP_NAME = 'GUC'
FLASK_CONFIG = os.getenv('FLASK_CONFIG') or 'development'
load_dotenv(verbose=True)

class Config:
    ''' General Config'''
    SLOW_API_TIME = 0.5
    API_LOGGING = False
    JSON_AS_ASCII = False
    JWT_TOKEN_LOCATION = ['headers']
    JWT_ACCESS_TOKEN_EXPIRES = 60 * 24 * 365
    JWT_REFRESH_TOKEN_EXPIRES = 60 * 24 * 365
    JWT_SESSION_COOKIE = False

    # MYSQL
    MYSQL_HOST = os.environ[APP_NAME + "_MYSQL_HOST"]
    MYSQL_PORT = os.environ[APP_NAME + "_MYSQL_PORT"]
    MYSQL_USER = os.environ[APP_NAME + "_MYSQL_USER"]
    MYSQL_PASSWORD = os.environ[APP_NAME + "_MYSQL_PASSWORD"]
    MYSQL_NAME = os.environ[APP_NAME + "_MYSQL_NAME"]

    # MongoDB
    MONGODB_URI = os.environ[APP_NAME + "_MONGODB_URI"]
    MONGODB_NAME = os.environ[APP_NAME + "_MONGODB_NAME"]

    @staticmethod
    def init_app(app):
        pass

if FLASK_CONFIG == 'development':
    class AppConfig(Config):
        DEBUG = True
        TESTING = False

elif FLASK_CONFIG == 'production':
    class AppConfig(Config):
        DEBUG = False
        TESTING = False
else:
    raise Exception("FLASK Config not Selected")
    
config = AppConfig

class TestConfig(Config):
    DEBUG = True
    TESTING = True

if __name__ == '__main__':
    pass