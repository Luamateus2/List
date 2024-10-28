from django.shortcuts import render
from ..models import Event

def list(request):
    events = Event.objects.all()
    for event in events:
        # Extrai os segundos do timedelta
        total_seconds = int(event.duration.total_seconds())
        event.duration_hours = total_seconds // 3600
        event.duration_minutes = (total_seconds % 3600) // 60
    return render(request, 'tasks/list.html', {'events': events})
