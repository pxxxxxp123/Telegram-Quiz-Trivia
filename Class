import random
import time

class trivia:
    def __init__(self, lst):
        self.players = {} #player:(correct option, full answer,asked, score, completed)
        self.lst = lst

    def get_playerinfo(self, update):
        return self.players[update.message.from_user.username]

    def add_player(self, update):
        self.players[update.message.from_user.username] = [None, None, [], 0, False]

    def next_question(self, update):
        data_list = self.lst
        selection = random.choice(data_list)
        selection = list(filter(lambda x: x != '' ,selection))
        if selection not in self.players[update.message.from_user.username][2]:
            ans = selection[1:]
            shuffled = random.sample(ans, len(ans))
            print(shuffled)
            helper = {0:'a', 1:'b', 2: 'c', 3:'d'}
            self.players[update.message.from_user.username] = [helper[shuffled.index(selection[1])],
                                                               selection[1],
                                                               self.players[update.message.from_user.username][2] + [selection],
                                                               self.players[update.message.from_user.username][3], False]
            print(self.players[update.message.from_user.username])
            string = ''
            for i in range(len(shuffled)):
                string += '  ' + helper[i] + '. '+shuffled[i]
            update.message.reply_text(selection[0] + "\n" +string)
        else:
            self.next_question(update)

    def correct_answer(self, update):
        update.message.reply_text("Correct!")
        self.players[update.message.from_user.username][3] += 1

    def wrong_answer(self, update):
        update.message.reply_text(f"Wrong! The answer is {self.players[update.message.from_user.username][1]}!")

    def get_score(self, update):
        return self.players[update.message.from_user.username][3]

    def end_quiz(self, update):
        self.players[update.message.from_user.username][4] = True

    def leaderboard(self, update):
        if len(self.players) != 0:
            helper = dict(sorted(self.players.items(), key = lambda x: x[1][3], reverse = True))
            print(helper)
            string = ''
            for key, value in helper.items():
                if self.players[key][4] == False:
                    string += str(key) + ': ' + str(value[3]) +" (Ongoing)" +"\n"
                else:
                    string += str(key) + ': ' + str(value[3]) +"\n"
            update.message.reply_text("===LeaderBoard===\n"+string)
            print("===LeaderBoard===\n"+string)
        else:
            update.message.reply_text("No one has attempted the Trivia yet")
        
    
        
    
        
