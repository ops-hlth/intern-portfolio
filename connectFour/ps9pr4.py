
# ps9pr4.py (Problem Set 9, Problem 4)
#
# AI Player for use in Connect Four  
#

import random  
from ps9pr3 import *

class AIPlayer(Player):
    
    def __init__(self, checker, tiebreak, lookahead):
        """ constructs a new AIPlayer object """
        assert(checker == 'X' or checker == 'O')
        assert(tiebreak == 'LEFT' or tiebreak == 'RIGHT' or tiebreak == 'RANDOM')
        assert(lookahead >= 0)
        super().__init__(checker)
        self.tiebreak = tiebreak
        self.lookahead = lookahead
        
        
    def __repr__(self):
        """ returns a string representing an
            AIPlayer object.
        """
        s = 'Player'
        return s + ' ' + str(self.checker) + ' ' + '(' + str(self.tiebreak)+ ',' + ' ' + str(self.lookahead) + ')'
    
    
    def max_score_column(self, scores):
        """ takes a list of scores containing a score
            for each column of the board and returns the
            index of the column with the maximum score
        """
        max_score = max(scores)
        
        result = []
        for x in range(len(scores)):
            if scores[x] == max_score:
                result += [x]
                  
        if self.tiebreak == 'LEFT':
            return result[0]
        elif self.tiebreak == 'RIGHT':
            return result[-1]
        elif self.tiebreak == 'RANDOM':
            return random.choice(result)
            
    def scores_for(self, b):
        """ takes a Board object b and determines the called 
            AIPlayer‘s scores for the columns in b.
        """
        scores = [0] * b.width 
        
        for col in range(b.width):
            if b.can_add_to(col) == False:
                scores[col] = -1
            elif b.is_win_for(self.checker) == True:
                     scores[col] = 100 
            elif b.is_win_for(self.opponent_checker()) == True: 
                     scores[col] = 0 
            elif self.lookahead == 0:
                scores[col] = 50
            else:
                b.add_checker(self.checker, col)
                opponent = self.opponent_checker()
                new_lookahead = self.lookahead - 1
                opp_player = AIPlayer(opponent, self.tiebreak, new_lookahead)
                opp_scores = opp_player.scores_for(b)
                b.remove_checker(col)
                if max(opp_scores) == 0:
                    scores[col] = 100
                elif max(opp_scores) == 100:
                    scores[col] = 0
                elif max(opp_scores) == 50:
                    scores[col] = 50
                     
        return scores    
                
    def next_move(self, b):
        """ returns the called AIPlayer‘s judgment of its best 
            possible move.
        """
        scores = self.scores_for(b)
        best_move = self.max_score_column(scores)
        self.num_moves += 1 
        return best_move
       