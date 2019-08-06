import pyowm #Либа
from colorama import init
from colorama import Fore, Back, Style
from termcolor import colored

owm = pyowm.OWM("6d00d1d4e704068d70191bad2673e0cc", language = "ru") #Настройки либы
init()


while 1: #Цикл программмы
	print(Fore.WHITE)
	print(Back.GREEN)
	place = input("Введите регион: ") #Получение от (продвинутого) юзера регион
	observation = owm.weather_at_place(place) #Получения данных со станций на регион
	w = observation.get_weather() #Получение погоды
	forecast = owm.daily_forecast(place) #Получение погоды на завтра
	#Получаем данные погоды
	temp = w.get_temperature("celsius")["temp"] #Получение температуры
	tempMax = w.get_temperature("celsius")["temp_max"] #Получение максимальной температуры
	tempMin = w.get_temperature("celsius")["temp_min"] #Получение минимальной температуры
	wind = w.get_wind()["speed"] #Получение скорости ветра
	hum = w.get_humidity() #Получение влажности
	pressur = w.get_pressure()["press"]
	#Что будет завтра?
	tomorrow = pyowm.timeutils.tomorrow() #Завтра, так завтра, ок
	forcClear = forecast.will_be_clear_at(tomorrow) #Завтра будет ясно?
	forcRain = forecast.will_be_rainy_at(tomorrow) #Завтра будет дождь?
	pressur = pressur / 1000
	atm = "атмосфер"
	if pressur == 1 or 2 or 3 or 4: atm = "атмосферы"
	else: atm = "атмосфер"
	print(Fore.RESET)
	print(Back.RESET)
	print("                                                                    ")
	print("                                                                    ")
	print("                                                                    ")
	print(colored("=============================Cегодня================================", "white", "on_yellow"))
	print("                                                                    ") #КАКОИТО ГУИ
	print(Back.GREEN + "В городе " + place + " сейчас " + w.get_detailed_status()) #Статус погоды
	print(Back.RESET + "                                                                    ")
	print(colored("===========================Темпер", "white", "on_cyan") + colored("атура==============================", "white", "on_red")) #КАКОИТО ГУИ
	print("                                                                    ") #КАКОИТО ГУИ
	print(Back.GREEN)
	print("Сейчас температура в районе " + str(round(temp)) + " °C") #Статус температуры
	print(Back.RED)
	print("Максимальная температура на сегодня в районе " + str(tempMax) + " °C") #Какая максимальная температура?
	print(Back.CYAN)
	print("Миниимальная температура на сегодня в районе " + str(tempMin) + " °C") #Какая МИНИМАЛЬНАЯ (я думал максимальная опять) температура?
	print(Back.BLUE)
	if temp < 10: print("СЕЙЧАС ОЧЕНЬ ХОЛОДНО, ОДЕВАЙСЯ КАК ТАНК!!!")
	print(Back.CYAN)
	if temp < 20: print("Сейчас прохладно, оденься потеплее.")
	print(Back.YELLOW)
	if temp > 20: print("Температура норм, одевайся, как хочешь")
	print(Back.CYAN)
 #КАКОИТО ГУИ
	print("==============================Ветер=================================") #КАКОИТО ГУИ
	print("                                                                    ") #КАКОИТО ГУИ
	print("Скорость ветра сегодня в районе " + str(wind) + " метров/с" + "     ") #Можно завтра запускать воздушный змей?
	print("                                                                    ") #КАКОИТО ГУИ
	print("============================Влажность===============================") #КАКОИТО ГУИ
	print("                                                                    ") #КАКОИТО ГУИ
	print("Влажность воздуха в районе " + str(hum) + ("%") + "                 ") #Я троеШник мне это нинада
	print("                                                                    ") #КАКОИТО ГУИ
	print("=============================Давление===============================") #КАКОИТО ГУИ
	print("                                                                    ") #КАКОИТО ГУИ
	print("Давление воздуха в районе " + str(pressur) + " " + atm + "          ")  #Как сильно на нас давит воздух?
	print("                                                                    ")
	print("====================================================================") #КАКОИТО ГУИ
	print("                                                                    ") #КАКОИТО ГУИ
	print("=============================Прогноз================================") #КАКОИТО ГУИ
	print(Back.RESET + "                                                                    ") #КАКОИТО ГУИ
	if forcClear == False and forcRain == False: print(Back.CYAN + Fore.WHITE + "Завтра будет облчано") #Я хотел позагорать :(
	elif forcRain == True  and forcClear == False: print(Back.BLUE + Fore.WHITE + "Завтра будет дождь") #Я хотел на улице играть :(
	if forcClear == True and forcRain == False: print(Back.YELLOW + Fore.WHITE + "Завтра будет ясно") #УРААА!11! МОЖНА ИГАРТЬ И ЗАГАРАТЬS
	print(Back.RESET + "                                                                    ") #КАКОИТО ГУИ
	print(Back.CYAN + "====================================================================") #КАКОИТО ГУИ
	print(Back.RESET + "                                                                    ")
	print(Back.GREEN) #КАКОИТО ГУИ
	yn = input("Новый прогноз? (y/n): ") #Еще нужно?
	if yn == "n": exit() #ДАСВИДАНИА
