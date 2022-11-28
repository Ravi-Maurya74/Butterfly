from django.db import models


# Create your models here.


class ApiUser(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30, blank=True)
    user_email = models.EmailField(unique=True)
    password = models.CharField(max_length=30)
    following = models.ManyToManyField("self", blank=True, symmetrical=False, related_name='followers')
    liked_posts = models.ManyToManyField('Post', blank=True, related_name='liked_by')
    bookmarked_posts = models.ManyToManyField('Post', blank=True, related_name='bookmarked_by')
    dob = models.DateField()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Post(models.Model):
    content = models.CharField(max_length=300)
    user_id = models.ForeignKey(ApiUser, on_delete=models.CASCADE, related_name='user_posts')
    created = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.content[0:20]


class Reply(models.Model):
    content = models.CharField(max_length=500)
    replied_to = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='replies')
    user_id = models.ForeignKey(ApiUser, on_delete=models.CASCADE, related_name='user_replies')
    created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.content[0:20]

    class Meta:
        ordering = ['created']
