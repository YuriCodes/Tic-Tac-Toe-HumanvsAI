import math
import random 

class Player:
    def __init__(self, letter):
    # x or o
     self.letter = letter 

    def get_move(self, game):
        pass

class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        square = random.choice(game.available_moves())
        return square

class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        valid_square = False
        value = None
        while not valid_square:
            square = input(self.letter + '\'s turn. Input move(0-8):')
            # Check if its the correct value casting it to an int
            # If not say it's invalid or if the spot is not available too
            try:
                value = int(square)
                if value not in game.available_moves():
                    raise ValueError
                valid_square = True 
            except ValueError:
                print('Invalid square. Try again.')

        return value 

class GeniusComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)
    
    def get_move(self, game):
        if len(game.available_moves()) == 9:
            square = random.choice(game.available_moves())
        else:
            #minmax algorithm
            square = self.minimax(game, self.letter)['position']
        return square
    
    def minimax(self, state, player):
        max_player = self.letter 
        other_player = 'O' if player == 'X' else 'X'
        # Check if the previous move was a winner move
        if state.current_winner == other_player:
            return {'position': None, 'score': 1 * (state.num_empty_squares() + 1) if other_player == max_player else -1 * (
                        state.num_empty_squares() + 1)
                        }

        elif not state.empty_squares():
            return {'position': None, 'score': 0}

        if player == max_player:
            # score the best position and score
            best = {'position': None, 'score':-math.inf} #initialize it to the minimal score

        else:
            best = {'position': None, 'score': math.inf}

        for possible_move in state.available_moves():
            # simulate each position
            state.make_move(possible_move, player)
            # recurse using minimax to simulate a game
            sim_score = self.minimax(state, other_player)
            #undo simulation to try again
            state.board[possible_move] = ' '
            state.current_winner = None
            sim_score['position'] = possible_move
            # update the dictionary if necessary
            if player == max_player:
                if sim_score['score'] > best['score']:
                    best = sim_score 
            else:
                if sim_score['score'] < best ['score']:
                    best = sim_score
        
        return best 
            