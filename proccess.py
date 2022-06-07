# need to know if each frame is a spare or strike
import random
from doctest import Example
def lucky_rand(n):
    return max(random.randint(0,n),random.randint(0,n))
    # function created to give a random number that is slightly better than average

class Frame:
    def __init__(self,balls):
        self.balls = balls
        # example: [3,7] = Spare /
        # example: [10] = Strike X
    
    def is_strike(self):
        return self.balls[0] == 10

    def is_spare(self):
        return len(self.balls) > 1 and self.balls[0] + self.balls[1] == 10

# example first_frame = Frame([3,6])

class Player:
    def __init__(self,name):
        self.name = name
        self.frames = []
    
    def calc_score(self):
        score = 0
        for i, frame in enumerate(self.frames):
            # pass
            # pass is useful in a situation where code might complicated to test without further code being written first
            # here, raphael wants to test a game without calculating scores yet
            # he is using pass so that he can test whether or not the game itself can be played first (players rolling 10 frames)
            print(frame.balls, i)
            if i == 9:
                if frame.is_strike():
                    score += 10 + frame.balls[1] + frame.balls[2]        
                elif frame.is_spare():
                    score += + frame.balls[2]
                else:
                    score += frame.balls[0] + frame.balls[1]

            elif frame.is_strike():
                score += + self.frames[i+1].balls[0]
                if len(self.frames[i+1].balls) > 1:
                    score += self.frames[i+1].balls[1]
                else:
                    score += self.frames[i+1].balls[1]

            elif frame.is_spare():
                score += 10 + self.frames[i+1].balls[0]
            else:
                score += frame.balls[0] + frame.balls[1]

        return score

class Game:
    def __init__(self,players):
        self.players = players
        self.current_frame = 0

    def play(self):
        for i in range(10):
            self.bowl_frame()
        for player in self.players:
            print(f"The final score for {player.name} is {player.calc_score()}.")

    def bowl_frame(self):
        if self.current_frame <= 9:
            self.current_frame += 1
            for player in self.players:
                balls = []
                # first throw
                balls.append(lucky_rand(10))
                if balls[0] < 10:
                    # if they didnt knock down 10 pins, they get a second chance
                    balls.append(lucky_rand(10 - balls[0]))

                    # on the final frame you get a third ball if you get a spare
                    if balls[0] + balls[1] == 10 and self.current_frame == 10:
                        balls.append(lucky_rand(10))

            
                if balls[0] == 10 and self.current_frame == 10:
                    balls.append(lucky_rand(10))
                    if balls[1] == 10:
                       balls.append(lucky_rand(10))
                    else:
                        balls.append(lucky_rand(10 - balls[1]))

                player.frames.append(Frame(balls))
players = []
for player in ['Alice', 'Bob' ,'Carol', 'Dan']:
    players.append(Player(player))

the_game = Game(players)
the_game.play()

print('finished bowling')

# output:

# [6, 3] 0
# [4, 2] 1
# [7, 3] 2
# [7, 3] 3
# [5, 4] 4
# [9, 1] 5
# [4, 5] 6
# [1, 5] 7
# [10] 8
# [6, 1] 9
# The final score for Alice is 99.
# [8, 2] 0
# [5, 2] 1
# [7, 2] 2
# [3, 2] 3
# [9, 0] 4
# [3, 2] 5
# [4, 4] 6
# [6, 2] 7
# [8, 1] 8
# [6, 4, 7] 9
# The final score for Bob is 82.
# [8, 2] 0
# [7, 3] 1
# [5, 3] 2
# [7, 1] 3
# [7, 2] 4
# [6, 4] 5
# [5, 3] 6
# [1, 2] 7
# [10] 8
# [10, 4, 3] 9
# The final score for Carol is 114.
# [6, 4] 0
# [8, 2] 1
# [5, 3] 2
# [8, 1] 3
# [8, 0] 4
# [7, 1] 5
# [6, 2] 6
# [2, 6] 7
# [10] 8
# [8, 2, 1] 9
# The final score for Dan is 93.
# finished bowling


    