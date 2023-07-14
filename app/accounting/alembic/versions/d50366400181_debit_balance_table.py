"""debit balance table

Revision ID: d50366400181
Revises: 8f083fcded30
Create Date: 2023-07-14 04:46:21.857888

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd50366400181'
down_revision = '8f083fcded30'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.execute("CREATE TABLE `shydans_accounting`.`debit_balance` (`id` INT NOT NULL AUTO_INCREMENT , `name` VARCHAR(255) NOT NULL , `debit` FLOAT NOT NULL , `created_at` DATETIME on update CURRENT_TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP , PRIMARY KEY (`id`)) ENGINE = InnoDB;")


def downgrade() -> None:
    op.drop_table("debit_balance")
