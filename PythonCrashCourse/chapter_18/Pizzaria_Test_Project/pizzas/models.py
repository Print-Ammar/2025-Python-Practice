from django.db import models

# Create your models here.

class Name(models.Model):
    """The type of pizza the user has selected"""
    text = models.CharField(max_length=30)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return representation of the model"""
        return self.text

class Topping(models.Model):
    """Topic for the pizza"""
    topping = models.ForeignKey(Name,on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        if len(self.text) > 50:
            return f"{self.text[:50]}"
        else:
            return self.text