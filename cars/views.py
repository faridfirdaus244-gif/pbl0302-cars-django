from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from .models import Car
from .forms import CarForm

def car_list(request):
    q = request.GET.get('q', '').strip()
    cars = Car.objects.all().order_by('id')
    if q:
        cars = cars.filter(
            Q(carname__icontains=q) |
            Q(carbrand__icontains=q) |
            Q(carmodel__icontains=q)
        )
    return render(request, 'cars/car_list.html', {'cars': cars, 'q': q})

def car_create(request):
    form = CarForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('car_list')
    return render(request, 'cars/car_form.html', {'form': form, 'title': 'Create Car Data'})

def car_update(request, pk):
    car = get_object_or_404(Car, pk=pk)
    form = CarForm(request.POST or None, instance=car)
    if form.is_valid():
        form.save()
        return redirect('car_list')
    return render(request, 'cars/car_form.html', {'form': form, 'title': 'Update Car Data'})

def car_delete(request, pk):
    car = get_object_or_404(Car, pk=pk)
    if request.method == 'POST':
        car.delete()
        return redirect('car_list')
    return render(request, 'cars/car_confirm_delete.html', {'car': car})