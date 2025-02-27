'''
Printer model specifications.

No rights reserved.
License CC0-1.0-only: https://directory.fsf.org/wiki/License:CC0
'''

class Model():
    ''' A printer model
        `paper_width`: pixels per line for the model/paper
        `is_new_kind`: some models have new "start print" command and can understand compressed data.
                the algorithm isn't implemented in Cat-Printer yet, but this should be no harm.
        `problem_feeding`: didn't yet figure out MX05/MX06 bad behavior giving feed command, use workaround for them
    '''
    paper_width: int = 384
    is_new_kind: bool = False
    problem_feeding: bool = False

Models = {}

# all known supported models
for name in 'GB01 GB02 GB03 GT01 MX05 MX06 YT01'.split(' '):
    Models[name] = Model()

# that can receive compressed data
for name in 'GB03'.split(' '):
    Models[name].is_new_kind = True

# that have problem giving feed command
for name in 'MX05 MX06'.split(' '):
    Models[name].problem_feeding = True
