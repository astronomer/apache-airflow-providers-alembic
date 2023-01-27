import os
from datetime import datetime

from airflow.models import DAG
from airflow.models.param import Param

from airflow_provider_alembic.operators.alembic import AlembicOperator

with DAG(
        "example_alembic",
        schedule="@once",  # also consider "None"
        start_date=datetime(1970, 1, 1),
        params={
            "command": Param("upgrade"),
            "revision": Param("head")
        }
) as dag:
    AlembicOperator(
        task_id="alembic_op",
        conn_id="sqlite",
        command="{{ params.command }}",
        revision="{{ params.revision }}",
        script_location="/usr/local/airflow/dags/migrations",
    )