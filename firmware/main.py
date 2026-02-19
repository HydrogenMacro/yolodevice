# You import all the IOs of your board
import board

# These are imports from the kmk library
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC
from kmk.modules.macros import Press, Release, Tap, Macros
from kmk.extensions.rgb import RGB, AnimationModes
from kmk.extensions.media_keys import MediaKeys

# This is the main instance of your keyboard
keyboard = KMKKeyboard()

keyboard.extensions.append(MediaKeys())

# Add the macro extension
macros = Macros()
keyboard.modules.append(macros)

# Define your pins here!
PINS = [board.D7, board.D8, board.D9, board.D10, board.D5, board.D4]

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

keyboard.keymap = [
    [KC.SPACE, KC.Z, KC.X, KC.C, KC.ESCAPE, KC.ESCAPE,]
]

# geometry dash keybinds

keyboard.keymap = [
    [KC.ESCAPE, KC.SPACE, KC.SPACE, KC.SPACE, KC.ESCAPE,]
]


# Encoder support
from kmk.modules.encoder import EncoderHandler
encoder_handler = EncoderHandler()
keyboard.modules.append(encoder_handler)

encoder_handler.pins = (
    (board.D1, board.D2, board.D0, False),
)
encoder_handler.map = [
    ((KC.AUDIO_VOL_DOWN, KC.AUDIO_VOL_UP, KC.AUDIO_MUTE),),
]

rgb = RGB(pixel_pin=board.D3, num_pixels=6, animation_mode = AnimationModes.BREATHING, sat_default = 0, breathe_center = 2, animation_speed = 5)
keyboard.extensions.append(rgb)

if __name__ == '__main__':
    print("Starting KMK:");
    keyboard.go()
