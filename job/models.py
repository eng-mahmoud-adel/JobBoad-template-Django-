from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User

# Create your models here.
class Job(models.Model):
    JOB_TYPE = (
        ('full time', 'full time'),
        ('part time', 'part time')
    )

    title = models.CharField(max_length=100, default='')
    # location = 
    job_type = models.CharField(max_length=50, choices=JOB_TYPE, default='')
    description = models.TextField(max_length=1000, default='')
    image = models.ImageField(upload_to='jobs/images', default='', null=True)
    published_at = models.DateTimeField(auto_now=True, auto_now_add=False)
    vacancy = models.IntegerField(default=1)
    salary = models.IntegerField(default=0)
    experience = models.IntegerField(default=1)
    slug = models.SlugField(blank=True, null=True)
    category = models.ForeignKey("Category", default='', on_delete=models.CASCADE)
    # owner of this job is the admin where id = 1
    owner = models.ForeignKey(User, default=1, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        return super(Job, self).save(*args, **kwargs)

class Category(models.Model):
    name = models.CharField(max_length=50, default='')

    def __str__(self):
        return self.name

class ApplyForJob(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    website = models.URLField(max_length=200)
    cv = models.FileField(upload_to='jobs/files', max_length=100)
    cover_letter = models.TextField()
    applied_at = models.DateTimeField(auto_now=True, auto_now_add=False)
    job = models.ForeignKey("Job", on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} - {self.job}'
    