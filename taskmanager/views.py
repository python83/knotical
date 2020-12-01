from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect


#import the forms and models we have created
from .forms import CreateTopicForm, CreateKnotForm
from taskmanager.models import Knots, KnotsTopics
# Create your views here.

#this function contains the logic for the "topics" page
def topics_index(request):

    #variable to track if a topic was deleted
    topic_deleted = False
    #vartiable to track if a topic was added
    topic_added = False

    #was a form submitted?
    if request.method == 'POST':

        #did the user try to delete a topic?
        if (request.POST.get('topic_to_delete')):
            #use try/except, so that we dont run into problems if a record is not found
            try:
                #delete the  topic
                delete_topic_query = KnotsTopics.objects.get(knot_topic_owner = request.user, knot_topic = request.POST.get('topic_to_delete')).delete()
                topic_deleted = True
            except KnotsTopics.DoesNotExist:
                print("delete error")

        #did the user try to add a topic?
        if (request.POST.get('topic_to_add')):
            #create form using the data from the webpage
            create_topic_form = CreateTopicForm(data=request.POST)
            # Check to see form is valid
            if create_topic_form.is_valid():
                # save form to database
                new_topic = create_topic_form.save(commit=False)
                #the topic owner is the current logged in user
                new_topic.knot_topic_owner = request.user
                #commit changes
                new_topic.save()
                # Successful!
                topic_added = True
            else:
                # there are some issues with the form
                print(create_topic_form.errors)

    #generate form to add topics
    create_topic_form = CreateTopicForm()

    #fetch list of topics
    topics_list_query = KnotsTopics.objects.filter(knot_topic_owner = request.user)

    #render page
    return render(request,'taskmanager/topics.html',
                          {'create_topic_form':create_topic_form,
                           'topic_added':topic_added,
                           'topics_list_query': topics_list_query,
                           'topic_deleted':topic_deleted})

#this function contains the logic for the "knots" page
def tasks_index(request):

    #vartiable to track if task was deleted
    knot_unraveled = False

    #variable to track if details are needed for a to
    knot_details = False

    #was a form submitted?
    if request.method == 'POST':

        if (request.POST.get('knot_to_edit')):
            # return tasks_edit(request)
            return redirect('taskmanager:tasks_edit',title = request.POST.get('knot_to_edit'))


        #did the user delete a task?
        if (request.POST.get('knot_to_unravel')):
            try:
                delete_knot_query = Knots.objects.get(knot_owner = request.user, knot_title = request.POST.get('knot_to_unravel')).delete()
                knot_unraveled = True
            except Knots.DoesNotExist:
                print("delete error")

        #do we need to show details of a task ?
        if (request.POST.get('knot_to_detail')):
            #grab the task we need to display details for
            task_details_query = Knots.objects.get(knot_owner = request.user, knot_title = request.POST.get('knot_to_detail'))
            knot_details = True

    #display list of all tasks
    if (request.POST.get('topic_to_view')):
        #filter tasks by topic
        task_list_query = Knots.objects.filter(knot_owner = request.user, knot_topic__knot_topic = request.POST.get('topic_to_view'))
    else:
        #filter tasks only by user
        task_list_query = Knots.objects.filter(knot_owner = request.user)

    if (knot_details):
        print(request.POST.get('topic_to_view'))
        return render(request,'taskmanager/tasks.html',
                          {'task_list_query': task_list_query,
                           'knot_unraveled' : knot_unraveled,
                           'knot_details': knot_details,
                           'task_details_query': task_details_query})
    else:
        return render(request,'taskmanager/tasks.html',
                          {'task_list_query': task_list_query,
                           'knot_unraveled' : knot_unraveled,
                           'knot_details': knot_details})

def tasks_add(request):

        #variable to track if task was created
        knot_tied = False

        #was a form submitted?
        if request.method == 'POST':

            #did the user create a task?
            if (request.POST.get('knot_to_tie')):
                #create form and fill using data from webpage
                create_knot_form = CreateKnotForm(request.user, data=request.POST)
                # Check to see form is valid
                if create_knot_form.is_valid():
                    # Save data
                    new_knot = create_knot_form.save(commit=False)
                    new_knot.knot_owner = request.user
                    # Check if there is an image
                    if 'knot_image' in request.FILES:
                        print('image found')
                        # If yes, then grab it from the POST form reply
                        new_knot.knot_image= request.FILES['knot_image']
                    #commit changes
                    new_knot.save()
                    #  Successful!
                    knot_tied = True
                else:
                    # handle errors
                    print(create_knot_form.errors)

        #generate form to add a task
        create_knot_form = CreateKnotForm(request.user)

        return render(request,'taskmanager/tasks_add.html',
                              {'create_knot_form':create_knot_form,
                               'knot_tied':knot_tied})

def tasks_edit(request,title):

    if (request.POST):
        edit_knot_instance = Knots.objects.get(knot_owner = request.user, knot_title = title)
        edit_knot_form = CreateKnotForm(request.user, data=request.POST, instance=edit_knot_instance)
        if edit_knot_form.is_valid():
            edit_knot_form.save()
        return redirect('taskmanager:tasks_edit',title = edit_knot_form.cleaned_data['knot_title'])
    else:
        edit_knot_instance = Knots.objects.get(knot_owner = request.user, knot_title = title)
        edit_knot_form = CreateKnotForm(request.user, instance=edit_knot_instance)
        print(edit_knot_form.errors)

    return render(request,'taskmanager/tasks_edit.html',
                           {'edit_knot_form': edit_knot_form})
