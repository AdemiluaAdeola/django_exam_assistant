from django.db import models
#from ckeditor.fields import RichTextField

# Create your models here.
class Courses(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'Course'
        verbose_name_plural = 'Courses'

    def __str__(self):
        return self.name
    
class Topics(models.Model):
    course = models.ForeignKey(Courses, on_delete=models.CASCADE, related_name='topics')
    name = models.CharField(max_length=20000)

    class Meta:
        verbose_name = 'Topic'
        verbose_name_plural = 'Topics'

    def __str__(self):
        return self.name + " - " + self.course.name
    
class Outline(models.Model):
    topic = models.ForeignKey(Topics, on_delete=models.CASCADE, related_name='topic')
    date = models.DateField(auto_now=True)
    body = models.TextField()

    class Meta:
        verbose_name = 'Outline'
        verbose_name_plural = 'Outlines'

    def __str__(self):
        return self.topic.name
    
