from django.shortcuts import render
from .models import data
def index(request):
    return render(request,'index.html')
def services(request):
    class1=data.objects.raw("select * from foundation_data where classname='1' order by subjectname")
    class2=data.objects.raw("select * from foundation_data where classname='2' order by subjectname")
    class3=data.objects.raw("select * from foundation_data where classname='3' order by subjectname")
    class4=data.objects.raw("select * from foundation_data where classname='4' order by subjectname")
    class5=data.objects.raw("select * from foundation_data where classname='5' order by subjectname")
    class6=data.objects.raw("select * from foundation_data where classname='6' order by subjectname")
    class7=data.objects.raw("select * from foundation_data where classname='7' order by subjectname")
    class8=data.objects.raw("select * from foundation_data where classname='8' order by subjectname")
    class9=data.objects.raw("select * from foundation_data where classname='9' order by subjectname")
    class10=data.objects.raw("select * from foundation_data where classname='10' order by subjectname")
    class11=data.objects.raw("select * from foundation_data where classname='11' order by subjectname")
    class12=data.objects.raw("select * from foundation_data where classname='12' order by subjectname")
    return render(request,'services.html',{'class1':class1, 'class2':class2, 'class3':class3, 'class4':class4,'class5':class5, 'class6':class6, 'class7':class7, 'class8':class8, 'class9':class9, 'class10':class10, 'class11':class11, 'class12':class12})

def video(request,clname,subname):
    vd=data.objects.raw(f"select * from foundation_data where classname='{clname}' and subjectname='{subname}'")
    return render(request,'video.html', {'vdo':vd}) 