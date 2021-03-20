from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Job
from django.core.paginator import Paginator
from .forms import ApplyForJobForm, AddJobForm
from django.contrib.auth.decorators import login_required
from .filters import JobFilter

# Create your views here.
def job_list(request):
    # retreiving all jobs
    jobs = Job.objects.all()

    # filter
    job_filter = JobFilter(request.GET, queryset=jobs)
    # because there is a paginator, i will pass qs for every page in pagination
    jobs = job_filter.qs

    # paginator
    paginator = Paginator(jobs, 5) # Show 25 contacts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'job/jobs.html', {
        'jobs': page_obj,
        'job_filter': job_filter
    })

def job_details(request, slug):
    job = Job.objects.get(slug=slug)

    if request.method == 'POST':
        form = ApplyForJobForm(request.POST, request.FILES)
        if form.is_valid():
            
            # dont save the form until i assign a job to the form
            submitted_form = form.save(commit=False)

            # get job field and assign a value that user has selected
            submitted_form.job = job
            
            # save the form
            submitted_form.save()
            
            # redirect again to the jobs page
            return redirect(reverse('jobs'))
    else:
        form = ApplyForJobForm()

    return render(request, 'job/job_details.html', {
        'job': job,
        'form': form
    })

@login_required
def add_job(request):
    if request.method == 'POST':
        pass
        form = AddJobForm(request.POST, request.FILES)
        if form.is_valid():
            # dont save the form until i assign an owner to the form
            submitted_form = form.save(commit=False)

            # get owner field and assign a value that user has added job
            submitted_form.owner = request.user
            
            # save the form
            submitted_form.save()

            # redirect again to the jobs page
            return redirect(reverse('jobs'))
    else:
        form = AddJobForm()
            
    return render(request, 'job/add_job.html', {
        'form': form
    })