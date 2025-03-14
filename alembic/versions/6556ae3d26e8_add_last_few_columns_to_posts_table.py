"""add last few columns to posts table

Revision ID: 6556ae3d26e8
Revises: c0c4ad5e609e
Create Date: 2025-02-20 17:39:45.575912

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "6556ae3d26e8"
down_revision: Union[str, None] = "c0c4ad5e609e"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column(
        "posts",
        sa.Column("published", sa.Boolean, nullable=True, server_default="true"),
    )
    op.add_column(
        "posts",
        sa.Column(
            "created_at",
            sa.TIMESTAMP(True),
            server_default=sa.text("NOW()"),
            nullable=False,
        ),
    )
    pass


def downgrade() -> None:
    op.drop_column("posts", "published")
    op.drop_column("posts", "created_at")
    pass
