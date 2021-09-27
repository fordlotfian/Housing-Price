# Python Standard Library Modules

# 3rd-party installed modules
import pickle
from flask import Flask, render_template, request
import pandas as pd
import catboost
# Custom Project Modules
from model.model import pickle_boy, data_prep_and_pred



app =Flask("housing-price-project")

@app.route("/")
def housing_lp():
    return render_template("housing-lp.html")


@app.route("/housing-form")
def housing_pred():
    return render_template("housing-form.html")

@app.route("/housing-pred", methods=["POST"])
def results():
    print(request.form)
    data =pd.DataFrame([request.form])



    print(data)
    print(data.info())
    # prediction=10000000
    model_fit = pickle_boy('model\model_fit.pickle')
    predictions = data_prep_and_pred(data, model_fit)
    return render_template("housing-pred.html", prediction=round(predictions[0]))



