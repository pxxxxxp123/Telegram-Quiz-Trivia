from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters
import csv
from Class import*
import random

def read_csv(csvfilename):
    with open(csvfilename, encoding='utf-8') as csvfile:
        rows = [row for row in csv.reader(csvfile)]
    return rows
  
"""
Input token and csv file below
"""
updater = Updater('Input Token Here', use_context = True)
file = read_csv('Input Csv file name')
quiz_name = file[0][0]
data_list = file[1:]
quiz = trivia(data_list)

def helper(update, context):
    update.message.reply_text("Available Command:\n/trivia\n/lb")

def trivia(update, context):
    if update.message.from_user.username not in quiz.players:
            quiz.add_player(update)
    if quiz.players[update.message.from_user.username][4] == True:
        update.message.reply_text("You have completed the quiz")
    else:
        update.message.reply_text("Warning! Don't Spam")
        update.message.reply_text("====Start Quiz====")
        quiz.next_question(update)

def quiz_leaderboard(update,context):
    quiz.leaderboard(update)

def handle_message(update, context):
    message_lower = update.message.text.lower()
    if quiz.players[update.message.from_user.username][4] == True:
        update.message.reply_text(random.choice(random_shit))
    elif message_lower in ['a', 'b', 'c', 'd']:
        if message_lower == quiz.players[update.message.from_user.username][0]:
            quiz.correct_answer(update)
        else:
            quiz.wrong_answer(update)
        if len(quiz.get_playerinfo(update)[2]) == len(data_list):
            update.message.reply_text("======= End Of Quiz =======")
            update.message.reply_text("Total : " + str(quiz.get_playerinfo(update)[3]) + '/' + str(len(data_list)))
            quiz.end_quiz(update)
            quiz.leaderboard(update)
        else:
            update.message.reply_text("====Next Question====")
            quiz.next_question(update)
            
updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('help', helper))
updater.dispatcher.add_handler(CommandHandler('trivia', trivia))
updater.dispatcher.add_handler(CommandHandler('lb', quiz_leaderboard))
updater.dispatcher.add_handler(MessageHandler(Filters.text, handle_message))
  
updater.start_polling()
