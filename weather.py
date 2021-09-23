import json
import tkinter as tk
import requests
import time

def getWeather(canvas):
    city= textfield.get()
    api = "http://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=c5c099acdf2c1c7206c3172cbb7753e6"
    json_data =requests.get(api).json()
    condition = json_data['weather'][0]['main']
    temp = int(json_data['main']['temp'] - 273.15)
    min_temp = int(json_data['main']['temp_min'] - 273.15)
    max_temp = int(json_data['main']['temp_max'] - 273.15)
    pressure = json_data['main']['pressure']
    humidity = json_data['main']['humidity']
    sunrise =time.strftime("%H:%M:%S", time.gmtime(json_data['sys']['sunrise']-21600))
    sunset =time.strftime("%H:%M:%S", time.gmtime(json_data['sys']['sunset']-21600))
    final_info = condition+"\n"+str(temp)+"°C"
    final_data = "\n" +"Max temp: " + str(max_temp) +"\n" + "Min temp: "+ str(min_temp) +"\n"+"Pressure: "+str(pressure) +"\nHumidity: "+str(humidity)+ "\nSunrise: "+sunrise+"\nSunset: "+sunset
    label1.config(text= final_info)
    label2.config(text= final_data)


canvas = tk.Tk()
canvas.geometry("600x500")
canvas.title("Weather App")

f = ("poppins" ,15 , "bold")
t = ("poppins" ,35 , "bold")

textfield = tk.Entry(canvas,justify='center', font= t)
textfield.pack(pady=20)
textfield.focus()
textfield.bind('<Return>', getWeather)

label1 = tk.Label(canvas, font = t)
label1.pack()
label2 = tk.Label(canvas, font =f)
label2.pack()

canvas.mainloop()
