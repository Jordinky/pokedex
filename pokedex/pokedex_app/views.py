from django.shortcuts import render
import requests
from .pokeForm import SearchPokemon


def pokedex(request):
    if request.method == "POST":
      form = SearchPokemon(request.POST)
      pokeForm = form['pokemon'].value().lower()
      if(form.is_valid):
        response=requests.get('https://pokeapi.co/api/v2/pokemon/'+pokeForm)
        if response.status_code == 200:
          #return the value of the pokemon (json format)
          poke = response.json()
          return render(request,'index.html',{'pokemon':poke,'form':form})
        elif response.status_code == 404:
          #if the pokemon doesn't exist poke set a dictionary with the unknown return values
          #and a questionmark .png as the poke img.
          poke = {'name': 'unknown','id': '?????','sprites':{'front_default': 'https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/3ce212da-22a2-4830-85cc-f5e5affc5cd6/dcxehfe-dd22d80d-4cff-49bf-be56-bb51f5ea0a78.gif?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7InBhdGgiOiJcL2ZcLzNjZTIxMmRhLTIyYTItNDgzMC04NWNjLWY1ZTVhZmZjNWNkNlwvZGN4ZWhmZS1kZDIyZDgwZC00Y2ZmLTQ5YmYtYmU1Ni1iYjUxZjVlYTBhNzguZ2lmIn1dXSwiYXVkIjpbInVybjpzZXJ2aWNlOmZpbGUuZG93bmxvYWQiXX0.FPZzigXwn6ZWFixDogw4z5uQbIfnJSzyq8TDI9K_3o8'}}
          return render(request,'index.html',{'pokemon':poke,'form':form})
    else:
      form  = SearchPokemon()
      return render(request,'index.html',{'form':form})

             

      
      


    
