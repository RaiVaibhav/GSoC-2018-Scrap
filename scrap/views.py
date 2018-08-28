from django.shortcuts import render, get_object_or_404, render_to_response
from scrap.models import Organization, Project, Technology
from django.db.models import Count
from django.shortcuts import redirect

def tag_display(request):
    item  = Technology.objects.order_by('name')
    all_org = Organization.objects.annotate(num_projects=Count('project')).order_by('-num_projects', 'name')
    technology_tags = None
    if request.method == 'POST':
        if 'Completed Projects' not in request.POST.get('item_id'):
            item_id = request.POST.getlist('item_id')
            tags_id = map(int, item_id)
            technology_objects = Technology.objects.filter(id__in = tags_id)
            for my_object in technology_objects:
                all_org = all_org.filter(technology_tags=my_object)
            technology_tags = [i.name for i in technology_objects]
            # all_org = Organization.objects.filter(technology_tags=technology_object).annotate(num_projects=Count('project')).order_by('-num_projects','name')
            all_org = all_org.annotate(num_projects=Count('project')).order_by('-num_projects','name')
    return render(request, 'scrap/base.html', {'tags':item, 'all_org': all_org,
        'group_name': request.POST.get('item_id'),
        'technology_tag': technology_tags})
