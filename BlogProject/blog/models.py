from django.db import models

# Create your models here.
from django.utils import timezone
# Create your models here.
from django.urls import reverse

class Post(models.Model):
    author = models.ForeignKey('auth.User',on_delete="DO_NOTHING")
    title = models.CharField(max_length=200)
    text = models.TextField()
    create_date = models.DateTimeField(default = timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def approve_comments(self):
        return self.comments.filter(approve_comment = True)

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={"pk":self.pk})

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey('blog.post', related_name="comments", on_delete="DO_NOTHING")
    author = models.CharField(max_length=200)
    text = models.TextField()
    create_date = models.DateTimeField(default=timezone.now)
    approve_comment = models.BooleanField(default=False)

    def approve(self):
        self.approve_comment = True
        self.save()

    def get_absolute_url(self):
        return reverse('post_list')


    def __str__(self):
        return self.text