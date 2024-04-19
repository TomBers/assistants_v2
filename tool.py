def get_tariffs(postcode):
    print("get_tariffs called")
    print(postcode)
    return [
        {
            "name": "Tariff 1",
            "price": 100
        },
        {
            "name": "Tariff 2",
            "price": 200
        },
        {
            "name": "Tariff 3",
            "price": 300
        }
    ]