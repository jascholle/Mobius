from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.db.models import Max

from .models import Person

from django.template import loader



def index(request):
    ordered_person_list = Person.objects.order_by('order')
    context = {'ordered_person_list': ordered_person_list}
    return render(request, 'tdlist/index.html', context)



def bump(request, person_id):

    person = get_object_or_404(Person, pk=person_id)

    max_order_object = Person.objects.all().aggregate(Max('order'))

    person.order = max_order_object['order__max'] + 1
    person.save()

    return HttpResponseRedirect(reverse('tdlist:index'))