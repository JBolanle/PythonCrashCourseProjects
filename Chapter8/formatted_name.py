def get_formatted_name(first_name, last_name):
    """Returns full name, neatly formatted"""
    full_name = first_name + " " + last_name
    return full_name.title()

musician = get_formatted_name('wiz', 'khalifa')
print(musician)

def city_country(city, country):
    formatted = city.title() + ", " + country.title()
    return formatted

print(city_country('Lagos', 'Nigeria'))

def make_album(artist_name, album_title):
    music_album = {
        'title': album_title,
        'artist': artist_name
    }
    return music_album

print(make_album('jay-z', 'empire state of mind - single'))

