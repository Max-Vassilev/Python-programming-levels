def forecast(*args):
    result = ""
    weather_cities = {"Sunny": [], "Cloudy": [], "Rainy": []}

    for arg in args:
        city = arg[0]
        weather = arg[1]
        weather_cities[weather].append(city)

    for city in weather_cities:
        weather_cities[city] = sorted(weather_cities[city])

    for weather, cities in weather_cities.items():
        for city in cities:
            result += f"{city} - {weather}" + "\n"

    return result
