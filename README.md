<!--suppress HtmlDeprecatedAttribute -->
<p align="center" >
  <a href="https://www.astronomer.io/">
    <img src="https://upload.wikimedia.org/wikipedia/commons/d/d7/SQLAlchemy.svg"
    alt="Alembic Provider Logo"
    height="200px" width="300px"
    style="display:block; margin-left: auto; margin-right: auto;" />
  </a>
</p>
<h1 align="center" style="text-align: center;">
   Alembic Provider
</h1>
<h3 align="center" style="text-align: center;">
  Alembic Database Migrations in Airflow.

Created with ❤️ by the CETA Team @ Astronomer
</h3>

# ⚠️ This project is a proof-of-concept and not officially supported nor maintained by Astronomer ⚠️


An Airflow Provider to use Alembic to manage database migrations
[Read more here](https://alembic.sqlalchemy.org/en/latest/)

## Setup
### Locally
Install the Alembic CLI with `pip install alembic`

### In Airflow
Add `airflow-provider-alembic` to your `requirements.txt` or equivalent

## Usage
- Create the required files for Alembic in either your `dags` folder or the `include` folder
```shell
mkdir dags/migrations
cd dags/migrations
alembic init .
```
**Note: You will not need to edit `alembic.ini` or `env.py` for the AlembicOperator or AlembicHook to work, however may need to for things like [autogenerating migrations](https://alembic.sqlalchemy.org/en/latest/autogenerate.html) from SQLAlchemy models.**

- Create a revision
```shell
alembic revision -m "My Database Revision"
```
- Edit the revision - adding, modifying, or removing objects as needed

```python
...

def upgrade():
    # Use ORM to create objects
    op.create_table(
        'foo',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(50), nullable=False),
        sa.Column('description', sa.Unicode(200)),
    )
    # Or run raw SQL
    op.execute("SELECT 1;")


def downgrade():
    # Specify the opposite of your upgrade, to rollback
    op.drop_table('account')
```

- Add a Connection to Airflow 
For demo purposes, we will add an in-memory SQLite3 Connection named `sqlite` via our `.env` file:
```dotenv
AIRFLOW_CONN_SQLITE="sqlite:///:memory:"
```
- Restart (or start) your project with `astro dev restart`
- Add a DAG, to run your revision. Because this has `@once`, it will run as soon as the DAG is turned on. Future runs for future revisions will need to be triggered. 
```python
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
```
## Extra Capabilities
- You can utilize any of the Alembic commands in the `AlembicOperator` - such as `downgrade`
- The `AlembicHook` has methods to run any [alembic commands](https://alembic.sqlalchemy.org/en/latest/api/commands.html)
