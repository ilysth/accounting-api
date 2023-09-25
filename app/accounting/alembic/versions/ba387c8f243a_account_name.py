"""account name

Revision ID: ba387c8f243a
Revises: 8e2f7994d23a
Create Date: 2023-09-15 07:38:33.457786

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ba387c8f243a'
down_revision = '1fea57136cc4'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.execute("CREATE TABLE `shydans_db`.`accounting_charts` (`id` INT NOT NULL AUTO_INCREMENT , `frame_id` INT NOT NULL, `name` VARCHAR(255) NOT NULL , `account_type` VARCHAR(255) NOT NULL , `code` VARCHAR(255) NOT NULL , `created_at` DATETIME on update CURRENT_TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP , PRIMARY KEY (`id`), FOREIGN KEY (`frame_id`) REFERENCES `accounting_frame` (`id`)) ENGINE = InnoDB;")

def downgrade() -> None:
    op.drop_table("accounting_charts")
