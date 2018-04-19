'''----------------------------------------------------------------------------------------------
This module handles the division of labor for each of the intents. For this skill, most of the
business logic is contained in this module
----------------------------------------------------------------------------------------------'''

import globals
import responses
from cards import buildResponse, buildSpeechletResponse
from exceptionTypes import ExIndexOutOfBounds
# from transact import performAlexaTransaction


def handleSessionEndRequest():
    '''----------------------------------------------------------------------------------------------
    Process a 'Cancel' intent

    Parameters
    ----------
        none

    Returns
    -------
        dictionary
            The Alexa JSON Response object
    ----------------------------------------------------------------------------------------------'''

    card_title = globals.alexaSkillName
    speech = 'Grazie.'
    shouldEndSession = True

    return buildResponse({}, buildSpeechletResponse(card_title, speech, None, shouldEndSession))


def getHelp(request, session):
    '''----------------------------------------------------------------------------------------------
    Produce a help response for the user

    Parameters
    ----------
        none

    Returns
    -------
        dictionary
            The Alexa JSON Response object
    ----------------------------------------------------------------------------------------------'''

    session_attributes = {}
    card_title = globals.alexaSkillName
    reprompt_text = ''
    shouldEndSession = True

    if globals.debug is True:
        print 'User asked for help.'
    return buildResponse(session_attributes, buildSpeechletResponse(card_title, responses.help(), reprompt_text, shouldEndSession))


def basicCall(system):
    '''----------------------------------------------------------------------------------------------
    This is the intent handler for a basic call with no slots

    Parameters
    ----------
        session : dictionary
            The 'session' section of the Alexa JSON Request object

    Returns
    -------
        dictionary
            The Alexa JSON Response object

    ----------------------------------------------------------------------------------------------'''
    card_title = globals.alexaSkillName
    reprompt_text = ''
    shouldEndSession = True
    session_attributes = {}

    # Put in code or call that will eventually fill the string 'speech' with the proper response
    # Use performAlexaTransaction() if you want to make calls to Alexa (lists, userinfo etc.)
    speech = 'This page left intentionally blank.'  # Code or call goes here

    return buildResponse(session_attributes, buildSpeechletResponse(card_title, speech, reprompt_text, shouldEndSession))


def basicCallWithSlot(system, intent):
    '''----------------------------------------------------------------------------------------------
    This is the intent handler for a basic call with a slot

    Parameters
    ----------
        session : dictionary
            The 'session' section of the Alexa JSON Request object
        intent : dictionary
            The 'intent' section of the Alexa JSON Request object

    Returns
    -------
        dictionary
            The Alexa JSON Response object
    ----------------------------------------------------------------------------------------------'''

    session_attributes = {}
    card_title = globals.alexaSkillName
    reprompt_text = 'Knock knock'
    shouldEndSession = True

    # Put in code or call that will eventually fill the string 'speech' with the proper response
    # Use the example in getNumericSlot to process a slot
    try:
        # Use performAlexaTransaction() if you want to make calls to Alexa (lists, userinfo etc.)
        requestedNumber = getNumericSlot(intent)
    except ExIndexOutOfBounds:
        speech = responses.invalidNumber()
    else:
        speech = 'User asked for number ' + str(requestedNumber)
    return buildResponse(session_attributes, buildSpeechletResponse(card_title, speech, reprompt_text, shouldEndSession))


def getNumericSlot(intent):
    '''----------------------------------------------------------------------------------------------
    Read the value for a numeric voice slot

    Parameters
    ----------
        intent : dictionary
            'intent' object as provided by Alexa JSON request

    Returns
    -------
        integer
            The number spoken by the user

    Raises
    ------
        ExIndexOutOfBounds - Invalid or missing value
    ----------------------------------------------------------------------------------------------'''

    # INDEX is the slot named in the model - change to match yours
    if 'INDEX' in intent['slots']:
        slot = intent['slots']['INDEX']
        if 'value' in slot:
            value = slot['value']
            return int(value)
        else:
            print 'No "value" in slot'
            raise ExIndexOutOfBounds(intent)
    else:
        print 'No "INDEX" in slot'
        raise ExIndexOutOfBounds(intent)
