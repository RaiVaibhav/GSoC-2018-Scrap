from django.shortcuts import render, get_object_or_404, render_to_response
from scrap.models import Organization, Project, Technology
from django.db.models import Count
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

from django.shortcuts import redirect

def tag_display(request):
    # import pdb; pdb.set_trace()
    item  = Technology.objects.order_by('name')
    all_org = Organization.objects.annotate(num_projects=Count('projects')).order_by('-num_projects', 'name')
    backup_all_org = all_org
    technology_tags = None
    if request.method == 'POST' and 'item_id' in request.POST:
        if 'Completed Projects' not in request.POST.get('item_id'):
            item_id = request.POST.getlist('item_id')
            tags_id = map(int, item_id)
            technology_objects = Technology.objects.filter(id__in = tags_id)
            for my_object in technology_objects:
                all_org = all_org.filter(technology_tags=my_object)
            if len(all_org)==0:
                all_org=backup_all_org.filter(technology_tags__in=technology_objects)
            technology_tags = [i.name for i in technology_objects]
            # all_org = Organization.objects.filter(technology_tags=technology_object).annotate(num_projects=Count('project')).order_by('-num_projects','name')
            all_org = all_org.annotate(num_projects=Count('projects')).order_by('-num_projects','name')
    return render(request, 'scrap/base.html', {'tags':item, 'all_org': all_org,
        'group_name': request.POST.get('item_id'),
        'technology_tag': technology_tags})

def register(request):
    if request.method =='POST':
        form  = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login')
        #if request method is 'POST' means user is sending data to web server
        #if request method is 'GET' it means the data/page from web server

    else:
        form = UserCreationForm()
    return render(request, 'scrap/register.html', {'form': form})

def logout_session(request):
    logout(request)
    return redirect('tag_list')