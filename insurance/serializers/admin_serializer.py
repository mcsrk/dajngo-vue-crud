from rest_framework import serializers

from insurance.models import Admin


class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admin
        fields = '__all__'
