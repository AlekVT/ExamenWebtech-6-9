from django.http import HttpResponse
from django.shortcuts import render

import redis

r = redis.StrictRedis()

movielist = r.keys('film:*')
if len(movielist) == 0:
	movies = open("movies.txt", "r")
	movielist = []
	actorlist = []
	for line in movies:
		actorlist.append(line)
		movielist.append('film:' + line.split(" : ")[0])

	for actor in actorlist:
		r.sadd("film:" + actor.split(" : ")[0], actor.split(" : ")[1])

print(movielist)

def index(request):
    context = {
        'movielist': movielist,
    }
    return render(request, 'movieservice/index.html', context)

def actors(request):
	movie_name = request.POST['movie_name']
	actors = "not found"
	for actors in actorlist:
		if actors.startswith(movie_name):
			actors = movie_name.split(" : ")[1]
	return HttpResponse(actors)
