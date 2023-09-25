"""department

Revision ID: 3c8d0019257a
Revises: e669efa3197e
Create Date: 2023-09-15 08:22:53.529685

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3c8d0019257a'
down_revision = 'e669efa3197e'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.execute("CREATE TABLE `shydans_db`.`accounting_company_department` (`id` INT NOT NULL AUTO_INCREMENT , `company_id` INT NOT NULL, `name` VARCHAR(255) NOT NULL , `code` VARCHAR(255) NOT NULL ,`created_at` DATETIME ON UPDATE CURRENT_TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP, PRIMARY KEY (`id`),FOREIGN KEY (`company_id`) REFERENCES `accounting_company` (`id`)) ENGINE = InnoDB;")


def downgrade() -> None:
    op.drop_table("accounting_company_department")
