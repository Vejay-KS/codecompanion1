from rest_framework import serializers
from .models import CodeCompanionUser

class CodeCompanionUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CodeCompanionUser
        fields = ('id', 'username', 'password1', 'password2', 'email', 'role', 'firstmname', 'lastname')