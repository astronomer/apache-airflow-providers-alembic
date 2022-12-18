"""inspired by https://github.com/gunziptarball/airflow-provider-alembic/"""
from typing import Any

from airflow.models import BaseOperator
from airflow.utils.context import Context

from astronomer.providers.alembic.hooks.alembic import AlembicHook


class AlembicOperator(BaseOperator):
    template_fields = ['conn_id', 'command', 'script_location', 'revision']
    ui_color = "#cdaaed"

    def __init__(
            self,
            conn_id: str,
            command: str,
            script_location: str,
            revision: str = 'head',
            command_kwargs: dict | None = None,
            *args,
            **kwargs
    ):
        """
        :param conn_id: Connection to use to run migrations against
        :param command: a command, as outlined here:
        :param script_location:
        :param revision:
        :param args:
        :param kwargs:
        """
        super(AlembicOperator, self).__init__(*args, **kwargs)
        self.command_kwargs = command_kwargs or {}
        self.revision = revision
        self.script_location = script_location
        self.command = command
        self.conn_id = conn_id

    def execute(self, context: Context) -> Any:
        hook = AlembicHook(
            conn_id=self.conn_id,
            script_location=self.script_location
        )
        return getattr(hook, self.command)(self.revision, **self.command_kwargs)
