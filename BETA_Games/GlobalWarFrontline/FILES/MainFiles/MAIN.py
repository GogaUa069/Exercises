from SysConfig import system
from Border import fog_border
from BETA_Games.GlobalWarFrontline.FILES.ECONOMY_FILES.Income import income
from BETA_Games.GlobalWarFrontline.FILES.ECONOMY_FILES.Budget import budget

pass_func = lambda: None
coming_soon = lambda: print(system.communicate("COMING SOON...", "LIGHTWHITE_EX"))

# CARGO TRANSPORT
trucks_option = system.Option("TRUCKS", coming_soon)  # ***
trains_option = system.Option("TRAINS", coming_soon)  # ***
cargo_aircraft_option = system.Option("CARGO AIRCRAFT", coming_soon)  # ***
from_cargo_transport_to_logistics = system.Option(system.underlined_text("BACK - LOGISTICS"), pass_func)

cargo_transport_options = (trucks_option, trains_option, cargo_aircraft_option, from_cargo_transport_to_logistics)
cargo_transport_menu = system.Menu("CARGO TRANSPORT", cargo_transport_options)

# URBANISATION
mines_option = system.Option("MINES", coming_soon)  # ***
fabrics_option = system.Option("FABRICS", coming_soon)  # ***
from_urbanisation_to_logistics = system.Option(system.underlined_text("BACK - LOGISTICS"), pass_func)

urbanisation_options = (mines_option, fabrics_option, from_urbanisation_to_logistics)
urbanisation_menu = system.Menu("URBANISATION", urbanisation_options)

# ECONOMY
income_option = system.Option("INCOME", income)
budget_option = system.Option("BUDGET", budget)
loan_option = system.Option("LOAN", coming_soon)  # ***
from_economy_to_logistics = system.Option(system.underlined_text("BACK - LOGISTICS"), pass_func)

economy_options = (income_option, budget_option, loan_option, from_economy_to_logistics)
economy_menu = system.Menu("ECONOMY", economy_options)

# ARMY TRANSPORT
arc_options = system.Option("ARC", coming_soon)  # ***
troop_transport_option = system.Option("TROOP TRANSPORT", coming_soon)  # ***
combat_aircraft_option = system.Option("COMBAT AIRCRAFT", coming_soon)  # ***
from_combat_transport_to_army = system.Option(system.underlined_text("BACK - ARMY"), pass_func)

combat_transport_options = (arc_options, troop_transport_option, combat_aircraft_option, from_combat_transport_to_army)
combat_transport_menu = system.Menu("COMBAT TRANSPORT", combat_transport_options)

# SOLDIERS
psychology_option = system.Option("PSYCHOLOGY", coming_soon)  # ***
equipment_option = system.Option("EQUIPMENT", coming_soon)  # ***
dislocation_option = system.Option("DISLOCATION", coming_soon)  # ***
habits_option = system.Option("HABITS", coming_soon)  # ***
sections_option = system.Option("SECTIONS", coming_soon)  # ***
from_soldiers_to_army = system.Option(system.underlined_text("BACK - ARMY"), pass_func)

soldiers_options = (psychology_option, equipment_option, dislocation_option, habits_option, sections_option, from_soldiers_to_army)
soldiers_menu = system.Menu("SOLDIERS", soldiers_options)

# LOGISTICS
economy_option = system.Option("ECONOMY", economy_menu)
urbanisation_option = system.Option("URBANISATION", urbanisation_menu)
cargo_transport_option = system.Option("CARGO TRANSPORT", cargo_transport_menu)
from_logistics_to_hq = system.Option(system.underlined_text("BACK - HEADQUARTER"), pass_func)

logistics_options = (economy_option, urbanisation_option, cargo_transport_option, from_logistics_to_hq)
logistics_menu = system.Menu("LOGISTICS", logistics_options)

# ARMY
soldiers_option = system.Option("SOLDIERS", soldiers_menu)
combat_transport_option = system.Option("COMBAT TRANSPORT", combat_transport_menu)
from_army_to_hq = system.Option(system.underlined_text("BACK - HEADQUARTER"), pass_func)

army_options = (soldiers_option, combat_transport_option, from_army_to_hq)
army_menu = system.Menu("ARMY", army_options)

# OPERATIONS
reports_option = system.Option("REPORTS", coming_soon)  # ***
map_option = system.Option("MAP", fog_border)
move_option = system.Option("MOVE", coming_soon)  # ***
from_operations_to_hq = system.Option(system.underlined_text("BACK - HEADQUARTER"), pass_func)

operations_options = (reports_option, map_option, move_option, from_operations_to_hq)
operations_menu = system.Menu("OPERATIONS", operations_options)

# HEADQUARTER
operations_option = system.Option("OPERATIONS", operations_menu)
army_option = system.Option("ARMY", army_menu)
logistics_option = system.Option("LOGISTICS", logistics_menu)
from_hq_to_main_menu = system.Option(system.underlined_text("BACK - MAIN MENU"), pass_func)

headquarter_options = (operations_option, army_option, logistics_option, from_hq_to_main_menu)
headquarter_menu = system.Menu("HEADQUARTER", headquarter_options)

# MAIN MENU
battle_option = system.Option("BATTLE", headquarter_menu)
settings_option = system.Option("SETTINGS", coming_soon)  # ***
quit_option = system.Option(system.underlined_text("QUIT"), pass_func)

main_menu_options = (battle_option, settings_option, quit_option)
main_menu = system.Menu("MAIN MENU", main_menu_options)

main_menu()
