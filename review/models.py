from django.db import models


# Create your models here.
class Review(models.Model):
    username = models.CharField(max_length=55)
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.username}    {self.date}"

    class Meta:
        ordering = ("-date",)
        verbose_name = "review"
        verbose_name_plural = "reviews"
