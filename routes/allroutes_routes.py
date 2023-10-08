# routes/allroutes_routes.py
from flask import Blueprint, render_template, current_app
from werkzeug.routing import Map

allroutes_bp = Blueprint('allroutes', __name__)

@allroutes_bp.route('/allroutes')
def all_routes():
    rules = set()
    for rule in current_app.url_map.iter_rules():
        if rule.endpoint and not rule.endpoint.startswith('static'):
            rules.add(rule.endpoint)
    return render_template('all_routes.html', rules=sorted(list(rules)))
    