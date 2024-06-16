from flask import Flask, jsonify
from flask_cors import CORS

# Initialize the Flask application
app = Flask(__name__)

# Configure CORS to allow requests from specified origins
CORS(app, resources={r"/*": {"origins": "*"}})


# hello world route
@app.route('/', methods=['GET'])
def greetings():
  return ("Hello World!")

@app.route('/shark', methods=['GET'])
def shark():
  return ("Shark 🦈!")

GAMES = [
  {
   'title':'Halo 3',
   'genre': 'Action',
   'played': False,
   },
  {
   'title':'2k21',
   'genre': 'sports',
   'played': False, 
   },
  {
   'title':'last of us',
   'genre': 'horror',
   'played': True,
   },
  {
   'title':'mario',
   'genre': 'retro',
   'played': True,
   },
  {
   'title':'mortal kombat',
   'genre': 'acction',
   'played': True, 
  },  
   
]

# Route to get all games
@app.route('/games', methods=['GET'])
def all_games():
  return jsonify({
    'games': GAMES,
    'status': 'success'
  })

if __name__ == "__main__":
  # Run the Flask application with debug mode enabled
  app.run(host="0.0.0.0", port=5001, debug=True)