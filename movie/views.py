from django.shortcuts import render, redirect
from .models import Movie, Score
from .forms import MovieForm, ScoreForm

# Create your views here.
def list(request):
    movies = Movie.objects.all()
    return render(request, 'movie/list.html', {"movies":movies})

def detail(request, id):
    movie = Movie.objects.get(id=id)
    form = ScoreForm()
    return render(request, 'movie/detail.html', {'movie':movie, 'form':form})
        
def update(request, id):
    movie = Movie.objects.get(id=id)
    if request.method=="POST":
        form = MovieForm(request.POST, instance=movie)
        if form.is_valid():
            form.save()
            return redirect("movie:list")
    else:
        form = MovieForm(instance=movie)
    return render(request, 'movie/form.html',{'form':form})

def delete(request, id):
    movie = Movie.objects.get(id=id)
    movie.delete()
    return redirect("movie:list")
    
def score_new(request, id):
    movie = Movie.objects.get(id=id)
    print("!!!!!!!!!!!!!!!!!!!!!")
    if request.method=="POST":
        form = ScoreForm(request.POST)
        if form.is_valid():
            score = form.save(commit=False)
            score.movie_id = movie
            score.save()
            return redirect("movie:list")
    else:
        form = ScoreForm()
    return render(request, 'movie/detail.html',{'form':form})
    
def score_delete(request, id, s_id):
    score = Score.objects.get(id=s_id)
    score.delete()
    return redirect("movie:detail", id)