from SYSTEM import system
from BORDER import fog_border

# MAIN MENU
battle_option = system.Option("battle", system.coming_soon)
settings_option = system.Option("settings", system.coming_soon)
quit_option = system.Option("quit", system.pass_func)

main_menu_options = (battle_option, settings_option, quit_option)
main_menu = system.Menu("main menu", main_menu_options)

main_menu()
