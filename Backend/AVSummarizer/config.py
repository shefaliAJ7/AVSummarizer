import os

class Config(object):
    SECRET_KEY = os.urandom(24)
    CORS_HEADERS = ['Content-Type', 'Authorization']
    UPLOAD_FOLDER = os.path.abspath(os.path.dirname(__file__)) \
                    + '\\resources\\AudioFiles\\'

class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    TESTING = True
    DEBUG = True


class ProductionConfig(Config):
    TESTING = False
    DEBUG = False


app_config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
}