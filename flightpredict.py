from flask import flask,render_template,request
import numpy as np
import pickle
model=pickle.load(open(r"model1.pk1",'rb'))
@app.route("/home")
def home():
    return render_template('home.html')
@app.route("/predict")
def home1():
    return render_template('predict.html')

@app.route("/pred",methods=['POST','GET'])
def predict():
    x=[[int(x) for x in request.from.values()]]
    print(x)

    print(x)
    pred=model1.predict(x)
    print(pred)
    return render_template('submit.html',prediction_text=pred)
if __name__ == "__main__":
    app.run(debug=false)