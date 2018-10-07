from django.db import models

# Create your models here.


class Category(models.Model):
    '''sort '''
    name = models.CharField(max_length=100)


class Tag(models.Model):
    '''tag'''
    name = models.CharField(max_length=100)


class Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    created_time = models.DateTimeField()
    modified_time = models.DateTimeField()
    excerpt = models.CharField(max_length=200, blank=True)  # 文章摘要，可为空
    category = models.ForeignKey(Category, on_delete=True)  # ForeignKey表示1对多（多个post对应1个category）
    tags = models.ManyToManyField(Tag, blank=True)
    views = models.PositiveIntegerField(default=0)  # 阅读量


class Record(models.Model):

    rid = models.IntegerField(primary_key=True)
    listener = models.CharField(max_length=100)
    song_name = models.CharField(max_length=100)
    singer_name = models.CharField(max_length=100)
    song_url = models.CharField(max_length=100)
    listen_time = models.DateTimeField()

    class Meta:
        db_table = 'records'


class Hot_50(models.Model):

    hid = models.IntegerField(primary_key=True)
    song_name = models.CharField(max_length=100)
    singer_name = models.CharField(max_length=100)
    album_name = models.CharField(max_length=100)
    comment_total = models.IntegerField()
    last_comment_total = models.IntegerField()
    song_id = models.IntegerField()
    comment_thread_id = models.CharField(max_length=100)
    duration = models.IntegerField()
    album_id = models.IntegerField()
    update_time = models.DateTimeField()
    last_update_time = models.DateTimeField()
    status = models.IntegerField()

    class Meta:
        db_table = 'hot_50'

