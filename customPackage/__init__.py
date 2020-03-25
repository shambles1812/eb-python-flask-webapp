from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
import shopify as shopify

shopify_api_key = 'fea943bb49a20eb4fbb51563dd946c1f'
shopify_api_password = '94dcb3f846b271fe237b5052d138054b'
shopify_api_version = '7.0.1'

application = app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
shop_url = "https://%s:%s@SHOP_NAME.myshopify.com/admin/api/%s" % (shopify_api_key,shopify_api_password , shopify_api_version)
shopify.ShopifyResource.set_site(shop_url)
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)


from customPackage import routes