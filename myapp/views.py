from django.shortcuts import render, get_object_or_404, redirect
from .models import Image, About, Contact
from django.db.models import Q
from .forms import ImageForm
# Create your views here.
""""     Home Page       """
def index(request):
    context = {}
    context['title'] = "Home | Image Grid"
    context['images'] = Image.objects.all().order_by("-id")
    context['about'] = About.objects.all()
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        msg = request.POST.get('msg')
        results = Contact(name=name, email=email, subject=subject, details=msg)
        if results:
            contact_msg = "ok"
            results.save()
            context['contact_msg'] = contact_msg
        else:
            contact_msg = "no"
            context['contact_msg'] = contact_msg
    return render(request, 'index.html', context)
""""     image Page       """
def image_page(request):
    context = {}
    context['title'] = "Image | Image Grid"
    context['images'] = Image.objects.all().order_by("-id")
    return render(request, 'image.html', context)

""""     details Page       """
def details(request, id):
    context = {}
    context['title'] = "| Image Grid"
    context['image'] = get_object_or_404(Image, id=id)
    return render(request, 'details.html', context)

""""     Search Page       """
def search(request):
    context = {}
    context['title'] = "Search | Image Grid"
    query = None
    result = []
    if request.method == "GET":
        query = request.GET.get('search')
        result = Image.objects.filter(Q(title__icontains=query) | Q(tags__icontains=query))
        context['query'] = query
        context['result'] = result
    return render(request, 'search.html', context)

""""     About Page       """
def about(request):
    context = {}
    context['title'] = "About | Image Grid"
    context['about'] = About.objects.all()
    return render(request, 'about.html', context)

""""     Contact Page       """
def contact(request):
    context = {}
    context['title'] = "Contact | Image Grid"
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        msg = request.POST.get('msg')
        results = Contact(name=name, email=email, subject=subject, details=msg)
        if results:
            contact_msg = "ok"
            results.save()
            context['contact_msg'] = contact_msg
        else:
            contact_msg = "no"
            context['contact_msg'] = contact_msg
    return render(request, 'contact.html', context)

""""     Add Image Page       """
def add_image(request):
    context = {}
    context['title'] = "Add | Image Grid"
    if request.method == "POST":
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/image-selection')
    form = ImageForm()
    context['form'] = form
    return render(request, 'add.html', context)

