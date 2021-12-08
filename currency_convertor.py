from forex_python.converter import CurrencyRates
from forex_python.converter import CurrencyCodes
d = CurrencyRates()
dec = CurrencyRates(force_decimal=True)
z = CurrencyCodes()
run = True
while run:

    print("              Welcome to the Currency Convertor             ")
    show = """
    Choose your preference:
    1. Current Currency Rate
    2. Currency Conversion
    3. Currency Code and Symbol
    4. Exit!""" 

    print(show)
    preference = int(input("Preference Number:"))

    if preference == 1:
        f = input("Currency Code name please:")
        g = d.get_rates(f)
        print(g)

    elif preference == 2:
        a = input("Currency code you want to convert:")
        b = input("Currency code in which you want to convert:")
        c = (input("Input the price(in numbers):"))
        sub_str = "."
        if (c.find(sub_str) == -1):
            h = (int(c))
            res = d.convert(a, b, h)
        else:
            h = (float(c))
            res = d.convert(a, b, h)
        print(res)

    elif preference == 3:
        show = """Choose accordingly:
        1. Get currency symbol using currency code
        2. Get currency name using currency code """
        print(show)
        acc = int(input("Provide your preference serial number:"))
        if acc == 1:
            name = input("Provide Currency Code:")
            x = z.get_symbol(name)
            print(x)
        elif acc == 2:
            name = input("Provide Currency Code:")
            xx = z.get_currency_name(name)
            print(xx)
        else:
            print("Invalid Input")

    elif preference == 4:
        break

    else:
        print("Invalid Input")
