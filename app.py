
from flask import Flask , request, jsonify
import pickle

app = Flask(__name__)

@app.route("/ping" , methods= ["GET"])
def ping():
    return "pong" , 200

with open("model_C=1.0.bin","rb") as in_f:
    dv, model = pickle.load(in_f)

@app.route("/predict" , methods = ["POST"])
def predict():
    customer = request.get_json()
    X = dv.transform([customer])
    y_predict  = model.predict_proba(X)[0,1]
    churn  = y_predict >= 0.5
    predc = {
        "chrun_probability": float(y_predict),
        "bool_churn": bool(churn)
    }
    return jsonify(predc)





if __name__ =="__main__":
    app.run(debug=True,host="0.0.0.0",port=5000)

