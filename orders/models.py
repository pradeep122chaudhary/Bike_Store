from django.db import models
from django.contrib.auth.models import User


# 2. Bike Model
class BikeModel(models.Model):
    name = models.CharField(max_length=255)
    model_number = models.CharField(max_length=255, unique=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    status_choices = [
        ('InStock', 'InStock'),
        ('OutOfStock', 'OutOfStock'),
    ]
    status = models.CharField(max_length=10, choices=status_choices, default='InStock')
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['name', 'model_number'], name='unique_bike_model')
        ]
    def __str__(self):
        return f"{self.name} ({self.model_number})"


# 3. Delivery Order Management
class DeliveryOrder(models.Model):
    customer_name = models.CharField(max_length=255,)
    mobile = models.CharField(max_length=15)
    gender_choices = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    ]
    gender = models.CharField(max_length=6, choices=gender_choices)
    full_address = models.TextField()
    bike_model = models.ForeignKey(BikeModel, on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    delivery_date = models.DateTimeField()
    status = models.ForeignKey("orders.StatusModel", on_delete=models.CASCADE)
    
    def save(self, *args, **kwargs):
        if not self.id:
            # Start ID from 10001
            max_id = DeliveryOrder.objects.all().aggregate(models.Max('id'))['id__max']
            if max_id is None:
                self.id = 10001
            else:
                self.id = max_id + 1
        if self.customer_name:
            self.customer_name = self.customer_name.capitalize()
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f"Order #{self.id} - {self.customer_name}"   


# 4. Status Management
class StatusModel(models.Model):
    name = models.CharField(max_length=25, unique= True)

    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    status = models.BooleanField(default=True)
    description= models.TextField()

    def __str__(self):
        return self.name


# 5. DeliveryOrder History Management
class DeliveryOrderHistory(models.Model):
    delivery_order = models.ForeignKey(DeliveryOrder, on_delete=models.CASCADE)
    status = models.ForeignKey(StatusModel, on_delete=models.CASCADE)
    message = models.TextField()
    old_delivery_date = models.DateTimeField()
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"History for Order #{self.delivery_order.id} - Status: {self.status.name}"
