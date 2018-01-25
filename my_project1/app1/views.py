'''
from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Task1
from django.template import loader
# Create your views here.
def index(request):
    task_list = Task1.objects.all()
    #output = ', '.join([q.task_name for q in task_list]) + '/n '  + ', '.join([n.task_priority for n in task_list])
    context = {
        'task_list': task_list
    }
    return render(request, 'app1/index.html', context)


###def detail(request):
 #   return HttpResponse('This is the detail view')


def detail(request, task_id):
    try:
        task = Task1.objects.get(pk = task_id)
    except Task1.DoesNotExist:
        raise Http404('Task does not exist')
    context = {
        'task': task
    }
    return render(request, 'app1/detail.html', context)

'''


from django.views import generic
from .models import Task1


class IndexView(generic.ListView):
    template_name = 'app1/index.html'

    def get_queryset(self):
        return Task1.objects.all()

class DetailView(generic.DetailView):
    model = Task1
    template_name = 'app1/detail.html'

    