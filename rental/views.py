from django.core.serializers import deserialize, serialize
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import RentalForm
from catalog.models import Game
from identity.models import Address
from .models import Rental


# Create your views here.

@login_required(login_url='login')
def rent_game(request, game_id):
    game = get_object_or_404(Game, id=game_id)

    if request.method == 'POST':
        form = RentalForm(request.POST, initial={'game': game, 'user': request.user})
        if form.is_valid():
            form.instance.user = request.user
            form.instance.status = 'pending'
            form.instance.game = game
            form.save()
            return redirect('home')
    else:
        form = RentalForm(initial={'game': game, 'user': request.user})
    return render(request, 'rent_game.html', {'form': form, 'game': game})


def get_address_details(request, address_id):
    address = get_object_or_404(Address, id=address_id)
    address_details = {
        'street': address.street,
        'city': address.city,
        'state': address.state,
        'zip_code': address.zip_code,
    }
    return JsonResponse(address_details)


@login_required(login_url='login')
def get_rental_history(request):
    user_rentals = Rental.objects.filter(user=request.user).prefetch_related('game')
    return render(request, 'rent_history.html', {'user_rentals': user_rentals})


def generate_rental_history_xml(request):
    if request.method == 'POST':
        user_rentals = Rental.objects.filter(user=request.user)
        xml_data = serialize('xml', user_rentals)
        response = HttpResponse(xml_data, content_type='application/xml')
        response['Content-Disposition'] = 'attachment; filename="rental_history.xml"'
        return response
    return HttpResponse(status=405)


def upload_rental_history_xml(request):
    if request.method == 'POST' and request.FILES.get('file'):
        uploaded_file = request.FILES['file']
        xml_data = uploaded_file.read().decode('utf-8')
        deserialized_data = list(deserialize('xml', xml_data))
        user_rentals = [obj.object for obj in deserialized_data if isinstance(obj.object, Rental)]
        context = {'user_rentals': user_rentals}
        return render(request, 'rent_history_upload.html', context)
    else:
        return render(request, 'rent_history_upload.html', {'user_rentals': ""})
