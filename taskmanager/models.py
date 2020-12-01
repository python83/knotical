from django.db import models
from usermanagement.models import UserProfile
from django.contrib.auth.models import  User

# Create your models here.

#available statuses, set in admin
class KnotsStatus(models.Model):
    status_name = models.CharField(max_length=256, blank=False, unique = True)

    def __str__(self):
        return self.status_name

#available categories, set in admin
class KnotsCategory(models.Model):

    category_name = models.CharField(max_length=256, blank=False, unique = True)

    def __str__(self):
        return self.category_name

#urgency level, set in admin
class KnotsUrgency(models.Model):
    urgency_title = models.CharField(max_length=256, blank=False, unique = True)

    def __str__(self):
        return self.urgency_title

#available topics (category)
class KnotsTopics(models.Model):
    knot_topic = models.CharField(max_length=256, blank=False, unique = True)
    knot_topic_owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.knot_topic


#model for a task, a task is called a knot
class Knots(models.Model):
    #task title
    knot_title = models.CharField(max_length=256, blank=False, unique = True)
    ## start of fields connected with other tables
    #the task belongs to
    knot_owner = models.ForeignKey(User, on_delete=models.CASCADE)
    #task topic
    knot_topic = models.ForeignKey(KnotsTopics, blank = True, null = True, on_delete=models.SET_NULL)
    #task category
    knot_category = models.ForeignKey(KnotsCategory, blank = True, null = True, on_delete=models.SET_NULL, default=1)
    #task status
    knot_status = models.ForeignKey(KnotsStatus, blank = True, null = True, on_delete=models.SET_NULL, default=1)
    #task status
    knot_urgency = models.ForeignKey(KnotsUrgency, blank = True, null = True, on_delete=models.SET_NULL, default=1)
    ## end of fields connected with other tables
    ## fields that only exist in this table
    knot_details = models.TextField(blank=True)
    knot_url = models.URLField(blank=True)
    knot_date = models.DateField(blank=True, null=True)
    knot_time = models.TimeField(blank=True, null=True)
    knot_image = models.ImageField(upload_to='uploads',blank=True, null=True)

    #location coordinates
    #place holder for integration with Google Maps
    knot_longitude = models.DecimalField(max_digits=9, decimal_places=6,blank=True, null=True)
    knot_latitude  = models.DecimalField(max_digits=9, decimal_places=6,blank=True, null=True)

    def __str__(self):
        return self.knot_title
