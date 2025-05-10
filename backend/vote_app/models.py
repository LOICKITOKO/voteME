from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

class Nominee(models.Model):
    category = models.ForeignKey(Category, related_name='nominees', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    image_url = models.URLField()

    def __str__(self):
        return self.name

class Vote(models.Model):
    nominee = models.ForeignKey(Nominee, related_name='votes', on_delete=models.CASCADE)
    ip_address = models.GenericIPAddressField()

    def __str__(self):
        return f"Vote for {self.nominee.name} from {self.ip_address}"
