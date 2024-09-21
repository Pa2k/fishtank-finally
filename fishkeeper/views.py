from django.shortcuts import render,redirect, get_object_or_404
from myapp.models import * 
from .forms import *


# Create your views here.


def create_fish(request):
    if request.method == 'POST':
        fish_form = FishForm(request.POST, request.FILES)
        if fish_form.is_valid():
            fish = fish_form.save()  # บันทึกข้อมูลปลา
            return redirect('add_food', fish_id=fish.id)  # เปลี่ยนเส้นทางไปยังหน้าเพิ่มอาหาร
    else:
        fish_form = FishForm()

    context = {
        'fish_form': fish_form,
    }
    return render(request, 'crud/create_fish.html', context)

def add_food(request, fish_id):
    fish = get_object_or_404(Fish, id=fish_id)
    if request.method == 'POST':
        food_form = FoodForm(request.POST)
        if food_form.is_valid():
            food = food_form.save(commit=False)
            food.fish = fish  # เชื่อมโยงอาหารกับปลา
            food.save()
            return redirect('add_habitat', fish_id=fish.id)  # เปลี่ยนเส้นทางไปยังหน้าเพิ่มแหล่งที่อยู่
    else:
        food_form = FoodForm()

    context = {
        'food_form': food_form,
        'fish': fish,
    }
    return render(request, 'crud/add_food.html', context)

def add_habitat(request, fish_id):
    fish = get_object_or_404(Fish, id=fish_id)
    if request.method == 'POST':
        habitat_form = HabitatForm(request.POST)
        if habitat_form.is_valid():
            habitat = habitat_form.save(commit=False)
            habitat.fish = fish  # เชื่อมโยงแหล่งที่อยู่กับปลา
            habitat.save()
            return redirect('fish_list')  # เปลี่ยนเส้นทางไปยังหน้ารายการปลา
    else:
        habitat_form = HabitatForm()

    context = {
        'habitat_form': habitat_form,
        'fish': fish,
    }
    return render(request, 'crud/add_habitat.html', context)

def edit_fish(request,fish_id):
    fish = get_object_or_404(Fish,id =fish_id)

    if request.method == 'POST':
        fish_form = FishForm(request.POST,request.FILES,instance=fish)
        if fish_form.is_valid():
            fish =fish_form.save()
            return redirect('fish_detail',fish_id =fish.id)
    else:
        fish_form = FishForm(instance=fish)
    
    context={
        'fish_form':fish_form,
        'fish':fish
    }
    return render(request,'crud/edit_fish.html',context)

def edit_food(request,food_id):
    food = get_object_or_404(Food,id = food_id)
    fish = food.fish
    if request.method == 'POST':
        food_form = FoodForm(request.POST,instance=food)
        if food_form.is_valid():
            food_form.save()
            return redirect('fish_detail',fish_id =food.fish.id)

    else:
        food_form = FoodForm(instance=food)

    context = {
        'food_form':food_form,
        'food':food,
        'fish': fish,
    }
    return render(request,'crud/edit_food.html',context)

def edit_habitat(request, habitat_id):
    habitat = get_object_or_404(Habitat, id=habitat_id)
    fish = habitat.fish  # เชื่อมโยงกับปลา

    if request.method == 'POST':
        habitat_form = HabitatForm(request.POST, instance=habitat)
        if habitat_form.is_valid():
            habitat_form.save()
            return redirect('fish_detail', fish_id=habitat.fish.id)

    else:
        habitat_form = HabitatForm(instance=habitat)

    context = {
        'habitat_form': habitat_form,
        'habitat': habitat,
        'fish': fish,
    }
    return render(request, 'crud/edit_habitat.html', context)

def fish_list(request):
    fishes = Fish.objects.all()
    return render(request,'crud/fish_list.html',{'fishes':fishes})

def fish_card(request):
    fishes = Fish.objects.all()
    return render(request,'crud/fish_card.html',{'fishes':fishes})

def fish_card_detail(request, fish_id):
    # ดึงข้อมูลปลาที่ต้องการแสดง
    fish = get_object_or_404(Fish, id=fish_id)
    # ดึงข้อมูลอาหารที่สัมพันธ์กับปลา
    foods = Food.objects.filter(fish=fish)
    # ดึงข้อมูลแหล่งที่อยู่ที่สัมพันธ์กับปลา
    habitats = Habitat.objects.filter(fish=fish)
    
    context = {
        'fish': fish,
        'foods': foods,
        'habitats': habitats
    }
    
    return render(request, 'crud/fish_card_detail.html', context)

def fish_detail(request, fish_id):
    # ดึงข้อมูลปลาที่ต้องการแสดง
    fish = get_object_or_404(Fish, id=fish_id)
    # ดึงข้อมูลอาหารที่สัมพันธ์กับปลา
    foods = Food.objects.filter(fish=fish)
    # ดึงข้อมูลแหล่งที่อยู่ที่สัมพันธ์กับปลา
    habitats = Habitat.objects.filter(fish=fish)
    
    context = {
        'fish': fish,
        'foods': foods,
        'habitats': habitats
    }
    
    return render(request, 'crud/fish_detail.html', context)

def delete_fish(request, fish_id):
    fish = get_object_or_404(Fish, id=fish_id)
    if request.method == 'POST':
        fish.delete()
        return redirect('fish_list')  # หรือหน้าอื่นที่ต้องการหลังจากลบ
    return render(request, 'crud/confirm_delete.html', {'fish': fish})