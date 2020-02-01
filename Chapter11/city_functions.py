def get_city_country(city, country, population=''):
    """Print's city and country in a nice lil format"""
    if population:
        city_country = city + ", " + country + ". Population: " + str(population)
    else:
        city_country = city + ", " + country
    return city_country.title()