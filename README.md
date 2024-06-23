# LinkedIn OAuth

This project demonstrates how to use LinkedIn OAuth to authenticate users and fetch their connections using Flask and Bootstrap. It includes a simple web interface to log in with LinkedIn and display a success message after fetching the connections.

## Project Structure

```
linkedin-api-project/
├── config/
│   ├── config.py               # Configuration file to store API credentials and settings
├── data/
│   ├── linkedin_details.txt    # Output file for LinkedIn details
├── src/
│   ├── templates/
│   │   ├── base.html           # Base template with Bootstrap integration
│   │   ├── home.html           # Home page template with login button
│   │   ├── callback.html       # Callback page template to display success message
│   ├── linkedin_api.py         # Script to interact with LinkedIn API
│   ├── main.py                 # Main script to run the project
│   ├── utils.py                # Utility functions
├── requirements.txt            # List of dependencies
├── README.md                   # Project description and setup instructions
```

## Setup Instructions

### 1. Clone the Repository

```sh
git clone https://github.com/Vikranth3140/LinkedIn-OAuth.git
cd LinkedIn-OAuth
```

### 2. Create a Virtual Environment

```sh
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```sh
pip install -r requirements.txt
```

### 4. Configure LinkedIn API Credentials

Create a `config/config.py` file with your LinkedIn API credentials:

```python
# config/config.py

CLIENT_ID = 'YOUR_CLIENT_ID'
CLIENT_SECRET = 'YOUR_CLIENT_SECRET'
REDIRECT_URI = 'http://localhost:8000/callback'
```

### 5. Run the Flask App

```sh
python src/main.py
```

### 6. Access the Application

Open your web browser and go to `http://localhost:8000/`. Click on the "Log in with LinkedIn" button to initiate the OAuth process. After successful authentication, you will be redirected to a success page.

## Troubleshooting

If you encounter issues with LinkedIn OAuth, check the following:

1. **LinkedIn Status**: Ensure LinkedIn is not experiencing any outages.
2. **Redirect URI**: Verify that the redirect URI in `config/config.py` matches the one in your LinkedIn app settings.
3. **Browser Cache**: Clear your browser cache and try again.
4. **App Permissions**: Ensure your LinkedIn app has the correct permissions (scopes) set up.
5. **API Limits**: Check if you are hitting any API rate limits.

## License

This project is licensed under the [MIT License](LICENSE).