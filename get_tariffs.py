def get_tariffs(customer_postcode, energy_supplier, tariff_name, yearly_spend):
    print("get_tariffs called")
    print(customer_postcode, energy_supplier, tariff_name, yearly_spend)
    
    return [
        {
            "name": "Tariff 1",
            "price": 500
        },
        {
            "name": "Tariff 2",
            "price": 1200
        },
        {
            "name": "Tariff 3",
            "price": 2300
        }
    ]
    
def tst():
    return "tst"