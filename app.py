from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# Replace 'YOUR_API_KEY_HERE' with your actual Fortnite-API key
API_KEY = 'cdf0f369-3a58-4d46-ac57-9128ba52ba82'
API_URL = 'https://fortnite-api.com/v2/stats/br/v2'

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        username = request.form['username']
        platform = request.form['platform']  # Example platforms: epic, psn, xbl
        stats = get_player_stats(username, platform)
        return render_template('index.html', stats=stats, username=username)
    return render_template('index.html')

def get_player_stats(username, platform):
    headers = {
        'Authorization': API_KEY
    }
    params = {
        'name': username,
        'accountType': platform
    }
    response = requests.get(API_URL, headers=headers, params=params)
    if response.status_code == 200:
        data = response.json()
        # Adjust the path according to the API documentation and your needs
        wins = data['data']['stats']['all']['overall']['wins']
        return {'wins': wins}
    else:
        print(f"Error fetching data: {response.status_code}")
        return {}

if __name__ == '__main__':
    app.run(debug=True)
