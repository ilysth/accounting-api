# from alembic import command
# from alembic.config import Config

from fastapi import FastAPI
from app.accounting import accounting
from app.dashboard import dashboard
from app.inventory import inventory
from app.crm import crm
from app.oauth import oauth

app = FastAPI(title="APP Features", description="App Integration Resources")

app.mount("/accounting", accounting.app)
app.mount("/dash", dashboard.app)
app.mount("/inventory", inventory.app)
app.mount("/crm", crm.app)
app.mount("/oauth", oauth.app)

# config_paths = [
#     'app/accounting/alembic.ini',
#     'app/dashboard/alembic.ini',
#     # 'app/crm/alembic.ini',
# ]

# for config_path in config_paths:
#     alembic_cfg = Config(config_path)
#     command.upgrade(alembic_cfg, 'head')
