from rest_framework import serializers
from .models import Client, Company, Invoice

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'

class InvoiceSerializer(serializers.ModelSerializer):
    client = ClientSerializer()
    company = CompanySerializer()
    class Meta:
        model = Invoice
        fields = '__all__'
    def create(self, validated_data):
        user = self.context['request'].user
        client_data = validated_data.pop('client')
        company_data = validated_data.pop('company')

        company_serializer = CompanySerializer(data=company_data)
        company_serializer.is_valid(raise_exception=True)
        company = company_serializer.save()

        client_serializer = ClientSerializer(data=client_data)
        client_serializer.is_valid(raise_exception=True)
        client = client_serializer.save()

        invoice = Invoice.objects.create(user=user,client=client, company=company, **validated_data)
    

        return invoice