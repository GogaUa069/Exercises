from teams import *


class Weapon:
    def __init__(self, weapon_type, team, name):
        self.weapon_type = weapon_type
        self.team = team
        self.name = name


class AssaultRifle(Weapon):
    def __init__(self, team, name):
        super().__init__(weapon_type="Assault Rifle", team=team, name=name)


SCARL = AssaultRifle(team=HECU, name="FN SCAR-L CQL")
M16A4 = AssaultRifle(team=HECU, name="M16A4")
G36C = AssaultRifle(team=HECU, name="H&K G36C")

HK416 = AssaultRifle(team=SWAT, name="HK416 D10RS")
DDM4V7 = AssaultRifle(team=SWAT, name="DDM4V7")
MCXVirtus = AssaultRifle(team=SWAT, name="MCX Virtus")


class Pistol(Weapon):
    def __init__(self, team, name):
        super().__init__(weapon_type="Pistol", team=team, name=name)


M9A3 = Pistol(team=HECU, name="M9A3")
MK19 = Pistol(team=HECU, name="Desert Eagle")
FN57 = Pistol(team=HECU, name="FN Five-Seven")

P226 = Pistol(team=SWAT, name="Beretta P226")
Glock17 = Pistol(team=SWAT, name="Glock 17")
USPCompact = Pistol(team=SWAT, name="H&K USP Compact")


class Knife(Weapon):
    def __init__(self, team, name):
        super().__init__(weapon_type="Knife", team=team, name=name)


KABarUSMC = Knife(team=HECU, name="KA Bar USMC")
M9Bayonet = Knife(team=HECU, name="M9 Bayonet")
RAT7 = Knife(team=HECU, name="Ontario RAT7")

LMF2 = Knife(team=SWAT, name="Gerber LMF II")
SugSealPupElite = Knife(team=SWAT, name="Sog Seal pup elite")
EmersonCommander = Knife(team=SWAT, name="Emerson Commander")


class Grenade(Weapon):
    def __init__(self, team, name):
        super().__init__(weapon_type="Grenade", team=team, name=name)


M61 = Grenade(team=HECU, name="M61")
M18 = Grenade(team=HECU, name="AN M18")
MK2 = Grenade(team=HECU, name="MK2")

M67 = Grenade(team=SWAT, name="M67")
M84 = Grenade(team=SWAT, name="M84")
M26 = Grenade(team=SWAT, name="M26")


class Heavy(Weapon):
    def __init__(self, team, name):
        super().__init__(weapon_type="Heavy", team=team, name=name)


M134 = Heavy(team=HECU, name="Minigun")
NSV = Heavy(team=HECU, name="NSV")

M2 = Heavy(team=SWAT, name="M2")
DShK = Heavy(team=SWAT, name="DShK")


class ERA(Weapon):
    def __init__(self, team, name):
        super().__init__(weapon_type="ERA", team=team, name=name)


M72 = ERA(team=HECU, name="M72")
FGM148 = ERA(team=HECU, name="FGM148")
M4 = ERA(team=HECU, name="Carl Gustaf M4")

AT4 = ERA(team=SWAT, name="AT4")
M320 = ERA(team=SWAT, name="M320")
Mk19 = ERA(team=SWAT, name="Mk19")


class SniperRifle(Weapon):
    def __init__(self, team, name):
        super().__init__(weapon_type="Sniper Rifle", team=team, name=name)


M40A1 = SniperRifle(team=HECU, name="M40A1")
Hecate2 = SniperRifle(team=HECU, name="Hecate II")
Scout = SniperRifle(team=HECU, name="Scout")

Remington700 = SniperRifle(team=SWAT, name="Remington 700")
AXMC = SniperRifle(team=SWAT, name="AXMC")
BarrettMRAD = SniperRifle(team=SWAT, name="Barrett MRAD")


class Shotgun(Weapon):
    def __init__(self, team, name):
        super().__init__(weapon_type="Shotgun", team=team, name=name)


SPAS12 = Shotgun(team=HECU, name="SPAS 12")
WinchesterSXP = Shotgun(team=HECU, name="Winchester SXP")
Mossberg590 = Shotgun(team=HECU, name="Mossberg 590")

BenelliM4 = Shotgun(team=SWAT, name="Benelli M4")
BerettaA300 = Shotgun(team=SWAT, name="Beretta A300")
Remington870 = Shotgun(team=SWAT, name="Remington 870")
