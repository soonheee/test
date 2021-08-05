from django.db import models


class Review(models.Model):
    writer = models.ForeignKey('User', on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    title = models.CharField(max_length=60)
    like_count = models.PositiveIntegerField(default=0)
    reviews = models.PositiveIntegerField(default=0)
    tmp_flag = models.BooleanField()
    d_day = models.PositiveIntegerField()
    review = models.TextField()


class ReviewLike(models.Model):
    review_num = models.ForeignKey('Review', on_delete=models.CASCADE)
    user_num = models.ForeignKey('User', on_delete=models.CASCADE)


class User(models.Model):
    name = models.CharField(max_length=30, default="?")
