from django.db import models
import datetime
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from sorl.thumbnail import ImageField


class Genre(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.name


def current_year():
    return datetime.date.today().year


def year_validator(value):
    if value < 1888 or value > current_year():
        raise ValidationError(
            _("%(value)s is not a valid year"),
            params={"value": value},
        )


class Movie(models.Model):
    class Meta:
        verbose_name = "Movie"
        verbose_name_plural = "Movies"
        get_latest_by = "created_at"
        ordering = ["-created_at"]

    name = models.CharField(max_length=100)
    year_released = models.IntegerField(
        default=0,
        help_text="YYYY",
        validators=[year_validator],
    )
    description = models.CharField(max_length=2000)
    poster = ImageField(upload_to="movie/posters", null=True, blank=True)
    rating = models.FloatField(
        default=0.0, blank=True, null=True, help_text="0.0 to 10.0"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    genre = models.ManyToManyField("Genre", related_name="movie")

    def __str__(self):
        return self.name
