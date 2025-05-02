from rest_framework import serializers
from hackathon.models import *
from django.utils.text import slugify

class HackathonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hackathon
        fields = ['id', 'title', 'slug', 'start_date', 'end_date', 'venue']
        read_only_fields = ['id', 'slug']

    def create(self, validated_data):
        title = validated_data.get('title')
        validated_data['slug'] = slugify(title)
        return super().create(validated_data)


class HackathonApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = HackathonApplication
        fields = ['hackathon', 'applied_at']
        read_only_fields = ['id', 'applied_at']
    
















    
    # def create(self, validated_data):
    #     hackathon = validated_data.get('hackathon')
    #     user = validated_data.get('user')
        
    #     if HackathonApplication.objects.filter(hackathon=hackathon, user=user).exists():
    #         raise serializers.ValidationError("You have already applied for this hackathon.")
    #     return super().create(validated_data)


    # def create(self, validated_data):
    #     hackathon_id = validated_data.get('hackathon')
    #     hackathon = Hackathon.objects.get(id=hackathon_id)
    #     print(hackathon)
    #     if HackathonApplication.objects.filter(hackathon=hackathon).exists():
    #         raise serializers.ValidationError("You have already applied for this hackathon.")
    #     return super().create(validated_data)