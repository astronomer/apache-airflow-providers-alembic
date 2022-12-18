from typing import Any, Dict


def get_provider_info() -> Dict[str, Any]:
    """Return provider metadata to Airflow"""
    return {
        # Required.
        "package-name": "apache-airflow-provider-alembic",
        "name": "apache-airflow-provider-alembic",
        "description": "An Apache Airflow Providers for Alembic Operators and Hooks from Astronomer",
        "versions": "0.1.0",
        # Optional.
        "hook-class-names": [],
        "extra-links": [],
    }