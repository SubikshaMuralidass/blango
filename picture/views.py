#from django.shortcuts import render
# Create your views here.

from django.views.generic import ListView, DetailView
from django.shortcuts import render, get_object_or_404
from .models import Event, Image

class GalleryView(ListView):
    model = Event
    template_name = 'Gallery.html'
    context_object_name = 'events'
    paginate_by = 9
    ordering = ['-date']

class EventDetailView(DetailView):
    model = Event
    template_name = 'event_detail.html'
    context_object_name = 'event'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['images'] = self.object.images.all()
        return context

def gallery_grid(request):
    events = Event.objects.all().order_by('-date')
    return render(request, 'gallery_grid.html', {
        'events': events
    })


def event_images(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    images = event.images.all()
    return render(request, 'event_images.html', {
        'event': event,
        'images': images
    })
