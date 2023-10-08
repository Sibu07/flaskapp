from flask import Flask
from routes.home_routes import home_bp
from routes.about_routes import about_bp
from routes.contact_routes import contact_bp
from routes.tgbot_routes import tgbot_bp
from routes.mongodb_routes import mongodb_bp
from routes.mongodb_update_routes import mongodb_update_bp
from routes.allroutes_routes import allroutes_bp  # Import the blueprint for allroutes

app = Flask(__name__)

# Register your route blueprints here
app.register_blueprint(home_bp)
app.register_blueprint(about_bp)
app.register_blueprint(contact_bp)
app.register_blueprint(tgbot_bp)
app.register_blueprint(mongodb_bp)
app.register_blueprint(mongodb_update_bp)
app.register_blueprint(allroutes_bp)  # Register the allroutes blueprint

if __name__ == '__main__':
    app.run(debug=True)
