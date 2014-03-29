from functools import partial

def center_object():
    print 'centering object'

def view_from(direction):
    print 'viewing from:', direction

def enter_mode(mode):
    print 'entering mode:', mode

_cmd_mapping = {
            'center': center_object,
            'over': partial(view_from, 'over'),
            'under': partial(view_from, 'under'),
            'left': partial(view_from, 'left'),
            'right': partial(view_from, 'right'),
            'paint': partial(enter_mode, 'paint'),
            'sculpt': partial(enter_mode, 'sculpt'),
            'object': partial(enter_mode, 'object'),
            'drop': partial(enter_mode, 'default'),
            }

def interpret_command(cmd):
    if cmd not in _cmd_mapping:
        print "C'est quoi ce dictionnaire de merde ???", cmd
    _cmd_mapping[cmd]()
