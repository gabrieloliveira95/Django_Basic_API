from django.db import models


class Base(models.Model):
    publicated = models.DateTimeField(auto_now=True)
    update = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        abstract = True


class Course(Base):
    title = models.CharField(max_length=255)
    url = models.URLField(unique=True)

    class Meta:
        verbose_name = 'Couse'
        verbose_name_plural = 'Courses'

    def __str__(self):
        return f'Course {self.title} has url = {self.url}'


class Evaluate(Base):
    course = models.ForeignKey(
        Course,
        related_name='Evaluates',
        on_delete=models.CASCADE
    )
    name = models.CharField(max_length=255)
    email = models.EmailField()
    comments = models.TextField(blank=True, default='')
    evaluate = models.DecimalField(max_digits=2, decimal_places=1)

    class Meta:
        verbose_name = 'Evaluate'
        verbose_name_plural = 'Evaluates'
        unique_together = ['email', 'course']

    def __str__(self):
        return f'{self.name} evaluate course {self.course} with {self.evaluate}.'
