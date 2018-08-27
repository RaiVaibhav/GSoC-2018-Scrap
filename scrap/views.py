from django.shortcuts import render, get_object_or_404, render_to_response
from scrap.models import Organization, Project, Technology
# Create your views here.
from django.shortcuts import redirect

# def list_display(request, org_objects):
#     return render(request, 'scrap/org_list.html', {'org_objects':org_objects})

def tag_display(request):
    item  = Technology.objects.order_by('name')
    # form = request.POST
    # import pdb; pdb.set_trace()
    print(request.method)
    if request.method == 'POST':
       technology_object = get_object_or_404(Technology, pk=request.POST.get('item_id'))
       # print(technology_object)
       org_objects = Organization.objects.filter(technology_tags=technology_object).order_by('name')
       # return redirect('list_display', org_objects=org_objects)
       # import pdb; pdb.set_trace()
       return render(request, 'scrap/org_list.html', {'org_objects':org_objects})
    return render(request, 'scrap/base.html', {'tags':item})
