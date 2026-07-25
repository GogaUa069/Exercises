from system_configuration import *
from border_generation import border, fog_border



# >>> MAIN MENU <<<

# BATTLE
frontline_option = Option("frontline", system.coming_soon)  # *****
from_battle_to_mm = Option("leave battle - back to main menu", system.pass_func)

battle_options = (frontline_option, from_battle_to_mm)
battle_menu = Menu("battle", battle_options)

# SETTINGS
guide_option = Option("guide", system.coming_soon)  # *****
audio_option = Option("audio", system.coming_soon)  # *****
credits_option = Option("credits", system.coming_soon)  # *****
from_settings_to_mm = Option("back - main menu", system.pass_func)

settings_options = (guide_option, audio_option, credits_option, from_settings_to_mm)
settings_menu = Menu("settings", settings_options)

# *************************

# MAIN MENU
battle_option = Option("battle", battle_menu)
settings_option = Option("settings", settings_menu)
quit_option = Option("quit", system.pass_func)

main_menu_options = (battle_option, settings_option, quit_option)
main_menu = Menu("main menu", main_menu_options)

# *************************
system.get_banner("Global wars: Frontline")
main_menu()
