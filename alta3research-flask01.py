  #!/usr/bin/env python3
  
'''
  Your script alta3research-flask01.py should demonstrate proficiency with the flask library. Ensure your application has:
  1) At least two endpoints
  2) At least one of your endpoints should return legal JSON
  3) One endpoint returns HTML that uses jinja2 logic
 '''

from flask import Flask
from flask import redirect
from flask import request
from flask import render_template
from flask import url_for
from flask import jsonify 


app = Flask(__name__)                           # flask constructor

# just some json data
houndData= [{ 
    "genus": "Canis",
    "species": "familiaris",
    "country": "England",
    "characteristics": [
        "super fast",
        "sight hound",
        "60mph couch potato"
              ]
             }]
  

@app.route("/")                                               # user can land at "/"
def start():
    return render_template("trivia_asker.html")               # look for templates/trivia_asker.html
 
# This is where trivia_asker.html POSTs data to
@app.route("/answer", methods = ["POST"])
def answer():
    if request.form.get("breed"):                             # if breed was assigned via the POST
        breed = request.form.get("breed")                     # grab the value of breed from the POST
        breed = breed.lower()                                 # make it lowercase
        return redirect(url_for("evalAnswer", breed = breed)) # pass back to /evalanswer

 ## This is where we want to redirect users to
@app.route("/evalanswer/<breed>")
def evalAnswer(breed):
    return render_template("eval_answer.html", breed = breed)

@app.route("/dogdata")
def data():
    return jsonify(houndData)                                 # returns JSON
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2224)                        # runs the application