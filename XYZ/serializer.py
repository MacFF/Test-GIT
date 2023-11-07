from rest_framework import serializers
from XYZ.models import *

class Blogserializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__'
    # Categoryyy = serializers.StringRelatedField()
    #**แต่ต้องกำหนดตัวแปนให้ตรงกับชื่อ field ของ model blog ให้ถูกต้องกรณีนี้มีฟิลด์เดิมชื่อ Categoryyy เลยต้องใช้ตัวแปรชื่อนี้เพื่อไปแทนตัวเก่า**

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
    blogs = Blogserializer(read_only=True,many=True)  
    #ที่ไม่ต้องระบุชื่อ field เพราะเรากำหนดชื่อ related_name='blogs' ที่ฟิลด์ Categoryyy ของmodel ไปแล้วการระบุชื่อนี้ก็เหมือนกับใช้ตัวแปรชื่อฟิลด์ Categoryyy ของ model


    # มันมีความสัมพันกันอยู่แล้วจาก related_name='blogs' จึงนำตัวแปร blogs มาใส่และเอา Blogserializer มาใส่ได้เลย
    # blogs = Blogserializer(read_only=True,many=True)  
    #ดึงเอาข้อมูลบทความที่เกี่ยวข้องที่อยู่ใน category นี้มาใช้งาน
    #blogs ตัวนี้มาจาก related_name='blogs'






'''
ถ้า category เป็นแบบด้านล่างและอยากให้ข้อมูล category แสดงแค่  "Categoryyy": "อาหารกระป๋อง",       

        "category": {
            "id": 1,
            "name": "อาหารกระป๋อง",
            "description": null
        },
ให้ทำตามด้านล่างนี้
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class Blogserializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__'
    Categoryyy = serializers.StringRelatedField()

##StringRelatedField ใน Django REST framework (DRF) เป็น serializer field ที่ใช้ในการแสดงค่าของฟิลด์ในรูปแบบข้อความ (string)
***แต่ต้องกำหนดตัวแปนให้ตรงกับชื่อ field ของ model blog ให้ถูกต้องเช่น Categoryyy**

'''