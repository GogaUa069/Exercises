from teams import *
from weapon_manufacturer import *


class Weapon:
    def __init__(self, weapon_type, team, name, manufacturer, single_use=False):
        self.weapon_type = weapon_type
        self.team = team
        self.name = name
        self.manufacturer = manufacturer
        self.single_use = single_use


class AssaultRifle(Weapon):
    def __init__(self, team, name, mf, rounds):
        super().__init__(weapon_type="Assault Rifle", team=team, name=name, manufacturer=mf)
        self.rounds = rounds


SCARL = AssaultRifle(team=HECU, name="SCAR-L CQC", mf=FN,      rounds=30)
M16A4 = AssaultRifle(team=HECU, name="M16A4",      mf=Colt_FN, rounds=30)
G36C = AssaultRifle( team=HECU, name="G36C",       mf=H_K,     rounds=30)

HK416 = AssaultRifle(    team=SWAT,  name="HK416 D10RS", mf=H_K,           rounds=30)
DDM4V7 = AssaultRifle(   team=SWAT,  name="DDM4 V7",     mf=DanielDefense, rounds=32)
MCXVirtus = AssaultRifle(team=SWAT,  name="MCX Virtus",  mf=SIG,           rounds=30)


class Pistol(Weapon):
    def __init__(self, team, name, mf, rounds):
        super().__init__(weapon_type="Pistol", team=team, name=name, manufacturer=mf)
        self.rounds = rounds


M9A3 = Pistol(       team=HECU, name="M9A3",                  mf=Beretta, rounds=17)
DesertEagle = Pistol(team=HECU, name="Desert Eagle Mark XIX", mf=IWI,     rounds=7)
FSMk2 = Pistol(      team=HECU, name="Five-SeveN Mk2",        mf=FN,      rounds=20)

P226 = Pistol(      team=SWAT, name="P226",          mf=SIG,   rounds=20)
Glock17 = Pistol(   team=SWAT, name="Glock 17 Gen5", mf=Glock, rounds=17)
USPCompact = Pistol(team=SWAT, name="USP Compact",   mf=H_K,   rounds=13)


class Knife(Weapon):
    def __init__(self, team, name, mf):
        super().__init__(weapon_type="Knife", team=team, name=name, manufacturer=mf)


USMC = Knife(     team=HECU, name="USMC Fighting Knife", mf=KA_BAR)
M9Bayonet = Knife(team=HECU, name="M9 Bayonet",          mf=Ontario)
RAT7 = Knife(     team=HECU, name="RAT-7",               mf=Ontario)

LMF2 = Knife(        team=SWAT, name="LMF II infantry", mf=Gerber)
SealPupElite = Knife(team=SWAT, name="Seal Pup Elite",  mf=SOG)
Commander = Knife(   team=SWAT, name="Commander",       mf=Emerson)


class Grenade(Weapon):
    def __init__(self, team, name, mf, amount=3):
        super().__init__(weapon_type="Grenade", team=team, name=name, manufacturer=mf)
        self.amount = amount


M61 = Grenade(team=HECU, name="M61 Fragmentation Grenade", mf=USA)
M18 = Grenade(team=HECU, name="AN/M18 Smoke Grenade",      mf=USA)
MK2 = Grenade(team=HECU, name="MK2 Fragmentation Grenade", mf=USA)

M67 = Grenade(team=SWAT, name="M67 Fragmentation Grenade", mf=USA)
M84 = Grenade(team=SWAT, name="M84 Stun Grenade",          mf=USA)
M26 = Grenade(team=SWAT, name="M26 Fragmentation Grenade", mf=USA)


class Heavy(Weapon):
    def __init__(self, team, name, mf, rounds, single_use=True):
        super().__init__(weapon_type="Heavy", team=team, name=name, manufacturer=mf, single_use=single_use)
        self.rounds = rounds


M134 = Heavy(team=HECU, name="M134 Minigun",   mf=GE,  rounds=3000)
NSV = Heavy( team=HECU, name="NSV 12.7mm HMG", mf=NSV, rounds=150)

M2HB = Heavy(team=SWAT, name="Browning M2HB",   mf=USA, rounds=100)
DShK = Heavy(team=SWAT, name="DShK 12.7mm HMG", mf=DS,  rounds=50)


class ERA(Weapon):
    def __init__(self, team, name, mf, rounds, single_use=False):
        super().__init__(weapon_type="ERA", team=team, name=name, manufacturer=mf, single_use=single_use)
        self.rounds = rounds


M72 = ERA(   team=HECU, name="M72 LAW",         mf=Nammo,    rounds=1, single_use=True)
FGM148 = ERA(team=HECU, name="FGM-148 Javelin", mf=Raytheon, rounds=1)
M4 = ERA(    team=HECU, name="Carl Gustaf M4",  mf=SBD,      rounds=1)

AT4 = ERA( team=SWAT, name="AT4",                         mf=SBD, rounds=84)
M320 = ERA(team=SWAT, name="M320 Grenade Launcher",       mf=H_K, rounds=1)
Mk19 = ERA(team=SWAT, name="Mk19 Mod 3 Grenade Launcher", mf=GD,  rounds=48)


class SniperRifle(Weapon):
    def __init__(self, team, name, mf, rounds):
        super().__init__(weapon_type="Sniper Rifle", team=team, name=name, manufacturer=mf)
        self.rounds = rounds


M40A1 = SniperRifle(  team=HECU, name="M40A1",     mf=Remington, rounds=5)
Hecate2 = SniperRifle(team=HECU, name="Hecate II", mf=PGM,       rounds=7)
Scout = SniperRifle(  team=HECU, name="Scout",     mf=Steyr,     rounds=10)

Remington700 = SniperRifle(team=SWAT, name="Remington 700", mf=Remington, rounds=5)
AXMC = SniperRifle(        team=SWAT, name="AXMC",          mf=AI,        rounds=10)
MRAD = SniperRifle(        team=SWAT, name="MRAD",          mf=BF,        rounds=10)


class Shotgun(Weapon):
    def __init__(self, team, name, mf, rounds):
        super().__init__(weapon_type="Shotgun", team=team, name=name, manufacturer=mf)
        self.rounds = rounds


SPAS12 = Shotgun(     team=HECU, name="SPAS-12",      mf=Franchi,    rounds=8)
SXP = Shotgun(        team=HECU, name="SXP Defender", mf=Winchester, rounds=8)
Mossberg590 = Shotgun(team=HECU, name="590A1",        mf=Mossberg,   rounds=9)

M4Super90 = Shotgun(   team=SWAT, name="M4 Super 90",       mf=Benelli,   rounds=6)
A300Patrol = Shotgun(  team=SWAT, name="A300 Patrol",       mf=Beretta,   rounds=8)
Remington870 = Shotgun(team=SWAT, name="870 Police Magnum", mf=Remington, rounds=12)
