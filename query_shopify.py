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
# unpacks api data
response = requests.get("https://fea943bb49a20eb4fbb51563dd946c1f:94dcb3f846b271fe237b5052d138054b@developer-test-software.myshopify.com/admin/api/2020-01/orders.json?fields=id,shipping_address")
api_dict = response.json()
# Gets user input for city and introduces program
print(" This code snippet will return the phone number and orders associated with your chosen city")
input("Press any key to continue...")
city = input("please input the city: ")
print("-"*20)
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

print(f"The address {city}'s phone numbers are")
for number in phone_in_address:
    print(number)
print(" and the unfulfilled order I.Ds going to it are")
for order_id in orders_for_address:
    print(order_id)
