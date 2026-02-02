from SYSTEM import system
from BORDER import fog_border

# BATTLE
frontline_option = system.Option("frontline", system.coming_soon)  # ***
sectors_option = system.Option("sectors", system.coming_soon)  # ***
citadel_option = system.Option("citadel", system.coming_soon)  # ***
from_battle_to_main_menu = system.Option(system.communicate("BACK - MAIN MENU", is_underlined=True), system.pass_func)

battle_options = (frontline_option, sectors_option, citadel_option, from_battle_to_main_menu)
battle_menu = system.Menu("BATTLE MODES", battle_options)

# MAIN MENU
battle_option = system.Option("battle modes", battle_menu)
settings_option = system.Option("settings", system.coming_soon)  # ***
quit_option = system.Option("quit", system.pass_func)

main_menu_options = (battle_option, settings_option, quit_option)
main_menu = system.Menu("main menu", main_menu_options)

main_menu()
