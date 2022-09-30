from django.db import models
from account.models import UserProfile
from django.shortcuts import reverse


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
    order_date = models.DateTimeField(auto_now_add=True)

    # %Y-%m-%d %H:%M:%S

    def __str__(self):
        return "{} due on {}".format(self.service_type, self.deadline.strftime("%Y-%m-%d"))

    def save(self, *args, **kwargs):
        self.prices = int((self.pages * 3.95 or self.words * 1.25))
        return super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'order type'
        verbose_name_plural = 'Paper Types'
        get_latest_by = 'order_date'


class OrderItem(models.Model):

    order = models.ForeignKey(OrderType, on_delete=models.CASCADE)
    topic = models.CharField(max_length=100)
    paper_details = models.TextField()
    files = models.FileField(upload_to='orders/files/', blank=True, null=True)
    subject_area = models.CharField(max_length=100)
    writer_type = models.CharField(default="BW", max_length=2)
    sources = models.PositiveIntegerField(default=0)
    powerpoint_slides = models.PositiveIntegerField(default=0)
    charts_graphs = models.PositiveIntegerField(default=0)
    paper_format = models.CharField(default="MLA", max_length=5)
    plag_report = models.CharField(default="standard", max_length=10)
    extras = models.CharField(blank=True, null=True, max_length=30)

    def __str__(self):
        return "{}".format(self.subject_area)

    class Meta:
        verbose_name = "Order Item"
        verbose_name_plural = "Order Items"
