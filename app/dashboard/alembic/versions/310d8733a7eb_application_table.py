"""application table

Revision ID: 310d8733a7eb
Revises: 27d66f688f92
Create Date: 2023-08-23 07:17:34.390165

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '310d8733a7eb'
down_revision = '27d66f688f92'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.execute("CREATE TABLE `shydans_db`.`dashboard_apps` (`id` INT NOT NULL AUTO_INCREMENT , `app_id` INT NULL , `platform_id` INT NULL , `app_architecture` INT NULL , `app_version` INT NULL , `app_name` VARCHAR(255) NULL , `app_zip` VARCHAR(255) NULL , `download_url` VARCHAR(255) NULL , `compressed_size` VARCHAR(255) NULL , `version_notes` VARCHAR(255) NULL , PRIMARY KEY (`id`)) ENGINE = InnoDB;")


def downgrade() -> None:
    op.drop_table("dashboard_apps")
