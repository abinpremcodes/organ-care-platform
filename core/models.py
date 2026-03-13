from django.db import models


# -----------------------------
# Donor Model
# -----------------------------
class Donor(models.Model):
    BLOOD_GROUP_CHOICES = [
        ('A+', 'A+'),
        ('A-', 'A-'),
        ('B+', 'B+'),
        ('B-', 'B-'),
        ('AB+', 'AB+'),
        ('AB-', 'AB-'),
        ('O+', 'O+'),
        ('O-', 'O-'),
    ]

    ORGAN_CHOICES = [
        ('Kidney', 'Kidney'),
        ('Liver', 'Liver'),
        ('Heart', 'Heart'),
        ('Lung', 'Lung'),
        ('Blood', 'Blood'),
    ]

    SUCCESS_RATE_CHOICES = [(f'{i}%', f'{i}%') for i in range(10, 110, 10)]

    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    blood_group = models.CharField(max_length=5, choices=BLOOD_GROUP_CHOICES)
    organ_type = models.CharField(max_length=50, choices=ORGAN_CHOICES)
    location = models.CharField(max_length=100)
    availability = models.BooleanField(default=True)
    medical_history = models.FileField(upload_to='medical_records/', blank=True, null=True)
    success_rate=models.CharField(max_length=5,choices=SUCCESS_RATE_CHOICES,default='50%')

    def __str__(self):
        return f"{self.name} - {self.organ_type}"


# -----------------------------
# Hospital Model
# -----------------------------
class Hospital(models.Model):
    name = models.CharField(max_length=150)
    location = models.CharField(max_length=100)
    contact_email = models.EmailField()

    def __str__(self):
        return self.name


# -----------------------------
# Recipient Model
# -----------------------------
class Recipient(models.Model):
    URGENCY_CHOICES = [
        ('Low', 'Low'),
        ('Medium', 'Medium'),
        ('High', 'High'),
        ('Critical', 'Critical'),
    ]

    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Matched', 'Matched'),
        ('Approved', 'Approved'),
        ('Completed', 'Completed'),
    ]

    name = models.CharField(max_length=100)
    email = models.EmailField()
    blood_group = models.CharField(max_length=5, choices=Donor.BLOOD_GROUP_CHOICES)
    required_organ = models.CharField(max_length=50, choices=Donor.ORGAN_CHOICES)
    urgency_level = models.CharField(max_length=20, choices=URGENCY_CHOICES)
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')

    def __str__(self):
        return f"{self.name} - {self.required_organ}"

