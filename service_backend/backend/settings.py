"""Application configuration.
For local development, use a .env file to set environment variables.
"""
from environs import Env

env = Env()
env.read_env()


FLASK_ENV = env.str("FLASK_ENV", default="production")

available_environments = ["production", "development"]
if FLASK_ENV not in available_environments:
    raise Exception(
        f"""Wrong FLASK_ENV configuration as {FLASK_ENV}
        Use only {available_environments}"""
    )


# Base configuration
if FLASK_ENV == 'production':
    SECRET_KEY = env.str("SECRET_KEY")
else:
    DEBUG = env.bool("DEBUG", default=True)
    SECRET_KEY = env.str("SECRET_KEY", default="not-so-secret")


# Database configuration
if FLASK_ENV == 'production':
    DB_ENGINE = env.str("DB_ENGINE")
    DB_USER = env.str("DB_USER")
    DB_PASSWORD = env.str("DB_PASSWORD")
    DB_HOST = env.str("DB_HOST")
    DB_PORT = env.str("DB_PORT")
    DB_NAME = env.str("DB_NAME")
else:
    DB_ENGINE = env.str("DB_ENGINE", default="not-defined")
    DB_USER = env.str("DB_USER", default="not-defined")
    DB_PASSWORD = env.str("DB_PASSWORD", default="not-defined")
    DB_HOST = env.str("DB_HOST", default="not-defined")
    DB_PORT = env.str("DB_PORT", default="not-defined")
    DB_NAME = env.str("DB_NAME", default="not-defined")

DB_CONNECTION = f'{DB_ENGINE}://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}'
SQLALCHEMY_DATABASE_URI = f'{DB_CONNECTION}/{DB_NAME}'
SQLALCHEMY_TRACK_MODIFICATIONS = False


# Cache and crypt configuration
BCRYPT_LOG_ROUNDS = env.int("BCRYPT_LOG_ROUNDS", default=13)
CACHE_TYPE = "simple"  # Can be "memcached", "redis", etc.


# Authorization configuration.
if FLASK_ENV == 'production':
    EGI_CLIENT_ID = env.str("OIDC_CLIENT_ID")
    EGI_CLIENT_SECRET = env.str("OIDC_CLIENT_SECRET")
else:
    EGI_CLIENT_ID = env.str("OIDC_CLIENT_ID", default="not-defined")
    EGI_CLIENT_SECRET = env.str("OIDC_CLIENT_SECRET", default="not-defined")

ADMIN_ASSURANCE = env.str(
    "ADMIN_ASSURANCE",
    default="https://refeds.org/assurance/IAP/low")


# API specs configuration
API_TITLE = 'EOSC Performance API'
API_VERSION = 'v1'
OPENAPI_VERSION = "3.0.2"
OPENAPI_JSON_PATH = "api-spec.json"
OPENAPI_URL_PREFIX = "/"
OPENAPI_SWAGGER_UI_PATH = "/"
OPENAPI_SWAGGER_UI_URL = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
API_SPEC_OPTIONS = {
    'security': [{"bearerAuth": []}],
    'components': {
        "securitySchemes": {
            "bearerAuth": {
                "type": "http",
                "scheme": "bearer",
                "bearerFormat": "JWT"
            }
        }
    }
}
