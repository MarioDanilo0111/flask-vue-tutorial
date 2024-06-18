from flask import Flask, jsonify, request
from flask_cors import CORS

# Import 'uuid' from the 'uuid' library
import uuid

# Initialize the Flask application
app = Flask(__name__)

# Configure CORS to allow requests from specified origins
CORS(app, resources={r"/*": {"origins": "*"}})


# hello world route
@app.route('/', methods=['GET'])
def greetings():
  return ("Hello World!")

@app.route('/shark', methods=['GET', 'POST'])
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
@app.route('/games', methods=['GET', 'POST'])
def all_games():
  respons_object = {'status':'success'}
  if request.method == 'POST':
    post_data = request.get_json()
    GAMES.append({
      'id': uuid.uuid4().hex,
      'title': post_data.get('title'),
      'genre': post_data.get('genre'),
      'played': post_data.get('played')
    })
    respons_object['message']='Game added successfully.' 
  else:
    respons_object['games'] = GAMES
  return jsonify(respons_object)

# Put & Delete Route handler.
@app.route('/games/<game_id>', methods=['PUT'])
def single_game(game_id):
  respons_object = {'status':'success'}
  if request.method == 'PUT':
    post_data = request.get_json()
    remove_game = (game_id)
    GAMES.append({       
      'id': uuid.uuid4().hex,
      'title': post_data.get('title'),
      'genre': post_data.get('genre'),
      'played': post_data.get('played') 
    })
    respons_object['message']='Game updated successfully.'    
  return jsonify(respons_object)
  
  # Delete route handler
  def remove_game(game_id):
    for game in GAMES:
      if game['id'] == game_id:
        GAMES.remove(game)
        return True
    return False


if __name__ == "__main__":
  # Run the Flask application with debug mode enabled
  app.run(host="0.0.0.0", port=5001, debug=True)