"""chart table

Revision ID: 1fea57136cc4
Revises: 
Create Date: 2023-05-30 07:53:18.985669

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1fea57136cc4'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.execute("CREATE TABLE `shydans_accounting`.`chart_of_accounts` (`id` INT NOT NULL AUTO_INCREMENT , `description` VARCHAR(255) NOT NULL , `account_type` VARCHAR(255) NOT NULL , `report_type` VARCHAR(255) NOT NULL , `created_at` DATETIME on update CURRENT_TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP , `is_deleted` INT NOT NULL DEFAULT '0' , PRIMARY KEY (`id`)) ENGINE = InnoDB;")


def downgrade() -> None:
    op.drop_table("chart_of_accounts")
