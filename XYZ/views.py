from django.shortcuts import render
from XYZ.serializer import Blogserializer,Blog,Category,CategorySerializer
from rest_framework import response
from rest_framework.decorators import api_view,APIView
from rest_framework.views import APIView
from rest_framework import status,viewsets,filters
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.authentication import BasicAuthentication #ยืนยันผ่าร user&pass
from rest_framework.permissions import IsAuthenticated,DjangoModelPermissions #IsAuthenticated ต้องยืนยันตัวต้นเท่านั้นถึงจะใช้ api นี้ได้

# Create your views here.

class Bloglist(APIView):
    queryset = Blog.objects.all() # ที่ใส่ตรงระดับคลาสอีกรอบเพราะ authentication_classes=[BasicAuthentication] ,permission_classes=[IsAuthenticated,DjangoModelPermissions] ไม่ควรใส่ระดับ method ควรใส่ระดับคลาสจึงต้องเพิ่ม query ไม่งั้น permission จะไม่มีข้อมูลใช้งาน
    authentication_classes=[BasicAuthentication] #ยืนยันผ่าร user&pass อันเดียวกับ admin 
    permission_classes=[IsAuthenticated,DjangoModelPermissions] #ต้องยืนยันตัวต้นเท่านั้นถึงจะใช้ api นี้ได้ไม่ใช่ใครก็ได้เข้าได้แบบไม่ต้อง sign in
    #DjangoModelPermissions คือให้ที่เราตั้งค่าที่ Django Admin >> user เช่น XYZ||can views blog ให้มีผลการใช้งานเพื่อกำจัดว่า member คนนี้ทำอะไรได้บ้างการใส่ DjangoModelPermissions ทำให้การกำจัดมีผลการใช้งานในโมเดลนี้

    def get(self,request):
        queryset = Blog.objects.all()    #objects.all() จะคืนค่าออกมาเป็น Queryset ที่มี object อยู่ด้านใน
        serializers = Blogserializer(queryset,many=True)
        return Response(serializers.data)

    def post(self,request):
        serializer = Blogserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED) #serializer.data ด้านหน้าคือให้แดงข้อมูลที่อัพเดตไปที่ user ด้วย
        return Response(serializer.errors,status.HTTP_400_BAD_REQUEST)
    
#GET PUT DELETE  เลือกเฉพาะตัว  
class Bloginterested(APIView):
    queryset = Blog.objects.all() # ที่ใส่ตรงระดับคลาสอีกรอบเพราะ authentication_classes=[BasicAuthentication] ,permission_classes=[IsAuthenticated,DjangoModelPermissions] ไม่ควรใส่ระดับ method ควรใส่ระดับคลาสจึงต้องเพิ่ม query ไม่งั้น permission จะไม่มีข้อมูลใช้งาน
    #เรามีใส่ global permission ตรง setting ไว้แล้วเลยไม่ต้องจุดนี้ตรง bloglist ใส่ให้ดูในกรณีที่ไม่ได้กำหนดตรง setting
    def get(self,request,id):     #request คือ request คืออ็อบเจ็กต์(django จะแปลงเป็น object)ที่เก็บข้อมูลและข้อมูลการร้องขอที่ถูกส่งมาจากผู้ใช้ผ่าน HTTP และรวมถึงข้อมูลเช่น HTTP headers, HTTP method (GET, POST, PUT, DELETE, ฯลฯ),
        blogs = Blog.objects.get(pk=id)
        serializers = Blogserializer(blogs)
        return Response(serializers.data)
    def put(self,request,id):
        blogs = Blog.objects.get(pk=id)
        serializer = Blogserializer(blogs,data=request.data)  #รับ JSON มาจาก user และใช้ Blogserializer มาแปลงเป็น object(model)
        # blogs ที่ได้จาก 29 เป็นข้อมูลเริ่มต้นสำหรับ Blogserializer ดูว่าจะอ้างอิงตัวไหนและ request.data ที่เป็นข้อมูลใหม่ที่จะมาอัพเดตแทน blogs 29
        if serializer.is_valid(): #เช็คว่ารูปแบบข้อมูลถูกต้อง
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status.HTTP_400_BAD_REQUEST)
    def delete(self,request,id):
        blogs = Blog.objects.get(pk=id)
        blogs.delete()  # save() delete() django มันจะไป save,ลบ ให้เองตามที่ตัวแปรนั้นได้มีการอ้างอิง model ไว้
        return Response(status=status.HTTP_204_NO_CONTENT)

class CategoryAPIViews(APIView):
    queryset = Blog.objects.all()
    def get(self, request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)