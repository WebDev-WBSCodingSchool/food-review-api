import os

class BaseConfig:
    PG_URI = os.getenv('PG_URI')