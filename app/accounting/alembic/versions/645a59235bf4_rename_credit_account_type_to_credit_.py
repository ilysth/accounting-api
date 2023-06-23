"""rename credit_account_type to credit_account_name

Revision ID: 645a59235bf4
Revises: ed9562743306
Create Date: 2023-06-20 06:17:02.371409

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '645a59235bf4'
down_revision = 'ed9562743306'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.execute("ALTER TABLE `journal_entry` CHANGE `credit_account_type` `credit_account_name` VARCHAR(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL;")


def downgrade() -> None:
    op.execute("ALTER TABLE `journal_entry` CHANGE `credit_account_name` `credit_account_type` VARCHAR(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL;")

