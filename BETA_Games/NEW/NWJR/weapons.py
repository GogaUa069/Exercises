from teams import *
from weapon_manufacturer import *


class Weapon:
    def __init__(self, weapon_type, team, name, manufacturer):
        self.weapon_type = weapon_type
        self.team = team
        self.name = name
        self.manufacturer = manufacturer


class AssaultRifle(Weapon):
    def __init__(self, team, name, mf):
        super().__init__(weapon_type="Assault Rifle", team=team, name=name, manufacturer=mf)


SCARL = AssaultRifle(team=HECU, name="SCAR-L CQC", mf=FN)
M16A4 = AssaultRifle(team=HECU, name="M16A4", mf=Colt_FN)
G36C = AssaultRifle(team=HECU, name="G36C", mf=H_K)

HK416 = AssaultRifle(team=SWAT, name="HK416 D10RS", mf=H_K)
DDM4V7 = AssaultRifle(team=SWAT, name="DDM4 V7", mf=DanielDefense)
MCXVirtus = AssaultRifle(team=SWAT, name="MCX Virtus", mf=SIG)


class Pistol(Weapon):
    def __init__(self, team, name, mf):
        super().__init__(weapon_type="Pistol", team=team, name=name, manufacturer=mf)


M9A3 = Pistol(team=HECU, name="M9A3", mf=Beretta)
DesertEagle = Pistol(team=HECU, name="Desert Eagle Mark XIX", mf=IWI)
FN57 = Pistol(team=HECU, name="Five-SeveN Mk2", mf=FN)

P226 = Pistol(team=SWAT, name="P226", mf=SIG)
Glock17 = Pistol(team=SWAT, name="Glock 17 Gen5", mf=Glock)
USPCompact = Pistol(team=SWAT, name="USP Compact", mf=H_K)


class Knife(Weapon):
    def __init__(self, team, name, mf):
        super().__init__(weapon_type="Knife", team=team, name=name, manufacturer=mf)


KABarUSMC = Knife(team=HECU, name="USMC Fighting Knife", mf=KA_BAR)
M9Bayonet = Knife(team=HECU, name="M9 Bayonet", mf=Ontario)
RAT7 = Knife(team=HECU, name="RAT-7", mf=Ontario)

LMF2 = Knife(team=SWAT, name="LMF II infantry", mf=Gerber)
SugSealPupElite = Knife(team=SWAT, name="Seal Pup Elite", mf=SOG)
EmersonCommander = Knife(team=SWAT, name="Commander", mf=Emerson)


class Grenade(Weapon):
    def __init__(self, team, name, mf):
        super().__init__(weapon_type="Grenade", team=team, name=name, manufacturer=mf)


M61 = Grenade(team=HECU, name="M61 Fragmentation Grenade", mf=USA)
M18 = Grenade(team=HECU, name="AN/M18 Smoke Grenade", mf=USA)
MK2 = Grenade(team=HECU, name="MK2 Fragmentation Grenade", mf=USA)

M67 = Grenade(team=SWAT, name="M67 Fragmentation Grenade", mf=USA)
M84 = Grenade(team=SWAT, name="M84 Stun Grenade", mf=USA)
M26 = Grenade(team=SWAT, name="M26 Fragmentation Grenade", mf=USA)


class Heavy(Weapon):
    def __init__(self, team, name, mf):
        super().__init__(weapon_type="Heavy", team=team, name=name, manufacturer=mf)


M134 = Heavy(team=HECU, name="M134 Minigun", mf=GE)
NSV = Heavy(team=HECU, name="NSV 12.7mm HMG", mf=NSV)

M2HB = Heavy(team=SWAT, name="Browning M2HB", mf=USA)
DShK = Heavy(team=SWAT, name="DShK 12.7mm HMG", mf=DS)


class ERA(Weapon):
    def __init__(self, team, name, mf):
        super().__init__(weapon_type="ERA", team=team, name=name, manufacturer=mf)


M72 = ERA(team=HECU, name="M72 LAW", mf=Nammo)
FGM148 = ERA(team=HECU, name="FGM-148 Javelin", mf=Raytheon)
M4 = ERA(team=HECU, name="Carl Gustaf M4", mf=SBD)

AT4 = ERA(team=SWAT, name="AT4", mf=SBD)
M320 = ERA(team=SWAT, name="M320 Grenade Launcher", mf=H_K)
Mk19 = ERA(team=SWAT, name="Mk19 Mod 3 Grenade Launcher", mf=GD)


class SniperRifle(Weapon):
    def __init__(self, team, name, mf):
        super().__init__(weapon_type="Sniper Rifle", team=team, name=name, manufacturer=mf)


M40A1 = SniperRifle(team=HECU, name="M40A1", mf=Remington)
Hecate2 = SniperRifle(team=HECU, name="Hecate II", mf=PGM)
Scout = SniperRifle(team=HECU, name="Scout", mf=Steyr)

Remington700 = SniperRifle(team=SWAT, name="Remington 700", mf=Remington)
AXMC = SniperRifle(team=SWAT, name="AXMC", mf=AI)
BarrettMRAD = SniperRifle(team=SWAT, name="MRAD", mf=BF)


class Shotgun(Weapon):
    def __init__(self, team, name, mf):
        super().__init__(weapon_type="Shotgun", team=team, name=name, manufacturer=mf)


SPAS12 = Shotgun(team=HECU, name="SPAS-12", mf=Franchi)
WinchesterSXP = Shotgun(team=HECU, name="SXP Defender", mf=Winchester)
Mossberg590 = Shotgun(team=HECU, name="590A1", mf=Mossberg)

BenelliM4 = Shotgun(team=SWAT, name="M4 Super 90", mf=Benelli)
BerettaA300 = Shotgun(team=SWAT, name="A300 Patrol", mf=Beretta)
Remington870 = Shotgun(team=SWAT, name="870 Police Magnum", mf=Remington)
