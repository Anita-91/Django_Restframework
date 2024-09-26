from rest_framework import serializers
from .models import Manager, Project, Task


# -- With Normal Serializer
'''
class ManagerSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=200)
    email = serializers.EmailField()
    phone_number = serializers.CharField(max_length=15, required=False)

    def create(self, validated_data):
        return Manager.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.email = validated_data.get('email', instance.email)
        instance.phone_number = validated_data.get('phone_number', instance.phone_number)
        instance.save()
        return instance

'''

 # # -- With ModelSerializer
import re
class ManagerSerializer(serializers.ModelSerializer):
    is_valid_email = serializers.SerializerMethodField()

    class Meta:
        model = Manager
        fields = ['id', 'name', 'email', 'phone_number', 'name_length', 'is_valid_email']

    def get_is_valid_email(self, obj):
        return self.validate_email(obj.email)

    def validate_email(self, value):
        # Example of a simple regex for email validation
        email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if not re.match(email_regex, value):
            raise serializers.ValidationError("Invalid email address.")
        return True  # Email is valid


class ProjectSerializer(serializers.ModelSerializer):
    managers = ManagerSerializer(many=True, read_only=True)  # Nested serializer for managers

    class Meta:
        model = Project
        fields = ['id', 'name', 'description', 'managers', 'created_at', 'status']

class TaskSerializer(serializers.ModelSerializer):
    project = serializers.PrimaryKeyRelatedField(queryset=Project.objects.all())  # Link to Project
    assigned_to = ManagerSerializer(read_only=True)  # Nested serializer for assigned manager

    class Meta:
        model = Task
        fields = ['id', 'project', 'title', 'description', 'assigned_to', 'status']