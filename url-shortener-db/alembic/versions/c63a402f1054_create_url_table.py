"""create url table

Revision ID: c63a402f1054
Revises:
Create Date: 2022-04-13 22:10:11.084345

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "c63a402f1054"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "URL",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("short_url", sa.String(), nullable=False),
        sa.Column("long_url", sa.String(), nullable=False),
    )


def downgrade():
    op.drop_table("URL")
