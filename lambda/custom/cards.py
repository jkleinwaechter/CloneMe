'''----------------------------------------------------------------------------------------------
This module is responsible for building the components of the Alexa JSON Repsonse objects
----------------------------------------------------------------------------------------------'''

import re


def buildResponse(session_attributes, speechlet_response):
    '''----------------------------------------------------------------------------------------------
    Create a fully formed Alexa JSON Response object

    Parameters
    ----------
        sessionAttributes : dictionary
            State variables that will be returned to us while in the same session
        speechletResponse : dictionary
            The 'response' section of the Alexa JSON Response object

    Returns
    -------
    dictionary
        The Alexa JSON Response object

    ----------------------------------------------------------------------------------------------'''
    return {
        "version": "1.0",
        "sessionAttributes": session_attributes,
        "response": speechlet_response
    }


def buildSpeechletResponse(title, output, reprompt="Knock Knock", shouldEndSession=True, cardType='Simple'):
    '''----------------------------------------------------------------------------------------------
    Build the 'response' section of the Alexa JSON Response object

    Parameters
    ----------
        title : string
            Text placed on title of card
        output : string
            SSML voice response, excluding the <speak> tags
        reprompt : string (optional)
            Voice response if user does not respond in time
        shouldEndSession - boolean (optional)
            Request that this be the end of the session
        cardType : string (optional)
            Alexa card types

    Returns
    -------
        dictionary
            'Response' section of the Alexa JSON Response object

    ----------------------------------------------------------------------------------------------'''

    # add the speak tag around the object so that the incoming text can be pure text or ssmal.
    voice = '<speak>' + output + '</speak>'  # Using SSML, but we will take care of encloising the string in a speak tag

    # Strip out ssml so we can print to the card
    cleanr = re.compile('<.*?>')
    cleanOutput = re.sub(cleanr, '', output)

    return {
        'outputSpeech': {
            'type': 'SSML',
            'ssml': voice
        },
        'card': {
            'type': cardType,
            'title': title,
            'content': cleanOutput
        },
        'reprompt': {
            'outputSpeech': {
                'type': 'PlainText',
                'text': reprompt
            }
        },
        'shouldEndSession': shouldEndSession
    }


def buildDelegateDirective(intentName=None, slotName=None, value=None):
    '''----------------------------------------------------------------------------------------------
    Build the 'response' section of a dialog delegate directive for a given slot, either named or next
    default. This is used when you make slots mandatory and there is at least one that hasn't been
    filled in yet.

    Parameters
    ----------
        intentName : string (optional)
            Name of the invoked intent. This is only needed if you are changing the default state of a slot
        slotName : string (optional)
            Name of the slot. This is only needed if you are changing the default state of a slot
        value : string (optional)
            Default value to set for the slot. This is only needed if you are changing its default state.

    Returns
    -------
        dictionary
            'Response' section of the Alexa JSON Response object
    ----------------------------------------------------------------------------------------------'''
    if intentName:  # indicating we want to change a slot's default
        d = {
            'directives': [
                {
                    'type': 'Dialog.Delegate',
                    'updatedIntent': {
                        'name': intentName,
                        'confirmationStatus': 'NONE',
                        'slots': {
                            slotName: {
                                'name': slotName,
                                'value': value,
                                'confirmationStatus': 'NONE'
                            }
                        }
                    }
                }
            ],

            'shouldEndSession': False
        }

    else:
        d = {
            'directives': [
                {
                    'type': 'Dialog.Delegate'
                }
            ],
            # 'shouldEndSession': False
        }

    if globals.debug:
        print 'Returned dialog.delegate:'
        print d
    return d


def buildElicitSlotDirective(slotName, output, reprompt):
    '''----------------------------------------------------------------------------------------------
    Make a user request to fill in a named slot. This is used when you want to control the conversation
    by prompting for a given slot.

    Parameters
    ----------
        slotName : string
            Name of the slot to prompt for.
        output : string
            SSML voice response, excluding the <speak> tags
        reprompt : string (optional)
            Voice response if user does not respond in time

    Returns
    -------
        dictionary
            'Response' section of the Alexa JSON Response object
    ----------------------------------------------------------------------------------------------'''
    if globals.debug:
        print '>>buildElicitSlotDirective slotName: %s, %s' % (slotName, output)

    # add the speak tag around the object so that the incoming text can be pure text or ssmal.
    voice = '<speak>' + output + '</speak>'  # Using SSML, but we will take care of encloising the string in a speak tag

    return {
        'directives': [
            {
                'type': 'Dialog.ElicitSlot',
                'slotToElicit': slotName
            }
        ],
        'outputSpeech': {
            'type': 'SSML',
            'ssml': voice
        },
        'reprompt': {
            'outputSpeech': {
                'type': 'PlainText',
                'text': reprompt
            }
        },
        'shouldEndSession': False
    }


def buildPermsNeededResponse(output):
    '''----------------------------------------------------------------------------------------------
    Hnadle getting the permissions from user with prompt

    Parameters
    ----------
        output : string
            Text you ant said to user

    Returns
    -------
        dictionary
            'Response' section of the Alexa JSON Response object
    ----------------------------------------------------------------------------------------------'''
    return {
        'outputSpeech': {
            'type': 'Simple',
            'ssml': 'You need permissions set in your Alexa app'
        },
        'card': {
            'type': 'AskForPermissionsConsent',
            'permissions': ['read::alexa:household:list']
        },
        # 'shouldEndSession': True
    }
