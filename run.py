#!usr/bin/env python
from flask import Flask
from add_app import addition_bp
from divide_app import division_bp
from multiply_app import multiplication_bp
from subtract_app import subtraction_bp

def create_app():
    app = Flask(__name__)

    #blueprints
    app.register_blueprint(addition_bp)
    app.register_blueprint(division_bp)
    app.register_blueprint(multiplication_bp)
    app.register_blueprint(subtraction_bp)
    return app