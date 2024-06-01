from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from .models import *

def home(request):
    return render(request,"home.html",context={'current_tab':"home"})

def blog(request):
    return render(request,"blog.html",context={'current_tab':"blog"})

def books0(request):
    return render(request,"books0.html",context={'current_tab':"books0"})

def reader_tab(request):
    if request.method == "GET":
        readers = reader.objects.all()
        return render(request,"readers.html",context={'current_tab':"readers","readers":readers})
    else :
        query = request.POST['query']
        readers = reader.objects.raw("select * from lib_sys_app_reader where reader_name like '%"+query+"%'")
        return render(request, "readers.html", context={'current_tab': "readers",
                                                        "readers": readers,
                                                        "query":query})

def save_reader(request):
    reader_item = reader(reference_id=request.POST['reader_ref_id'],
                         reader_name=request.POST['reader_name'],
                         reader_contact=request.POST['reader_contact'],
                         reader_address=request.POST['address'],
                         active=True
                        )
    reader_item.save()
    return redirect("/readers")


def book_tab(request):
    if request.method == "GET":
        books = book.objects.all()
        return render(request,"books.html",context={'current_tab':"books","books":books})
    else :
        query = request.POST['query']
        books = book.objects.raw("select * from lib_sys_app_book where title like '%"+query+"'%")
        return render(request, "books.html",context = {'current_tab': "books",
                                                        "books": books,
                                                        "query":query})

def save_book(request):
    book_item = book(   title=request.POST['title'],
                         author=request.POST['author'],
                         publisher=request.POST['publisher'],
                         year=request.POST['year'],
                        )
    book_item.save()
    return redirect("/books")