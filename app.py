from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from models import Car, Brand

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:coderslab@localhost:5432/cars_db'
db = SQLAlchemy(app)


class CarDB(object):

    @app.route('/brand/new', methods=['POST'])
    def crate_brand(self, name):
        new_brand = Brand(name)
        db.session.add(new_brand)
        db.session.commit()
        return jsonify(new_brand)

    @app.route('/car/new', methods=['POST'])
    def create_car(self, brand, model, **info):
        new_car = Car(brand, model, **info)
        db.session.add(new_car)
        db.session.commit()
        return jsonify(new_car)

    @app.route('/car', methods=['GET'])
    def get_all_cars(self):
        cars = Car.query.all()
        output = []
        for car in cars:
            car_data = {'id': car.id, 'model': car.model, 'brand': car.brand, 'info': car.info}
            output.append(car_data)
        return jsonify(output)

    @app.route('/brand', methods=['GET'])
    def get_all_brands(self):
        brands = Brand.query.all()
        output = []
        for brand in brands:
            brand_data = {'id': brand.id, 'name': brand.name}
            output.append(brand_data)
        return jsonify(output)

    @app.route('/car/<int:car_id>', methods=['DELETE'])
    def car_delete(car_id):
        car = Car.query.get(car_id)
        if car in None:
            return '404'
        db.session.delete(car)
        db.session.commit()
        return 'The car has been deleted'

    @app.route('/car/<int:car_id>', methods=['PUT'])
    def car_update(car_id):
        car = Car.query.get(car_id)
        if car is None:
            return '404'
        model = request.json['model']
        brand = request.json['brand']
        info = request.json['info']
        car.model = model
        car.brand = brand
        car.info = info
        db.session.commit()
        return "The requested update has been made"



if __name__ == '__main__':
    app.run(debug=True)
