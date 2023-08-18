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
    op.execute("CREATE TABLE `shydans_db`.`accounting_journal` (`id` INT NOT NULL AUTO_INCREMENT, `supplier_id` INT NULL, `document_no` VARCHAR(255) NULL, `debit_acct_id` INT NULL, `credit_acct_id` INT NULL, `debit` FLOAT NULL, `credit` FLOAT NULL, `date` DATETIME NOT NULL, `notes` VARCHAR(255) NULL, `created_at` DATETIME ON UPDATE CURRENT_TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP, `is_supplier` INT NOT NULL DEFAULT '0', PRIMARY KEY (`id`), FOREIGN KEY (`supplier_id`) REFERENCES `accounting_supplier` (`id`), FOREIGN KEY (`debit_acct_id`) REFERENCES `accounting_chart` (`id`), FOREIGN KEY (`credit_acct_id`) REFERENCES `accounting_chart` (`id`)) ENGINE=InnoDB;")


def downgrade() -> None:
    op.drop_table("accounting_journal")
