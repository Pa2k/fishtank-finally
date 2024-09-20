from django.shortcuts import render,redirect, get_object_or_404
from myapp.models import * 
from .forms import *
from django.forms import inlineformset_factory
# Create your views here.
def panel(request):
    return render(request,"mains/base.html")

# สร้าง formsets สำหรับ Food และ Habitat
FoodFormSet = inlineformset_factory(Fish, Food, form=FoodForm, extra=1)
HabitatFormSet = inlineformset_factory(Fish, Habitat, form=HabitatForm, extra=1)

def create_fish(request):
    if request.method == 'POST':
        fish_form = FishForm(request.POST, request.FILES)
        food_formset = FoodFormSet(request.POST, instance=None)  # instance=None เนื่องจากยังไม่มี Fish ที่จะเชื่อม
        habitat_formset = HabitatFormSet(request.POST, instance=None)

        if fish_form.is_valid() and food_formset.is_valid() and habitat_formset.is_valid():
            fish = fish_form.save()  # บันทึกข้อมูลปลา
            food_formset.instance = fish  # เชื่อมโยง food กับ fish
            food_formset.save()  # บันทึกข้อมูลอาหาร
            habitat_formset.instance = fish  # เชื่อมโยง habitat กับ fish
            habitat_formset.save()  # บันทึกข้อมูลที่อยู่
            return redirect('panel')  # กลับไปหน้า panel หลังบันทึกสำเร็จ
    else:
        fish_form = FishForm()
        food_formset = FoodFormSet(instance=None)  # ไม่ต้องใส่ instance ตอนแรก
        habitat_formset = HabitatFormSet(instance=None)

    return render(request, "crud/create_fish.html", {
        'fish_form': fish_form,
        'food_formset': food_formset,
        'habitat_formset': habitat_formset,
    })

def edit_fish(request, fish_id):
    # ดึงข้อมูลปลา (Fish) ที่ต้องการแก้ไข ถ้าไม่มีจะได้ 404
    fish = get_object_or_404(Fish, id=fish_id)

    # สร้าง form สำหรับ Fish, Food, Habitat โดยใช้ instance ของปลา (Fish)
    if request.method == 'POST':
        fish_form = FishForm(request.POST, request.FILES, instance=fish)
        food_formset = FoodFormSet(request.POST, instance=fish)
        habitat_formset = HabitatFormSet(request.POST, instance=fish)

        # ตรวจสอบว่าแต่ละฟอร์มถูกต้องหรือไม่
        if fish_form.is_valid() and food_formset.is_valid() and habitat_formset.is_valid():
            # บันทึกการแก้ไข
            fish = fish_form.save()
            food_formset.instance = fish  # เชื่อมโยง food กับปลา
            food_formset.save()
            habitat_formset.instance = fish  # เชื่อมโยง habitat กับปลา
            habitat_formset.save()

            return redirect('fish_list')
    else:
        # GET: แสดงข้อมูลในฟอร์มเพื่อแก้ไข
        fish_form = FishForm(instance=fish)
        food_formset = FoodFormSet(instance=fish)
        habitat_formset = HabitatFormSet(instance=fish)

    # ส่ง form และ formset ไปยัง template
    return render(request, 'crud/edit_fish.html', {
        'fish_form': fish_form,
        'food_formset': food_formset,
        'habitat_formset': habitat_formset,
    })

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