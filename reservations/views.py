from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import Table, Reservation
from .forms import ReservationForm
from django.contrib.auth.forms import UserCreationForm
from django.utils import timezone

# Index page
def index(request):
    return render(request, 'reservations/index.html')

# Login view
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'reservations/login.html', {'error': 'Invalid credentials'})
    return render(request, 'reservations/login.html')

# Signup view
def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'reservations/signup.html', {'form': form})

# Home page
@login_required
def home(request):
    return render(request, 'reservations/home.html')

# Logout view
def logout_view(request):
    logout(request)
    return redirect('index')

# About page
def about(request):
    return render(request, 'reservations/about.html')

# Menu page
def menu(request):
    return render(request, 'reservations/menu.html')

# Reservation page
@login_required
def reservation(request):
    form = ReservationForm()
    return render(request, 'reservations/reservation.html', {'form': form})

# Choose table for reservation
@login_required
def choose_table(request, reservation_id):
    reservation = get_object_or_404(Reservation, id=reservation_id)
    tables = Table.objects.filter(available=True)
    return render(request, 'reservations/choose_table.html', {'reservation': reservation, 'tables': tables})

# Save reservation
@login_required
def save_reservation(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.user = request.user
            reservation.save()
            table = reservation.table
            table.available = False
            table.save()
            return redirect('myreserve')
    return redirect('reservation')

# Get reservation details
@login_required
def get_reservation(request):
    reservations = Reservation.objects.filter(user=request.user)
    return render(request, 'reservations/get_reservation.html', {'reservations': reservations})

# View user's reservations
@login_required
def my_reserve_view(request):
    reservations = Reservation.objects.filter(user=request.user)
    return render(request, 'reservations/my_reserve.html', {'reservations': reservations})

# Confirm reservation API
def confirm_reservation(request):
    if request.method == 'POST':
        reservation_id = request.POST.get('reservation_id')
        reservation = get_object_or_404(Reservation, id=reservation_id)
        reservation.confirmed = True
        reservation.save()
        return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'error'}, status=400)

# Get tables API
def get_tables(request):
    tables = Table.objects.all().values('number', 'capacity', 'available')
    return JsonResponse({'tables': list(tables)})
