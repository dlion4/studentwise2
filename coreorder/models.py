from django.db import models
from account.models import UserProfile
from django.shortcuts import reverse
from coreorder.store.models import SUBJECT_AREA, TAST_TYPE, ACADEMIC_LEVEL


class OrderType(models.Model):
    student = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    service_type = models.CharField(max_length=100)
    academic_level = models.CharField(max_length=100)
    task_type = models.CharField(
        choices=TAST_TYPE, blank=True, max_length=100,
        default="ESSAY"
    )
    pages = models.PositiveIntegerField(blank=True, default=1)
    words = models.PositiveIntegerField(blank=True, default=275)
    prices = models.DecimalField(
        max_digits=6, decimal_places=2, blank=True, null=True)
    deadline = models.DateField()
    order_date = models.DateTimeField(auto_now_add=True)

    # %Y-%m-%d %H:%M:%S

    def __str__(self):
        return "{} due on {}".format(self.service_type, self.deadline.strftime("%Y-%m-%d"))

    class Meta:
        verbose_name = 'order type'
        verbose_name_plural = 'Paper Types'
        get_latest_by = 'order_date'


class OrderItem(models.Model):

    order = models.ForeignKey(OrderType, on_delete=models.CASCADE)
    topic = models.CharField(max_length=100)
    paper_details = models.TextField()
    files = models.FileField(upload_to='orders/files/',
                             blank=True, null=True)
    subject_area = models.CharField(
        choices=SUBJECT_AREA, max_length=100, default="LAW")
    writer_type = models.CharField(
        choices=(
            ("BW", "Basic Writer"),
            ("FW", "Fast Writer"),
            ("PW", "Pro Writer")
        ),
        default="BW", max_length=10)
    sources = models.PositiveIntegerField(default=0)
    powerpoint_slides = models.PositiveIntegerField(default=0)
    charts_graphs = models.PositiveIntegerField(default=0)
    paper_format = models.CharField(
        choices=(
            ("MLA", "MLA"),
            ("APA", "APA"),
            ("CHICAGO", "Chicago"),
            ("HARVAD", "Harvad"),
            ("OTHER", "Other"),

        ),
        default="MLA", max_length=20)
    plag_report = models.CharField(
        choices=(
            ("None", None),
            ("STARNDARD", "Standard"),
            ("PREMIUM", "Premium"),
        ),
        default="None", max_length=10)
    grammerly_report = models.CharField(
        choices=(
            ("None", "None"),
            ("INCLUDE", "Inlude"),
        ),
        max_length=10,
        default="None",
    )
    price = models.DecimalField(max_digits=9, decimal_places=2)
    # progress_update = models.BooleanField(default=False)
    # sources_copy = models.BooleanField(default=False)
    # outline = models.BooleanField(default=False)
    # info_graph = models.BooleanField(default=False)
    # page_abstract = models.BooleanField(default=False)
    # page_summary = models.BooleanField(default=False)

    def __str__(self):
        return "{}".format(self.subject_area)

    class Meta:
        verbose_name = "Order Item"
        verbose_name_plural = "Order Items"
