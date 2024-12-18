from django.db import models

# Create your models here.
class Imgupload(models.Model):
    main_image=models.ImageField(upload_to='image/') 

