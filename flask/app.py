#we import flask 

from flask import Flask, jsonify, redirect, render_template, request, session
import pickle


app = Flask(__name__)


with open('model-lin.b', 'rb') as f_in:
    (dv, model) = pickle.load(f_in)

def prepare_features(house):
    features = {}
    features['squareMeters'] = house['squareMeters']
    return features

def predict(features):
    X = dv.transform(features)
    preds = model.predict(X)
    print(preds)
    return "{:,}".format(round(preds[0]))


# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

@app.route("/")
def index():
    return render_template("index.html")
#
#

@app.route("/predict/", methods=["GET", "POST"])
def prediction():
    if request.method == "POST":
        
        #: takes the user entry
        if not request.form.get("squaremeter"):
            return render_template("index.html")

        else:
            size = request.form.get("squaremeter")
            size = int(size)
            house = {"squareMeters": size }
            features = prepare_features(house)
            pred = predict(features)
            result = {'House price': pred}
            price = result['House price']
            sizes = house["squareMeters"]
            return render_template("index.html", prices=price, sizes=sizes)
            #return redirect("/")
            
            #db.execute("INSERT INTO birthday (name, city, birthday, language) VALUES(?,?,?,?)", name, city, month, language)
            

    else:
        
        return render_template("index.html")


if __name__=="__main__":
    app.run(debug=True)