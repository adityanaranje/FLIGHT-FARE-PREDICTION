from flask import Flask, render_template, request
import pandas as pd
import numpy as np
import getdata

app = Flask(__name__)



@app.route('/')
@app.route('/home',methods=['POST','GET'])
def home():

    airlines = getdata.airlines
    sources = getdata.sources
    dests = getdata.dests
    stops = getdata.stops
    addinfos = getdata.addinfos
    durhrs = getdata.durhrs
    durmins = getdata.durmins
    months = getdata.months
    dates = getdata.dates
    dephrs = getdata.dephrs
    depmins = getdata.depmins
    arrhrs = getdata.arrhrs
    arrmins = getdata.arrmins

    model = getdata.model
    p = 0

    if request.method == "POST":
        p = 1

        airline = str(request.form['airline'])
        source =  str(request.form['source'])
        destination = str(request.form['dest'])
        total_stops = int(request.form['stop'])
        additional_info = addinfos[int(request.form['addinfo'])]
        duration_in_min = int(request.form['durhr'])*60+int(request.form['durmin'])
        journey_day = int(request.form['date'])
        journey_month = int(request.form['month'])
        dept_hour = int(request.form['dephr'])
        dept_min = int(request.form['depmin'])
        arrv_hour = int(request.form['arrhr'])
        arrv_min = int(request.form['arrmin'])
        data = pd.DataFrame({'airline':[airline], 'source':[source], 'destination':[destination],
                        'total_stops':[total_stops], 'additional_info':[additional_info],
        'duration_in_min':[duration_in_min], 'journey_day':[journey_day], 'journey_month':[journey_month],
                        'dept_hour':[dept_hour],'dept_min':[dept_min],
                        'arrv_hour':[arrv_hour], 'arrv_min':[arrv_min]})

        print(data)
        pred = float(model.predict(data))
        pred1 = int(np.ceil(pred-(pred*0.10)))
        pred2 = int(np.ceil(pred+(pred*0.10)))

        if source==destination:
            p = 2
            pred1= pred2 = 0

        return render_template('home.html',airlines=airlines, sources=sources, dests = dests,
    stops=stops, addinfos=addinfos,durhrs=durhrs,durmins=durmins,months=months,
    dates=dates,dephrs=dephrs,depmins=depmins,arrhrs=arrhrs,arrmins=arrmins,pred1=pred1,pred2=pred2,p=p)


    return render_template('home.html',airlines=airlines, sources=sources, dests = dests,
    stops=stops, addinfos=addinfos,durhrs=durhrs,durmins=durmins,months=months,
    dates=dates,dephrs=dephrs,depmins=depmins,arrhrs=arrhrs,arrmins=arrmins,p=p)

if __name__ == '__main__':
    app.run(debug=False)