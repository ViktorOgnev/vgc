from django.conf.urls import patterns, include, url



urlpatterns = patterns('',
    url(r'^$', 'personnel.views.employee_list',name="personnel_employee_list"),
)