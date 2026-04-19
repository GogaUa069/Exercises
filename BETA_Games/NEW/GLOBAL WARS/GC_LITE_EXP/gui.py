from system import *

# MAIN MENU
combat_modes_option = Option("combat modes", system.coming_soon)
settings_option = Option("settings", system.coming_soon)
quit_game_option = Option("quit", system.pass_func)

main_menu_options = (combat_modes_option, settings_option, quit_game_option)
main_menu = Menu("main menu", main_menu_options)

main_menu()
