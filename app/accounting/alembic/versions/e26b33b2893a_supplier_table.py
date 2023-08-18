"""supplier table

Revision ID: e26b33b2893a
Revises: 1fea57136cc4
Create Date: 2023-07-26 04:02:54.089968

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e26b33b2893a'
down_revision = '1fea57136cc4'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.execute("CREATE TABLE `shydans_accounting`.`supplier` (`id` INT NOT NULL AUTO_INCREMENT , `first_name` VARCHAR(255) NOT NULL , `last_name` VARCHAR(255) NOT NULL , `business_type` VARCHAR(255) NULL , `email` VARCHAR(255) NULL , `contact_number` VARCHAR(255) NULL , `tel_number` VARCHAR(255) NULL , `address` VARCHAR(255) NULL , `tin` VARCHAR(255) NULL , `sec` VARCHAR(255) NULL , `dti` VARCHAR(255) NULL , `created_at` DATETIME on update CURRENT_TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP , PRIMARY KEY (`id`)) ENGINE = InnoDB;")


def downgrade() -> None:
    op.drop_table("supplier")
