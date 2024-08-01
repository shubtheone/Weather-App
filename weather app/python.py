from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import ttk,messagebox
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz

root=Tk()
root.title("Weather")
root.geometry("900x500+300+100")



def getWeather():
    
    city=textfield.get()

    geolocator=Nominatim(user_agent="geoApiExcercises")
    location=geolocator.geocode(city)
    obj=TimezoneFinder()
    result=obj.timezone_at(lng=location.longitude,lat=location.latitude)
    
    
    home=pytz.timezone(result)
    local_time=datetime.now(home)
    current_time=local_time.strftime("%I %M %p")
    clock.config(text=current_time)
    name.config(text="CURRENT WEATHER")


    api="https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=4ee1313562f802dbf7704e76e34b2a0a"

    json_data=requests.get(api).json()
    condition=json_data['weather'][0]['main']
    description=json_data['weather'][0]['description']
    temp=int(json_data['main']['temp']-273.15)
    pressure=json_data['main']['pressure']
    humidity=json_data['main']['humidity']
    wind=json_data['wind']['speed']

    t.config(text=(temp,"°"))
    c.config(text=(condition,"looks","like",temp,"°"))


    w.config(text=wind)
    h.config(text=humidity)
    d.config(text=description)
    p.config(text=pressure)






#Search Box 
searchBar_image=PhotoImage(file="searchbar.png")
myimage=Label(image=searchBar_image)
myimage.place(x=20,y=20)

textfield=tk.Entry(root,justify="center",width=20,font=("Rubik",25),bg="#1E1E1E",border=0,fg="white")
textfield.place(x=50,y=35)
textfield.focus()

searchicon=PhotoImage(file="Searc.png")
myimage_icon=Button(image=searchicon,borderwidth=0,cursor="hand2",bg="#1E1E1E",command=getWeather)
myimage_icon.place(x=400,y=27)


logo_image=PhotoImage(file="Copy of logo.png")
my_logo=Label(image=logo_image)
my_logo.place(x=600,y=80)


#time
name=Label(root,font=("Rubik",15,"bold"))
name.place(x=40,y=100)
clock=Label(root,font=("Rubik",15))
clock.place(x=40,y=130)



label1=Label(root,text="WIND",font=("Rubik",20 ,"italic"),fg="black")
label1.place(x=220,y=350)

label2=Label(root,text="HUMIDITY",font=("Rubik",20 ,"italic"),fg="black")
label2.place(x=30,y=350)

label3=Label(root,text="DESCRIPTION",font=("Rubik",20 ,"italic"),fg="black")
label3.place(x=360,y=350)

label4=Label(root,text="PRESSURE",font=("Rubik",20 ,"italic"),fg="black")
label4.place(x=600,y=350)

t=Label(font=("Rubik",25,"bold"),fg="#ee666d")
t.place(x=30,y=200)

c=Label(font=("Rubik",25,"bold"))
c.place(x=30,y=270)

w=Label(text="...",font=("Rubik",20,"bold"),fg="#1ab5ef")
w.place(x=220,y=430)
h=Label(text="...",font=("Rubik",20,"bold"),fg="#1ab5ef")
h.place(x=30,y=430)
d=Label(text="...",font=("Rubik",20,"bold"),fg="#1ab5ef")
d.place(x=360,y=430)
p=Label(text="...",font=("Rubik",20,"bold"),fg="#1ab5ef")
p.place(x=600,y=430)



root.mainloop()