from django.shortcuts import render, redirect
from .models import Gallery
from django.core.files.storage import FileSystemStorage

def user_gallery(request):
    user_images = Gallery.objects.all()
    return render(request, 'user_gallery.html', {'user_images': user_images})

def upload_image(request):
    if request.method == 'POST' and request.FILES.get('image'):
        image = request.FILES['image']
        title = request.POST.get('title')
        description = request.POST.get('description')
        
        new_image = Gallery(

            image=image,
            title=title,
            description=description
        )
        new_image.save()

        return redirect('user_gallery')

    return render(request,'upload_image.html')

def delete(request,pk):
        image = Gallery.objects.get(pk=pk)
        image.delete()
        return redirect(user_gallery)

 
