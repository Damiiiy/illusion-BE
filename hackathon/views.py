from rest_framework import generics
from hackathon.models import *
from .serializers import *
from rest_framework.permissions import AllowAny, IsAuthenticated
from permissions.permissions import IsHackathonUser

class HackathonCreateView(generics.CreateAPIView):
    permission_classes = [AllowAny]
    queryset = Hackathon.objects.all()
    serializer_class = HackathonSerializer
    


class HackathonListView(generics.ListAPIView):
    queryset = Hackathon.objects.all()
    serializer_class = HackathonSerializer


# class HackathonRegistration(generics.CreateAPIView):

#     queryset = HackathonApplication.objects.all()
#     serializer_class = HackathonApplicationSerializer
#     permission_classes = [IsHackathonUser, IsAuthenticated]

#     def perform_create(self, serializer):

#         user = self.request.user
#         print(user.id)
#         if user.id == validated_data.get('user'):
#             pass
#         else:
#             raise serializers.ValidationError("You cannot apply for your own hackathon.")
#         hackathon = serializer.validated_data.get('hackathon')

#         # Prevent duplicate applications
#         if HackathonApplication.objects.filter(user=user, hackathon=hackathon).exists():
#             raise serializers.ValidationError("You have already applied for this hackathon.")

#         # Save the application
#         serializer.save(user=user)


class HackathonRegistration(generics.CreateAPIView):
    queryset = HackathonApplication.objects.all()
    serializer_class = HackathonApplicationSerializer
    permission_classes = [IsHackathonUser, IsAuthenticated]

    def perform_create(self, serializer):
        user = self.request.user
        payload_user = serializer.validated_data.get('user')
        hackathon = serializer.validated_data.get('hackathon')

        if user != payload_user:
            raise serializers.ValidationError("You cannot continue this registration.")
        
        if HackathonApplication.objects.filter(user=user, hackathon=hackathon).exists():
            raise serializers.ValidationError("You have already applied for this hackathon.")

        serializer.save(user=user)


        # .git .github .idea .venv accounts courses hackathon illusion jobs permissions serializers setting staticfiles templates venv .env .gitignore changelogs.md db.sqlite3 LICENSE.md manage.py README.md requirements.txt
