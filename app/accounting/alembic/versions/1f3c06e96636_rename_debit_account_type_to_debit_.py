"""rename debit_account_type to debit_account_name

Revision ID: 1f3c06e96636
Revises: 645a59235bf4
Create Date: 2023-06-20 06:21:50.661368

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1f3c06e96636'
down_revision = '645a59235bf4'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.execute("ALTER TABLE `journal_entry` CHANGE `debit_account_type` `debit_account_name` VARCHAR(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL;")


def downgrade() -> None:
    op.execute("ALTER TABLE `journal_entry` CHANGE `debit_account_name` `debit_account_type` VARCHAR(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL;")
