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
    op.execute("CREATE TABLE `shydans_users`.`users` (`id` INT NOT NULL AUTO_INCREMENT , `username` VARCHAR(255) NOT NULL , `password` VARCHAR(255) NOT NULL , `first_name` VARCHAR(255) NOT NULL , `last_name` VARCHAR(255) NOT NULL , `role` INT NOT NULL , `created_at` DATETIME on update CURRENT_TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP , `creation_update` DATE NOT NULL , PRIMARY KEY (`id`)) ENGINE = InnoDB;")

def downgrade() -> None:
    op.drop_table("users")
