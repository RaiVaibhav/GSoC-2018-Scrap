from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from scrap.models import Organization, Technology, Project
from .serializers import OrganizationSerializer, ProjectsSerializer, UserLoginSerializer
from django.utils.decorators import method_decorator
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt

from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)
from rest_framework.response import Response

class OrganizationListAPIView(ListAPIView):
    authentication_classes = [TokenAuthentication, BasicAuthentication]
    permission_classes = (IsAuthenticated,)
    serializer_class = OrganizationSerializer

    def get_queryset(self):
        queryset = Organization.objects.all()
        org_id = self.request.query_params.get('org_id',None)
        if org_id is not None:
            queryset = Organization.objects.filter(pk=int(org_id))
        return queryset

# class OrganizationRetrieveAPIView(RetrieveAPIView):
#     serializer_class = OrganizationSerializer
#     # queryset = Organization.objects.get(pk=self.kwargs['pk'])
#     def get_queryset(self):
#         return Organization.objects.filter(pk=int(self.kwargs['pk']))

class ProjectListAPIView(ListAPIView):
    authentication_classes = [TokenAuthentication, BasicAuthentication]
    permission_classes = (IsAuthenticated,)
    serializer_class = ProjectsSerializer
    def get_queryset(self):
        queryset = Project.objects.all()
        proj_id = self.request.query_params.get('project_id',None)
        if proj_id is not None:
            queryset = Project.objects.filter(project_id=int(proj_id))
        return queryset

# @csrf_exempt
# @api_view(["POST"])
# @permission_classes((AllowAny,))
# def login(request):
#     username = request.data.get("username")
#     password = request.data.get("password")
#     if username is None or password is None:
#         return Response({'error': 'Please provide both username and password'},
#                         status=HTTP_400_BAD_REQUEST)
#     user = authenticate(username=username, password=password)
#     if not user:
#         return Response({'error': 'Invalid Credentials'},
#                         status=HTTP_404_NOT_FOUND)
#     token, _ = Token.objects.get_or_create(user=user)
#     return Response({'token': token.key},
#                     status=HTTP_200_OK)

class UserLoginView(APIView):
    permission_classes = (AllowAny,)
    serializer_class = UserLoginSerializer

    # @method_decorator(csrf_exempt)
    # def dispatch(self, request, *args, **kwargs):
    #     return super(LoginView, self).dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = UserLoginSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            new_data = serializer.data
            return Response(new_data, status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
        # username = request.data.get("username")
        # password = request.data.get("password")
        # user = authenticate(username=username, password=password)
        # # if user is not None:
        # #     if user.is_active:
        # #         login(request, user)
        # #         return JsonResponse({'status': True})
        # if not user:
        #     return Response({'error': 'Invalid Credentials'},
        #                     status=HTTP_404_NOT_FOUND)
        # token, _ = Token.objects.get_or_create(user=user)
        # return Response({'token': token.key},
        #                 status=HTTP_200_OK)