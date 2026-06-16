def calculate_taxes(
    japan_price,
    shipping,
    engine_size,
    crsp,
    fuel_type="petrol"
):

    
    # STEP 1: REAL COST (CIF)
    
    cif = japan_price + shipping

    
    # STEP 2: TAX BASE (CRSP ONLY HERE)
    
    
    customs_value = max(cif, crsp*0.85)

    
    # STEP 3: IMPORT DUTY (25%)
    
    import_duty = customs_value * 0.25

    
    # STEP 4: EXCISE DUTY 
    
    if fuel_type.lower() == "electric":
        excise_rate = 0.10
    elif engine_size > 3000:
        excise_rate = 0.35
    elif engine_size > 1500:
        excise_rate = 0.25
    else:
        excise_rate = 0.20

    
    excise_duty = customs_value * excise_rate

    
    # STEP 5: VAT 
    
    vat_base = customs_value + import_duty + excise_duty
    vat = vat_base * 0.16

    
    # STEP 6: LEVIES
    
    idf = customs_value * 0.035
    rdl = customs_value * 0.02

    
    # STEP 7: TOTAL TAXES
    
    total_tax = import_duty + excise_duty + vat + idf + rdl

    
    # STEP 8: FINAL IMPORT COST 
    
    
    total_cost = cif + total_tax

    return {
        "cif": round(cif, 2),
        "crsp": round(crsp, 2),
        "customs_value": round(customs_value, 2),

        "import_duty": round(import_duty, 2),
        "excise_duty": round(excise_duty, 2),
        "vat": round(vat, 2),
        "idf": round(idf, 2),
        "rdl": round(rdl, 2),

        "total_tax": round(total_tax, 2),
        "total_cost": round(total_cost, 2)
    }