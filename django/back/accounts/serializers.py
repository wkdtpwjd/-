from rest_framework import serializers
from django.contrib.auth import get_user_model

class ProfileSerializer(serializers.ModelSerializer):
    followers = serializers.PrimaryKeyRelatedField(queryset=get_user_model().followers, many=True)
    class Meta:
        model = get_user_model()
        fields = ('username', 'first_name', 'last_name','gender','age','region','followings', 'followers')


