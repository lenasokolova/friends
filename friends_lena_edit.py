favorite_languages = {
	"janek" : "python",
	"sara" : "c",
	"edward" : "ruby",
	"paweł" : "python",
	}
friends = ['janek','paweł','edward']

for name in favorite_languages.keys():
	print(f"\n{name.title()}")
	
	if name in friends:
		print('Witaj, ' + name.title() + "! Widzę, że Twoim ulubionym językiem programowania jest " + favorite_languages[name].title() + '!')
	if name not in friends:
		print("Zapraszam do wypełnienia akiety!")

print('\nW ankiecie zostały wymienione następujące języki programowania:')
for language in set(favorite_languages.values()):
	print('\n' + language.title())
