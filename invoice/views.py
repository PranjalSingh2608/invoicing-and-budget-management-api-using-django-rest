from rest_framework import generics,permissions
from .models import Invoice,Client, Company
from .serializers import InvoiceSerializer,ClientSerializer,CompanySerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from drf_yasg.utils import swagger_auto_schema
from  rest_framework.authentication import TokenAuthentication

@swagger_auto_schema(
    method='post',
)



class InvoiceListCreateAPIView(generics.ListCreateAPIView):
    queryset=Invoice.objects.all()
    serializer_class=InvoiceSerializer
    permission_classes=[IsAuthenticated]
    authentication_classes=[TokenAuthentication]
invoice_list_create_view=InvoiceListCreateAPIView.as_view()

class InvoiceDetailAPIView(generics.RetrieveAPIView):
    queryset=Invoice.objects.all()
    serializer_class=InvoiceSerializer
    permission_classes=[IsAuthenticated]
    authentication_classes=[TokenAuthentication]
invoice_detail_view=InvoiceDetailAPIView.as_view()

class InvoiceUpdateAPIView(generics.UpdateAPIView):
    queryset=Invoice.objects.all()
    serializer_class=InvoiceSerializer
    permission_classes=[IsAuthenticated]
    authentication_classes=[TokenAuthentication]
invoice_update_view=InvoiceUpdateAPIView.as_view()

class InvoiceDestroyAPIView(generics.DestroyAPIView):
    queryset=Invoice.objects.all()
    serializer_class=InvoiceSerializer
    permission_classes=[IsAuthenticated]
    authentication_classes=[TokenAuthentication]
    lookup_field='pk'    
    def perform_destroy(self, instance):
        super().perform_destroy(instance)

invoice_delete_view = InvoiceDestroyAPIView.as_view()
