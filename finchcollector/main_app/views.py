# MAIN APP VIEWS

from django.shortcuts import render

finches = [
  {'name': 'Charm', 'breed': 'Pine Siskin', 'description': 'Loves fresh mountain air. Hates cats.', 'age': 4},
  {'name': 'Heinz', 'breed': 'Evening Grosbeak', 'description': 'Cannot sing but has a burry chirp!', 'age': 7}
]

def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def finches_index(request):
  return render(request, 'finches/index.html', {'finches': finches})
