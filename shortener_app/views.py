from django.shortcuts import render
from hashlib import md5
from .models import URL

def home(request):
    if request.method == 'GET':
        return render(request, 'add.html')
    elif request.method == 'POST':
        entered_url = request.POST['url']
        if URL.objects.filter(original_url = entered_url).exists():
            all_urls = URL.objects.all()
            return render(request, 'list.html', {'objects': all_urls})
        else:
            hashed = md5(f'{entered_url}'.encode()).hexdigest()[:5]

            while(URL.objects.filter(shortened_url = hashed)):
                hashed = md5(f'{entered_url}'.encode()).hexdigest()[:5]

            new_URL_object = URL.objects.create(
                original_url = entered_url, 
                shortened_url = hashed
                )
            new_URL_object.save()
            all_urls = URL.objects.all()
            return render(request, 'list.html', {'objects': all_urls})
            


        
        
