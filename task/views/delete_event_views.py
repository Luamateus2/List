from django.shortcuts import redirect, get_object_or_404
from ..models import Event

def delete_event(request, id):
    event = get_object_or_404(Event, id=id)
    event.delete()
    return redirect('list')