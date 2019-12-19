from django.db import models


class FacebookUser(models.Model):
    name = models.CharField(max_length=20)
    friends = models.ManyToManyField('self')

    def __str__(self):
        return self.name


class InstargramUser(models.Model):
    name = models.CharField(max_length=20)
    following = models.ManyToManyField(
        'self', through='Relation', symmetrical=False, related_name='followers'
    )

    def __str__(self):
        return self.name


class Relation(models.Model):
    from_user = models.ForeignKey(InstargramUser, on_delete=models.CASCADE, related_name='from_relation_set')
    to_user = models.ForeignKey(InstargramUser, on_delete=models.CASCADE, related_name='to_relation_set')
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Relation (me :{self.from_user.name}, counterpart : {self.to_user.name}'
