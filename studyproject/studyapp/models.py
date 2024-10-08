from django.db import models
from django.contrib.auth.models import User

class Study(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    study_name = models.CharField(max_length=255)
    study_description = models.TextField(blank=True)
    
    PHASE_CHOICES = [
        ('Phase I', 'Phase I'),
        ('Phase II', 'Phase II'),
        ('Phase III', 'Phase III'),
        ('Phase IV', 'Phase IV'),
    ]
    study_phase = models.CharField(
        max_length=10,
        choices=PHASE_CHOICES,
        blank=False 
    )
    sponsor_name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.study_name} - {self.study_phase}"

    class Meta:
        unique_together = ('user', 'study_name')  
        verbose_name = 'Study'
        verbose_name_plural = 'Studies'
