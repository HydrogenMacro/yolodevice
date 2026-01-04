# You import all the IOs of your board
import board

# These are imports from the kmk library
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC
from kmk.modules.macros import Press, Release, Tap, Macros
from kmk.extensions.RGB import RGB

# This is the main instance of your keyboard
keyboard = KMKKeyboard()

# Add the macro extension
macros = Macros()
keyboard.modules.append(macros)

# Define your pins here!
PINS = [board.D1, board.D2, board.D4, board.D3, board.D7, board.D6]

# Tell kmk we are not using a key matrix
keyboard.matrix = KeysScanner(
    pins=PINS,
    value_when_pressed=False,
)

# Here you define the buttons corresponding to the pins
# Look here for keycodes: https://github.com/KMKfw/kmk_firmware/blob/main/docs/en/keycodes.md
# And here for macros: https://github.com/KMKfw/kmk_firmware/blob/main/docs/en/macros.md

# qwerty equivalent keys
keyboard.keymap = [
    [KC.W, KC.A, KC.S, KC.D, KC.F, KC.Q,]
]

# osu! keybinds
"""
keyboard.keymap = [
    [KC.ENTER, KC.Z, KC.X, KC.Z, KC.ESCAPE, KC.ESCAPE,]
]
"""

# Ok I dont have the board in front of me, so who knows if this code works or not

# Encoder support
from kmk.modules.encoder import EncoderHandler
encoder_handler = EncoderHandler()
keyboard.modules.append(encoder_handler)
encoder_handler.pins = (
    (board.GP27, board.GP28, board.GP26,),
)
encoder_handler.map = [
    ((KC.VOLD, KC.VOLU, KC.MUTE),),
]

# RGB colors (currently hard white, will tinker with once I have the board)
rgb = RGB(pixel_pin=board.D29, num_pixels=6, rgb_order=(1, 0, 2))
rgb.set_rgb_fill(255, 255, 255)
keyboard.extensions.append(rgb)


# Start kmk!
if __name__ == '__main__':
    keyboard.go()
