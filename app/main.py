from alembic import command
from alembic.config import Config

from fastapi import FastAPI
from app.accounting import accounting
from app.users import users
from app.oauth import oauth

app = FastAPI(title="APP Features", description="App Integration Resources")

app.mount("/accounting", accounting.app)
app.mount("/users", users.app)
app.mount("/oauth", oauth.app)

# config_paths = [
#     'app/accounting/alembic.ini',
# ]

# for config_path in config_paths:
#     alembic_cfg = Config(config_path)
#     command.upgrade(alembic_cfg, 'head')