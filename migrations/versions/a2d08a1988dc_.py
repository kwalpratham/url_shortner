"""empty message

Revision ID: a2d08a1988dc
Revises: b13d2cd88921
Create Date: 2023-09-15 12:33:47.669334

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a2d08a1988dc'
down_revision = 'b13d2cd88921'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('short_urls', schema=None) as batch_op:
        batch_op.alter_column('original_url',
               existing_type=sa.VARCHAR(length=500),
               type_=sa.String(length=1000),
               existing_nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('short_urls', schema=None) as batch_op:
        batch_op.alter_column('original_url',
               existing_type=sa.String(length=1000),
               type_=sa.VARCHAR(length=500),
               existing_nullable=False)

    # ### end Alembic commands ###
