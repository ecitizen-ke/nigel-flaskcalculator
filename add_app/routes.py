from . import additon_bp
from flask import request , jsonify
from .add import add

@additon_bp.route('/add',methods=['GET'])
def add_route():
    num1 = int(request.args.get('num1',0))
    num2 = int(request.args.get('num1',0))
    result = add(num1,num2)
    return jsonify({'result':result})