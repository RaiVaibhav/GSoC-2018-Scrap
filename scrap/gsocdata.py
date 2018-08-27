import requests
from pprint import pprint as pp
from scrap.models import Organization, Project

def data(url, data_list):
    if url==None:
        return data_list
    headers = {'Content-Type': 'application/json'}
    res = requests.get(url, headers=headers)
    # import pdb; pdb.set_trace()
    data_list.extend(res.json()['results'])
    url = res.json()['next']
    return data(url,data_list)

def organization_data():
    organization_list = []
    url = 'https://summerofcode.withgoogle.com/api/program/current/organization/?page=1&page_size=70'
    return data(url, data_list=organization_list)

def org_project_data(org_id):
    org_project_list = []
    str_org_id = str(org_id)
    url= 'https://summerofcode.withgoogle.com/api/program/current/project/?organization='+str_org_id+"&page=1&page_size=20"
    return data(url, data_list=org_project_list)

def project_data(org_id, org_object):
    org_project_data_list = org_project_data(org_id)
    # import pdb; pdb.set_trace()
    for project in org_project_data_list:
        # import pdb; pdb.set_trace()
        project_object = Project.objects.get_or_create(organization=org_object,
            project_id=project['id'],title=project['title'],
            display_name = project['student']['display_name'],
            description = project['abstract'],
            assignee_display_names = project['assignee_display_names'])
