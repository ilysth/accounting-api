"""rename description column to account_name

Revision ID: 36a223f4a521
Revises: 1fea57136cc4
Create Date: 2023-06-05 03:36:25.204035

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '36a223f4a521'
down_revision = '1fea57136cc4'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.execute("ALTER TABLE `chart_of_accounts` CHANGE `description` `account_name` VARCHAR(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL;")


def downgrade() -> None:
    op.execute("ALTER TABLE `chart_of_accounts` CHANGE `account_name` `description` VARCHAR(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL;")

