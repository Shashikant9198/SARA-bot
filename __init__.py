# -*- coding: utf-8 -*-
"""This module contains a template MindMeld application"""
from mindmeld import Application

app = Application(__name__)

__all__ = ['app']


#@app.handle(intent='greet')
#def welcome(request, responder):
    #"""This is a default handler."""
    #responder.reply('Hello there!')


#@app.handle(intent='greet')
#def welcome(request, responder):
#    responder.reply('Hello')







 

@app.handle(intent='greet')
def welcome(request, responder):
    """
    When the user starts a conversation, say hi and give some restaurant suggestions to explore.
    """
    #try:
        # Get user's name from session information in a request to personalize the greeting.
        #responder.slots['name'] = request.context['name']
        #prefix = 'Hello, {name}. '
   # except KeyError:
    #    prefix = 'Hello. '

    # Get suggestions for three restaurants from the knowledge base.
    # Ideally, these should be selected using factors like popularity, proximity, etc.
    #restaurants = app.question_answerer.get(index='restaurants')
    #suggestions = ', '.join([r['name'] for r in restaurants[0:3]])

    # Build up the final natural language response and reply to the user.
    responder.reply('Hello!Just let me know how can i help you?')


@app.handle(intent='exit')
def say_goodbye(request, responder):
    """
    When the user ends a conversation, clear the dialogue frame and say goodbye.
    """
    # Clear the dialogue frame to start afresh for the next user request.
    responder.frame = {}

    # Respond with a random selection from one of the canned "goodbye" responses.
    responder.reply(['Bye!', 'Goodbye!', 'Have a nice day.', 'See you later.'])



@app.handle(intent='weather',entity='location')
def weather1(request, responder):
    """
    When the user starts a conversation, say hi and give some restaurant suggestions to explore.
    """
    #try:
        # Get user's name from session information in a request to personalize the greeting.
        #responder.slots['name'] = request.context['name']
        #prefix = 'Hello, {name}. '
   # except KeyError:
    #    prefix = 'Hello. '

    # Get suggestions for three restaurants from the knowledge base.
    # Ideally, these should be selected using factors like popularity, proximity, etc.
    #restaurants = app.question_answerer.get(index='restaurants')
    #suggestions = ', '.join([r['name'] for r in restaurants[0:3]])

    # Build up the final natural language response and reply to the user.
    #responder.reply('I'm sorry, I wasn't able to recognize that location, could you try again?')
    responder.reply('Maut agayi hai bahar?')






