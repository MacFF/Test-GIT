from django.db import models

#ทุกครั้งที่มีการแก้ไขเกี่ยวกับ field หรือสร้าง model ใหม่ต้อง makemigrations และ migrate ทุกครั้ง

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)   #เอาไว้สร้างชื่อ category ใน model ตอนเพิ่มข้อมูล

    def __str__(self) -> str:
        return self.name

class Blog(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=150 , help_text="ชื่อรายการงาน")
    date = models.DateField(auto_now_add=True)
    Categoryyy = models.ForeignKey(Category,on_delete=models.CASCADE,
                                 related_name='blogs',default=None)
    def __str__(self) -> str:
        return self.title

    # ForeignKey มีวัตถุประสงค์เพื่อเชื่อมโยงระหว่าง model แห่งแรกกับ model แห่งที่สอง โดยอ้างอิงถึงคีย์หลักของ model แห่งที่สองคือ id
    # default=None  คือถ้าไม่เลือกจะเป็น null (นัล)
'''
    # related_name ใช้สำหรับกำหนดชื่อ model ที่เราจะใช้เพื่ออ้างถึง reverse relation หรือการเชื่อมโยงกลับไปยังโมเดลเริ่มต้น เช่นข้อมูลอะไรอยู่ใน category นี้
    หรือดึงเอาข้อมูลไปทำงานที่ category ได้ด้วยก็คือฟิลด์ Category จะเชื่อมโยงความสัมพันกับโมเดล Blog สามารถดูได้ว่าหมวดหมู่นี้มีบทความอะไรบ้าง
    โดยไปใส่ข้อมูลเพิ่มที่ serializers
'''
    
    




