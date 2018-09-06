from django.http import HttpResponse
from django.shortcuts import render

import redis

r = redis.StrictRedis()

movielist = r.keys('movie:*')
if len(movielist) == 0:
	movies = open("movies.txt", "r")
	movielist = []
	actorlist = []
	for line in movies:
		actorlist.append(line)
		movielist.append('movie:' + line.split(" : ")[0])

def index(request):
    context = {
        'movielist': movielist,
    }
    return render(request, 'index.html', context)

