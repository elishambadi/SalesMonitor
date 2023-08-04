from django.shortcuts import render, redirect
from .models import Customer, Call, Channel, Representative, Payment, Sale
from .forms import CustomerForm, CallForm, ChannelForm, RepresentativeForm, PaymentForm, SaleForm


# Home view
def home(request):
    return render(request, 'home.html')

# Customer views
def customer_list(request):
    customers = Customer.objects.all()
    return render(request, 'myapp/customer_list.html', {'customers': customers})

def customer_detail(request, customer_id):
    customer = Customer.objects.get(id=customer_id)
    return render(request, 'myapp/customer_detail.html', {'customer': customer})

def customer_create(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('customer_list')
    else:
        form = CustomerForm()
    return render(request, 'myapp/customer_form.html', {'form': form})

# Call views

def add_call(request):
    if request.method == 'POST':
        form = CallForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_calls')
    else:
        form = CallForm()
    return render(request, 'myapp/add_call.html', {'form': form})

def call_detail(request, pk):
    call = get_object_or_404(Call, pk=pk)
    return render(request, 'myapp/call_detail.html', {'call': call})

def view_calls(request):
    calls = Call.objects.all()
    return render(request, 'myapp/view_calls.html', {'calls': calls})

def delete_call(request, pk):
    call = get_object_or_404(Call, pk=pk)
    call.delete()
    return redirect('view_calls')

# Channel views

def add_channel(request):
    if request.method == 'POST':
        form = ChannelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_channels')
    else:
        form = ChannelForm()
    return render(request, 'myapp/add_channel.html', {'form': form})

def view_channels(request):
    channels = Channel.objects.all()
    return render(request, 'myapp/view_channels.html', {'channels': channels})

def channel_detail(request, pk):
    channel = get_object_or_404(Channel, pk=pk)
    return render(request, 'myapp/channel_detail.html', {'channel': channel})

def delete_channel(request, pk):
    channel = get_object_or_404(Channel, pk=pk)
    channel.delete()
    return redirect('view_channels')

# Representative views

def add_representative(request):
    if request.method == 'POST':
        form = RepresentativeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_representatives')
    else:
        form = RepresentativeForm()
    return render(request, 'myapp/add_representative.html', {'form': form})

def view_representatives(request):
    representatives = Representative.objects.all()
    return render(request, 'myapp/view_representatives.html', {'representatives': representatives})

def representative_detail(request, pk):
    representative = get_object_or_404(Representative, pk=pk)
    return render(request, 'myapp/representative_detail.html', {'representative': representative})

def delete_representative(request, pk):
    representative = get_object_or_404(Representative, pk=pk)
    representative.delete()
    return redirect('view_representatives')

# Payment views

def add_payment(request):
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_payments')
    else:
        form = PaymentForm()
    return render(request, 'myapp/add_payment.html', {'form': form})

def view_payments(request):
    payments = Payment.objects.all()
    return render(request, 'myapp/view_payments.html', {'payments': payments})

def payment_detail(request, pk):
    payment = get_object_or_404(Payment, pk=pk)
    return render(request, 'myapp/payment_detail.html', {'payment': payment})

def delete_payment(request, pk):
    payment = get_object_or_404(Payment, pk=pk)
    payment.delete()
    return redirect('view_payments')

# Sale views

def add_sale(request):
    if request.method == 'POST':
        form = SaleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_sales')
    else:
        form = SaleForm()
    return render(request, 'myapp/add_sale.html', {'form': form})

def view_sales(request):
    sales = Sale.objects.all()
    return render(request, 'myapp/view_sales.html', {'sales': sales})

def sale_detail(request, pk):
    sale = get_object_or_404(Sale, pk=pk)
    return render(request, 'myapp/sale_detail.html', {'sale': sale})

def delete_sale(request, pk):
    sale = get_object_or_404(Sale, pk=pk)
    sale.delete()
    return redirect('view_sales')

