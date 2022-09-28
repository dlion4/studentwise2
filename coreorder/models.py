from django.db import models
from account.models import UserProfile

# Create your models here.


class OrderType(models.Model):
    student = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    service_type = models.CharField(max_length=100)
    academic_level = models.CharField(max_length=100)
    paper_type = models.CharField(max_length=100, blank=True)
    subject_area = models.CharField(blank=True, max_length=100)
    pages = models.PositiveIntegerField(blank=True, default=1)
    words = models.PositiveIntegerField(blank=True, default=275)
    prices = models.DecimalField(
        max_digits=6, decimal_places=2, blank=True, null=True)
    deadline = models.DateField()

    # %Y-%m-%d %H:%M:%S

    def __str__(self):
        return "{} due {}".format(self.service_type, self.deadline)

    def save(self):
        self.prices = int((self.pages * 3.95 or self.words * 1.25))
        return super().save()

    class Meta:
        verbose_name = 'order type (paper)'
        verbose_name_plural = 'Order (Paper) Types'
