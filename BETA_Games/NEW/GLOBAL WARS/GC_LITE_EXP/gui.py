from system import *

# HEADQUARTER
operations_option = Option("operations", system.coming_soon)  # COMING SOON
army_option = Option("army", system.coming_soon)  # COMING SOON
logistics_option = Option("logistics", system.coming_soon)  # COMING SOON
from_hq_to_battle_modes = Option("leave battle", system.pass_func)

hq_options = (operations_option, army_option, logistics_option, from_hq_to_battle_modes)
hq_menu = Menu("headquarter", hq_options)

# COMBAT MODES
frontline_mode_option = Option("frontline", hq_menu)
from_modes_to_mm = Option("back - main menu", system.pass_func)

combat_modes_options = (frontline_mode_option, from_modes_to_mm)
combat_modes_menu = Menu("combat modes", combat_modes_options)

# MAIN MENU
combat_modes_option = Option("combat modes", combat_modes_menu)
settings_option = Option("settings", system.coming_soon)  # COMING SOON
quit_game_option = Option("quit", system.pass_func)

main_menu_options = (combat_modes_option, settings_option, quit_game_option)
main_menu = Menu("main menu", main_menu_options)

main_menu()
