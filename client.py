import socketio
import random

from minimax import minimax

sio = socketio.Client()
username = input("Nombre: ") 
tournamentID = input("Tournament ID: ")

@sio.event
def connect():
    sio.emit('signin',
        {
            'tournament_id': tournamentID,
            'user_role': 'player',
            'user_name': username
        }
    )
    print('CONECTADO AL SERVIDOR')

@sio.event
def ready(data):
    gameID = data['game_id']
    playerTurnID = data['player_turn_id']
    board = data['board']
    movementCoordinates = [0, 0]

    #print("Ready")
    #print(board)

    movementCoordinates = minimax(board, True)

    sio.emit('play',
        {
            'tournament_id': tournamentID,
            'player_turn_id': playerTurnID,
            'game_id': gameID,
            'movement': movementCoordinates
        }
    )

    #print("Movement sent")
    

@sio.event
def finish(data):
    gameID = data['game_id']
    playerTurnID = data['player_turn_id']
    winnerTurnID = data['winner_turn_id']
    board = data['board']

    sio.emit('player_ready',
        {
            'tournament_id': tournamentID,
            'player_turn_id': playerTurnID,
            'game_id': gameID,
        }
    )
    
    status = ""
    if(winnerTurnID == playerTurnID):
        status = "WINNER"
    else:
        status = "LOSER"
    

    print("\n----- Juego Finalizado | " + status + " -----\n")
    

@sio.event
def disconnect():
    print('disconnected from server')

sio.connect('http://3.12.129.126:4000')
#sio.connect('http://127.0.0.1:4000')
sio.wait()