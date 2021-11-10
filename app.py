from re import template
from flask import Flask,request
from flask.templating import render_template
import requests
app= Flask(__name__)
btnRem=1 #
para1=1 #

@app.route("/", methods=['GET','POST'])
def work():
    para1=True #
    value=request.form.getlist('box')
    city = request.form.get('cityName')
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&units=Metric&appid=fbbbacb6f5fdb3fc78798f876675efb1'
    data= requests.get(url.format(city)).json()
    default={
        'city': city,
        'temperature': data['main']['temp'],
        'description': data['weather'][0]['description'],
        'humidity':data['main']['humidity'],
        'icon': data['weather'][0]['icon'],
        'windSpeed':data['wind']['speed'],
        'windAng':data['wind']['deg'],
        'sunrise':data['sys']['sunrise'],
        'sunset':data['sys']['sunset'],
        'visiblity':data['visibility'],
        'pressure':data['main']['pressure'],
        'tempMin':data['main']['temp_min'],
        'tempMax':data['main']['temp_max'],
        'feelsLike':data['main']['feels_like']
      }
    myList=[("Temperature: ",default['temperature'],"°C"),("Humidity: ",default['humidity'],"%"),("Wind Speed: ",default['windSpeed'],"m/s ",default['windAng'],"degrees. "),
            ("Minimum Temperature: ",default['tempMin'],"°C,"," Maximum Temperature: ",default['tempMax'],"°C,"," Feels Like:",default['feelsLike'],"°C."),("Sunrise: ",default['sunrise'],"Sunset",default['sunset']),
            ("Visibility: ",default['visiblity']),("Pressure: ",default['pressure'],"mbar.")]
    toShow=[]
    btns=[]
    op=[]
    for i in value:
        i=int(i)
        toShow.append(myList[i])
        btns.append(i)
    print("toShow",toShow)
    for i in range(len(toShow)):
        x=" "
        for j in toShow[i]:
            j=str(j)
            x= x+j
        op.append(x)
    print("x", op)
    print(myList)
    if request.method == "POST":
        print("default ",btns)
        return render_template('wData.html',show=op,city1="City: ",city=city,message1='You need Premium to view',message2='Min,Max Temperature, Feels Like,Visibility,etc.')
    return render_template('wData.html',btnRem=btnRem,para1=para1,message1='You need Premium to view',message2='Min,Max Temperature, Feels Like,Visibility,etc.')


@app.route("/premium", methods=['GET','POST'])
def pre():
    global btnRem #
    btnRem=True #
    if request.method =="POST":
        say0="Free Premium for IIT Bhilai,"
        say="Premium is now activated!!"
        btnPress= 1
        return render_template('wData.html', write=say, btnPress=btnPress,btnRem=btnRem,say0=say0,para1=para1)
    return render_template('wData.html',btnRem=btnRem)

if __name__ == '__main__':
    app.run()