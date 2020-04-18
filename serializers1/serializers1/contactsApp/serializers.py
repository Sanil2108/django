from rest_framework import serializers

from contactsApp.models import User, Car, Engine

class Contact(object):
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

# class Car(object):
#     def __init__(self, model, make):
#         self.model = model
#         self.make = make

# class Engine(object):
#     def __init__(self, name, year);
#         self.name = name
#         self.year = year

# class EngineSerializer(serializers.Serializer):
#     name = serializers.CharField(max_length = 200)
#     year = serializers.IntegerField()

#     def create(self, validated_data):
#         return Engine(**validated_data)

# class CarSerializer(serializers.Serializer):
#     model = serializers.CharField(max_length = 200)
#     make = serializers.IntegerField()
#     engineSerializer = EngineSerializer()

#     def create(self, validated_data):
#         engineData = validated_data.pop('engine')
#         car = Car(validated_data.pop('model'), validated_data.pop('make'))
#         car.engine = EngineSerializer


class ContactSerializer(serializers.Serializer):
    name = serializers.CharField(max_length = 200)
    phone = serializers.IntegerField()

    def create(self, validated_data):
        return Contact(**validated_data)

    def update(self, instance, validated_data):
        return instance

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class EngineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Engine
        fields = '__all__'

class CarSerializer(serializers.ModelSerializer):
    # name = serializers.CharField(required = False)
    # engines = serializers.StringRelatedField(many = True)
    engines = EngineSerializer(many = True, read_only = True)

    class Meta:
        model = Car
        fields = '__all__'
        # depth = 2