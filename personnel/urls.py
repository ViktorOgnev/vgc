from django.conf.urls import patterns, url



urlpatterns = patterns('',
    url(r'^$', 'personnel.views.employee_list',name="personnel_employee_list"),
    url(r'^(?P<slug>[-\w]+)/?$', 'personnel.views.employee_detail',
        name="personnel_employee_detail"),

)