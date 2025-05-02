from django.db import models
from django.utils.text import slugify
from accounts.models import User

class Hackathon(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    start_date = models.DateField()
    end_date = models.DateField()
    venue = models.CharField(max_length=255)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class HackathonApplication(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='hackathon_applications')
    hackathon = models.ForeignKey(Hackathon, on_delete=models.CASCADE, related_name='applications')
    applied_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'hackathon')

    def __str__(self):
        return f"{self.user.username} applied to {self.hackathon.title}"
