"""empty message

Revision ID: d079d7c6fd7b
Revises: 
Create Date: 2021-11-24 05:26:03.531593

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd079d7c6fd7b'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('HICEN_SCSC',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('subject', sa.String(length=200), nullable=False),
    sa.Column('writer', sa.String(length=20), nullable=False),
    sa.Column('date', sa.String(length=20), nullable=False),
    sa.Column('link', sa.String(length=400), nullable=False),
    sa.Column('width', sa.Integer(), nullable=False),
    sa.Column('height', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_HICEN_SCSC'))
    )
    op.create_table('HICEN_class',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('subject', sa.String(length=200), nullable=False),
    sa.Column('writer', sa.String(length=20), nullable=False),
    sa.Column('date', sa.String(length=20), nullable=False),
    sa.Column('link', sa.String(length=400), nullable=False),
    sa.Column('width', sa.Integer(), nullable=False),
    sa.Column('height', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_HICEN_class'))
    )
    op.create_table('HICEN_department',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('subject', sa.String(length=200), nullable=False),
    sa.Column('writer', sa.String(length=20), nullable=False),
    sa.Column('date', sa.String(length=20), nullable=False),
    sa.Column('link', sa.String(length=400), nullable=False),
    sa.Column('width', sa.Integer(), nullable=False),
    sa.Column('height', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_HICEN_department'))
    )
    op.create_table('HICEN_employment',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('subject', sa.String(length=200), nullable=False),
    sa.Column('writer', sa.String(length=20), nullable=False),
    sa.Column('date', sa.String(length=20), nullable=False),
    sa.Column('link', sa.String(length=400), nullable=False),
    sa.Column('width', sa.Integer(), nullable=False),
    sa.Column('height', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_HICEN_employment'))
    )
    op.create_table('HICEN_scholarship',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('subject', sa.String(length=200), nullable=False),
    sa.Column('writer', sa.String(length=20), nullable=False),
    sa.Column('date', sa.String(length=20), nullable=False),
    sa.Column('link', sa.String(length=400), nullable=False),
    sa.Column('width', sa.Integer(), nullable=False),
    sa.Column('height', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_HICEN_scholarship'))
    )
    op.create_table('HIUN_contest',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('subject', sa.String(length=200), nullable=False),
    sa.Column('writer', sa.String(length=20), nullable=False),
    sa.Column('date', sa.String(length=20), nullable=False),
    sa.Column('link', sa.String(length=400), nullable=False),
    sa.Column('width', sa.Integer(), nullable=False),
    sa.Column('height', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_HIUN_contest'))
    )
    op.create_table('HIUN_corona',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('subject', sa.String(length=200), nullable=False),
    sa.Column('writer', sa.String(length=20), nullable=False),
    sa.Column('date', sa.String(length=20), nullable=False),
    sa.Column('link', sa.String(length=400), nullable=False),
    sa.Column('width', sa.Integer(), nullable=False),
    sa.Column('height', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_HIUN_corona'))
    )
    op.create_table('HIUN_generalno',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('subject', sa.String(length=200), nullable=False),
    sa.Column('writer', sa.String(length=20), nullable=False),
    sa.Column('date', sa.String(length=20), nullable=False),
    sa.Column('link', sa.String(length=400), nullable=False),
    sa.Column('width', sa.Integer(), nullable=False),
    sa.Column('height', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_HIUN_generalno'))
    )
    op.create_table('HIUN_studentsno',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('subject', sa.String(length=200), nullable=False),
    sa.Column('writer', sa.String(length=20), nullable=False),
    sa.Column('date', sa.String(length=20), nullable=False),
    sa.Column('link', sa.String(length=400), nullable=False),
    sa.Column('width', sa.Integer(), nullable=False),
    sa.Column('height', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_HIUN_studentsno'))
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('HIUN_studentsno')
    op.drop_table('HIUN_generalno')
    op.drop_table('HIUN_corona')
    op.drop_table('HIUN_contest')
    op.drop_table('HICEN_scholarship')
    op.drop_table('HICEN_employment')
    op.drop_table('HICEN_department')
    op.drop_table('HICEN_class')
    op.drop_table('HICEN_SCSC')
    # ### end Alembic commands ###
