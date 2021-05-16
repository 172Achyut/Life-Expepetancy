import numpy as np
import pandas as pd
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('finalized_model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    int_features = [x for x in request.form.values()]
    final_features = [np.array(int_features)]
    print(final_features)
    # print(type(final_features))
    s= pd.DataFrame(final_features,columns=['Adult Mortality', 'Alcohol', 'BMI', 'Country', 'Diphtheria', 'GDP',
       'HIV/AIDS', 'Hepatitis B', 'Income composition of resources', 'Measles',
       'Polio', 'Population', 'Schooling', 'Status', 'Total expenditure',
       'Year', 'infant deaths', 'percentage expenditure',
       'thinness  1-19 years', 'thinness 5-9 years', 'under-five deaths '])
    prediction = model.predict(s)

    output = round(prediction[0], 2)

    return render_template('result.html', prediction_text='Life expectancy is {} years'.format(output))

@app.route('/predict_api',methods=['POST'])
def predict_api():
    '''
    For direct API calls trought request
    '''
    data = request.get_json(force=True)
    prediction = model.predict([np.array(list(data.values()))])

    output = prediction[0]
    return jsonify(output)

if __name__ == "__main__":
    app.run(debug=True)