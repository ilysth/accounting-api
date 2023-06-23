"""supplier table

Revision ID: 92b0161913e7
Revises: 1f3c06e96636
Create Date: 2023-06-21 03:28:29.737146

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '92b0161913e7'
down_revision = '1f3c06e96636'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.execute("CREATE TABLE `shydans_accounting`.`supplier` (`id` INT NOT NULL AUTO_INCREMENT , `business_type` VARCHAR(255) NOT NULL , `first_name` VARCHAR(255) NOT NULL , `last_name` VARCHAR(255) NOT NULL , `email` VARCHAR(255) NOT NULL , `contact_number` VARCHAR(255) NOT NULL , `address` VARCHAR(255) NOT NULL , `tin` VARCHAR(255) NOT NULL , `sec_registration` VARCHAR(255) NOT NULL , `dti_registration` VARCHAR(255) NOT NULL , PRIMARY KEY (`id`)) ENGINE = InnoDB;")


def downgrade() -> None:
    op.drop_table("supplier")
