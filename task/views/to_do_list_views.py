from django.shortcuts import render, redirect
from ..models import Event
from datetime import timedelta  # Make sure to import timedelta

def create_list(request):
    days_of_week = Event.DAY_OF_WEEK_CHOICES  # Get the choices from the Event model

    if request.method == 'POST':
        title = request.POST.get('title')
        start_date = request.POST.get('start_date')
        description = request.POST.get('description', '')
        duration = request.POST.get('duration')
        selected_days = request.POST.getlist('days_of_week')  # Use getlist for multiple selections

        # Create and save the event instance
        event = Event(
            title=title,
            start_date=start_date,
            description=description,
            duration=timedelta(hours=int(duration.split(':')[0]), minutes=int(duration.split(':')[1])),
            days_of_week=','.join(selected_days)
        )
        event.save()
        return render(request,'tasks/create_list.html')

    return render(request, 'tasks/create_list.html', {'days_of_week': days_of_week})
