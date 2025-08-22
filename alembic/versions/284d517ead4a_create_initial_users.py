"""create initial users

Revision ID: 284d517ead4a
Revises: 9df287856594
Create Date: 2025-07-21 22:27:46.509714

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '284d517ead4a'
down_revision: Union[str, None] = '9df287856594'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    import uuid
    from datetime import datetime

    # Password hashes generated with get_password_hash
    marketing_password = '$2b$12$rOrCDA//i5hC3rZylk.Kj.mFFOBOE9S65ezfRoY2VY.c6MfPKanru'
    developer_password = '$2b$12$7c6HVPorQxzvmAcsz2U7heVauIK.pz1axhXjILlWeAy/pvyuK4a0K'

    users = [
        # Marketing
        {"username": "haidar", "password": marketing_password, "email": "haidar@cakai.dev", "team": "marketing", "full_name": "haidar"},
        {"username": "daffa", "password": marketing_password, "email": "daffa@cakai.dev", "team": "marketing", "full_name": "daffa"},
        {"username": "raiyen", "password": marketing_password, "email": "raiyen@cakai.dev", "team": "marketing", "full_name": "raiyen"},
        {"username": "salva", "password": marketing_password, "email": "salva@cakai.dev", "team": "marketing", "full_name": "salva"},
        # Developer
        {"username": "dio", "password": developer_password, "email": "dio@cakai.dev", "team": "developer", "full_name": "dio"},
        {"username": "yosh", "password": developer_password, "email": "yosh@cakai.dev", "team": "developer", "full_name": "yosh"},
        {"username": "rizgi", "password": developer_password, "email": "rizgi@cakai.dev", "team": "developer", "full_name": "rizgi"},
    ]

    for user in users:
        op.execute(f"""
            INSERT INTO users (id, username, full_name, password, email, team, created_at, created_by, updated_at, updated_by)
            VALUES ('{{}}', '{{}}', '{{}}', '{{}}', '{{}}', '{{}}', now(), 'SYSTEM', now(), 'SYSTEM')
        """.format(str(uuid.uuid4()), user["username"], user["full_name"], user["password"], user["email"], user["team"]))


def downgrade() -> None:
    usernames = [
        "haidar", "daffa", "raiyen", "salva",
        "dio", "yosh", "rizgi"
    ]
    for username in usernames:
        op.execute(f"DELETE FROM users WHERE username = '{{}}'".format(username))
