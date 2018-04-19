'''----------------------------------------------------------------------------------------------
This module contains all of the text handlers that will be used to respopnd to the user.
----------------------------------------------------------------------------------------------'''
import globals


def insufficientPermission():
    '''----------------------------------------------------------------------------------------------
        User does not have the correct permissions requested for this app,
    Returns
    -------
        string
            Message to present to user
    ----------------------------------------------------------------------------------------------'''

    if globals.debug is True:
        print 'Insufficient perms'
    return('I need to have permission to access your list.')


def invalidNumber():
    '''----------------------------------------------------------------------------------------------
    Item solicited is not a valid number
    Returns
    -------
        string
            Message to present to user
    ----------------------------------------------------------------------------------------------'''

    if globals.debug is True:
        print 'Invalid number requested'
    return ('I\'m sorry, I do not recognize your request. I only understand numbers as an option. ')


def help():
    '''----------------------------------------------------------------------------------------------
    Message for helping the user know how to use this skill
    Returns
    -------
        string
            Message to present to user
    ----------------------------------------------------------------------------------------------'''

    if globals.debug is True:
        print 'Help requested - now with add txt'
        return ('You need help with ' + globals.alexaSkillName + ' and apparenly I haven\'t written it yet')
