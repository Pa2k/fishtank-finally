from django.db import models

# Create your models here.

class Fish(models.Model):
    GENDER_CHOICES = [
        ('M', 'เพศผู้'),
        ('F', 'เพศเมีย'),
        ('U', 'ไม่ทราบเพศ'),
    ]
    fish_name = models.CharField(max_length=255,verbose_name='ชื่อปลา')
    species = models.CharField(max_length=255,verbose_name='สายพันธ์ุ')
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default='U', verbose_name='เพศ')
    birth_date = models.DateField(verbose_name='วันเกิด')
    description = models.TextField(verbose_name='รายละเอียด')
    size = models.FloatField(verbose_name='ขนาด')
    image = models.ImageField(upload_to='fishimage',verbose_name='รูปปลา')

    def __str__(self) :
        return self.fish_name

class Food(models.Model):
    FOOD_SOURCE_CHOICES = [
        ('SUR', 'บนผิวน้ำ'),
        ('DEE', 'น้ำลึก'),
        ('SHA', 'น้ำตื้น'),
        ('BOT', 'พื้นดิน'),
    ]

    fish = models.ForeignKey(Fish, on_delete=models.CASCADE, verbose_name='ปลา')
    food_type = models.CharField(max_length=255,verbose_name='ประเภทอาหาร')
    food_name = models.CharField(max_length=255, verbose_name='ชื่ออาหาร')
    feeding_frequency = models.IntegerField(verbose_name='ความถี่ในการให้อาหาร')
    food_source = models.CharField(max_length=3, choices=FOOD_SOURCE_CHOICES, default='SUR', verbose_name='แหล่งอาหาร')

    def __str__(self) :
        return self.food_name

class Habitat(models.Model):
    MIGRATION_CHOICES = [
        ('Y', 'อพยพ'),
        ('N', 'ไม่อพยพ'),
        ('S', 'อพยพตามฤดูกาล'),
    ]
    fish = models.ForeignKey(Fish, on_delete=models.CASCADE, verbose_name='ปลา')
    habitat_name = models.CharField(max_length=255, verbose_name='ชื่อแหล่งที่อยู่')  
    temperature = models.FloatField(verbose_name='อุณหภูมิ') 
    ph_level = models.FloatField(verbose_name='ค่าความเป็นกรด-ด่าง (pH)')  
    migration = models.CharField(max_length=1, choices=MIGRATION_CHOICES, default='N', verbose_name='การอพยพ') 

    def __str__(self) :
        return self.habitat_name