from django.db import models

class DateTimeModel(models.Model):
    """ A base model with created and edited datetime fields """
    class Meta:
        abstract = True

    created = models.DateTimeField(auto_now_add=True)
    edited = models.DateTimeField(auto_now=True)

class School(DateTimeModel):
    """School of thought model"""
    name = models.CharField(max_length=350)

    def __str__(self):
        """String for representing the Model object."""
        return self.name

class Philosopher(DateTimeModel):
    """Philosopher model"""
    name = models.CharField(max_length=250)
    photo = models.CharField(max_length=500, default="")
    born_date = models.DateField(null=True, blank=True)
    death_date = models.DateField(null=True, blank=True)
    school = models.ManyToManyField(School, help_text='Select the schools of this thinker', related_name="philosophers")
    nationality = models.CharField(max_length=350)
    era = models.CharField(max_length=350)

    def __str__(self):
        """String for representing the Model object."""
        return self.name

class Book(DateTimeModel):
    """Book model"""
    title = models.CharField(max_length=250)
    cover = models.CharField(max_length=500, default="")
    abstract = models.TextField(max_length=1000, help_text='Abstract of the Book')
    country = models.CharField(max_length=350)
    language = models.CharField(max_length=350)
    published = models.DateField(null=True, blank=True)
    author = models.ForeignKey(Philosopher, related_name='books', on_delete=models.CASCADE)

    def __str__(self):
        """String for representing the Model object."""
        return self.title

class Idea(DateTimeModel):
    """Idea model"""
    quote = models.TextField(max_length=1000, help_text='Quote of the Author')
    author = models.ForeignKey(Philosopher, related_name='ideas', on_delete=models.CASCADE)

    def __str__(self):
        """String for representing the Model object."""
        return self.quote