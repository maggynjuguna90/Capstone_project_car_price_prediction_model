# PROJECT OVERVIEW 
This is a project that helps Kenyan-buyers compare the cost of buying cars locally versus importing them from Japan.Machine learning is used to predict import cost  and it is combined with Kenyan market data(shipping cost ,taxes).It enables the user to make a clear decision before purchasing a vehicle.The project focuses on car models manufactured between the year 2018 upto date.


## OBJECTIVES 

1. Predict japan car prices.
2. Calculate the cost of importing cars to Kenya.
3. Compare the import cost versus the local market prices.
4. Enable the user to chose the best option(importing/ buying locally)

## DATASETS 
Japanese car listing platforms(SBT Japan ,BE Forward)
Kenyan market price estimates(jiji cars, peach cars)
KRA import duty guidelines(CRSP-2025)


## HOW THE PROJECT WORKS 
The user enters the car details(make,model,year,mileage ,engine-size).The Machine Learning model predicts the japan market price.System calculates shipping cost and import taxes then compares the total import cost versus the local cost.Outputs recommends whether to import or buy locally.


Repository: https://github.com/maggynjuguna90/Capstone_project_car_price_prediction_model.git

1. Clone the repository
git clone https://github.com/maggynjuguna90/Capstone_project_car_price_prediction_model.git
cd Capstone_project_car_price_prediction_model
2. Create virtual environment
python -m venv venv
Activate it:

Windows

venv\Scripts\activate

Mac/Linux

source venv/bin/activate
Run the application
python app.py

Open in browser:

http://127.0.0.1:5000