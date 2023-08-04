from django import forms
from .models import Customer, Call, Channel, Representative, Payment, Sale

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'  # Or specify the fields you want to include in the form

class CallForm(forms.ModelForm):
    class Meta:
        model = Call
        fields = ['call_type', 'call_category']

class ChannelForm(forms.ModelForm):
    class Meta:
        model = Channel
        fields = ['channel_type']

class RepresentativeForm(forms.ModelForm):
    class Meta:
        model = Representative
        fields = ['name', 'phone']

class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ['amount', 'payment_mode', 'payment_code', 'cheque_date']

class SaleForm(forms.ModelForm):
    class Meta:
        model = Sale
        fields = ['customer', 'call', 'channel', 'representative', 'value', 'date', 'region', 'amount', 'payment', 'comments']


