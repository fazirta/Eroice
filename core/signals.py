from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.contrib.auth.models import Group


from .models import Profile

def profile(sender, instance, created, **kwargs):
    if created:
        try:
            group = Group.objects.get(name='user')
            instance.groups.add(group)
        except:
            pass
        Profile.objects.create(
			user=instance,
			name=instance.username,
			)
        print('Profile created!')

post_save.connect(profile, sender=User)