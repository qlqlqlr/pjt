from django.shortcuts import render
from .forms import KeywordForm
from .models import Keyword

# Create your views here.

def keyword(request):
    keyword_form = KeywordForm()
    context = {
        'keyword_from': keyword_form,
    }
    return render(request, 'keyword.html', context)