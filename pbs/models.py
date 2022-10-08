from django.db import models
from django.utils import timezone
import random


def generate_pk(typeMod):
    number = random.randint(1000, 9999)
    return "{}-{}{}".format(typeMod, timezone.now().strftime('%y%m%d'), number)


class PBS(models.Model):
    id = models.CharField(primary_key=True, max_length=255,
                          unique=True,  editable=False)
    name = models.CharField(max_length=200)
    type = models.CharField(max_length=10, default="pbs")

    def save(self, *args, **kwargs):
        self.id = generate_pk(self.type[0:1])
        super(PBS, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.id}-{self.name}"


class Zonal(models.Model):
    id = models.CharField(primary_key=True, max_length=255,
                          unique=True,  editable=False)
    parent = models.ForeignKey(
        PBS, on_delete=models.CASCADE, related_name='child')
    name = models.CharField(max_length=200)
    type = models.CharField(max_length=10, default="zonal")

    def save(self, *args, **kwargs):
        self.id = generate_pk(self.type[0:1])
        super(Zonal, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.id}-{self.name}"


class SubZonal(models.Model):
    id = models.CharField(primary_key=True, max_length=255,
                          unique=True,  editable=False)
    parent = models.ForeignKey(
        Zonal, on_delete=models.CASCADE, related_name='child')
    name = models.CharField(max_length=200)
    type = models.CharField(max_length=10, default="subzonal")

    def save(self, *args, **kwargs):
        self.id = generate_pk("sz")
        super(SubZonal, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.id}-{self.name}"


class ComplainCenter(models.Model):
    id = models.CharField(primary_key=True, max_length=255,
                          unique=True,  editable=False)
    parent = models.ForeignKey(
        SubZonal, on_delete=models.CASCADE, related_name="child")
    name = models.CharField(max_length=200)
    type = models.CharField(max_length=10, default="cc")

    def save(self, *args, **kwargs):
        self.id = generate_pk(self.type[0:1])
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.id}-{self.name}"


status = (
    ('Active', 'Active'),
    ('Working', 'Working'),
    ('Fault', 'Fault'),
    ('Loadshedding', 'Loadshedding'),
)


class Fider(models.Model):
    id = models.CharField(primary_key=True, max_length=255,
                          unique=True,  editable=False)
    parent = models.ForeignKey(
        ComplainCenter, on_delete=models.CASCADE, related_name="child")
    fiderNo = models.IntegerField(blank=True)
    name = models.CharField(max_length=200,)
    type = models.CharField(max_length=10, default="fider")
    latitude = models.FloatField(blank=False,default=0)
    longitude = models.FloatField(blank=False,default=0)
    status = models.CharField(max_length=15, choices=status)
    message = models.CharField(max_length=200, blank=True)
    address = models.CharField(max_length=200, blank=True,editable=False)

    def save(self, *args, **kwargs):
        if self.address == "":
            self.address = f"{self.parent.parent.parent.parent.name}>{self.parent.parent.parent.name}>{self.parent.parent.name}>{self.parent.name}>{self.name}"
        self.id = generate_pk(self.type[0:1])
        super(Fider, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.id}-{self.name}"


status2 = (
    ('Pending', 'Pending'),
    ('Solved', 'Solved'),
)


class Report(models.Model):
    id = models.CharField(primary_key=True, max_length=255,
                          unique=True,  editable=False)
    parent = models.ForeignKey(
        ComplainCenter, on_delete=models.CASCADE, related_name="report")
    fidername = models.CharField(max_length=200, default="")
    issue = models.CharField(max_length=200, default="")
    priority = models.IntegerField(blank=False)
    latitude = models.FloatField(blank=False)
    longitude = models.FloatField(blank=False)
    address = models.CharField(max_length=200,editable=False )
    contact = models.IntegerField()
    reporterName = models.CharField(max_length=200, default="")
    status = models.CharField(
        max_length=10, choices=status2, default="Pending")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    solved_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if self.status == "Solved":
            self.solved_at = timezone.now()
        elif not self.status == "Solved":
            self.solved_at = None


        if not self.address:
            self.address = f"{self.parent.parent.parent.parent.name}>{self.parent.parent.parent.name}>{self.parent.parent.name}>{self.parent.name}>{self.fidername}"
        self.id = generate_pk("r")

        super(Report, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.fidername}-{self.reporterName}"


"""
123 posts
258 followers
117 following
"""
