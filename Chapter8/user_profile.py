def build_profile(first, last, **user_info):
    """Build dictionary containing everything we know about a user"""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last

    for key, value in user_info.items():
        profile[key] = value
    return profile

user_profile = build_profile('jumoke', 'bolanle', location = 'ypsilanti, mi', field = 'computer science')

print(user_profile)