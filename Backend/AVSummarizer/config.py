import os

class Config(object):
    SECRET_KEY = os.urandom(24)
    CORS_HEADERS = ['Content-Type', 'Authorization']
    UPLOAD_FOLDER = os.path.abspath(os.path.dirname(__file__)) \
                    + '/resources/Mp3Files/'
    # AWS credentials
    ACCESS_KEY_ID = "AKIAVR2JSCFVAVI34XFX"
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