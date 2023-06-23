"""rename is_deleted to is_supplier

Revision ID: 9bbd381bb49f
Revises: 20fd2412c933
Create Date: 2023-06-23 07:01:46.482137

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9bbd381bb49f'
down_revision = '20fd2412c933'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.execute("ALTER TABLE `journal_entry` CHANGE `is_deleted` `is_supplier` INT NOT NULL DEFAULT '0';")


def downgrade() -> None:
    op.execute("ALTER TABLE `journal_entry` CHANGE `is_supplier` `is_deleted`  INT NOT NULL DEFAULT '0';")
