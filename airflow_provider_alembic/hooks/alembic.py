"""inspired by https://github.com/gunziptarball/airflow-provider-alembic/"""
from airflow.hooks.base import BaseHook
from alembic.command import downgrade, upgrade, stamp, show, merge, history, heads, ensure_version, current, branches
from alembic.config import Config


class AlembicHook(BaseHook):
    """Thin wrapper around Alembic's Python SDK"""

    def __init__(self, conn_id: str, script_location):
        super().__init__()
        self.conn_id = conn_id
        self.script_location = script_location

        hook = BaseHook().get_connection(self.conn_id).get_hook()
        self.url = hook.get_sqlalchemy_engine().url

        cfg = Config()
        cfg.set_main_option("sqlalchemy.url", str(self.url))
        cfg.set_main_option("script_location", str(self.script_location))
        self.cfg = cfg

    # Not entirely sure what should get returned here????
    def get_conn(self) -> Config:
        return self.cfg

    def downgrade(self, *args, **kwargs):
        """https://alembic.sqlalchemy.org/en/latest/api/commands.html"""
        return downgrade(self.cfg, *args, **kwargs)

    def upgrade(self, *args, **kwargs):
        """https://alembic.sqlalchemy.org/en/latest/api/commands.html"""
        return upgrade(self.cfg, *args, **kwargs)

    def stamp(self, *args, **kwargs):
        """https://alembic.sqlalchemy.org/en/latest/api/commands.html"""
        return stamp(self.cfg, *args, **kwargs)

    def show(self, *args, **kwargs):
        """https://alembic.sqlalchemy.org/en/latest/api/commands.html"""
        return show(self.cfg, *args, **kwargs)

    def merge(self, *args, **kwargs):
        """https://alembic.sqlalchemy.org/en/latest/api/commands.html"""
        return merge(self.cfg, *args, **kwargs)

    def history(self, *args, **kwargs):
        """https://alembic.sqlalchemy.org/en/latest/api/commands.html"""
        return history(self.cfg, *args, **kwargs)

    def heads(self, *args, **kwargs):
        """https://alembic.sqlalchemy.org/en/latest/api/commands.html"""
        return heads(self.cfg, *args, **kwargs)

    def ensure_version(self, *args, **kwargs):
        """https://alembic.sqlalchemy.org/en/latest/api/commands.html"""
        return ensure_version(self.cfg, *args, **kwargs)

    def current(self, *args, **kwargs):
        """https://alembic.sqlalchemy.org/en/latest/api/commands.html"""
        return current(self.cfg, *args, **kwargs)

    def branches(self, *args, **kwargs):
        """https://alembic.sqlalchemy.org/en/latest/api/commands.html"""
        return branches(self.cfg, *args, **kwargs)
