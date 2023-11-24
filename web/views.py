from django.shortcuts import render
from datetime import datetime

# Create your views here.


def main_view(request):
    year = datetime.now().year
    return render(request, 'web/index.html', {
        'year': year,
    })
