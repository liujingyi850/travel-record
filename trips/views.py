from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Trip

def trip_list(request):
    trips = Trip.objects.all()
    return render(request, 'trips/trip_list.html', {'trips': trips})
from django.shortcuts import render, redirect
from .models import Trip

@login_required
def trip_new(request):
    if request.method == 'POST':
        place = request.POST.get('place', '')
        date = request.POST.get('date') or None
        with_who = request.POST.get('with_who', '')
        memo = request.POST.get('memo', '')

        Trip.objects.create(
            user=request.user,   # 先写着，后面我们再加登录限制
            place=place,
            date=date,
            with_who=with_who,
            memo=memo
        )
        return redirect('trip_list')

    return render(request, 'trips/trip_new.html')
from django.shortcuts import get_object_or_404

@login_required
def trip_edit(request, trip_id):
    trip = get_object_or_404(Trip, id=trip_id, user=request.user)

    if request.method == 'POST':
        trip.place = request.POST.get('place', '')
        trip.date = request.POST.get('date') or None
        trip.with_who = request.POST.get('with_who', '')
        trip.memo = request.POST.get('memo', '')
        trip.save()
        return redirect('trip_list')

    return render(request, 'trips/trip_edit.html', {'trip': trip})
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Trip

@login_required
def trip_delete(request, trip_id):
    trip = get_object_or_404(Trip, id=trip_id, user=request.user)

    if request.method == 'POST':
        trip.delete()
        return redirect('trip_list')

    return render(request, 'trips/trip_delete.html', {'trip': trip})
