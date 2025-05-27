from django.apps import AppConfig


class VUsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'v_users'

    def ready(self):
        import v_users.signals
