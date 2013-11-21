from django.shortcuts import render_to_response
from django.template import RequestContext

from .models import Employee, Specialisation


def employee_list(request):
    result = []
    for specialisation in Specialisation.objects.all():
        result.append({"specialisation": specialisation,
                       "image": specialisation.image.url,
                       "trainers": []})
        for employee in Employee.objects.filter(specialisation=specialisation):
            result[-1]["trainers"].append(employee)
    context = {"specialisations": result}
    return render_to_response("personnel/employee_list.html", context,
                              context_instance=RequestContext(request))


def employee_detail(request, slug):
    employee = Employee.objects.get(slug=slug)
    context = {'trainer': employee}
    return render_to_response("personnel/employee_detail.html", context,
                              context_instance=RequestContext(request))
