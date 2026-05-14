
# from django.shortcuts import render
# import requests
# import datetime

# # Create your views here.
# def home(request):

#     # Default city
#     city = 'Indore'

#     if request.method == "POST":

#         city = request.POST.get('city')

#         # Remove extra spaces
#         city = city.strip()

#         # Empty city validation
#         if city == "":

#             return render(request, 'weatherapp/index.html', {
#                 'error': 'Please enter a city name.'
#             })

#     # OpenWeather API URL
#     url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=aa4880e0857581977313d9b2076b359f&units=metric'

#     try:

#         response = requests.get(url)
#         data = response.json()

#         # Wrong city name
#         if str(data.get("cod")) == "404":

#             context = {
#                 'error': 'City name is wrong. Please check the city name.'
#             }

#         # Weather data unavailable
#         elif not data.get("weather"):

#             context = {
#                 'error': f'Weather data for "{city}" is not available in API.'
#             }

#         else:

#             # Weather Details
#             description = data['weather'][0]['description']
#             icon = data['weather'][0]['icon']
#             temp = data['main']['temp']
#             humidity = data['main']['humidity']
#             wind_speed = data['wind']['speed']
#             main_weather = data['weather'][0]['main']

#             # Date & Day
#             day = datetime.date.today().strftime("%A")
#             date = datetime.date.today().strftime("%d %B %Y")

#             # Dynamic Background Image
#             background_image = f"https://images.unsplash.com/photo-1506744038136-46273834b3fb?q={city}"

#             context = {
#                 'description': description,
#                 'icon': icon,
#                 'temp': temp,
#                 'humidity': humidity,
#                 'wind_speed': wind_speed,
#                 'day': day,
#                 'date': date,
#                 'city': city.title(),
#                 'main_weather': main_weather,
#                 'background_image': background_image,
#             }

#     except Exception:

#         context = {
#             'error': 'Unable to connect to weather service. Please try again later.'
#         }

#     return render(request, 'weatherapp/index.html', context)



from django.shortcuts import render
import requests
import datetime

# Create your views here.
def home(request):

    # Default city
    city = 'Indore'

    if request.method == "POST":

        city = request.POST.get('city')

        # Remove extra spaces
        city = city.strip()

        # Empty city validation
        if city == "":

            return render(request, 'weatherapp/index.html', {
                'error': 'Please enter a city name.'
            })

    # OpenWeather API URL
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=aa4880e0857581977313d9b2076b359f&units=metric'

    try:

        response = requests.get(url)
        data = response.json()

        # Wrong city name
        if str(data.get("cod")) == "404":

            context = {
                'error': 'City name is wrong. Please check the city name.'
            }

        # Weather data unavailable
        elif not data.get("weather"):

            context = {
                'error': f'Weather data for "{city}" is not available in API.'
            }

        else:

            # Weather Details
            description = data['weather'][0]['description']
            icon = data['weather'][0]['icon']
            temp = data['main']['temp']
            humidity = data['main']['humidity']
            wind_speed = data['wind']['speed']
            main_weather = data['weather'][0]['main']

            # Date & Day
            day = datetime.date.today().strftime("%A")
            date = datetime.date.today().strftime("%d %B %Y")

            # Famous City Backgrounds

            city_backgrounds = {

                'delhi': 'https://images.unsplash.com/photo-1587474260584-136574528ed5',
                'agra': 'https://images.unsplash.com/photo-1564507592333-c60657eea523',
                'mumbai': 'https://images.unsplash.com/photo-1570168007204-dfb528c6958f',
                'jaipur': 'https://images.unsplash.com/photo-1477587458883-47145ed94245',
                'srinagar': 'https://images.unsplash.com/photo-1598091383021-15ddea10925d',
                'paris': 'https://images.unsplash.com/photo-1549144511-f099e773c147',
                'dubai': 'https://images.unsplash.com/photo-1512453979798-5ea266f8880c',
                'new york': 'https://images.unsplash.com/photo-1499092346589-b9b6be3e94b2',
                'tokyo': 'https://images.unsplash.com/photo-1540959733332-eab4deabeeaf',
                'london': 'https://images.unsplash.com/photo-1513635269975-59663e0ac1ad',
            }

            # Default background image

            background_image = city_backgrounds.get(
                city.lower(),
                'https://images.unsplash.com/photo-1506744038136-46273834b3fb'
            )

            context = {
                'description': description,
                'icon': icon,
                'temp': temp,
                'humidity': humidity,
                'wind_speed': wind_speed,
                'day': day,
                'date': date,
                'city': city.title(),
                'main_weather': main_weather,
                'background_image': background_image,
            }

    except Exception:

        context = {
            'error': 'Unable to connect to weather service. Please try again later.'
        }

    return render(request, 'weatherapp/index.html', context)