"""supplier table

Revision ID: 8f083fcded30
Revises: 1215f29b7210
Create Date: 2023-07-14 03:58:34.003318

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8f083fcded30'
down_revision = '1215f29b7210'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.execute("CREATE TABLE `shydans_accounting`.`supplier` (`id` INT NOT NULL AUTO_INCREMENT , `first_name` VARCHAR(255) NOT NULL , `last_name` VARCHAR(255) NOT NULL , `business_type` VARCHAR(255) NOT NULL , `email` VARCHAR(255) NOT NULL , `contact_number` VARCHAR(255) NOT NULL , `tel_number` VARCHAR(255) NOT NULL , `address` VARCHAR(255) NOT NULL , `tin` VARCHAR(255) NOT NULL , `sec` VARCHAR(255) NOT NULL , `dti` VARCHAR(255) NOT NULL , `created_at` DATETIME on update CURRENT_TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP , PRIMARY KEY (`id`)) ENGINE = InnoDB;")


def downgrade() -> None:
    op.drop_table("supplier")
