"""add particulars column to journal table

Revision ID: f35abb3eb848
Revises: 2e54d7602cc7
Create Date: 2023-10-02 03:44:54.641706

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f35abb3eb848'
down_revision = '2e54d7602cc7'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.execute("ALTER TABLE `accounting_transaction` ADD `particulars` VARCHAR(255) NULL AFTER `amount`;")


def downgrade() -> None:
    op.drop_column("accounting_transaction", "particulars")
