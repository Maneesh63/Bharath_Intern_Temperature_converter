from flask import Flask, render_template, request

app = Flask(__name__)
def celsius_to_fahrenheit(celsius):
    return celsius * 9/5 + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

@app.route("/", methods=["GET", "POST"])
def index():
    result = None

    if request.method == "POST":
        temperature = float(request.form["temperature"])
        conversion_type = request.form["conversion_type"]

        if conversion_type == "celsius_to_fahrenheit":
            result = celsius_to_fahrenheit(temperature)
        elif conversion_type == "fahrenheit_to_celsius":
            result = fahrenheit_to_celsius(temperature)

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
