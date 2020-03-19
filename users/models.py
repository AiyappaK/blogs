from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# Create your models here.
class profileModel(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg',upload_to='images')

    def __str__(self):
        return self.user.username
        # this method runs after the model is saved for reducing the size of image into databases
    def save(self):
        super().save()
        # this arrtibute will take care of current imge
        img = Image.open(self.image.path)

        if img.height > 100 or img.width >100:
            output_size = (100, 100)
            img.thumbnail(output_size)
            img.save(self.image.path)
