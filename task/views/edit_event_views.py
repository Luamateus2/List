from django.shortcuts import render,redirect, get_object_or_404
from ..models import Event
from datetime import timedelta  # Certifique-se de importar timedelta

def edit_event(request, id):
    event = get_object_or_404(Event, id=id)

    # Calcular horas e minutos da duração
    total_seconds = int(event.duration.total_seconds())
    event.duration_hours = total_seconds // 3600
    event.duration_minutes = (total_seconds % 3600) // 60

    if request.method == 'POST':
        event.title = request.POST.get('title')
        event.start_date = request.POST.get('start_date')
        event.description = request.POST.get('description', '')
        event.days_of_week = request.POST.getlist('days_of_week')
        
        # Atualizar a duração
        duration_hours = int(request.POST.get('duration').split(':')[0])
        duration_minutes = int(request.POST.get('duration').split(':')[1])
        event.duration = timedelta(hours=duration_hours, minutes=duration_minutes)

        event.save()
        return redirect('list')  # Substitua 'list' pelo nome correto da URL ou pela URL real
        # Redirecionar ou renderizar outra página

    days_of_week = Event.DAY_OF_WEEK_CHOICES  # Supondo que isso esteja no modelo
    return render(request, 'tasks/edit_event.html', {
        'event': event,
        'days_of_week': days_of_week,
        'duration_hours': event.duration_hours,
        'duration_minutes': event.duration_minutes
    })
