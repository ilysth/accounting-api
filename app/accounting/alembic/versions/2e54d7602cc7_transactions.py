"""transaction

Revision ID: 2e54d7602cc7
Revises: 8e2f7994d23a
Create Date: 2023-09-15 08:38:59.529151

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2e54d7602cc7'
down_revision = '8e2f7994d23a'
branch_labels = None
depends_on = None


def upgrade() -> None:
      op.execute("CREATE TABLE `shydans_db`.`accounting_transaction` (`id` INT NOT NULL AUTO_INCREMENT , `journal_id` INT NOT NULL, `chart_id` INT NOT NULL , `amount` FLOAT NULL , `is_type` INT NOT NULL , `created_at` DATETIME ON UPDATE CURRENT_TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP, PRIMARY KEY (`id`), FOREIGN KEY (`journal_id`) REFERENCES `accounting_journal` (`id`), FOREIGN KEY (`chart_id`) REFERENCES `accounting_charts` (`id`)) ENGINE = InnoDB;")


def downgrade() -> None:
    op.drop_table("accounting_transaction")
