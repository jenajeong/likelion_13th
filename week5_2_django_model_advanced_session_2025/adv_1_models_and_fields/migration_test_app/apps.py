from django.apps import AppConfig


class MigrationTestAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'migration_test_app'
