from django.shortcuts import render,redirect
from .models import Imgupload

# Create your views here.
def files(request):
    if request.POST:
        main_image = request.FILES.get('files')
        obj=Imgupload(main_image=main_image)
        obj.save()
        return redirect('files')
    feeds=Imgupload.objects.all()
    return render(request,'index.html',{'feeds':feeds})

def delete(request,pk):
    de=Imgupload.objects.get(pk=pk)
    de.delete()
    return redirect(files)

    


