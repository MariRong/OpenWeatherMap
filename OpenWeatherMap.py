import pyowm
import datetime
import time
print('OpenWeatherMap')
owm = pyowm.OWM('c8608f3d3d2ab222d6e958fc7c150c29')
observation = owm.weather_at_place('Rostov-na-Donu')
weather = observation.get_weather()
location = observation.get_location()
translate = {'Rostov-na-Donu': 'Ростове-на-Дону', 'RU': 'Россия', 'Clouds': 'Облачно'}
def get_wind_direction(weather):
    deg = weather.get_wind().get('deg')
    if 0<=deg<=20 :return 'северный'
    if 20 < deg <= 70: return 'северо-восточный'
    if 70 < deg <= 120: return 'восточный'
    if 120 < deg <= 160: return 'юго-восточный'
    if 160 < deg <= 200: return 'южный'
    if 200 < deg <= 250: return 'юго-западный'
    if 250 < deg <= 290: return 'западный'
    if 290 < deg <= 360: return 'северо-западный'
def WhatIsCloudness() :
    if 0<= weather.get_clouds()<=10:
        return 'ясная'
    if 10< weather.get_clouds()<=30:
        return 'немного облочная'
    if 30< weather.get_clouds()<=70:
        return 'пасмурная'
    if 70< weather.get_clouds()<=100:
        return 'мрачная'
print('Погода в '+ translate[location.get_name()]+'('+translate[location.get_country()]+') сегодня в '+ datetime.datetime.now().strftime('%H:%M')+''
' '+WhatIsCloudness()+', ветер '+ get_wind_direction(weather) + ', скорость '+str(weather.get_wind().get('speed')) + ' м/с'+', давление '+str(round(weather.get_pressure()['press']*0.75,1)) + ' мм.рт.с'+''
', температура '+str(round(weather.get_temperature('celsius')['temp']))+' градусов цельсия'+', ночью '+ str(round(weather.get_temperature('celsius')['temp_min'])) + ' , днем ' + str(weather.get_temperature('celsius')['temp_max'])+
' градусов')
time.sleep(20)