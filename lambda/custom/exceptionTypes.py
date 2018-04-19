'''----------------------------------------------------------------------------------------------
This module contains the exceptions raised within the application
----------------------------------------------------------------------------------------------'''


class Error(Exception):
    '''Base class for exceptions in this module.'''
    pass


class ExNotFound(Error):
    '''Use this when we can't find what was requested '''

    def __init__(self, m):
        self.message = 'Item NotFound: ' + str(m)
        print self.message


class ExProviderFailure(Error):
    '''Service provider unable to process'''

    def __init__(self, m):
        self.message = 'Provider failure: ' + str(m)
        print self.message


class ExInsufficientPermission(Error):
    '''request denied due to insufficient permissions'''

    def __init__(self, m):
        self.message = 'Insufficient permission: ' + str(m)
        print self.message


class ExIndexOutOfBounds(Error):
    '''index into list is not within range'''

    def __init__(self, m):
        self.message = 'Index out of bounds: ' + str(m)
        print self.message


class ExNoData(Error):
    '''use this when we can't find what was requested'''

    def __init__(self, m):
        self.message = 'No Data Found: ' + str(m)
        print self.message
