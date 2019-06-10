from django.http import HttpResponse
from django.shortcuts import render
from collections import Counter
import operator

def home_page(request):
    return render(request, 'home.html', {'Hithere': 'this is me'} ) #<- datas can passed through this dictionary
def count(request):
    full_text = request.GET['full_text'].split() 
    counter_texts =  sorted(Counter(full_text).items(), key=operator.itemgetter(1), reverse=True)
    return render(request, 'count.html',{'full_text': counter_texts }) 
def about(request):
    return render(request, 'about.html') 