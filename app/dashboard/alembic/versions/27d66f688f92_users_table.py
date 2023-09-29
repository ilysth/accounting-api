"""users table

Revision ID: 27d66f688f92
Revises: 
Create Date: 2023-06-30 05:33:11.997660

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '27d66f688f92'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.execute("CREATE TABLE `shydans_db`.`dashboard_users` (`id` INT NOT NULL AUTO_INCREMENT , `username` VARCHAR(255) NULL , `password` VARCHAR(255) NULL , `role` INT NULL , `fname` VARCHAR(255) NULL , `lname` VARCHAR(255) NULL , `email` VARCHAR(255) NULL , `contact` VARCHAR(255) NULL , `image` VARCHAR(255) NULL , `apps` VARCHAR(255) NULL , `country` INT NULL , `creation_date` DATE NOT NULL , `creation_update` DATETIME on update CURRENT_TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP , `is_superuser` BOOLEAN NULL , PRIMARY KEY (`id`)) ENGINE = InnoDB;")

def downgrade() -> None:
    op.drop_table("dashboard_users")
