import os

class Config(object):
    SECRET_KEY = os.urandom(24)
    CORS_HEADERS = ['Content-Type', 'Authorization']
    UPLOAD_FOLDER = os.path.abspath(os.path.dirname(__file__)) \
                    + '\\resources\\AudioFiles\\'
    # AWS credentials
    ACCESS_KEY_ID = "AKIAVR2JSCFVBIFRQKZY"
    ACCESS_SECRET_KEY = "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"
    BUCKET_NAME = "avsummarizer"

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