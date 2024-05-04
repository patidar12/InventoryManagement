from app.config.config_parser import config_args

args = config_args

class AppConfig(object):
    PORT = args.port
    APP_NAME = "catalog"
    POSTGRES_DATABASES = {
        "catalog": {
            "host": args.postgres_catalog_read_write
        }
    }