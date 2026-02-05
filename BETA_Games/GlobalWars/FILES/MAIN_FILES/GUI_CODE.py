from SYSTEM import system

# HEADQUARTER
operations_option = system.Option("operations", system.coming_soon)  # ***
army_option = system.Option("army", system.coming_soon)  # ***
logistics = system.Option("logistics", system.coming_soon)  # ***
from_hq_to_main_menu = system.Option("leave battle", system.pass_func)

hq_options = (operations_option, army_option, logistics, from_hq_to_main_menu)
hq_menu = system.Menu("headquarter", hq_options)

# BATTLE
frontline_option = system.Option("frontline", hq_menu)
sectors_option = system.Option("sectors", hq_menu)
citadel_option = system.Option("citadel", hq_menu)
from_battle_to_main_menu = system.Option("back - main menu", system.pass_func)

battle_options = (frontline_option, sectors_option, citadel_option, from_battle_to_main_menu)
battle_menu = system.Menu("battle modes", battle_options)

# MAIN MENU
battle_option = system.Option("battle modes", battle_menu)
settings_option = system.Option("settings", system.coming_soon)  # ***
quit_option = system.Option("quit", system.pass_func)

main_menu_options = (battle_option, settings_option, quit_option)
main_menu = system.Menu("main menu", main_menu_options)

main_menu()
