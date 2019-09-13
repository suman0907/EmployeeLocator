from flask import Flask



def create_app():
    app = Flask(__name__)
    from app.LocateEmployee.views import test as my_route
    app.register_blueprint(my_route, url_prefix = '/locate')
    return app