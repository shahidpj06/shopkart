from django.db import models

# model for showing the seasonal offer banner on the site.
class SiteSetting(models.Model):
    banner = models.ImageField(upload_to='media/site/')
    caption = models.TextField()