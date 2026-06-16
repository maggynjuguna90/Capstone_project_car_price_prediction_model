# services/shipping.py

def get_shipping_cost(vehicle_type):

    rates = {
        "small": 150000,
        "sedan": 180000,
        "wagon": 200000,
        "suv": 250000,
        "large_suv": 350000,
        "pickup": 300000
    }

    return rates.get(vehicle_type, 200000)