from flask import Flask, request, render_template,jsonify


app = Flask(__name__)

@app.route('/')
def Home():
    print("Home API")
    return render_template("User_input.html")

@app.route("/predicted_charges", methods = ["POST", "GET"])
def Insurance_charges():
    if request.method == "POST":
        data = request.form

        name = data["name"]
       
    
    return  render_template("User_input.html", name =name)
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug= True)