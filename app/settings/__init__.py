import os
import importlib
import ssl
from funcy import distinct, remove

from .helpers import (
    fix_assets_path,
    array_from_string,
    parse_boolean,
    int_or_none,
    set_from_string,
    add_decode_responses_to_redis_url,
)

# _REDIS_URL is the unchanged REDIS_URL we get from env vars, to be used later with RQ
_REDIS_URL = os.environ.get(
    "REDASH_REDIS_URL", os.environ.get("REDIS_URL", "redis://localhost:6379/0")
)
# This is the one to use for Redash' own connection:
REDIS_URL = add_decode_responses_to_redis_url(_REDIS_URL)

# Database settings
SQLALCHEMY_DATABASE_URI = os.environ.get('JOB_DATABASE_URL', "postgresql://postgres@localhost:5432/postgres")