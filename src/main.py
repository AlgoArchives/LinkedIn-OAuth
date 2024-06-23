# src/main.py

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from flask import Flask, redirect, request, render_template, url_for
from linkedin_api import get_access_token, get_connections, get_profile_details
from utils import save_details_to_file
from config.config import CLIENT_ID

app = Flask(__name__)

REDIRECT_URI = 'http://localhost:8000/callback'

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login')
def login():
    authorization_url = (
        "https://www.linkedin.com/oauth/v2/authorization?response_type=code&client_id={}&redirect_uri={}&scope=r_liteprofile%20r_emailaddress%20w_member_social"
    ).format(CLIENT_ID, REDIRECT_URI)
    return redirect(authorization_url)

@app.route('/callback')
def callback():
    auth_code = request.args.get('code')
    access_token = get_access_token(auth_code)
    connections = get_connections(access_token)
    
    pending_connections = []  # Add logic to filter pending connections
    high_follower_connections = []

    for connection in connections['elements']:
        connection_id = connection['id']
        profile = get_profile_details(connection_id, access_token)
        follower_count = profile.get('numConnections')
        if follower_count and follower_count > 10000:
            high_follower_connections.append(f'{profile["localizedFirstName"]} {profile["localizedLastName"]} ({follower_count} followers)')
    
    save_details_to_file(pending_connections, high_follower_connections)
    
    return render_template('callback.html')

if __name__ == '__main__':
    app.run(debug=True, port=8000)