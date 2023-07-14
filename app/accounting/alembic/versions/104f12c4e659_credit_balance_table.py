"""credit balance table

Revision ID: 104f12c4e659
Revises: d50366400181
Create Date: 2023-07-14 06:03:45.716595

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '104f12c4e659'
down_revision = 'd50366400181'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.execute("CREATE TABLE `shydans_accounting`.`credit_balance` (`id` INT NOT NULL AUTO_INCREMENT , `name` VARCHAR(255) NOT NULL , `credit` FLOAT NOT NULL , `created_at` DATETIME on update CURRENT_TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP , PRIMARY KEY (`id`)) ENGINE = InnoDB;")
    
    
def downgrade() -> None:
    op.drop_table("credit_balance")
