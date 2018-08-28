from django.shortcuts import render, get_object_or_404, render_to_response
from scrap.models import Organization, Project, Technology
from django.db.models import Count
from django.shortcuts import redirect

def tag_display(request):
    item  = Technology.objects.order_by('name')
    all_org = Organization.objects.annotate(num_projects=Count('project')).order_by('-num_projects', 'name')
    technology_tag = None
    if request.method == 'POST':
        if request.POST.get('item_id')!='Completed Projects':
            technology_object = get_object_or_404(Technology, pk=int(request.POST.get('item_id')))
            technology_tag = technology_object.name
            all_org = Organization.objects.filter(technology_tags=technology_object).order_by('name')
    return render(request, 'scrap/base.html', {'tags':item, 'all_org': all_org,
        'group_name': request.POST.get('item_id'),
        'technology_tag': technology_tag})
