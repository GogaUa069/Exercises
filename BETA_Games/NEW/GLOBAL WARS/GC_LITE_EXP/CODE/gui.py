from system import *

# ARMY
soldiers_option = Option("soldiers", system.coming_soon)  # COMING SOON
combat_transport = Option("combat transport", system.coming_soon)  # COMING SOON
from_army_to_hq = Option("back - headquarter", system.pass_func)

army_options = (soldiers_option, combat_transport, from_army_to_hq)
army_menu = Menu("army", army_options)

# OPERATIONS
info_option = Option("info", system.coming_soon)  # COMING SOON
reports_option = Option("reports", system.coming_soon)  # COMING SOON
map_option = Option("map", system.coming_soon)  # COMING SOON
move_option = Option("move", system.coming_soon)  # COMING SOON
from_operations_to_hq = Option("back - headquarter", system.pass_func)  # COMING SOON

operations_options = (info_option, reports_option, map_option, move_option, from_operations_to_hq)
operations_menu = Menu("operations", operations_options)

# HEADQUARTER
operations_option = Option("operations", operations_menu)
army_option = Option("army", army_menu)
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
