"""empty message

Revision ID: e94caecdba42
Revises: 4a98e8229206
Create Date: 2022-03-05 13:50:26.557237

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e94caecdba42'
down_revision = '4a98e8229206'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('user_profiles_email_key', 'user_profiles', type_='unique')
    op.drop_column('user_profiles', 'email')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user_profiles', sa.Column('email', sa.VARCHAR(length=255), autoincrement=False, nullable=True))
    op.create_unique_constraint('user_profiles_email_key', 'user_profiles', ['email'])
    # ### end Alembic commands ###
