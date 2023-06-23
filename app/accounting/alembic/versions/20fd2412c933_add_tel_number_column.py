"""add tel_number column

Revision ID: 20fd2412c933
Revises: 92b0161913e7
Create Date: 2023-06-21 04:05:31.960936

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '20fd2412c933'
down_revision = '92b0161913e7'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.execute("ALTER TABLE `supplier` ADD `tel_number` VARCHAR(255) NOT NULL AFTER `contact_number`;")


def downgrade() -> None:
    op.drop_column('supplier', 'tel_number')
