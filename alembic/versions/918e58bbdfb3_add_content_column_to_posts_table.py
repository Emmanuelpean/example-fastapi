"""add content column to posts table

Revision ID: 918e58bbdfb3
Revises: 0fcc27b62b34
Create Date: 2025-02-20 16:40:13.329201

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "918e58bbdfb3"
down_revision: Union[str, None] = "0fcc27b62b34"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column("posts", sa.Column("content", sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column("posts", "content")
    pass
