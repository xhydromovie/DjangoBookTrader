from django.contrib.auth.models import User
from django.db import models


class Book(models.Model):
    """
    Model of book that contains information about book like: author name, book title, ISBN, publication date
    """
    # Author name
    author = models.CharField(max_length=50)
    # Book title
    title = models.CharField(max_length=50)
    # ISBN
    isbn = models.CharField(max_length=50)
    # Publication date
    publication_date = models.DateField('publication_date')

    def __str__(self):
        """
        Method returns Book Title
        :return: Book Title
        """
        return self.title


class Advertisement(models.Model):
    """
    Model of Advertisement, contains information like: advertisement tile, description, date of publication and date of expiration.
    """
    title = models.CharField(max_length=50)
    description = models.TextField()
    creater = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    # TODO location here
    date_of_publication = models.DateField()
    date_of_expiration = models.DateField()

    def __str__(self):
        return self.title


class Report(models.Model):
    """
    Model of report, contains information like: which advertisement is for, date of report, description, and reporting user.
    """
    advertisement = models.ForeignKey(Advertisement, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    report_date = models.DateTimeField('report_date')
    description = models.TextField()

    def __str__(self):
        """
        Method returns reported advertisement name
        :return: reported advertisement name
        """
        return self.advertisement
