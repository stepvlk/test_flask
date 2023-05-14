from flask import Blueprint, request, jsonify, Response
routes = Blueprint('routes', __name__, static_folder='static', template_folder='templates')
import json
import toml
import sys
import gzip
from graph import Vis, Graph
from account import Accounts
import databases


config = toml.load('')
base = getattr(databases, config['server']['db'])

@routes.route('/api/v1/netmap/records', methods=['GET', 'POST', 'DELETE'])
def records():
    
    if request.method == 'GET':

        params = json.dumps(request.args)
        
        if len(params) > 2:
            data = base.select(params)
        else:  
            data = base.select_all()
    
    if request.method == 'POST':
        
        query = request.get_json()
        data  = base.insert(query) 
    
    if request.method == "DELETE":

        query = request.form.getlist('data')
        data  = base.delete(query[0])
    
    return jsonify({"data": data}), 200