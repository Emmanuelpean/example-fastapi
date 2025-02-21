"""add foreign key to posts table

Revision ID: c0c4ad5e609e
Revises: 6e40b4d2b2d4
Create Date: 2025-02-20 17:34:35.975786

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "c0c4ad5e609e"
down_revision: Union[str, None] = "6e40b4d2b2d4"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column("posts", sa.Column("owner_id", sa.Integer, nullable=False))
    op.create_foreign_key(
        "post_user_fk",
        source_table="posts",
        referent_table="users",
        local_cols=["owner_id"],
        remote_cols=["id"],
        ondelete="CASCADE",
    )
    pass


def downgrade() -> None:
    op.drop_constraint("post_user_fk", "posts")
    op.drop_column("posts", "owner_id")
    pass
