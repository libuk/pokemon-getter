#! usr/bin/env python
# Pokemon GETTER / Built by @libuk

import urllib2
import json

f = open('pokemon.txt', 'w')

pokemon_info = 'http://pokeapi.co/api/v1/pokemon/'
poke_data = []

def GetPokemon(number):
	for n in range(1, number):
		pokemon = pokemon_info + str(n)
		json_obj = urllib2.urlopen(pokemon)
		json_data = json.load(json_obj)
		poke_data.append(json_data)
		f.write(poke_data[(n-1)]['name'] + '\n')

# Grabs the first 9 pokemon (the first starters and their evolutions)
if __name__ == '__main__':
	GetPokemon(10)

f.close()