def make_car(manufacturer, model, **other_parts):
    build_car = {}
    build_car['make'] = manufacturer
    build_car['model'] = model

    for key, value in other_parts.items():
        build_car[key] = value
    return build_car

car = make_car('toyota', 'corolla s', color='white', sun_roof=False, extra_hp=True)

print(car)