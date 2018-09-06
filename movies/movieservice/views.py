from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

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
		r.set("film:" + actor.split(" : ")[0], actor.split(" : ")[1])
		print(actor.split(" : ")[1])
else:
	temp = []
	for movie in movielist:
		temp.append(movie.decode('utf-8').split(":")[1])
	movielist = temp

print(movielist)

def index(request):
	list = []
	for movie in movielist:
		list.append(movie + " - ")
	return HttpResponse(movielist)

#def index(request):
#    context = {
#        'movielist': movielist,
#    }
#    return render(request, 'movieservice/index.html', context)

@csrf_exempt
def actors(request):
	movie_name = request.POST['movie_name']
	actors = r.get("film:" + movie_name)
	return HttpResponse(actors)
