"""journal entry table

Revision ID: ed9562743306
Revises: 36a223f4a521
Create Date: 2023-06-07 03:17:56.007962

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ed9562743306'
down_revision = '36a223f4a521'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.execute("CREATE TABLE `shydans_accounting`.`journal_entry` (`id` INT NOT NULL AUTO_INCREMENT , `debit_account_type` VARCHAR(255) NOT NULL , `credit_account_type` VARCHAR(255) NOT NULL , `debit` VARCHAR(255) NOT NULL , `credit` VARCHAR(255) NOT NULL , `date` DATETIME NOT NULL , `notes` VARCHAR(255) NOT NULL , `created_at` DATETIME on update CURRENT_TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP , `is_deleted` INT NOT NULL DEFAULT '0' , PRIMARY KEY (`id`)) ENGINE = InnoDB;")


def downgrade() -> None:
    op.drop_table("journal_entry")
