"""journal table

Revision ID: 1215f29b7210
Revises: 1fea57136cc4
Create Date: 2023-07-14 03:49:30.963433

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1215f29b7210'
down_revision = '1fea57136cc4'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.execute("CREATE TABLE `shydans_accounting`.`journal_entry` (`id` INT NOT NULL AUTO_INCREMENT, `supplier_name` VARCHAR(255) NOT NULL, `document_no` VARCHAR(255) NOT NULL, `debit_acct_id` INT NOT NULL DEFAULT '0', `credit_acct_id` INT NOT NULL DEFAULT '0', `debit` FLOAT NOT NULL, `credit` FLOAT NOT NULL, `date` DATETIME NOT NULL, `notes` VARCHAR(255) NOT NULL, `created_at` DATETIME ON UPDATE CURRENT_TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP, `is_supplier` INT NOT NULL DEFAULT '0', PRIMARY KEY (`id`), FOREIGN KEY (`debit_acct_id`) REFERENCES `chart_of_accounts` (`id`), FOREIGN KEY (`credit_acct_id`) REFERENCES `chart_of_accounts` (`id`)) ENGINE=InnoDB;")


def downgrade() -> None:
    op.drop_table("journal_entry")