from predictions import predict_japan_price
from calculator import calculate_taxes
from crsplookup import get_crsp_value
from constants import USD_TO_KES, FALLBACK_MULTIPLIER
from shippincost import get_shipping_cost
from kenyanlocal_prices import get_kenya_price


def compare_car(car):

    predicted_usd = predict_japan_price(
        Make=car["Make"],
        Model_no_year=car["Model_No_Year"],
        Mileage=car["Mileage"],
        Year=car["Year"],
        Engine_size=car["Engine_size"],
        Transmission_type=car["Transmission_type"]
    )

    predicted_kes = predicted_usd * USD_TO_KES

    shipping_cost = get_shipping_cost(car.get("Body_Type", "sedan"))

    cif = predicted_kes + shipping_cost

    crsp = get_crsp_value(car["Make"], car["Model_No_Year"])
    if crsp <= 0:
        crsp = cif

    tax_data = calculate_taxes(
        japan_price=predicted_kes,
        shipping=shipping_cost,
        engine_size=car["Engine_size"],
        crsp=crsp,
        fuel_type=car.get("Fuel_Type", "petrol")
    )

    kenya_price = get_kenya_price(
        car["Make"],
        car["Model_No_Year"],
        car["Year"]
    )

    price_estimated = False

    if kenya_price is None:
        kenya_price = predicted_kes * FALLBACK_MULTIPLIER
        price_estimated = True

    total_import_cost = tax_data["total_cost"]

    savings = kenya_price - total_import_cost

    if savings > 0:
        recommendation = "Import from Japan"
    elif savings < 0:
        recommendation = "Buy Locally in Kenya"
    else:
        recommendation = "Either option"

    return {
        "predicted_japan_price_usd": round(predicted_usd, 2),
        "predicted_japan_price_kes": round(predicted_kes, 2),

        "shipping_cost": round(shipping_cost, 2),

        "cif": round(cif, 2),
        "crsp": round(crsp, 2),

        "customs_value": tax_data["customs_value"],
        "import_duty": tax_data["import_duty"],
        "excise_duty": tax_data["excise_duty"],
        "vat": tax_data["vat"],
        "idf": tax_data["idf"],
        "rdl": tax_data["rdl"],

        "taxes": tax_data["total_tax"],
        "total_import_cost": total_import_cost,

        "kenya_market_price": round(kenya_price, 2),
        "price_estimated": price_estimated,

        "savings": round(savings, 2),
        "recommendation": recommendation
    }