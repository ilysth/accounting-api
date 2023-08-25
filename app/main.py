# from alembic import command
# from alembic.config import Config

from fastapi import FastAPI
from app.accounting import accounting
from app.dashboard import dashboard
from app.oauth import oauth
from app.bency import bency

app = FastAPI(title="APP Features", description="App Integration Resources")

app.mount("/accounting", accounting.app)
app.mount("/dashboard", dashboard.app)
app.mount("/oauth", oauth.app)
app.mount("/bency", bency.app)

# config_paths = [
#     'app/accounting/alembic.ini',
#     'app/users/alembic.ini',
# ]

# for config_path in config_paths:
#     alembic_cfg = Config(config_path)
#     command.upgrade(alembic_cfg, 'head')