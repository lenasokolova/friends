favorite_languages = {
	"janek" : "python",
	"sara" : "c",
	"edward" : "ruby",
	"paweł" : "python",
	}
friends = ['paweł', 'sara', 'edward']

for name in favorite_languages.keys():
	print(name.title())
	
	if name in friends:
		print(' Witaj, ' + name.title() + "! Widzę, że Twoim ulubionym językiem programowania jest " + favorite_languages[name].title() + '!')
	if 'elżbieta' not in favorite_languages.keys():
		print('\nElżbieta, proszę, weź udział w naszej ankiecie!')

for name in sorted(favorite_languages.keys()):
	print('\n' + name.title() + ', dziękujemy za udział w ankiecie.')
	
	
print('\nW ankiecie zostały wymienione następujące języki programowania:')
for language in set(favorite_languages.values()):
	print('\n' + language.title())
