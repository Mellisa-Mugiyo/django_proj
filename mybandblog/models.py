from django.db import models

class Member(models.Model):
        """
    Stores a single blog member, related to :model:`blog.Blog` and
    :model:`auth.User`.The name_member,age_member,and id are the fields of this 
    models
    """
        name_member = models.CharField(max_length=200)
        age_member = models.IntegerField()
        id = models.IntegerField(primary_key=True)



