from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect
import csv
from .forms import CSVUploadForm
from django.db import connection
from django.urls import reverse


# Create your views here.
from .models import *

def home(request):
    books = book.objects.filter(score__gte=4.2)
    return render(request,"home.html",context={'current_tab':"home",
                                               'books':books})

def blog(request):
    return render(request,"blog.html",context={'current_tab':"blog"})



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
        query = request.POST.get('query','')
        books = book.objects.raw("select * from lib_sys_app_book where title like '%"+query+"%'")        
        return render(request,"books.html",context = {'current_tab': "books",
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


def upload_csv(request):
    if request.method == 'POST':
        form = CSVUploadForm(request.POST, request.FILES)
        if form.is_valid():
            csv_file = request.FILES['csv_file']
            try:
                decoded_file = csv_file.read().decode('utf-8').splitlines()
                reader = csv.DictReader(decoded_file)
                books_to_create = []
                for row in reader:
                    books_to_create.append(book(
                        title=row['title'],
                        author=row['author'],
                        score=row['score'],
                        year=row['year'],
                        image=row['image'],
                    ))
                book.objects.bulk_create(books_to_create)
                print('Books imported successfully')
            except Exception as e:
                print( f"Error processing file: {e}")
            return redirect('/books')  
    else:
        form = CSVUploadForm()
    return render(request, 'upload.html', {'form': form})

def chart(request):
    if request.method == 'POST':
        book_id = request.POST.get('book_id')
        if not request.session.get('chart'):
            request.session['chart'] = []
        chart = request.session['chart']
        if book_id not in chart:
            chart.append(book_id)
            request.session['chart'] = chart
    return redirect('/books')  

def bag(request):
    if request.method == 'POST':
        readers_id = request.POST.get('reader_id')
        start = request.POST.get('startdate')
        end = request.POST.get('enddate')
        chart = request.session.get('chart', [])
        books = book.objects.filter(id__in=chart)
        readers = reader.objects.filter(reference_id=readers_id)

        selected_reader = None  # Rename 'reader' variable
        if readers.exists():
            selected_reader = readers.first()
        
        return render(request, 'bag.html', {
            'current_tab': "bag",
            'books': books,
            'reader': selected_reader,  # Update usage here
            'startdate': start,
            'enddate': end
        })
    else:
        return render(request, "bag.html", context={'current_tab': "bag"})
