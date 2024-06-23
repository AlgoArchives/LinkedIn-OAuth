# src/linkedin_api.py

import requests
from config.config import CLIENT_ID, CLIENT_SECRET, REDIRECT_URI

def get_access_token(auth_code):
    response = requests.post(
        'https://www.linkedin.com/oauth/v2/accessToken',
        data={
            'grant_type': 'authorization_code',
            'code': auth_code,
            'redirect_uri': REDIRECT_URI,
            'client_id': CLIENT_ID,
            'client_secret': CLIENT_SECRET
        }
    )
    return response.json().get('access_token')

def get_connections(access_token):
    headers = {
        'Authorization': f'Bearer {access_token}',
        'Connection': 'Keep-Alive',
        'X-Restli-Protocol-Version': '2.0.0'
    }
    response = requests.get(
        'https://api.linkedin.com/v2/connections?q=viewer&start=0&count=50',
        headers=headers
    )
    return response.json()

def get_profile_details(connection_id, access_token):
    headers = {
        'Authorization': f'Bearer {access_token}',
        'Connection': 'Keep-Alive',
        'X-Restli-Protocol-Version': '2.0.0'
    }
    response = requests.get(
        f'https://api.linkedin.com/v2/people/(id:{connection_id})',
        headers=headers
    )
    return response.json()