"""auto-vote

Revision ID: a4002cafe0a5
Revises: 6556ae3d26e8
Create Date: 2025-02-20 17:52:29.643594

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "a4002cafe0a5"
down_revision: Union[str, None] = "6556ae3d26e8"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "votes",
        sa.Column("user_id", sa.Integer(), nullable=False),
        sa.Column("post_id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(["post_id"], ["posts.id"], ondelete="CASCADE"),
        sa.ForeignKeyConstraint(["user_id"], ["users.id"], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("user_id", "post_id"),
    )
    op.alter_column(
        "posts",
        "title",
        existing_type=sa.INTEGER(),
        type_=sa.String(),
        existing_nullable=False,
    )
    op.alter_column(
        "posts",
        "published",
        existing_type=sa.BOOLEAN(),
        nullable=False,
        existing_server_default=sa.text("true"),
    )
    op.create_index(op.f("ix_posts_title"), "posts", ["title"], unique=False)
    op.add_column("users", sa.Column("username", sa.String(), nullable=False))
    op.create_index(op.f("ix_users_username"), "users", ["username"], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f("ix_users_username"), table_name="users")
    op.drop_column("users", "username")
    op.drop_index(op.f("ix_posts_title"), table_name="posts")
    op.alter_column(
        "posts",
        "published",
        existing_type=sa.BOOLEAN(),
        nullable=True,
        existing_server_default=sa.text("true"),
    )
    op.alter_column(
        "posts",
        "title",
        existing_type=sa.String(),
        type_=sa.INTEGER(),
        existing_nullable=False,
    )
    op.drop_table("votes")
    # ### end Alembic commands ###
