from . import additon_bp
from flask import request , jsonify
from .subtract import subtract

@additon_bp.route('/subtract',methods=['GET'])
def subtract_route():
    num1 = int(request.args.get('num1',0))
    num2 = int(request.args.get('num2',0))
    result = subtract(num1,num2)
    return jsonify({'result':result})