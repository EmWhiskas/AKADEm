from django.shortcuts import render, redirect
import os
from .models import *
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from .forms import *
from django.contrib import messages
from django.db.models import Sum
from django.contrib.auth.decorators import login_required
# Create your views here.
def register(req):
    # form = UserCreationForm
    if req.POST:
        form = FormRegister(req.POST)
        if form.is_valid():
            k1 = form.cleaned_data.get('username')
            k2 = form.cleaned_data.get('password1')
            k3 = form.cleaned_data.get('email')
            k4 = form.cleaned_data.get('first_name')
            k5 = form.cleaned_data.get('last_name')
            user = User.objects.create_user(username=k1, password=k2)
            user = User.objects.get(username=k1)
            user.email = k3
            user.last_name = k5
            user.first_name = k4
            login(req, user)
            user.save()
            return redirect('home')
    else:
        form = FormRegister()
    data = {'form':form}
    return render(req, 'registration/registration.html', data)

def profile(req):
    return render(req, 'index.html')

def index(request):
    forma = AddFile()
    if request.user.is_authenticated:
        user = request.user
        user_files = File.objects.filter(user=user)
        if user_files:
            total_file_size = File.objects.filter(user=user).aggregate(total_size=Sum('file_size'))['total_size'] or 0
            total_file_size_gb = total_file_size / (1024 ** 3)
            for file in user_files:
                storages = file.size.all()
                for storage in storages:
                    size_gb = storage.size / (1024 ** 3)
            total_file_sizeMB = total_file_size / (1024 * 1024)
        else:
            return redirect('add')
    else:
        return redirect('login')

    data = {'files': user_files, 'forma':forma, 'total_file_size':total_file_size_gb, 'limit':size_gb, 'total_file_sizeMB':total_file_sizeMB}
    return render(request, 'index.html', data)

def look(req, cat):
    item = File.objects.filter(category=cat, user_id=req.user.id)
    forma = AddFile()
    data = {'item':item, 'forma':forma}
    return render(req, 'look.html', data)

# def add(req):
#     forma = AddFile()
#     data = {'forma': forma}
#     return render(req, 'add.html', data)

def add(request):
    global k3
    if request.POST:
        forma = AddFile(request.POST, request.FILES)  # Передаем данные POST и FILES
        print("Данные формы:", request.POST)
        print("FILES:", request.FILES)
        if forma.is_valid():
            print(2)
            photo = [
                'svg',  # Scalable Vector Graphics
                'jpg',  # JPEG image
                'jpeg',  # JPEG image
                'png',  # Portable Network Graphics
                'gif',  # Graphics Interchange Format
                'bmp',  # Bitmap Image File
                'tiff',  # Tagged Image File Format
                'webp',  # Web Picture format
                'heic',  # High Efficiency Image Container
                'raw',  # Raw Image Format
            ]
            video = [
                'mp4',  # MPEG-4 Video
                'mov',  # QuickTime Movie
                'avi',  # Audio Video Interleave
                'mkv',  # Matroska Video
                'mpg',  # MPEG Video
                'mpeg',  # Moving Picture Experts Group
                'wmv',  # Windows Media Video
                'flv',  # Flash Video
                'webm',  # WebM Video Format
                '3gp',  # 3rd Generation Partnership Project
                'vob',  # Video Object
            ]
            doc = forma.cleaned_data['file']
            dot_index = doc.name.rfind('.')
            typefile = doc.name[dot_index + 1:]
            k1 = doc.name
            k2 = forma.cleaned_data['file']
            k3 = 'Д'
            if typefile in photo:
                k3 = 'Ф'
            elif typefile in video:
                k3 = 'В'

            if k3 == 'Ф':
                k4 = forma.cleaned_data['file']
            elif k3 == 'В':
                k4 = 'app/static/img/video.png'
            elif typefile == 'docx':
                k4 = 'app/static/img/MSword.png'
            elif typefile == 'pptx':
                k4 = 'app/static/img/MSpowerpoint.png'
            elif typefile == 'xlsx':
                k4 = 'app/static/img/MSexcel.png'
            elif typefile == 'pdf':
                k4 = 'app/static/img/pdf.png'
            elif typefile == 'txt':
                k4 = 'app/static/img/txt.png'
            elif typefile == 'zip' or typefile == 'rar':
                k4 = 'app/static/img/zip.png'
            else:
                k4 = 'app/static/img/doc.png'
            k5 = k2.size
            File.objects.create(
                name=k1,
                file=k2,
                category=k3,
                img=k4,
                user_id=request.user.id,
                file_size=k5
            )
            return redirect('look/' + k3)
        else:
            print("Ошибки формы:", forma.errors)
            messages.error(request, "Ошибка в данных формы: " + str(forma.errors))
    else:
        forma = AddFile()

    data = {'forma': forma}
    return render(request, 'add.html', data)
def deletefile(req, id):
    itemid = int(id)
    item = File.objects.get(id=itemid)
    cat = item.category
    os.remove('app/static/'+str(item.file))
    item.delete()
    return render(req, 'index.html')

def addgb(request):
    pass

