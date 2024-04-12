from django.db import models

class Car(models.Model):
    model = models.CharField(max_length=100)
    year = models.IntegerField()
    availability = models.BooleanField(default=True)  # True if available, False if not available
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='car_images/')

    # Explicitly include the id field
    car_id = models.AutoField(primary_key=True)

    def __str__(self):
        return self.model
