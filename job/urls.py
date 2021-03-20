from django.urls import path, include
from . import views
from . import api

urlpatterns = [
    path('jobs', views.job_list, name="jobs"),
    path('jobs/job_details/<str:slug>', views.job_details, name='job_details'),
    path('jobs/add_job', views.add_job, name='add_job'),

    # api
    path('api/jobs', api.jobs, name='jobs'),
    path('api/jobs/<int:pk>', api.job_detail, name='job_detail'),
    path('api/jobs/create_job', api.create_job, name='create_job'),
]
