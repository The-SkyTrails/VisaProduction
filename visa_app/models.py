from django.db import models
from django.core.validators import FileExtensionValidator, MaxValueValidator, MinValueValidator

VISA_SERVICES_CHOICES = [
    ("Work Visa","Work Visa"),
    ("Tourist Visa","Tourist Visa")
]

BLOGS_TYPES_CHOICES = [
    ("Latest Updates","Latest Updates"),
    ("Editors Pick","Editors Pick"),
    ("Featured Articles","Featured Articles"),
]

class Cvsubmit(models.Model):
    Name = models.CharField(max_length=50)
    email = models.EmailField()
    contact_no = models.CharField(max_length=15)
    address = models.CharField(max_length=100)
    country = models.CharField(max_length = 100)
    cv_file = models.FileField(upload_to="visa/cvs/")
    job_profile = models.CharField(max_length=50)
    
    
    
class ContactUs(models.Model):
    Firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    Phone_number = models.CharField(max_length=50)
    Email = models.EmailField()
    visa_services = models.CharField(max_length=50,choices=VISA_SERVICES_CHOICES)
    notes = models.TextField(max_length=200,blank=True, null=True)
    

class Appointment(models.Model):
    Firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    Phone_number = models.CharField(max_length=50)
    Email = models.EmailField()
    visa_services = models.CharField(max_length=50,choices=VISA_SERVICES_CHOICES)
    notes = models.TextField(max_length=200,blank=True, null=True)
    date = models.DateTimeField()
    
    
class Testimonials(models.Model):
    name = models.CharField(max_length=100,blank=True, null=True)
    rating = models.IntegerField(blank=True, null=True)
    file = models.FileField(
        upload_to="visa/testimonials/",
        blank=True,
        null=True,
        validators=[
            FileExtensionValidator(
                allowed_extensions=['jpg', 'jpeg', 'png', 'gif', 'mp4', 'avi', 'mov']
            )
        ],
    )

    def get_file_type(self):
        image_extensions = ['.jpg', '.jpeg', '.png']
        video_extensions = ['.gif', '.mp4', '.avi', '.mov']

        file_extension = self.file.name.lower().split('.')[-1]

        if file_extension in image_extensions:
            return 'image'
        elif file_extension in video_extensions:
            return 'video'
        else:
            return 'unknown'
        
        
class Blogs(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.FileField(upload_to="visa/bogs/")
    written_by = models.CharField(max_length=100)
    written_by_profile = models.FileField(upload_to="visa/blogs/profile/")
    registered_at = models.DateTimeField(auto_now=True)
    read_time = models.CharField(max_length=20)
    blogs_type = models.CharField(max_length=100,choices=BLOGS_TYPES_CHOICES)
    category = models.CharField(max_length=100)
    
    
    

