"""journal table

Revision ID: d372734c9b17
Revises: e26b33b2893a
Create Date: 2023-07-26 04:03:44.981779

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd372734c9b17'
down_revision = 'e26b33b2893a'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.execute("CREATE TABLE `shydans_accounting`.`journal_entry` (`id` INT NOT NULL AUTO_INCREMENT, `supplier_id` INT NULL, `document_no` VARCHAR(255) NOT NULL, `debit_acct_id` INT NULL, `credit_acct_id` INT NULL, `debit` FLOAT NOT NULL, `credit` FLOAT NOT NULL, `date` DATETIME NOT NULL, `notes` VARCHAR(255) NOT NULL, `created_at` DATETIME ON UPDATE CURRENT_TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP, `is_supplier` INT NOT NULL DEFAULT '0', PRIMARY KEY (`id`), FOREIGN KEY (`supplier_id`) REFERENCES `supplier` (`id`), FOREIGN KEY (`debit_acct_id`) REFERENCES `chart_of_accounts` (`id`), FOREIGN KEY (`credit_acct_id`) REFERENCES `chart_of_accounts` (`id`)) ENGINE=InnoDB;")


def downgrade() -> None:
    op.drop_table("journal_entry")
