# routes/tgbot_routes.py
from flask import Blueprint, request, jsonify, render_template
import requests

tgbot_bp = Blueprint('tgbot', __name__)

# Define a route to take input from the user for BOT_TOKEN
@tgbot_bp.route('/get_bot_info', methods=['GET', 'POST'])
def get_bot_info():
    if request.method == 'POST':
        # Retrieve the BOT_TOKEN from the form input
        BOT_TOKEN = request.form.get('bot_token')

        # Make a request to get bot information
        bot_info_url = f"https://api.telegram.org/bot{BOT_TOKEN}/getMe"
        response = requests.get(bot_info_url)
        data = response.json()

        if data["ok"]:
            bot_username = data["result"]["username"]
            return render_template('bot_info.html', bot_username=bot_username)
        else:
            error_message = "Failed to retrieve bot information"
            return render_template('bot_info.html', error_message=error_message)

    return render_template('bot_info.html')
    
