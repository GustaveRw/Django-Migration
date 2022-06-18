from django.db import models
from django.db import models

class Post(models.Model):
    post_title = models.CharField('title')
    post_author = models.ForeignKey('Author')
    post_text = models.TextField()
    create_date = models.DateTimeField('Date created')
    pub_date = models.DateTimeField('date published')
