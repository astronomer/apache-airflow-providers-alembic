# Alembic Provider

## Usage
We are going to use Alembic slightly differently than you would normally, notably not using the `alembic` CLI directly

In a new Astronomer Project (if one does not already exist)
```shell
astro dev init
```

Have alembic installed locally
```shell
pip install alembic
```

- in the DAGs directory, in a folder called `alembic`, with a folder called `versions`
- In the `alembic` folder, make a file called `script.py.mako`
```shell
mkdir -p dags/alembic/versions
touch dags/alembic/script.py.mako 
cd dags/alembic
```

- fill `script.py.mako` with the following contents. Mako is a templating system like Jinja, used by Alembic
```shell
"""${message}

Revision ID: ${up_revision}
Revises: ${down_revision | comma,n}
Create Date: ${create_date}

"""
from alembic import op
import sqlalchemy as sa
${imports if imports else ""}

# revision identifiers, used by Alembic.
revision = ${repr(up_revision)}
down_revision = ${repr(down_revision)}
branch_labels = ${repr(branch_labels)}
depends_on = ${repr(depends_on)}


def upgrade() -> None:
    ${upgrades if upgrades else "pass"}


def downgrade() -> None:
    ${downgrades if downgrades else "pass"}
```

- Make an initial revision

(note: this is effectively `alembic revision -m "this is the title of my migration"`, but this form enables us to skip some boilerplate that is otherwise required)
```shell
python -c "import alembic.command as cd; import alembic.config as cg; import sys; c=cg.Config(); c.set_main_option('script_location', '.'); cd.revision(c, sys.argv[1])" \
  "<title of my migration>"
```
Change `"<title of my migration>"` to a good title

- In the initial revision, modify the `upgrade` and `downgrade` methods.
  - `upgrade`: the actual database migration - this can be a table creation, alteration, column addition, or anything
  - `downgrade`: the reverse of the database migration - to be applied in the event of a revert
