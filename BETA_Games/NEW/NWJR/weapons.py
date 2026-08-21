from teams import *
from weapon_manufacturer import *


class Weapon:
    def __init__(self, weapon_type, team, name, manufacturer):
        self.weapon_type = weapon_type
        self.team = team
        self.name = name
        self.manufacturer = manufacturer


class AssaultRifle(Weapon):
    def __init__(self, team, name, manufacturer):
        super().__init__(weapon_type="Assault Rifle", team=team, name=name, manufacturer=manufacturer)


SCARL = AssaultRifle(team=HECU, name="SCAR-L CQC")
M16A4 = AssaultRifle(team=HECU, name="Colt/FN M16A4")
G36C = AssaultRifle(team=HECU, name="H&K G36C")

HK416 = AssaultRifle(team=SWAT, name="HK416 D10RS")
DDM4V7 = AssaultRifle(team=SWAT, name="Daniel Defense DDM4 V7")
MCXVirtus = AssaultRifle(team=SWAT, name="SIG Sauer MCX Virtus")


class Pistol(Weapon):
    def __init__(self, team, name):
        super().__init__(weapon_type="Pistol", team=team, name=name)


M9A3 = Pistol(team=HECU, name="Beretta M9A3")
DesertEagle = Pistol(team=HECU, name="IWI Desert Eagle Mark XIX")
FN57 = Pistol(team=HECU, name="FN Five-SeveN Mk2")

P226 = Pistol(team=SWAT, name="SIG Sauer P226")
Glock17 = Pistol(team=SWAT, name="Glock 17 Gen5")
USPCompact = Pistol(team=SWAT, name="H&K USP Compact")


class Knife(Weapon):
    def __init__(self, team, name):
        super().__init__(weapon_type="Knife", team=team, name=name)


KABarUSMC = Knife(team=HECU, name="KA-BAR USMC")
M9Bayonet = Knife(team=HECU, name="M9 Bayonet")
RAT7 = Knife(team=HECU, name="Ontario RAT-7")

LMF2 = Knife(team=SWAT, name="Gerber LMF II infantry")
SugSealPupElite = Knife(team=SWAT, name="SOG Seal Pup Elite")
EmersonCommander = Knife(team=SWAT, name="Emerson Commander")


class Grenade(Weapon):
    def __init__(self, team, name):
        super().__init__(weapon_type="Grenade", team=team, name=name)


M61 = Grenade(team=HECU, name="M61 Fragmentation Grenade")
M18 = Grenade(team=HECU, name="AN/M18 Smoke Grenade")
MK2 = Grenade(team=HECU, name="MK2 Fragmentation Grenade")

M67 = Grenade(team=SWAT, name="M67 Fragmentation Grenade")
M84 = Grenade(team=SWAT, name="M84 Stun Grenade")
M26 = Grenade(team=SWAT, name="M26 Fragmentation Grenade")


class Heavy(Weapon):
    def __init__(self, team, name):
        super().__init__(weapon_type="Heavy", team=team, name=name)


M134 = Heavy(team=HECU, name="M134 Minigun")
NSV = Heavy(team=HECU, name="NSV 12.7mm HMG")

M2HB = Heavy(team=SWAT, name="Browning M2HB")
DShK = Heavy(team=SWAT, name="DShK 12.7mm HMG")


class ERA(Weapon):
    def __init__(self, team, name):
        super().__init__(weapon_type="ERA", team=team, name=name)


M72 = ERA(team=HECU, name="M72 LAW")
FGM148 = ERA(team=HECU, name="FGM-148 Javelin")
M4 = ERA(team=HECU, name="Carl Gustaf M4")

AT4 = ERA(team=SWAT, name="AT4")
M320 = ERA(team=SWAT, name="M320 Grenade Launcher")
Mk19 = ERA(team=SWAT, name="Mk19 Mod 3 Grenade Launcher")


class SniperRifle(Weapon):
    def __init__(self, team, name):
        super().__init__(weapon_type="Sniper Rifle", team=team, name=name)


M40A1 = SniperRifle(team=HECU, name="M40A1")
Hecate2 = SniperRifle(team=HECU, name="PGM Hecate II")
Scout = SniperRifle(team=HECU, name="Steyr Scout")

Remington700 = SniperRifle(team=SWAT, name="Remington 700")
AXMC = SniperRifle(team=SWAT, name="Accuracy International AXMC")
BarrettMRAD = SniperRifle(team=SWAT, name="Barrett MRAD")


class Shotgun(Weapon):
    def __init__(self, team, name):
        super().__init__(weapon_type="Shotgun", team=team, name=name)


SPAS12 = Shotgun(team=HECU, name="Franchi SPAS-12")
WinchesterSXP = Shotgun(team=HECU, name="Winchester SXP Defender")
Mossberg590 = Shotgun(team=HECU, name="Mossberg 590A1")

BenelliM4 = Shotgun(team=SWAT, name="Benelli M4 Super 90")
BerettaA300 = Shotgun(team=SWAT, name="Beretta A300 Patrol")
Remington870 = Shotgun(team=SWAT, name="Remington 870 Police Magnum")
