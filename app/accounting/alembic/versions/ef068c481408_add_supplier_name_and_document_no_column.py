"""add supplier name and document no column

Revision ID: ef068c481408
Revises: 9bbd381bb49f
Create Date: 2023-06-23 08:44:35.710478

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ef068c481408'
down_revision = '9bbd381bb49f'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.execute("ALTER TABLE `journal_entry` ADD `supplier_name` VARCHAR(255) NOT NULL AFTER `id`, ADD `document_no` VARCHAR(255) NOT NULL AFTER `supplier_name`;")


def downgrade() -> None:
    op.drop_column('journal_entry', 'supplier_name')
    op.drop_column('journal_entry', 'document_no')
