from django.contrib.auth import login
from django.shortcuts import redirect,render,get_object_or_404
from django.contrib.auth.views import  LoginView,LogoutView
from django.urls import reverse_lazy
from .forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test

def staff_required(user):
    return user.is_staff

# Create your views here.
def index(request):
    return render(request,"main/index.html")


@user_passes_test(staff_required)
def staff_home(request):
    return render(request,"staff/fishkeeper/fishkeeper_home.html")

@login_required
def home(request):
    return render(request,"member/fish/fish_home.html")


@login_required
def fish_card_member(request):
    fishes = Fish.objects.all()
    return render(request,'member/fish/fish_card.html',{'fishes':fishes})

@login_required
def fish_card_detail_member(request, fish_id):
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
    
    return render(request, 'member/fish/fish_card_detail.html', context)


def registration_view(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect("index")
    else:
        form = RegistrationForm()

    return render(request,"registration/register_form.html",{"form":form})

class UserLoginView(LoginView):
    template_name = 'registration/login_form.html'
    success_url = reverse_lazy("fish-home")
    
    def form_valid(self, form):
        # เข้าสู่ระบบผู้ใช้
        user = form.get_user()
        login(self.request, user)

        # ตรวจสอบสถานะ staff
        if user.is_staff:
            return redirect("staff-home")  # เปลี่ยน "staff-home" เป็นชื่อ URL ที่ต้องการให้ไปเมื่อผู้ใช้เป็น staff

        return redirect(self.get_success_url())  # ถ้าไม่ใช่ staff ให้ไปที่ success_url
    
class UserLogoutView(LogoutView):
    next_page = reverse_lazy("user-login")

@user_passes_test(staff_required)
def fish_list(request):
    fishes = Fish.objects.all()
    return render(request,'staff/fishkeeper/fish_list.html',{'fishes':fishes})
@user_passes_test(staff_required)
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
    
    return render(request, 'staff/fishkeeper/fish_detail.html', context)

@user_passes_test(staff_required)
def fish_card(request):
    fishes = Fish.objects.all()
    return render(request,'staff/fishkeeper/fish_card.html',{'fishes':fishes})
@user_passes_test(staff_required)
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
    
    return render(request, 'staff/fishkeeper/fish_card_detail.html', context)
@user_passes_test(staff_required)
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
    return render(request, 'staff/fishkeeper/create_fish.html', context)
@user_passes_test(staff_required)
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
    return render(request, 'staff/fishkeeper/add_food.html', context)
@user_passes_test(staff_required)
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
    return render(request, 'staff/fishkeeper/add_habitat.html', context)
@user_passes_test(staff_required)
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
    return render(request,'staff/fishkeeper/edit_fish.html',context)
@user_passes_test(staff_required)
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
    return render(request,'staff/fishkeeper/edit_food.html',context)
@user_passes_test(staff_required)
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
    return render(request, 'staff/fishkeeper/edit_habitat.html', context)
@user_passes_test(staff_required)
def delete_fish(request, fish_id):
    fish = get_object_or_404(Fish, id=fish_id)
    if request.method == 'POST':
        fish.delete()
        return redirect('fish_list')  # หรือหน้าอื่นที่ต้องการหลังจากลบ
    return render(request, 'staff/fishkeeper/confirm_delete.html', {'fish': fish})
@user_passes_test(staff_required)
def dashboard(request):
    fish = Fish.objects.all()
    fish_count = Fish.objects.count()
   
    # ดึงข้อมูลเพศปลาและนับจำนวนแต่ละเพศ
    male_count = Fish.objects.filter(gender='M').count()
    female_count = Fish.objects.filter(gender='F').count()
    unknown_count = Fish.objects.filter(gender='U').count()


    # Dictionary สำหรับแปลงรหัสย่อให้เป็นชื่อเต็มของแหล่งอาหาร
    FOOD_SOURCE_DICT = dict([
        ('SUR', 'บนผิวน้ำ'),
        ('DEE', 'น้ำลึก'),
        ('SHA', 'น้ำตื้น'),
        ('BOT', 'พื้นดิน'),
    ])

    # นับจำนวนปลาในแต่ละ food source
    food_sources = Food.objects.values('food_source').distinct()  # ดึงแหล่งอาหารที่ไม่ซ้ำกัน
    food_data = []
    food_labels = []
    for food in food_sources:
        count = Food.objects.filter(food_source=food['food_source']).count()
        food_labels.append(FOOD_SOURCE_DICT[food['food_source']])  # ชื่อแหล่งอาหาร
        food_data.append(count)  # จำนวนปลาในแต่ละแหล่งอาหาร

    context = {
        'fish':fish,
        'fish_count':fish_count,
        'male_count': male_count,
        'female_count': female_count,
        'unknown_count': unknown_count,
        'food_labels': food_labels,  # ส่ง label แหล่งอาหารไปยัง template
        'food_data': food_data,  # ส่งจำนวนปลาแต่ละแหล่งอาหารไปยัง template


    }
    return render(request,'staff/fishkeeper/dashboard.html',context)