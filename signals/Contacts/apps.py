from django.apps import AppConfig

# @receiver


class ContactsConfig(AppConfig):
    name = 'Contacts'

    def ready(self):
        pass
        # Can register signals here.
        # print('Ready called')