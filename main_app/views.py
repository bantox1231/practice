from django.shortcuts import render, get_object_or_404
from .models import CarsListModel, Afisha, Slider
def car_list_view(request):
    if request.method == "GET":
        car_list = CarsListModel.objects.all()
        afisha_list = Afisha.objects.all()
        slider_list = Slider.objects.all()
        return render(request, template_name='cars/index.html', context={
            'car_list': car_list,
            'afisha_list': afisha_list,
            'slider_list': slider_list
        })

def car_list_detail_view(request, id):
    if request.method == 'GET':
        car_id = get_object_or_404(CarsListModel, id=id)
        return render(request, template_name='cars/car_detail.html', context={'car_id': car_id})