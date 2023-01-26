import os
from datetime import datetime

from airflow.models import DAG
from airflow.models.param import Param

from astronomer.providers.alembic.operators.alembic import AlembicOperator

os.environ['AIRFLOW_CONN_SQLITE'] = "sqlite:///:memory:"

with DAG(
        "example_alembic",
        schedule=None,
        start_date=datetime(1970, 1, 1),
        params={
            "command": Param("upgrade"),
            "revision": Param("head")
        }
) as dag:
    AlembicOperator(
        task_id="alembic_op",
        conn_id="sqlite",
        command="{{ param.command }}",
        revision="{{ param.revision }}",
        script_location="/usr/local/airflow/dags/migrations",
    )
