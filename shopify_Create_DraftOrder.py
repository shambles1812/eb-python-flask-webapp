import shopify as shopify

# API Credentials
API_KEY = 'fea943bb49a20eb4fbb51563dd946c1f'
PASSWORD = '94dcb3f846b271fe237b5052d138054b'
SHARED_SECRET = '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'
API_VERSION = '2020-01'
SHOP_NAME = 'developer-test-software'

# Shop Link
shop_url = "https://%s:%s@%s.myshopify.com/admin/api/%s" % (API_KEY,PASSWORD,SHOP_NAME, API_VERSION)
shopify.ShopifyResource.set_site(shop_url)


# Create an Order
order =shopify.Order()
order.line_items = [{"title": "Custom Tee",
        "price": "20.00",
        "quantity": 2}]
order.save()
success = order.save()

# Checks whether the order is saved 
print(success)
if order.errors:
   print (order.errors.full_messages())