from django.urls import path
from hackathon.views import *

urlpatterns = [
    path('hackathon/create/', HackathonCreateView.as_view(), name='hackathon_create'),
    path('hackathons/', HackathonListView.as_view(), name='hackathon_list'),
    path('hackathon/register/', HackathonRegistration.as_view(), name='hackathon-register')
    # path('hackathons/<int:pk>/update/', HackathonUpdateView.as_view(), name='hackathon_update'),
    # path('hackathons/<int:pk>/delete/', HackathonDeleteView.as_view(), name='hackathon_delete'),
]
