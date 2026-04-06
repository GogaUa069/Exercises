from system import *
from game_v1 import *

# SETTINGS

tutorial_option = GUIOption("tutorial", system.get_tutorial)
credits_option = GUIOption("credits", system.coming_soon)
audio_option = GUIOption("audio", system.coming_soon)
from_settings_to_mm = GUIOption("leave - main menu", system.pass_func)

settings_options = (tutorial_option, credits_option, audio_option, from_settings_to_mm)
settings_menu = Menu("settings", settings_options)

# MAIN MENU

play_option = GUIOption("play", game)
settings_option = GUIOption("settings", settings_menu)
quit_option = GUIOption("quit", system.pass_func)

mm_options = (play_option, settings_option, quit_option)
main_menu = Menu("main menu", mm_options)

main_menu()
