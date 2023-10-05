"""add is_deleted column

Revision ID: 234ecdad4051
Revises: f35abb3eb848
Create Date: 2023-10-04 06:37:51.615300

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '234ecdad4051'
down_revision = 'f35abb3eb848'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.execute("ALTER TABLE `accounting_frame` ADD `is_deleted` INT NULL DEFAULT '0' AFTER `code`;")
    op.execute("ALTER TABLE `accounting_charts` ADD `is_deleted` INT NULL DEFAULT '0' AFTER `code`;")
    op.execute("ALTER TABLE `accounting_company` ADD `is_deleted` INT NULL DEFAULT '0' AFTER `code`;")
    op.execute("ALTER TABLE `accounting_department` ADD `is_deleted` INT NULL DEFAULT '0' AFTER `code`;")

def downgrade() -> None:
    op.drop_column("accounting_frame", "is_deleted")
    op.drop_column("accounting_charts", "is_deleted")
    op.drop_column("accounting_company", "is_deleted")
    op.drop_column("accounting_department", "is_deleted")
