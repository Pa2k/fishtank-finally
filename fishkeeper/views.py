from django.shortcuts import render,redirect, get_object_or_404
from myapp.models import * 
from .forms import *
# Create your views here.
def panel(request):
    return render(request,"crud/base.html")

def create_fish(request):
    if request.method == 'POST':
        fish_form = FishForm(request.POST, request.FILES)
        if fish_form.is_valid():
            fish = fish_form.save()
            request.session['fish_id'] = fish.id
            return redirect("create_food")
    else:
        fish_form = FishForm()
    return render(request, "crud/create_fish.html", {'fish_form': fish_form})

def create_food(request):
    fish_id = request.session.get('fish_id')
    if not fish_id:
        return redirect('create_fish')
    if request.method == 'POST':
        food_form = FoodForm(request.POST)
        if food_form.is_valid():
            food = food_form.save(commit=False)
            food.fish_id = fish_id
            food.save()
            return redirect("create_habitat")
    else:
        food_form = FoodForm()
    return render(request, "crud/create_food.html", {'food_form': food_form})

def create_habitat(request):
    fish_id = request.session.get('fish_id')  # ดึง fish_id จาก session

    if not fish_id:
        return redirect('create_fish')
    
    try:
        fish = Fish.objects.get(id=fish_id)
    except Fish.DoesNotExist:
        return redirect('create_fish')
    
    if request.method == 'POST':
        habitat_form = HabitatForm(request.POST)
        if habitat_form.is_valid():
            habitat = habitat_form.save(commit=False) # อย่าเพิ่งบันทึกในฐานข้อมูล
            habitat.fish = fish  # ใช้ object ของ fish แทนการตั้งค่า id โดยตรง
            habitat.save()
            del request.session['fish_id']  # ลบ fish_id ออกจาก session
            return redirect("panel")
    else:
        habitat_form = HabitatForm()
    return render(request, "crud/create_habitat.html", {'habitat_form': habitat_form})

def fish_list(request):
    fishes = Fish.objects.all()
    return render(request,'crud/fish_list.html',{'fishes':fishes})

def fish_detail(request,fish_id):
    fish = get_object_or_404(Fish, id=fish_id)  # ดึงข้อมูลปลาที่ต้องการแสดง
    foods = Food.objects.filter(fish=fish)  # ดึงข้อมูลอาหารที่สัมพันธ์กับปลา
    habitats = Habitat.objects.filter(fish=fish)
    return render(request, 'crud/fish_detail.html', {
        'fish': fish,
        'foods': foods,
        'habitats': habitats
    })

def delete_fish(request, fish_id):
    fish = get_object_or_404(Fish, id=fish_id)
    if request.method == 'POST':
        fish.delete()
        return redirect('panel')  # หรือหน้าอื่นที่ต้องการหลังจากลบ
    return render(request, 'crud/confirm_delete.html', {'fish': fish})