"""Create posts table

Revision ID: 0fcc27b62b34
Revises: 
Create Date: 2025-02-19 19:29:43.273446

"""

from typing import Sequence, Union

from alembic import op
from sqlalchemy import Column, Integer


# revision identifiers, used by Alembic.
revision: str = "0fcc27b62b34"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "posts",
        Column("id", Integer, primary_key=True, nullable=False),
        Column("title", Integer, nullable=False),
    )
    pass


def downgrade() -> None:
    op.drop_table("posts")
    pass
