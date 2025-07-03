from django.db import models

class Expense(models.Model):
    title = models.CharField(max_length=100)
    amount = models.FloatField()
    paid_by = models.CharField(max_length=100)
    shared_with = models.TextField()  # Store names as comma-separated values

    def __str__(self):
        return self.title
