from urllib import request
from flask import Flask, render_template, request
from plot import Plot
from predict import Predict
from receive import Data


app= Flask(__name__)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/author')
def author():
    return render_template('author.html')


@app.route('/', methods=['GET', 'POST'])
def screen():
    data_y = Data().year_data()
    data_d = Data().day_data()
    data_m = Data().model_data()
    graph = Plot().plot(data_y)
    current_value = data_d['close'].values[0].round(2)
    
    if request.method=='POST':
        if request.form.get('pr')=='PREDICT':
            prediction = Predict().predict_stock(data_m)
            return render_template('main.html', current_value=current_value, graph=graph, prediction= prediction)
    elif request.method == 'GET':
        return render_template('main.html', current_value=current_value, graph=graph, prediction='... ')

if __name__=='__main__':
    app.run(debug=True)