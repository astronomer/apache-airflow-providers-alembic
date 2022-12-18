# WIP - the initial idea here was to have a plugin to make new migrations and such, or get metadata, without the CLI


# from airflow.plugins_manager import AirflowPlugin
# from flask import Blueprint
# from flask_appbuilder import BaseView as AppBuilderBaseView
#
# bp = Blueprint(
#     "alembic",
#     __name__,
#     template_folder="templates",  # registers airflow/plugins/templates as a Jinja template folder
#     static_folder="static",
#     static_url_path="/static/alembic",
# )
#
#
# # Creating a flask appbuilder BaseView
# class Alembic(AppBuilderBaseView):
#     default_view = "main"
#
#     def main(self):
#         return '200'
#
#
# v_appbuilder_view = Alembic()
#
#
# # Defining the plugin class
# class AlembicPlugin(AirflowPlugin):
#     name = "alembic"
#     hooks = []
#     macros = []
#     flask_blueprints = [bp]
#     appbuilder_views = [
#         {
#             "name": "Alembic Migrations",
#             "category": "Astronomer",
#             "view": v_appbuilder_view,
#         },
#     ]
#     appbuilder_menu_items = []
#     global_operator_extra_links = []
#     operator_extra_links = []

