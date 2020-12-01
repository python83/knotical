from django import forms
#import the task models
from taskmanager.models import KnotsTopics, Knots

#form to create new topics
class CreateTopicForm(forms.ModelForm):
    #create a form for adding topics
    class Meta():
        model = KnotsTopics
        #only use topic title field, user is added automatically
        fields = ['knot_topic']

#form to create new tasks
class CreateKnotForm(forms.ModelForm):
    #create a form for adding topics
    class Meta():
        model = Knots
        #user is added automatically, lat long not used yet
        fields = ['knot_title', 'knot_topic', 'knot_category', 'knot_status',
                  'knot_urgency', 'knot_details', 'knot_url', 'knot_date',
                  'knot_time', 'knot_image']

    #custom init function due to filtered topics
    def __init__(self, user, *args, **kwargs):
        super(CreateKnotForm, self).__init__(*args, **kwargs)
        #filter the list of topics to match current user
        self.fields['knot_topic'].queryset = KnotsTopics.objects.filter(knot_topic_owner=user)
