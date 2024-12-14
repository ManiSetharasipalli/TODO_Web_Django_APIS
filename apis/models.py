from django.db import models

class TODO(models.Model):
    PRIORITY_CHOICES = (
        ('high','High'),
        ('medium', 'Medium'),
        ('low', 'Low')
    )
    title = models.CharField(max_length=50, blank=False, null=False)
    description = models.TextField(blank=True, null=True)
    priority = models.CharField(max_length=10, null=False, choices=PRIORITY_CHOICES, default='medium')
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.title} ({self.get_priority_details()})'