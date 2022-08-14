#we import flask 

from flask import Flask, jsonify, redirect, render_template, request, session


app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

#@app.route("/")
#def home():
#    return render_template("index.html")
#
#

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        
        #: Add the user's entry into the database
        if not request.form.get("squaremeter"):
            return render_template("index.html")

        else:
            square = request.form.get("squaremeter")
            return render_template("index.html", prices=square)
            #return redirect("/")
            
            #db.execute("INSERT INTO birthday (name, city, birthday, language) VALUES(?,?,?,?)", name, city, month, language)
            

    else:
        
        #squaremeter = "squaremeters"
        return render_template("index.html")


#if __name__=="__main__":
#    app.run(debug=True)