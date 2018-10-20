from django.db import models

# Create your models here.


class Advertisement(models.model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    # TODO location here
    date_of_publication = models.DateField()
    date_of_expiration = models.DateField()

    def __str__(self):
        return self.title