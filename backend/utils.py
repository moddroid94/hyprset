import hyprland
import asyncio


def gettype(setting,values):
    types = SpecialTypes()
    special = None
    match setting:
        case 'follow_mouse':
            special = types.follow_mouse()
        case 'inactive_opacity':
            special = types.window_opacity()
            
    if special is not None:
        return special
    
    
    print('not found in gettype')

class SpecialTypes():
            
    def follow_mouse(self):
        options = [
            [0 , 'no follow'],
            [1 , 'full on mouse'],
            [2 , 'focus on mouse, keyboard on click'],
            [3 , 'focus on mouse, keyboard on shortcut'],
        ]
        return {"options": options, "interval": 1, "digits": 0, "max_value": 3}

    def window_opacity(self):
        options = [
            [0 , 'transparent'],
            [1 , 'fully opaque']
        ]
        return {"options": options, "interval": 0.5, "digits": 2, "max_value": 1}