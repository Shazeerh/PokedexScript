# Pokedex beta

Pokedex simple version script, utilisant un fichier JSON https://github.com/fanzeyi/pokemon.json


Fonction sorting (iterable, key=lambda d: d, reverse)

	def sorting_id(reverse=False):
		sorted_id = sorted(data, key=lambda d: d["id"], reverse=reverse)
		return sorted_id
		

Je suis en train de créer le projet final, en utilisant Kivy pour créer une interface graphique, du scraping avec BeautifulSoup afin de télecharger les images, une base de donnée SQLite pour stocker les données relatives à chaque Pokemon
