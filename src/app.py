from flask import Flask, render_template, request

from carlisting import get_all_cars
from comparison import compare_car

app = Flask(__name__)



# HOME PAGE

@app.route("/")
def home():
    return render_template("homepage.html")



@app.route("/cars")
def browse_cars():

    cars = get_all_cars(limit=100)

    return render_template(
        "index.html",
        cars=cars.to_dict(orient="records")
    )



@app.route("/search")
def search_page():

    cars = get_all_cars(limit=100)

    return render_template(
        "search.html",
        cars=cars.to_dict(orient="records")
    )



@app.route("/compare", methods=["POST"])
def compare():

    car = {
        "Make": request.form["Make"],
        "Model_No_Year": request.form["Model_No_Year"],
        "Mileage": float(request.form["Mileage"]),
        "Year": float(request.form["Year"]),
        "Engine_size": float(request.form["Engine_size"]),
        "Transmission_type": request.form["Transmission_type"]
    }

    result = compare_car(car)

    return render_template(
        "result.html",
        car=car,
        result=result
    )



# RUN APP

if __name__ == "__main__":
    app.run(debug=True)