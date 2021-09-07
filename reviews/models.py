from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.conf import settings
from django.db import models
from tickets.models import Ticket


# Create your models here.

class Review(models.Model):
    ticket = models.ForeignKey(to=Ticket, on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField(
        verbose_name='Note',
        # validates that rating must be between 0 and 5
        validators=[MinValueValidator(0), MaxValueValidator(5)])
    headline = models.CharField(verbose_name='Titre', max_length=128)
    body = models.CharField(verbose_name='Critique', max_length=8192, blank=True)
    user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    time_created = models.DateTimeField(auto_now_add=True)
