import datetime
import periodictable
from countryinfo import CountryInfo


current_time = datetime.datetime.now()
datetime_format = current_time.strftime("%H:%M:%S")
date_format = current_time.strftime("%d-%m-%Y")

print(f"Time: {datetime_format}")
print(f"Date: {date_format}")
print(" ")

print("1. Periodic Table")
print("2. Check Country Information")
print(" ")

try:
    option = int(input("Select Option: "))
except ValueError:
    print("Invalid input. Please enter a number between 1 and 2.")
    exit()
print(" ")

def get_element_info(symbol):
    try:
        element = periodictable.elements.symbol(symbol)
        print(f"Element: {element.name}")
        print(f"Symbol: {element.symbol}")
        print(f"Atomic Number: {element.number}")
        print(f"Atomic Weight: {element.mass}")
        print(f"Density: {element.density}")
        print(f"Ion: {element.ion}")
        print(f"Isotopes: {element.isotopes}")
    except KeyError:
        print("Invalid element symbol")

if option == 1:
    element_symbol = input("Enter the symbol of the element: ")
    get_element_info(element_symbol)

elif option == 2:
    country_name = input("Enter Country Name: ")
    try:
        country = CountryInfo(country_name)
        print("Country Name:", country.name())
        print("Country's Capital:", country.capital())
        print("Country's Population:", country.population())
        print("Area (in square kilometers):", country.area())
        print("Region:", country.region())
        print("Sub Region:", country.subregion())
        print("Demonym:", country.demonym())
        print("Currency:", country.currencies())
        print("Languages:", country.languages())
        print("Borders:", country.borders())
    except KeyError:
        print("Invalid country name or information not available")


else:
    print("Option does not exist")
