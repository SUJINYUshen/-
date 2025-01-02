from django.shortcuts import render,redirect
from info import models
from django.http import HttpResponse
from django.contrib.auth import authenticate,login

def check_login(request):
    if not request.session.get('is_logged_in'):
        return redirect('login')  # 如果没有登录，重定向到登录页面
    return None
# Create your views here.
def login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        if username == "admin" and password == "123456":
            request.session['is_logged_in'] = True
            departments = models.Department.objects.all()
            return render(request,"info_depart.html",{"departments":departments})
        else:
            return render(request,"info_login.html",{"error":"用户名或密码错误"})
    else:
        return render(request,'info_login.html')
    
def index(request):
    return render(request,"info_index.html")


def depart(request):
    # #models.Department.objects.create(title='技术部',name='zhangsan',phone='123456',sex='男',age=18,email='123@qq.com')
    # models.Department.objects.create(title='市场部',name='lisi',phone='3903186',sex='男',age=18,email='456@qq.com')
    # #models.Department.objects.filter(id__gte=3).delete()
    # for i in models.Department.objects.filter(title='技术部').all():
    #     print(i.title,i.name,i.age,i.email,i.sex,i.phone)
    
    # return HttpResponse('ok')
    if check_login(request):
        return check_login(request)
    
    departments = models.Department.objects.all()
    return render(request,"info_depart.html",{"departments":departments})

# views.py

from django.shortcuts import render, redirect
from .models import Department

def create_department(request):
    if check_login(request):
        return check_login(request)
    
    if request.method == 'POST':
        title = request.POST.get('title')
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        sex = request.POST.get('sex')
        age = request.POST.get('age')
        email = request.POST.get('email')
        
        # 保存新部门
        Department.objects.create(
            title=title,
            name=name,
            phone=phone,
            sex=sex,
            age=age,
            email=email
        )
        
        # 创建成功后重定向到部门列表页面
        return redirect('depart')

    return render(request, 'info_department_create.html')


def depart_delete(request):

    if check_login(request):
        return check_login(request)
    

    if request.method == 'POST':
        id = request.POST.get('id')
        Department.objects.filter(id=id).delete()
        return redirect('depart')
    return render(request, 'info_department_delete.html')

from django.shortcuts import render, redirect
from .models import Department

from django.shortcuts import render, redirect
from .models import Department  # 假设你有一个 Department 模型来存储部门数据

def depart_update(request):

    if check_login(request):
        return check_login(request)
    
    # 如果是 POST 请求，则处理更新
    if request.method == "POST":
        dept_id = request.POST.get("id")
        
        # 检查是否存在 ID，如果不存在，则返回错误信息
        if not dept_id:
            return render(request, "info_department_update.html", {"error": "Department ID is required."})

        # 使用 filter().update() 更新部门信息
        updated_rows = Department.objects.filter(id=dept_id).update(
            title=request.POST.get("title"),
            name=request.POST.get("name"),
            phone=request.POST.get("phone"),
            sex=request.POST.get("sex"),
            age=request.POST.get("age"),
            email=request.POST.get("email")
        )
        
        # 如果更新的行数为 0，说明没有找到对应的部门
        if updated_rows == 0:
            return render(request, "info_department_update.html", {"error": "Department with this ID does not exist."})

        # 更新成功后跳转到部门列表
        return redirect('depart')  # 更新成功后跳转到部门列表

    # 如果没有提供 ID，返回错误信息
    return render(request, "info_department_update.html")

