"""create url table

Revision ID: 4da5f792dafa
Revises: 
Create Date: 2022-04-13 19:27:51.465338

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4da5f792dafa'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
     op.create_table(
        'URL',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('short_url', sa.String(), nullable=False),
        sa.Column('long_url', sa.String(), nullable=False),
    )


def downgrade():
    op.drop_table('URL')
