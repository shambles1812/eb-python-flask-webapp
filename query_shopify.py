import requests
import json

# API Credentials
API_KEY = 'fea943bb49a20eb4fbb51563dd946c1f'
PASSWORD = '94dcb3f846b271fe237b5052d138054b'
SHARED_SECRET = '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'
API_VERSION = '2020-01'
SHOP_NAME = 'developer-test-software'
#local variables for data gatherd
phone_in_address = []
orders_for_address = []
cities_available = []
# unpacks api data
response = requests.get("https://fea943bb49a20eb4fbb51563dd946c1f:94dcb3f846b271fe237b5052d138054b@developer-test-software.myshopify.com/admin/api/2020-01/orders.json?fields=id,shipping_address")
api_dict = response.json()
for item in api_dict['orders']:
    if "shipping_address" in item:
        for address_item in item['shipping_address']:
            if item['shipping_address']['city'] in cities_available:
                pass
            else: 
                cities_available.append(item['shipping_address']['city'])
def program_intro():
    # Gets user input for city and introduces program
    print(" This code snippet will return the phone number and orders associated with your chosen city")
    input("Press any key to continue...")
def select_city():
    print(" The cities available are: ")
    # shows cities that can be chosen
    for city_selection in cities_available:
        print(city_selection)
    global city
    city = input("please input the city: ")
    print("-"*20)
program_intro()
select_city()
def parse_info():
    for item in api_dict['orders']:
        if "shipping_address" in item:
            for address_item in item['shipping_address']:
                if item['shipping_address']['city'] == city:
                    if item['shipping_address']['phone'] in phone_in_address:
                        pass
                    else:
                        phone_in_address.append(item['shipping_address']['phone'])
                    if item['id'] in orders_for_address:
                        pass
                    else:
                        orders_for_address.append(item['id'])
def output_info():
    if city in cities_available:
        parse_info()
        print(f"{city}'s phone numbers is/are")
        for number in phone_in_address:
            print(number)
        print(" and the unfulfilled order I.Ds going to it are")
        for order_id in orders_for_address:
            print(order_id)
        input("Press any key to close the program...")
    else:
        print("It seems you didn't choose from the selection")
        input("Press any key to continue...")
        print("please pick a city from the selection below: ")
        select_city()
        output_info()
output_info()