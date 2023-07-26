"""credit table

Revision ID: 8e2f7994d23a
Revises: 5b9c9c207720
Create Date: 2023-07-26 04:04:57.862044

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8e2f7994d23a'
down_revision = '5b9c9c207720'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.execute("CREATE TABLE `shydans_accounting`.`credit_balance` (`id` INT NOT NULL AUTO_INCREMENT , `name` VARCHAR(255) NOT NULL , `credit` FLOAT NOT NULL , `created_at` DATETIME on update CURRENT_TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP , PRIMARY KEY (`id`)) ENGINE = InnoDB;")
    
    
def downgrade() -> None:
    op.drop_table("credit_balance")
