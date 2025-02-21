"""add User table

Revision ID: 6e40b4d2b2d4
Revises: 918e58bbdfb3
Create Date: 2025-02-20 16:46:27.846981

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "6e40b4d2b2d4"
down_revision: Union[str, None] = "918e58bbdfb3"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "users",
        sa.Column("id", sa.Integer, primary_key=True, nullable=False),
        sa.Column("email", sa.String, unique=True, nullable=False),
        sa.Column("password", sa.String, nullable=False),
        sa.Column(
            "created_at",
            sa.TIMESTAMP(True),
            server_default=sa.text("NOW()"),
            nullable=False,
        ),
    )
    pass


def downgrade() -> None:
    op.drop_table("users")
    pass
