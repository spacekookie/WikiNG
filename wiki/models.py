from django.contrib.auth.models import User
from django.db import models


def get_sentinel_user():
    return User.objects.get_or_create(username='deleted', first_name='deleted', last_name='user')[0]


class Page(models.Model):
    uuid = models.UUIDField(unique=True)
    name = models.CharField(max_length=255)
    revision = models.IntegerField()
    author = models.ForeignKey(User, related_name="pages", on_delete=models.SET(get_sentinel_user))
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


# class Profile(models.Model):
#
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#
#     @receiver(post_save, sender=get_user_model())
#     def create_user_profile(sender, instance, created, **kwargs):
#         if created:
#             Author.objects.create(user=instance)
#
#     @receiver(post_save, sender=get_user_model())
#     def save_user_profile(sender, instance, **kwargs):
#         instance.profile.save()
#
#     def __str__(self):
#         return "%s <%s>" % (self.user.username, self.user.email)
#
#     class Meta:
#         ordering = ('user', )
