from __future__ import absolute_import, print_function
import sys


def dotter(dot_size, character='.'):
    '''Prints progress dots to the screen
    Returns a function which you call whenever you make progress.

    dot_size is the accumulated amount required before printing a '.'
    '''
    data = [0]

    def accumulate(amount):
        '''Amount is the amount of progress done since the last update.
        Do not test the total work done, only the delta of work done.
        '''
        data[0] += amount
        while data[0] > dot_size:
            sys.stdout.write(character)
            sys.stdout.flush()
            data[0] -= dot_size
    return accumulate
