from rest_framework import serializers
from app.models import *

class ChoicesField(serializers.Field):
    def __init__(self, choices, **kwargs):
        self._choices = choices
        super(ChoicesField, self).__init__(**kwargs)

    def to_representation(self, obj):
        return self._choices[obj]

    def to_internal_value(self, data):
        return getattr(self._choices, data)

class InstanceSerializer(serializers.ModelSerializer):
    #env = serializers.CharField(source="get_env_display",read_only=True)
    #env = serializers.SerializerMethodField(read_only=False)
    #env = ChoicesField(choices=Instance.ENVS)
    class Meta:
        model = Instance
        fields = '__all__'
