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
