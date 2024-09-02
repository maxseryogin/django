import sys
import os
import django


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")
django.setup()

from users_app .models import *

# user1 = User(name="Artem", email="emain@gmail.com", role="admin")
# user1.save()

# user2 = User(name="Kirill", email="fdsafasd@gmail.com")
# user2.save()

user3 = User.objects.get(id=1)
user3.role="user"
user3.save()