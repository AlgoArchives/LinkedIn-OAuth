# src/main.py

from flask import Flask, request, redirect
from linkedin_api import get_access_token, get_connections, get_profile_details
from utils import save_details_to_file

app = Flask(__name__)

@app.route('/')
def home():
    return 'Welcome to the LinkedIn OAuth example!'

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
    
    return 'Details saved to file.'

if __name__ == '__main__':
    app.run(debug=True, port=8000)