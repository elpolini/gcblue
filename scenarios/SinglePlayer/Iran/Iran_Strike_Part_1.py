# Created on 05/22/11 21:04:12
from math import *
from random import *
from UnitCommands import *

def CreateScenario(SM):

    SM.SetScenarioDescription("""Iran Strike Part 1\n\nSAM Strike!\n\nThis is the first scenario of a battleset focusing on an US - Iranian \nconflict. The scenarios are arranged in a chronological order.\n\nIn this first scenario your job is to plough the way for your heavy \nbombers. You are facing a dilemma: time is short but you cannot afford \nmaking mistakes.\n\n\n\n""")
    SM.SetScenarioName("""Iran Strike Part 1""")
    SM.CreateAlliance(1, 'USA')
    SM.SetAllianceDefaultCountry(1, 'USA')
    SM.SetAlliancePlayable(1, 1)
    SM.CreateAlliance(2, 'Iran')
    SM.SetAllianceDefaultCountry(2, 'Iran')
    SM.SetAlliancePlayable(2, 0)
    SM.SetUserAlliance(1)

    SM.SetDateTime(2004,10,1,10,0,0)
    SM.SetStartTheater(50.529171, 28.737503) # (lon, lat) in degrees, negative is West or South
    SM.SetScenarioLoaded(1)

    SM.SetSeaState(1)

    SM.SetSVP('0.000000,1515.000000,200.000000,1500.000000,300.000000,1510.000000,500.000000,1520.000000,5000.000000,1600.000000')

    ####################
    SM.SetSimpleBriefing(1, """ORDERS FOR CMDR US OPERATIONS\n\n\nINTELLIGENCE\n\nAfter 3 days of air strikes we have finally established an airbase near \nGanaveh.\n\nA major strike of facilities is due to begin in 180 minutes and it is critical \nthat we completely wipe out Iranian fighter cover and known SAMs prior \nto the inbound B-52 \nwave.\n\n\nMISSION\n\nSearch and Destroy SAMS and the air cover protecting them.\n\nThere are known to be 8 SAMS in the area that must be found and \ndestroyed.\n\nExpect heavy fighter cover over Iran.\n\n\n\nEXECUTION\n\nAB Ganaveh will supply most of the strike capability.\n\nThe USS Truman Carrier Battle Group is in the area to help with air \nsuperiority as well as a an additional air to ground punch.\n\nProceed with care. Expect heavy air resistance. Sub threat unknown.\n\nDo not forget your time window. You have only three hours to find and \ndestroy the SAM sites. If you fail our bombers have to withdraw.\n\n\nCOMMAND AND SIGNAL\n\nCVN Harry S. Truman\n\n\n\n\n\n\n\n\n\n\n\n\n""")

    ####################
    SM.SetSimpleBriefing(2, """TASKING ORDERS:\n\nPrevious carrier-based strikes have all but decimated our airbases.  Only Esfahan and Shiraz\nare still operational.  The infidels have established a base in Ganaveh and intelligence suspects they\nare mounting a major strike from this base assisted by an aircraft carrier in the gulf.\n\nIMMEDIATELY LAUNCH and proceed to patrol the SAM sites.  Intercept any detected enemy aircraft.\n\n""")

    ##############################
    ### Alliance 1 units
    ##############################

    unit = SM.GetDefaultUnit()
    unit.className = 'Airstrip'
    unit.unitName = "Ganaveh"
    unit.SetPosition(50.450000, 29.650000, -0.0)
    unit.heading = 0.00
    unit.speed = 0.0
    SM.AddUnitToAlliance(unit, 1)
    SM.SetUnitAlwaysVisibleState(unit.unitName, 1)
    UI = SM.GetUnitInterface(unit.unitName)
    SM.AddToUnitMagazine("Ganaveh", 'Fuel', 1000000)
    SM.AddToUnitMagazine("Ganaveh", 'Chaff-1', 10000)
    SM.AddToUnitMagazine("Ganaveh", 'Flare-1', 10000)
    SM.AddToUnitMagazine("Ganaveh", 'AIM-9M', 376)
    SM.AddToUnitMagazine("Ganaveh", 'AIM-120C', 138)
    SM.AddToUnitMagazine("Ganaveh", '20mm PGU', 100)
    SM.AddToUnitMagazine("Ganaveh", 'AGM-65D', 100)
    SM.AddToUnitMagazine("Ganaveh", '1400 liter tank', 100)
    SM.AddToUnitMagazine("Ganaveh", 'AIM-7M', 100)
    SM.AddToUnitMagazine("Ganaveh", 'Mk-82', 414)
    SM.AddToUnitMagazine("Ganaveh", 'Mk-84', 300)
    SM.AddToUnitMagazine("Ganaveh", 'Skyflash', 116)
    SM.AddToUnitMagazine("Ganaveh", 'AIM-9L', 108)
    SM.AddToUnitMagazine("Ganaveh", 'BAe Sea Eagle', 108)
    SM.AddToUnitMagazine("Ganaveh", '330 gallon wing tank', 140)
    SM.AddToUnitMagazine("Ganaveh", '594 gallon wing tank', 100)
    SM.AddToUnitMagazine("Ganaveh", 'AIM-132 ASRAAM', 92)
    SM.AddToUnitMagazine("Ganaveh", 'AS.34 Kormoran', 100)
    SM.AddToUnitMagazine("Ganaveh", 'Mk-83', 100)
    SM.AddToUnitMagazine("Ganaveh", 'Mk-81', 100)
    SM.AddToUnitMagazine("Ganaveh", 'GBU-32', 108)
    SM.AddToUnitMagazine("Ganaveh", 'GBU-31(V)1/B', 100)
    SM.AddToUnitMagazine("Ganaveh", 'GBU-27', 100)
    SM.AddToUnitMagazine("Ganaveh", 'GBU-16 Mk-83', 100)
    SM.AddToUnitMagazine("Ganaveh", 'GBU-12 Mk-82', 100)
    SM.AddToUnitMagazine("Ganaveh", 'GBU-10 Mk-84', 100)
    SM.AddToUnitMagazine("Ganaveh", 'ASPIDE-1A', 100)
    SM.AddToUnitMagazine("Ganaveh", 'AS.34 Kormoran II', 100)
    UI.SetSensorState(0, 1)
    UI.AddTask('RefuelAllAircraft', 3.000000, 3)
    BB = UI.GetBlackboardInterface()
    
    SM.AddUnitToFlightDeck('Ganaveh', 'F-16C', 'Zapper1', 3)
    SM.SetFlightDeckUnitLoadout('Ganaveh', 'Zapper1', '2 AIM-120C;2 AIM-120C;2 AIM-120C;2 1400 liter tank;6 20mm PGU;25 Flare-1;25 Chaff-1;')
    
    SM.AddUnitToFlightDeck('Ganaveh', 'F-16C', 'Zapper2', 3)
    SM.SetFlightDeckUnitLoadout('Ganaveh', 'Zapper2', '2 AIM-120C;2 AIM-120C;2 AIM-120C;2 1400 liter tank;6 20mm PGU;25 Flare-1;25 Chaff-1;')
    
    SM.AddUnitToFlightDeck('Ganaveh', 'E-2C', 'Skyeye1', 2)
    SM.SetFlightDeckUnitLoadout('Ganaveh', 'Skyeye1', '')
    
    SM.AddUnitToFlightDeck('Ganaveh', 'E-2C', 'Skyeye2', 2)
    SM.SetFlightDeckUnitLoadout('Ganaveh', 'Skyeye2', '')
    
    SM.AddUnitToFlightDeck('Ganaveh', 'E-2C', 'Skyeye3', 2)
    SM.SetFlightDeckUnitLoadout('Ganaveh', 'Skyeye3', '')
    
    SM.AddUnitToFlightDeck('Ganaveh', 'E-2C', 'Skyeye4', 2)
    SM.SetFlightDeckUnitLoadout('Ganaveh', 'Skyeye4', '')
    
    SM.AddUnitToFlightDeck('Ganaveh', 'F-16C', 'Hammer-1', 2)
    SM.SetFlightDeckUnitLoadout('Ganaveh', 'Hammer-1', '2 AIM-120C;0 Empty;0 Empty;2 1400 liter tank;6 20mm PGU;25 Flare-1;25 Chaff-1;')
    
    SM.AddUnitToFlightDeck('Ganaveh', 'F-16C', 'Hammer-2', 2)
    SM.SetFlightDeckUnitLoadout('Ganaveh', 'Hammer-2', '2 AIM-120C;0 Empty;0 Empty;2 1400 liter tank;6 20mm PGU;25 Flare-1;25 Chaff-1;')
    
    SM.AddUnitToFlightDeck('Ganaveh', 'F-16C', 'Hammer-3', 2)
    SM.SetFlightDeckUnitLoadout('Ganaveh', 'Hammer-3', '2 AIM-120C;0 Empty;0 Empty;2 1400 liter tank;6 20mm PGU;25 Flare-1;25 Chaff-1;')
    
    SM.AddUnitToFlightDeck('Ganaveh', 'F-16C', 'Hammer-4', 1)
    SM.SetFlightDeckUnitLoadout('Ganaveh', 'Hammer-4', '2 AIM-120C;0 Empty;0 Empty;2 1400 liter tank;6 20mm PGU;25 Flare-1;25 Chaff-1;')
    
    SM.AddUnitToFlightDeck('Ganaveh', 'F-16C', 'Hammer-5', 1)
    SM.SetFlightDeckUnitLoadout('Ganaveh', 'Hammer-5', '2 AIM-120C;0 Empty;0 Empty;2 1400 liter tank;6 20mm PGU;25 Flare-1;25 Chaff-1;')
    
    SM.AddUnitToFlightDeck('Ganaveh', 'F-16C', 'Hammer-6', 1)
    SM.SetFlightDeckUnitLoadout('Ganaveh', 'Hammer-6', '2 AIM-120C;0 Empty;0 Empty;2 1400 liter tank;6 20mm PGU;25 Flare-1;25 Chaff-1;')
    
    SM.AddUnitToFlightDeck('Ganaveh', 'F-16C', 'Hammer-7', 1)
    SM.SetFlightDeckUnitLoadout('Ganaveh', 'Hammer-7', '2 AIM-9M;2 AIM-9M;6 Mk-82;2 1400 liter tank;6 20mm PGU;25 Flare-1;25 Chaff-1;')
    
    SM.AddUnitToFlightDeck('Ganaveh', 'F-16C', 'Hammer-8', 1)
    SM.SetFlightDeckUnitLoadout('Ganaveh', 'Hammer-8', '2 AIM-9M;2 AIM-9M;6 Mk-82;2 1400 liter tank;6 20mm PGU;25 Flare-1;25 Chaff-1;')
    
    SM.AddUnitToFlightDeck('Ganaveh', 'F-16C', 'Hammer-9', 1)
    SM.SetFlightDeckUnitLoadout('Ganaveh', 'Hammer-9', '2 AIM-9M;2 AIM-9M;6 Mk-82;2 1400 liter tank;6 20mm PGU;25 Flare-1;25 Chaff-1;')
    
    SM.AddUnitToFlightDeck('Ganaveh', 'F-16C', 'Hammer-10', 1)
    SM.SetFlightDeckUnitLoadout('Ganaveh', 'Hammer-10', '2 AIM-120C;0 Empty;0 Empty;2 1400 liter tank;6 20mm PGU;25 Flare-1;25 Chaff-1;')
    
    SM.AddUnitToFlightDeck('Ganaveh', 'F-16C', 'Ambush-1', 1)
    SM.SetFlightDeckUnitLoadout('Ganaveh', 'Ambush-1', '2 AIM-120C;0 Empty;0 Empty;2 1400 liter tank;6 20mm PGU;25 Flare-1;25 Chaff-1;')
    
    SM.AddUnitToFlightDeck('Ganaveh', 'F-16C', 'Ambush-2', 1)
    SM.SetFlightDeckUnitLoadout('Ganaveh', 'Ambush-2', '2 AIM-120C;0 Empty;0 Empty;2 1400 liter tank;6 20mm PGU;25 Flare-1;25 Chaff-1;')
    
    SM.AddUnitToFlightDeck('Ganaveh', 'F-16C', 'Ambush-3', 1)
    SM.SetFlightDeckUnitLoadout('Ganaveh', 'Ambush-3', '2 AIM-120C;0 Empty;0 Empty;2 1400 liter tank;6 20mm PGU;25 Flare-1;25 Chaff-1;')
    
    SM.AddUnitToFlightDeck('Ganaveh', 'F-16C', 'Ambush-4', 1)
    SM.SetFlightDeckUnitLoadout('Ganaveh', 'Ambush-4', '2 AIM-120C;0 Empty;0 Empty;2 1400 liter tank;6 20mm PGU;25 Flare-1;25 Chaff-1;')
    
    SM.AddUnitToFlightDeck('Ganaveh', 'F-16C', 'Ambush-5', 1)
    SM.SetFlightDeckUnitLoadout('Ganaveh', 'Ambush-5', '2 AIM-120C;0 Empty;0 Empty;2 1400 liter tank;6 20mm PGU;25 Flare-1;25 Chaff-1;')
    
    SM.AddUnitToFlightDeck('Ganaveh', 'F-16C', 'Ambush-6', 1)
    SM.SetFlightDeckUnitLoadout('Ganaveh', 'Ambush-6', '2 AIM-120C;0 Empty;0 Empty;2 1400 liter tank;6 20mm PGU;25 Flare-1;25 Chaff-1;')
    
    SM.AddUnitToFlightDeck('Ganaveh', 'F-16C', 'Ambush-7', 1)
    SM.SetFlightDeckUnitLoadout('Ganaveh', 'Ambush-7', '2 AIM-120C;0 Empty;0 Empty;2 1400 liter tank;6 20mm PGU;25 Flare-1;25 Chaff-1;')
    
    SM.AddUnitToFlightDeck('Ganaveh', 'F-16C', 'Ambush-8', 1)
    SM.SetFlightDeckUnitLoadout('Ganaveh', 'Ambush-8', '2 AIM-120C;0 Empty;0 Empty;2 1400 liter tank;6 20mm PGU;25 Flare-1;25 Chaff-1;')
    
    SM.AddUnitToFlightDeck('Ganaveh', 'F-16C', 'Ambush-9', 1)
    SM.SetFlightDeckUnitLoadout('Ganaveh', 'Ambush-9', '2 AIM-120C;0 Empty;0 Empty;2 1400 liter tank;6 20mm PGU;25 Flare-1;25 Chaff-1;')
    
    SM.AddUnitToFlightDeck('Ganaveh', 'F-16C', 'Ambush-10', 1)
    SM.SetFlightDeckUnitLoadout('Ganaveh', 'Ambush-10', '2 AIM-120C;0 Empty;0 Empty;2 1400 liter tank;6 20mm PGU;25 Flare-1;25 Chaff-1;')
    
    SM.AddUnitToFlightDeck('Ganaveh', 'Tornado GR.Mk.1B', 'Retaliator-1', 1)
    SM.SetFlightDeckUnitLoadout('Ganaveh', 'Retaliator-1', '2 330 gallon wing tank;0 Empty;0 Empty;2 AIM-132 ASRAAM;2 AIM-120C;2 AIM-120C;')
    
    SM.AddUnitToFlightDeck('Ganaveh', 'Tornado GR.Mk.1B', 'Retaliator-2', 1)
    SM.SetFlightDeckUnitLoadout('Ganaveh', 'Retaliator-2', '2 330 gallon wing tank;0 Empty;0 Empty;2 AIM-132 ASRAAM;2 AIM-120C;2 AIM-120C;')
    
    SM.AddUnitToFlightDeck('Ganaveh', 'Tornado GR.Mk.1B', 'Retaliator-3', 1)
    SM.SetFlightDeckUnitLoadout('Ganaveh', 'Retaliator-3', '2 330 gallon wing tank;0 Empty;0 Empty;2 AIM-132 ASRAAM;2 AIM-120C;2 AIM-120C;')
    
    SM.AddUnitToFlightDeck('Ganaveh', 'Tornado GR.Mk.1B', 'Retaliator-4', 1)
    SM.SetFlightDeckUnitLoadout('Ganaveh', 'Retaliator-4', '2 330 gallon wing tank;0 Empty;0 Empty;2 AIM-132 ASRAAM;2 AIM-120C;2 AIM-120C;')
    
    SM.AddUnitToFlightDeck('Ganaveh', 'Tornado GR.Mk.4', 'Terminator-1', 2)
    SM.SetFlightDeckUnitLoadout('Ganaveh', 'Terminator-1', '0 Empty;2 GBU-32;2 GBU-32;2 AIM-9L;2 Skyflash;2 Skyflash;')
    
    SM.AddUnitToFlightDeck('Ganaveh', 'Tornado GR.Mk.4', 'Terminator-2', 1)
    SM.SetFlightDeckUnitLoadout('Ganaveh', 'Terminator-2', '0 Empty;2 GBU-32;2 GBU-32;2 AIM-9L;2 Skyflash;2 Skyflash;')
    
    SM.AddUnitToFlightDeck('Ganaveh', 'Tornado GR.Mk.4', 'Terminator-3', 1)
    SM.SetFlightDeckUnitLoadout('Ganaveh', 'Terminator-3', '0 Empty;2 GBU-32;2 GBU-32;2 AIM-9L;2 Skyflash;2 Skyflash;')
    
    SM.AddUnitToFlightDeck('Ganaveh', 'Tornado GR.Mk.4', 'Terminator-4', 1)
    SM.SetFlightDeckUnitLoadout('Ganaveh', 'Terminator-4', '0 Empty;2 GBU-32;2 GBU-32;2 AIM-9L;2 Skyflash;2 Skyflash;')
    
    SM.AddUnitToFlightDeck('Ganaveh', 'Tornado GR.Mk.4', 'Terminator-5', 1)
    SM.SetFlightDeckUnitLoadout('Ganaveh', 'Terminator-5', '0 Empty;2 GBU-32;2 GBU-32;2 AIM-9L;2 Skyflash;2 Skyflash;')
    
    SM.AddUnitToFlightDeck('Ganaveh', 'Tornado GR.Mk.4', 'Terminator-6', 1)
    SM.SetFlightDeckUnitLoadout('Ganaveh', 'Terminator-6', '0 Empty;2 GBU-32;2 GBU-32;2 AIM-9L;2 Skyflash;2 Skyflash;')
    
    SM.AddUnitToFlightDeck('Ganaveh', 'Tornado GR.Mk.4', 'Terminator-7', 1)
    SM.SetFlightDeckUnitLoadout('Ganaveh', 'Terminator-7', '0 Empty;2 GBU-32;2 GBU-32;2 AIM-9L;2 Skyflash;2 Skyflash;')
    
    SM.AddUnitToFlightDeck('Ganaveh', 'Tornado GR.Mk.4', 'Terminator-8', 1)
    SM.SetFlightDeckUnitLoadout('Ganaveh', 'Terminator-8', '0 Empty;2 GBU-32;2 GBU-32;2 AIM-9L;2 Skyflash;2 Skyflash;')
    
    SM.AddUnitToFlightDeck('Ganaveh', 'Tornado GR.Mk.4', 'Terminator-9', 1)
    SM.SetFlightDeckUnitLoadout('Ganaveh', 'Terminator-9', '0 Empty;2 GBU-32;2 GBU-32;2 AIM-9L;2 Skyflash;2 Skyflash;')
    
    SM.AddUnitToFlightDeck('Ganaveh', 'Tornado GR.Mk.4', 'Terminator-10', 1)
    SM.SetFlightDeckUnitLoadout('Ganaveh', 'Terminator-10', '0 Empty;2 GBU-32;2 GBU-32;2 AIM-9L;2 Skyflash;2 Skyflash;')
    
    SM.AddUnitToFlightDeck('Ganaveh', 'Tornado GR.Mk.4', 'Terminator-11', 1)
    SM.SetFlightDeckUnitLoadout('Ganaveh', 'Terminator-11', '0 Empty;2 GBU-32;2 GBU-32;2 AIM-9L;2 Skyflash;2 Skyflash;')
    
    SM.AddUnitToFlightDeck('Ganaveh', 'Tornado GR.Mk.4', 'Terminator-12', 1)
    SM.SetFlightDeckUnitLoadout('Ganaveh', 'Terminator-12', '0 Empty;2 GBU-32;2 GBU-32;2 AIM-9L;2 Skyflash;2 Skyflash;')
    
    SM.AddUnitToFlightDeck('Ganaveh', 'Tornado GR.Mk.4', 'Terminator-13', 1)
    SM.SetFlightDeckUnitLoadout('Ganaveh', 'Terminator-13', '0 Empty;2 GBU-32;2 GBU-32;2 AIM-9L;2 Skyflash;2 Skyflash;')
    
    SM.AddUnitToFlightDeck('Ganaveh', 'Tornado GR.Mk.4', 'Terminator-14', 1)
    SM.SetFlightDeckUnitLoadout('Ganaveh', 'Terminator-14', '0 Empty;2 GBU-32;2 GBU-32;2 AIM-9L;2 Skyflash;2 Skyflash;')
    
    SM.AddUnitToFlightDeck('Ganaveh', 'Tornado GR.Mk.4', 'Terminator-15', 1)
    SM.SetFlightDeckUnitLoadout('Ganaveh', 'Terminator-15', '0 Empty;2 GBU-32;2 GBU-32;2 AIM-9L;2 Skyflash;2 Skyflash;')
    
    SM.AddUnitToFlightDeck('Ganaveh', 'Tornado GR.Mk.4', 'Terminator-16', 1)
    SM.SetFlightDeckUnitLoadout('Ganaveh', 'Terminator-16', '0 Empty;2 GBU-32;2 GBU-32;2 AIM-9L;2 Skyflash;2 Skyflash;')
    
    SM.AddUnitToFlightDeck('Ganaveh', 'Tornado GR.Mk.4', 'Terminator-17', 1)
    SM.SetFlightDeckUnitLoadout('Ganaveh', 'Terminator-17', '0 Empty;2 GBU-32;2 GBU-32;2 AIM-9L;2 Skyflash;2 Skyflash;')
    
    SM.AddUnitToFlightDeck('Ganaveh', 'Tornado GR.Mk.4', 'Terminator-18', 1)
    SM.SetFlightDeckUnitLoadout('Ganaveh', 'Terminator-18', '0 Empty;2 GBU-32;2 GBU-32;2 AIM-9L;2 Skyflash;2 Skyflash;')
    
    SM.AddUnitToFlightDeck('Ganaveh', 'Tornado GR.Mk.4', 'Terminator-19', 1)
    SM.SetFlightDeckUnitLoadout('Ganaveh', 'Terminator-19', '0 Empty;2 GBU-32;2 GBU-32;2 AIM-9L;2 Skyflash;2 Skyflash;')
    
    SM.AddUnitToFlightDeck('Ganaveh', 'Tornado GR.Mk.4', 'Terminator-20', 1)
    SM.SetFlightDeckUnitLoadout('Ganaveh', 'Terminator-20', '0 Empty;2 GBU-32;2 GBU-32;2 AIM-9L;2 Skyflash;2 Skyflash;')
    
    unit = SM.GetDefaultUnit()
    unit.className = 'Nimitz CVN-68 USS Nimitz(RCOH)'
    unit.unitName = "USS Nimitz"
    unit.SetPosition(50.220039, 28.964794, 0.0)
    unit.heading = 90.00
    unit.speed = 3.0
    SM.AddUnitToAlliance(unit, 1)
    SM.SetUnitLauncherItem(unit.unitName, 0, 'RIM-7P(v1)', 8)
    SM.SetUnitLauncherItem(unit.unitName, 1, 'RIM-7P(v1)', 8)
    SM.SetUnitLauncherItem(unit.unitName, 2, 'RIM-116A RAM', 21)
    SM.SetUnitLauncherItem(unit.unitName, 3, 'RIM-116A RAM', 21)
    UI = SM.GetUnitInterface(unit.unitName)
    SM.AddToUnitMagazine("USS Nimitz", 'Fuel', 10600000)
    SM.AddToUnitMagazine("USS Nimitz", 'AIM-9M', 415)
    SM.AddToUnitMagazine("USS Nimitz", 'AIM-9X', 7)
    SM.AddToUnitMagazine("USS Nimitz", 'AIM-7P', 218)
    SM.AddToUnitMagazine("USS Nimitz", 'AIM-120C5', 523)
    SM.AddToUnitMagazine("USS Nimitz", 'AGM-88C', 404)
    SM.AddToUnitMagazine("USS Nimitz", 'AGM-84F Harpoon', 249)
    SM.AddToUnitMagazine("USS Nimitz", 'AGM-65F', 902)
    SM.AddToUnitMagazine("USS Nimitz", 'AGM-114 Hellfire', 25)
    SM.AddToUnitMagazine("USS Nimitz", 'AGM-119B', 16)
    SM.AddToUnitMagazine("USS Nimitz", 'Mk-46 Mod5', 153)
    SM.AddToUnitMagazine("USS Nimitz", 'Mk-50', 22)
    SM.AddToUnitMagazine("USS Nimitz", 'Mk-54', 22)
    SM.AddToUnitMagazine("USS Nimitz", 'Mk-82', 1169)
    SM.AddToUnitMagazine("USS Nimitz", 'Mk-83', 909)
    SM.AddToUnitMagazine("USS Nimitz", 'Mk-84', 454)
    SM.AddToUnitMagazine("USS Nimitz", 'GBU-31C(v)4', 194)
    SM.AddToUnitMagazine("USS Nimitz", 'GBU-32A(v)2', 259)
    SM.AddToUnitMagazine("USS Nimitz", 'GBU-32B(v)2', 292)
    SM.AddToUnitMagazine("USS Nimitz", 'GBU-32C(v)4', 309)
    SM.AddToUnitMagazine("USS Nimitz", 'B-83 50kT', 28)
    SM.AddToUnitMagazine("USS Nimitz", 'B-83 200kT', 21)
    SM.AddToUnitMagazine("USS Nimitz", 'B-83 800kT', 15)
    SM.AddToUnitMagazine("USS Nimitz", '1400 liter tank', 0)
    SM.AddToUnitMagazine("USS Nimitz", 'FPU-6', 4)
    SM.AddToUnitMagazine("USS Nimitz", '120 gallon tank', 6)
    SM.AddToUnitMagazine("USS Nimitz", '20mm PGU', 2311)
    SM.AddToUnitMagazine("USS Nimitz", 'Chaff-1', 2459)
    SM.AddToUnitMagazine("USS Nimitz", 'Flare-1', 2459)
    SM.AddToUnitMagazine("USS Nimitz", 'LOFAR (100) Sonobuoy', 482)
    SM.AddToUnitMagazine("USS Nimitz", 'DICASS (100) Sonobuoy', 452)
    SM.AddToUnitMagazine("USS Nimitz", 'DIFAR (100) Sonobuoy', 1388)
    SM.AddToUnitMagazine("USS Nimitz", 'RIM-7P(v1)', 48)
    SM.AddToUnitMagazine("USS Nimitz", 'RIM-116A RAM', 168)
    UI.AddTask('MissileWarning', 3.000000, 3)
    UI.AddTask('RefuelAllAircraft', 3.000000, 3)
    BB = UI.GetBlackboardInterface()
    
    SM.AddUnitToFlightDeck('USS Nimitz', 'F/A-18F', 'Fast Eagle 1', 1)
    SM.SetFlightDeckUnitLoadout('USS Nimitz', 'Fast Eagle 1', '1 1400 liter tank;2 AIM-120C5;2 GBU-32C(v)4;2 GBU-32C(v)4;4 AGM-65F;2 AIM-9X;6 20mm PGU;30 Chaff-1;30 Chaff-1;')
    
    SM.AddUnitToFlightDeck('USS Nimitz', 'F/A-18F', 'Fast Eagle 2', 1)
    SM.SetFlightDeckUnitLoadout('USS Nimitz', 'Fast Eagle 2', '1 1400 liter tank;2 AIM-120C5;2 GBU-32C(v)4;2 GBU-32C(v)4;4 AGM-65F;2 AIM-9X;6 20mm PGU;30 Chaff-1;30 Chaff-1;')
    
    SM.AddUnitToFlightDeck('USS Nimitz', 'F/A-18F', 'Fast Eagle 3', 1)
    SM.SetFlightDeckUnitLoadout('USS Nimitz', 'Fast Eagle 3', '1 1400 liter tank;2 AIM-120C5;2 GBU-32C(v)4;2 GBU-32C(v)4;4 AGM-65F;2 AIM-9X;6 20mm PGU;30 Chaff-1;30 Chaff-1;')
    
    SM.AddUnitToFlightDeck('USS Nimitz', 'F/A-18F', 'Fast Eagle 4', 1)
    SM.SetFlightDeckUnitLoadout('USS Nimitz', 'Fast Eagle 4', '1 1400 liter tank;2 AIM-120C5;2 GBU-32C(v)4;2 GBU-32C(v)4;4 AGM-65F;2 AIM-9X;6 20mm PGU;30 Chaff-1;30 Chaff-1;')
    
    SM.AddUnitToFlightDeck('USS Nimitz', 'F/A-18F', 'Fast Eagle 5', 1)
    SM.SetFlightDeckUnitLoadout('USS Nimitz', 'Fast Eagle 5', '1 1400 liter tank;2 AIM-120C5;2 GBU-32C(v)4;2 GBU-32C(v)4;4 AGM-65F;2 AIM-9X;6 20mm PGU;30 Chaff-1;30 Chaff-1;')
    
    SM.AddUnitToFlightDeck('USS Nimitz', 'F/A-18F', 'Fast Eagle 6', 1)
    SM.SetFlightDeckUnitLoadout('USS Nimitz', 'Fast Eagle 6', '1 1400 liter tank;2 AIM-120C5;2 GBU-32C(v)4;2 GBU-32C(v)4;4 AGM-65F;2 AIM-9X;6 20mm PGU;30 Chaff-1;30 Chaff-1;')
    
    SM.AddUnitToFlightDeck('USS Nimitz', 'F/A-18F', 'Fast Eagle 7', 1)
    SM.SetFlightDeckUnitLoadout('USS Nimitz', 'Fast Eagle 7', '1 1400 liter tank;2 AIM-120C5;2 GBU-32C(v)4;2 GBU-32C(v)4;4 AGM-65F;2 AIM-9X;6 20mm PGU;30 Chaff-1;30 Chaff-1;')
    
    SM.AddUnitToFlightDeck('USS Nimitz', 'F/A-18F', 'Fast Eagle 8', 1)
    SM.SetFlightDeckUnitLoadout('USS Nimitz', 'Fast Eagle 8', '1 1400 liter tank;2 AIM-120C5;2 GBU-32C(v)4;2 GBU-32C(v)4;4 AGM-65F;2 AIM-9X;6 20mm PGU;30 Chaff-1;30 Chaff-1;')
    
    SM.AddUnitToFlightDeck('USS Nimitz', 'F/A-18F', 'Fast Eagle 9', 1)
    SM.SetFlightDeckUnitLoadout('USS Nimitz', 'Fast Eagle 9', '1 1400 liter tank;2 AIM-120C5;2 GBU-32C(v)4;2 GBU-32C(v)4;4 AGM-65F;2 AIM-9X;6 20mm PGU;30 Chaff-1;30 Chaff-1;')
    
    SM.AddUnitToFlightDeck('USS Nimitz', 'F/A-18F', 'Fast Eagle 10', 1)
    SM.SetFlightDeckUnitLoadout('USS Nimitz', 'Fast Eagle 10', '1 1400 liter tank;2 AIM-120C5;2 GBU-32C(v)4;2 GBU-32C(v)4;4 AGM-65F;2 AIM-9X;6 20mm PGU;30 Chaff-1;30 Chaff-1;')
    
    SM.AddUnitToFlightDeck('USS Nimitz', 'F/A-18F', 'Fast Eagle 11', 1)
    SM.SetFlightDeckUnitLoadout('USS Nimitz', 'Fast Eagle 11', '1 1400 liter tank;2 AIM-120C5;2 GBU-32C(v)4;2 GBU-32C(v)4;4 AGM-65F;2 AIM-9X;6 20mm PGU;30 Chaff-1;30 Chaff-1;')
    
    SM.AddUnitToFlightDeck('USS Nimitz', 'F/A-18F', 'Fast Eagle 12', 1)
    SM.SetFlightDeckUnitLoadout('USS Nimitz', 'Fast Eagle 12', '1 1400 liter tank;2 AIM-120C5;2 GBU-32C(v)4;2 GBU-32C(v)4;4 AGM-65F;2 AIM-9X;6 20mm PGU;30 Chaff-1;30 Chaff-1;')
    
    SM.AddUnitToFlightDeck('USS Nimitz', 'F/A-18E', 'Camelot 1', 1)
    SM.SetFlightDeckUnitLoadout('USS Nimitz', 'Camelot 1', '1 1400 liter tank;2 AIM-120C5;2 FPU-6;2 AGM-84F Harpoon;2 AGM-84F Harpoon;2 AIM-9X;6 20mm PGU;30 Chaff-1;30 Chaff-1;')
    
    SM.AddUnitToFlightDeck('USS Nimitz', 'F/A-18E', 'Camelot 2', 1)
    SM.SetFlightDeckUnitLoadout('USS Nimitz', 'Camelot 2', '1 1400 liter tank;2 AIM-120C5;2 FPU-6;2 AGM-84F Harpoon;2 AGM-84F Harpoon;2 AIM-9X;6 20mm PGU;30 Chaff-1;30 Chaff-1;')
    
    SM.AddUnitToFlightDeck('USS Nimitz', 'F/A-18E', 'Camelot 3', 1)
    SM.SetFlightDeckUnitLoadout('USS Nimitz', 'Camelot 3', '1 1400 liter tank;2 AIM-120C5;2 FPU-6;2 AGM-84F Harpoon;2 AGM-84F Harpoon;2 AIM-9X;6 20mm PGU;30 Chaff-1;30 Chaff-1;')
    
    SM.AddUnitToFlightDeck('USS Nimitz', 'F/A-18E', 'Camelot 4', 1)
    SM.SetFlightDeckUnitLoadout('USS Nimitz', 'Camelot 4', '1 1400 liter tank;2 AIM-120C5;2 FPU-6;2 AGM-84F Harpoon;2 AGM-84F Harpoon;2 AIM-9X;6 20mm PGU;30 Chaff-1;30 Chaff-1;')
    
    SM.AddUnitToFlightDeck('USS Nimitz', 'F/A-18E', 'Camelot 5', 1)
    SM.SetFlightDeckUnitLoadout('USS Nimitz', 'Camelot 5', '1 1400 liter tank;2 AIM-120C5;2 FPU-6;2 AGM-84F Harpoon;2 AGM-84F Harpoon;2 AIM-9X;6 20mm PGU;30 Chaff-1;30 Chaff-1;')
    
    SM.AddUnitToFlightDeck('USS Nimitz', 'F/A-18E', 'Camelot 6', 1)
    SM.SetFlightDeckUnitLoadout('USS Nimitz', 'Camelot 6', '1 1400 liter tank;2 AIM-120C5;2 FPU-6;2 AGM-84F Harpoon;2 AGM-84F Harpoon;2 AIM-9X;6 20mm PGU;30 Chaff-1;30 Chaff-1;')
    
    SM.AddUnitToFlightDeck('USS Nimitz', 'F/A-18E', 'Camelot 7', 1)
    SM.SetFlightDeckUnitLoadout('USS Nimitz', 'Camelot 7', '1 1400 liter tank;2 AIM-120C5;2 FPU-6;2 AGM-84F Harpoon;2 AGM-84F Harpoon;2 AIM-9X;6 20mm PGU;30 Chaff-1;30 Chaff-1;')
    
    SM.AddUnitToFlightDeck('USS Nimitz', 'F/A-18E', 'Camelot 8', 1)
    SM.SetFlightDeckUnitLoadout('USS Nimitz', 'Camelot 8', '1 1400 liter tank;2 AIM-120C5;2 FPU-6;2 AGM-84F Harpoon;2 AGM-84F Harpoon;2 AIM-9X;6 20mm PGU;30 Chaff-1;30 Chaff-1;')
    
    SM.AddUnitToFlightDeck('USS Nimitz', 'F/A-18E', 'Camelot 9', 1)
    SM.SetFlightDeckUnitLoadout('USS Nimitz', 'Camelot 9', '1 1400 liter tank;2 AIM-120C5;2 FPU-6;2 AGM-84F Harpoon;2 AGM-84F Harpoon;2 AIM-9X;6 20mm PGU;30 Chaff-1;30 Chaff-1;')
    
    SM.AddUnitToFlightDeck('USS Nimitz', 'F/A-18E', 'Camelot 10', 1)
    SM.SetFlightDeckUnitLoadout('USS Nimitz', 'Camelot 10', '1 1400 liter tank;2 AIM-120C5;2 FPU-6;2 AGM-84F Harpoon;2 AGM-84F Harpoon;2 AIM-9X;6 20mm PGU;30 Chaff-1;30 Chaff-1;')
    
    SM.AddUnitToFlightDeck('USS Nimitz', 'F/A-18E', 'Camelot 11', 1)
    SM.SetFlightDeckUnitLoadout('USS Nimitz', 'Camelot 11', '1 1400 liter tank;2 AIM-120C5;2 FPU-6;2 AGM-84F Harpoon;2 AGM-84F Harpoon;2 AIM-9X;6 20mm PGU;30 Chaff-1;30 Chaff-1;')
    
    SM.AddUnitToFlightDeck('USS Nimitz', 'F/A-18E', 'Camelot 12', 1)
    SM.SetFlightDeckUnitLoadout('USS Nimitz', 'Camelot 12', '1 1400 liter tank;2 AIM-120C5;2 FPU-6;2 AGM-84F Harpoon;2 AGM-84F Harpoon;2 AIM-9X;6 20mm PGU;30 Chaff-1;30 Chaff-1;')
    
    SM.AddUnitToFlightDeck('USS Nimitz', 'F/A-18A', 'Warhawk 1', 1)
    SM.SetFlightDeckUnitLoadout('USS Nimitz', 'Warhawk 1', '1 1400 liter tank;2 AIM-7P;2 FPU-6;2 AIM-7P;2 AIM-9X;6 20mm PGU;30 Chaff-1;30 Flare-1;')
    
    SM.AddUnitToFlightDeck('USS Nimitz', 'F/A-18A', 'Warhawk 2', 1)
    SM.SetFlightDeckUnitLoadout('USS Nimitz', 'Warhawk 2', '1 1400 liter tank;2 AIM-7P;2 FPU-6;2 AIM-7P;2 AIM-9X;6 20mm PGU;30 Chaff-1;30 Flare-1;')
    
    SM.AddUnitToFlightDeck('USS Nimitz', 'F/A-18A', 'Warhawk 3', 1)
    SM.SetFlightDeckUnitLoadout('USS Nimitz', 'Warhawk 3', '1 1400 liter tank;2 AIM-7P;2 FPU-6;2 AIM-7P;2 AIM-9X;6 20mm PGU;30 Chaff-1;30 Flare-1;')
    
    SM.AddUnitToFlightDeck('USS Nimitz', 'F/A-18A', 'Warhawk 4', 1)
    SM.SetFlightDeckUnitLoadout('USS Nimitz', 'Warhawk 4', '1 1400 liter tank;2 AIM-7P;2 FPU-6;2 AIM-7P;2 AIM-9X;6 20mm PGU;30 Chaff-1;30 Flare-1;')
    
    SM.AddUnitToFlightDeck('USS Nimitz', 'F/A-18A', 'Warhawk 5', 1)
    SM.SetFlightDeckUnitLoadout('USS Nimitz', 'Warhawk 5', '1 1400 liter tank;2 AIM-7P;2 FPU-6;2 AIM-7P;2 AIM-9X;6 20mm PGU;30 Chaff-1;30 Flare-1;')
    
    SM.AddUnitToFlightDeck('USS Nimitz', 'F/A-18A', 'Warhawk 6', 1)
    SM.SetFlightDeckUnitLoadout('USS Nimitz', 'Warhawk 6', '1 1400 liter tank;2 AIM-7P;2 FPU-6;2 AIM-7P;2 AIM-9X;6 20mm PGU;30 Chaff-1;30 Flare-1;')
    
    SM.AddUnitToFlightDeck('USS Nimitz', 'F/A-18A', 'Warhawk 7', 1)
    SM.SetFlightDeckUnitLoadout('USS Nimitz', 'Warhawk 7', '1 1400 liter tank;2 AIM-7P;2 FPU-6;2 AIM-7P;2 AIM-9X;6 20mm PGU;30 Chaff-1;30 Flare-1;')
    
    SM.AddUnitToFlightDeck('USS Nimitz', 'F/A-18A', 'Warhawk 8', 1)
    SM.SetFlightDeckUnitLoadout('USS Nimitz', 'Warhawk 8', '1 1400 liter tank;2 AIM-7P;2 FPU-6;2 AIM-7P;2 AIM-9X;6 20mm PGU;30 Chaff-1;30 Flare-1;')
    
    SM.AddUnitToFlightDeck('USS Nimitz', 'F/A-18A', 'Warhawk 9', 1)
    SM.SetFlightDeckUnitLoadout('USS Nimitz', 'Warhawk 9', '1 1400 liter tank;2 AIM-7P;2 FPU-6;2 AIM-7P;2 AIM-9X;6 20mm PGU;30 Chaff-1;30 Flare-1;')
    
    SM.AddUnitToFlightDeck('USS Nimitz', 'F/A-18A', 'Warhawk 10', 1)
    SM.SetFlightDeckUnitLoadout('USS Nimitz', 'Warhawk 10', '1 1400 liter tank;2 AIM-7P;2 FPU-6;2 AIM-7P;2 AIM-9X;6 20mm PGU;30 Chaff-1;30 Flare-1;')
    
    SM.AddUnitToFlightDeck('USS Nimitz', 'F/A-18A', 'Warhawk 11', 1)
    SM.SetFlightDeckUnitLoadout('USS Nimitz', 'Warhawk 11', '1 1400 liter tank;2 AIM-7P;2 FPU-6;2 AIM-7P;2 AIM-9X;6 20mm PGU;30 Chaff-1;30 Flare-1;')
    
    SM.AddUnitToFlightDeck('USS Nimitz', 'F/A-18A', 'Warhawk 12', 1)
    SM.SetFlightDeckUnitLoadout('USS Nimitz', 'Warhawk 12', '1 1400 liter tank;2 AIM-7P;2 FPU-6;2 AIM-7P;2 AIM-9X;6 20mm PGU;30 Chaff-1;30 Flare-1;')
    
    SM.AddUnitToFlightDeck('USS Nimitz', 'F/A-18C', 'Hobo 1', 1)
    SM.SetFlightDeckUnitLoadout('USS Nimitz', 'Hobo 1', '1 1400 liter tank;2 AIM-120C5;2 AIM-120C5;2 AIM-120C5;2 AIM-9X;6 20mm PGU;30 Chaff-1;30 Flare-1;')
    
    SM.AddUnitToFlightDeck('USS Nimitz', 'F/A-18C', 'Hobo 2', 1)
    SM.SetFlightDeckUnitLoadout('USS Nimitz', 'Hobo 2', '1 1400 liter tank;2 AIM-120C5;2 AIM-120C5;2 AIM-120C5;2 AIM-9X;6 20mm PGU;30 Chaff-1;30 Flare-1;')
    
    SM.AddUnitToFlightDeck('USS Nimitz', 'F/A-18C', 'Hobo 3', 1)
    SM.SetFlightDeckUnitLoadout('USS Nimitz', 'Hobo 3', '1 1400 liter tank;2 AIM-120C5;2 AIM-120C5;2 AIM-120C5;2 AIM-9X;6 20mm PGU;30 Chaff-1;30 Flare-1;')
    
    SM.AddUnitToFlightDeck('USS Nimitz', 'F/A-18C', 'Hobo 4', 1)
    SM.SetFlightDeckUnitLoadout('USS Nimitz', 'Hobo 4', '1 1400 liter tank;2 AIM-120C5;2 AIM-120C5;2 AIM-120C5;2 AIM-9X;6 20mm PGU;30 Chaff-1;30 Flare-1;')
    
    SM.AddUnitToFlightDeck('USS Nimitz', 'F/A-18C', 'Hobo 5', 1)
    SM.SetFlightDeckUnitLoadout('USS Nimitz', 'Hobo 5', '1 1400 liter tank;2 AIM-120C5;2 AIM-120C5;2 AIM-120C5;2 AIM-9X;6 20mm PGU;30 Chaff-1;30 Flare-1;')
    
    SM.AddUnitToFlightDeck('USS Nimitz', 'F/A-18C', 'Hobo 6', 1)
    SM.SetFlightDeckUnitLoadout('USS Nimitz', 'Hobo 6', '1 1400 liter tank;2 AIM-120C5;2 AIM-120C5;2 AIM-120C5;2 AIM-9X;6 20mm PGU;30 Chaff-1;30 Flare-1;')
    
    SM.AddUnitToFlightDeck('USS Nimitz', 'F/A-18C', 'Hobo 7', 1)
    SM.SetFlightDeckUnitLoadout('USS Nimitz', 'Hobo 7', '1 1400 liter tank;2 AIM-120C5;2 AIM-120C5;2 AIM-120C5;2 AIM-9X;6 20mm PGU;30 Chaff-1;30 Flare-1;')
    
    SM.AddUnitToFlightDeck('USS Nimitz', 'F/A-18C', 'Hobo 8', 1)
    SM.SetFlightDeckUnitLoadout('USS Nimitz', 'Hobo 8', '1 1400 liter tank;2 AIM-120C5;2 AIM-120C5;2 AIM-120C5;2 AIM-9X;6 20mm PGU;30 Chaff-1;30 Flare-1;')
    
    SM.AddUnitToFlightDeck('USS Nimitz', 'F/A-18C', 'Hobo 9', 1)
    SM.SetFlightDeckUnitLoadout('USS Nimitz', 'Hobo 9', '1 1400 liter tank;2 AIM-120C5;2 AIM-120C5;2 AIM-120C5;2 AIM-9X;6 20mm PGU;30 Chaff-1;30 Flare-1;')
    
    SM.AddUnitToFlightDeck('USS Nimitz', 'F/A-18C', 'Hobo 10', 1)
    SM.SetFlightDeckUnitLoadout('USS Nimitz', 'Hobo 10', '1 1400 liter tank;2 AIM-120C5;2 AIM-120C5;2 AIM-120C5;2 AIM-9X;6 20mm PGU;30 Chaff-1;30 Flare-1;')
    
    SM.AddUnitToFlightDeck('USS Nimitz', 'F/A-18C', 'Hobo 11', 1)
    SM.SetFlightDeckUnitLoadout('USS Nimitz', 'Hobo 11', '1 1400 liter tank;2 AIM-120C5;2 AIM-120C5;2 AIM-120C5;2 AIM-9X;6 20mm PGU;30 Chaff-1;30 Flare-1;')
    
    SM.AddUnitToFlightDeck('USS Nimitz', 'F/A-18C', 'Hobo 12', 1)
    SM.SetFlightDeckUnitLoadout('USS Nimitz', 'Hobo 12', '1 1400 liter tank;2 AIM-120C5;2 AIM-120C5;2 AIM-120C5;2 AIM-9X;6 20mm PGU;30 Chaff-1;30 Flare-1;')
    
    SM.AddUnitToFlightDeck('USS Nimitz', 'EA-6B', 'Black Ravens 1', 1)
    SM.SetFlightDeckUnitLoadout('USS Nimitz', 'Black Ravens 1', '2 AGM-88C;2 FPU-6;')
    
    SM.AddUnitToFlightDeck('USS Nimitz', 'EA-6B', 'Black Ravens 2', 1)
    SM.SetFlightDeckUnitLoadout('USS Nimitz', 'Black Ravens 2', '2 AGM-88C;2 FPU-6;')
    
    SM.AddUnitToFlightDeck('USS Nimitz', 'EA-6B', 'Black Ravens 3', 1)
    SM.SetFlightDeckUnitLoadout('USS Nimitz', 'Black Ravens 3', '2 AGM-88C;2 FPU-6;')
    
    SM.AddUnitToFlightDeck('USS Nimitz', 'EA-6B', 'Black Ravens 4', 1)
    SM.SetFlightDeckUnitLoadout('USS Nimitz', 'Black Ravens 4', '2 AGM-88C;2 AGM-88C;')
    
    SM.AddUnitToFlightDeck('USS Nimitz', 'EA-6B', 'Black Ravens 5', 1)
    SM.SetFlightDeckUnitLoadout('USS Nimitz', 'Black Ravens 5', '2 AGM-88C;2 AGM-88C;')
    
    SM.AddUnitToFlightDeck('USS Nimitz', 'EA-6B', 'Black Ravens 6', 1)
    SM.SetFlightDeckUnitLoadout('USS Nimitz', 'Black Ravens 6', '2 AGM-88C;2 AGM-88C;')
    
    SM.AddUnitToFlightDeck('USS Nimitz', 'E-2C 2000 NP', 'Wallbangers 1', 1)
    SM.SetFlightDeckUnitLoadout('USS Nimitz', 'Wallbangers 1', '')
    
    SM.AddUnitToFlightDeck('USS Nimitz', 'E-2C 2000 NP', 'Wallbangers 2', 1)
    SM.SetFlightDeckUnitLoadout('USS Nimitz', 'Wallbangers 2', '')
    
    SM.AddUnitToFlightDeck('USS Nimitz', 'E-2C 2000 NP', 'Wallbangers 3', 1)
    SM.SetFlightDeckUnitLoadout('USS Nimitz', 'Wallbangers 3', '')
    
    SM.AddUnitToFlightDeck('USS Nimitz', 'E-2C 2000 NP', 'Wallbangers 4', 1)
    SM.SetFlightDeckUnitLoadout('USS Nimitz', 'Wallbangers 4', '')
    
    SM.AddUnitToFlightDeck('USS Nimitz', 'S-3B', 'Dragon Fires 1', 1)
    SM.SetFlightDeckUnitLoadout('USS Nimitz', 'Dragon Fires 1', '12 DICASS (100) Sonobuoy;12 LOFAR (100) Sonobuoy;36 DIFAR (100) Sonobuoy;2 Mk-46 Mod5;2 Mk-46 Mod5;3 AGM-65F;3 AGM-65F;')
    
    SM.AddUnitToFlightDeck('USS Nimitz', 'S-3B', 'Dragon Fires 2', 1)
    SM.SetFlightDeckUnitLoadout('USS Nimitz', 'Dragon Fires 2', '12 DICASS (100) Sonobuoy;12 LOFAR (100) Sonobuoy;36 DIFAR (100) Sonobuoy;2 Mk-46 Mod5;2 Mk-46 Mod5;3 AGM-65F;3 AGM-65F;')
    
    SM.AddUnitToFlightDeck('USS Nimitz', 'S-3B', 'Dragon Fires 3', 1)
    SM.SetFlightDeckUnitLoadout('USS Nimitz', 'Dragon Fires 3', '12 DICASS (100) Sonobuoy;12 LOFAR (100) Sonobuoy;36 DIFAR (100) Sonobuoy;2 Mk-46 Mod5;2 Mk-46 Mod5;3 AGM-65F;3 AGM-65F;')
    
    SM.AddUnitToFlightDeck('USS Nimitz', 'S-3B', 'Dragon Fires 4', 1)
    SM.SetFlightDeckUnitLoadout('USS Nimitz', 'Dragon Fires 4', '12 DICASS (100) Sonobuoy;12 LOFAR (100) Sonobuoy;36 DIFAR (100) Sonobuoy;2 Mk-46 Mod5;2 Mk-46 Mod5;3 AGM-65F;3 AGM-65F;')
    
    SM.AddUnitToFlightDeck('USS Nimitz', 'S-3B', 'Dragon Fires 5', 1)
    SM.SetFlightDeckUnitLoadout('USS Nimitz', 'Dragon Fires 5', '12 DICASS (100) Sonobuoy;12 LOFAR (100) Sonobuoy;36 DIFAR (100) Sonobuoy;2 Mk-46 Mod5;2 Mk-46 Mod5;3 AGM-65F;3 AGM-65F;')
    
    SM.AddUnitToFlightDeck('USS Nimitz', 'S-3B', 'Dragon Fires 6', 1)
    SM.SetFlightDeckUnitLoadout('USS Nimitz', 'Dragon Fires 6', '12 DICASS (100) Sonobuoy;12 LOFAR (100) Sonobuoy;36 DIFAR (100) Sonobuoy;2 Mk-54;2 Mk-54;1 AGM-84F Harpoon;3 AGM-84F Harpoon;')
    
    SM.AddUnitToFlightDeck('USS Nimitz', 'KS-3B', 'Dragon Fires 7', 1)
    SM.SetFlightDeckUnitLoadout('USS Nimitz', 'Dragon Fires 7', '')
    
    SM.AddUnitToFlightDeck('USS Nimitz', 'KS-3B', 'Dragon Fires 8', 1)
    SM.SetFlightDeckUnitLoadout('USS Nimitz', 'Dragon Fires 8', '')
    
    SM.AddUnitToFlightDeck('USS Nimitz', 'SH-60F', 'Indians 1', 1)
    SM.SetFlightDeckUnitLoadout('USS Nimitz', 'Indians 1', '1 Mk-46 Mod5;1 120 gallon tank;1 Mk-46 Mod5;30 Flare-1;30 Chaff-1;5 DICASS (100) Sonobuoy;10 DIFAR (100) Sonobuoy;')
    
    SM.AddUnitToFlightDeck('USS Nimitz', 'SH-60F', 'Indians 2', 1)
    SM.SetFlightDeckUnitLoadout('USS Nimitz', 'Indians 2', '1 Mk-46 Mod5;1 120 gallon tank;1 Mk-46 Mod5;30 Flare-1;30 Chaff-1;5 DICASS (100) Sonobuoy;10 DIFAR (100) Sonobuoy;')
    
    SM.AddUnitToFlightDeck('USS Nimitz', 'SH-60F', 'Indians 3', 1)
    SM.SetFlightDeckUnitLoadout('USS Nimitz', 'Indians 3', '1 Mk-46 Mod5;1 120 gallon tank;1 Mk-46 Mod5;30 Flare-1;30 Chaff-1;5 DICASS (100) Sonobuoy;10 DIFAR (100) Sonobuoy;')
    
    SM.AddUnitToFlightDeck('USS Nimitz', 'SH-60F', 'Indians 4', 1)
    SM.SetFlightDeckUnitLoadout('USS Nimitz', 'Indians 4', '1 Mk-46 Mod5;1 120 gallon tank;1 Mk-46 Mod5;30 Flare-1;30 Chaff-1;5 DICASS (100) Sonobuoy;10 DIFAR (100) Sonobuoy;')
    
    SM.AddUnitToFlightDeck('USS Nimitz', 'SH-60F', 'Indians 5', 1)
    SM.SetFlightDeckUnitLoadout('USS Nimitz', 'Indians 5', '1 Mk-46 Mod5;1 120 gallon tank;1 Mk-46 Mod5;30 Flare-1;30 Chaff-1;5 DICASS (100) Sonobuoy;10 DIFAR (100) Sonobuoy;')
    
    SM.AddUnitToFlightDeck('USS Nimitz', 'SH-60F', 'Indians 6', 1)
    SM.SetFlightDeckUnitLoadout('USS Nimitz', 'Indians 6', '1 Mk-46 Mod5;1 120 gallon tank;1 Mk-46 Mod5;30 Flare-1;30 Chaff-1;5 DICASS (100) Sonobuoy;10 DIFAR (100) Sonobuoy;')
    
    SM.AddUnitToFlightDeck('USS Nimitz', 'C-2A', 'Password 1', 1)
    SM.SetFlightDeckUnitLoadout('USS Nimitz', 'Password 1', '')
    
    SM.AddUnitToFlightDeck('USS Nimitz', 'C-2A', 'Password 2', 1)
    SM.SetFlightDeckUnitLoadout('USS Nimitz', 'Password 2', '')
    
    SM.AddUnitToFlightDeck('USS Nimitz', 'SH-60B', 'Sabrehawks 1', 1)
    SM.SetFlightDeckUnitLoadout('USS Nimitz', 'Sabrehawks 1', '4 AGM-114 Hellfire;1 120 gallon tank;1 120 gallon tank;25 Chaff-1;25 Chaff-1;5 DICASS (100) Sonobuoy;5 DICASS (100) Sonobuoy;15 DICASS (100) Sonobuoy;')
    
    SM.AddUnitToFlightDeck('USS Nimitz', 'SH-60B', 'Sabrehawks 2', 1)
    SM.SetFlightDeckUnitLoadout('USS Nimitz', 'Sabrehawks 2', '4 AGM-114 Hellfire;1 120 gallon tank;1 120 gallon tank;25 Chaff-1;25 Chaff-1;5 DICASS (100) Sonobuoy;5 DICASS (100) Sonobuoy;15 DICASS (100) Sonobuoy;')
    
    unit = SM.GetDefaultUnit()
    unit.className = 'Spruance DDG VLS 93'
    unit.unitName = "USS Paul F. Foster"
    UI = SM.GetUnitInterface('USS Nimitz')
    leader_track = UI.GetTrackById(UI.GetPlatformId())
    lon_deg = 57.296*leader_track.Lon + -0.0804
    lat_deg = 57.296*leader_track.Lat + -0.1076
    unit.SetPosition(lon_deg, lat_deg, 0.0)
    unit.heading = 90.00
    unit.speed = 3.0
    SM.AddUnitToAlliance(unit, 1)
    SM.SetUnitLauncherItem(unit.unitName, 0, 'RUM-139 Mod4 ASROC', 1)
    SM.SetUnitLauncherItem(unit.unitName, 1, 'BGM-109 TASM', 1)
    SM.SetUnitLauncherItem(unit.unitName, 2, 'BGM-109 TLAM', 1)
    SM.SetUnitLauncherItem(unit.unitName, 3, 'RIM-7P(v1)', 8)
    SM.SetUnitLauncherItem(unit.unitName, 4, '127mm mk 80 HE-PD mk 67', 20)
    SM.SetUnitLauncherItem(unit.unitName, 5, '127mm mk 80 HE-PD mk 67', 20)
    SM.SetUnitLauncherItem(unit.unitName, 6, '20mm mark 244-0 ELC', 97)
    SM.SetUnitLauncherItem(unit.unitName, 7, '20mm mark 244-0 ELC', 97)
    SM.SetUnitLauncherItem(unit.unitName, 8, 'RGM-84F Harpoon', 4)
    SM.SetUnitLauncherItem(unit.unitName, 9, 'RGM-84F Harpoon', 4)
    SM.SetUnitLauncherItem(unit.unitName, 10, 'RIM-116A RAM', 21)
    UI = SM.GetUnitInterface(unit.unitName)
    SM.AddToUnitMagazine("USS Paul F. Foster", 'Fuel', 65176)
    SM.AddToUnitMagazine("USS Paul F. Foster", 'Mk-46 Mod5', 23)
    SM.AddToUnitMagazine("USS Paul F. Foster", 'Mk-50', 2)
    SM.AddToUnitMagazine("USS Paul F. Foster", '120 gallon tank', 4)
    SM.AddToUnitMagazine("USS Paul F. Foster", 'AGM-114 Hellfire', 16)
    SM.AddToUnitMagazine("USS Paul F. Foster", 'AGM-119B', 4)
    SM.AddToUnitMagazine("USS Paul F. Foster", 'LOFAR (100) Sonobuoy', 263)
    SM.AddToUnitMagazine("USS Paul F. Foster", 'DICASS (100) Sonobuoy', 263)
    SM.AddToUnitMagazine("USS Paul F. Foster", 'DIFAR (100) Sonobuoy', 788)
    SM.AddToUnitMagazine("USS Paul F. Foster", 'RUM-139 Mod4 ASROC', 15)
    SM.AddToUnitMagazine("USS Paul F. Foster", 'BGM-109 TASM', 5)
    SM.AddToUnitMagazine("USS Paul F. Foster", 'BGM-109 TLAM', 38)
    SM.AddToUnitMagazine("USS Paul F. Foster", '20mm mark 244-0 ELC', 1046)
    SM.AddToUnitMagazine("USS Paul F. Foster", 'RIM-116A RAM', 42)
    SM.AddToUnitMagazine("USS Paul F. Foster", '127mm mk 80 HE-PD mk 67', 1200)
    UI.AddTask('MissileWarning', 3.000000, 3)
    UI.AddTask('RefuelAllAircraft', 3.000000, 3)
    BB = UI.GetBlackboardInterface()
    leader_id = UI.LookupFriendlyId('USS Nimitz')
    UI.SetFormationLeader(leader_id)
    UI.SetFormationMode(2)
    UI.SetFormationPosition(13.956, 2.647, 2.114, 0.230)
    UI.SetFormationAltitudeOffset(0.0)
    UI.SetFormationUseNorthBearing(0)
    
    SM.AddUnitToFlightDeck('USS Paul F. Foster', 'SH-60B', 'Spruance VLS 93 DDG Seahawk 101', 1)
    SM.SetFlightDeckUnitLoadout('USS Paul F. Foster', 'Spruance VLS 93 DDG Seahawk 101', '1 AGM-119B;1 120 gallon tank;1 Mk-46 Mod5;25 Chaff-1;25 Chaff-1;5 DICASS (100) Sonobuoy;5 LOFAR (100) Sonobuoy;15 DIFAR (100) Sonobuoy;')
    
    SM.AddUnitToFlightDeck('USS Paul F. Foster', 'SH-60B', 'Spruance VLS 93 DDG Seahawk 102', 1)
    SM.SetFlightDeckUnitLoadout('USS Paul F. Foster', 'Spruance VLS 93 DDG Seahawk 102', '1 AGM-119B;1 120 gallon tank;1 Mk-46 Mod5;25 Chaff-1;25 Chaff-1;5 DICASS (100) Sonobuoy;5 LOFAR (100) Sonobuoy;15 DIFAR (100) Sonobuoy;')
    
    unit = SM.GetDefaultUnit()
    unit.className = 'Oliver Hazard Perry FFGHM'
    unit.unitName = "USS Nicholas"
    UI = SM.GetUnitInterface('USS Nimitz')
    leader_track = UI.GetTrackById(UI.GetPlatformId())
    lon_deg = 57.296*leader_track.Lon + 0.0760
    lat_deg = 57.296*leader_track.Lat + -0.0874
    unit.SetPosition(lon_deg, lat_deg, 0.0)
    unit.heading = 90.00
    unit.speed = 3.0
    SM.AddUnitToAlliance(unit, 1)
    SM.SetUnitLauncherItem(unit.unitName, 0, '20mm mark 244-0 ELC', 97)
    SM.SetUnitLauncherItem(unit.unitName, 1, '76mm HE-MOM', 80)
    SM.SetUnitLauncherItem(unit.unitName, 2, 'RIM-66L', 1)
    SM.SetUnitLauncherItem(unit.unitName, 3, 'Mk-46 Mod5', 3)
    SM.SetUnitLauncherItem(unit.unitName, 4, 'Mk-46 Mod5', 3)
    UI = SM.GetUnitInterface(unit.unitName)
    SM.AddToUnitMagazine("USS Nicholas", 'Fuel', 28098)
    SM.AddToUnitMagazine("USS Nicholas", 'Mk-46 Mod5', 19)
    SM.AddToUnitMagazine("USS Nicholas", 'Mk-50', 1)
    SM.AddToUnitMagazine("USS Nicholas", 'AGM-114 Hellfire', 8)
    SM.AddToUnitMagazine("USS Nicholas", 'AGM-119B', 2)
    SM.AddToUnitMagazine("USS Nicholas", '120 gallon tank', 2)
    SM.AddToUnitMagazine("USS Nicholas", 'Chaff-1', 50)
    SM.AddToUnitMagazine("USS Nicholas", 'Flare-1', 50)
    SM.AddToUnitMagazine("USS Nicholas", 'DICASS (100) Sonobuoy', 105)
    SM.AddToUnitMagazine("USS Nicholas", 'LOFAR (100) Sonobuoy', 105)
    SM.AddToUnitMagazine("USS Nicholas", 'DIFAR (100) Sonobuoy', 315)
    SM.AddToUnitMagazine("USS Nicholas", 'RIM-66L', 35)
    SM.AddToUnitMagazine("USS Nicholas", 'RGM-84F Harpoon', 4)
    SM.AddToUnitMagazine("USS Nicholas", '20mm mark 244-0 ELC', 523)
    SM.AddToUnitMagazine("USS Nicholas", '76mm HE-MOM', 240)
    UI.AddTask('MissileWarning', 3.000000, 3)
    UI.AddTask('RefuelAllAircraft', 3.000000, 3)
    BB = UI.GetBlackboardInterface()
    leader_id = UI.LookupFriendlyId('USS Nimitz')
    UI.SetFormationLeader(leader_id)
    UI.SetFormationMode(2)
    UI.SetFormationPosition(11.988, 2.857, 0.913, 0.531)
    UI.SetFormationAltitudeOffset(0.0)
    UI.SetFormationUseNorthBearing(0)
    
    SM.AddUnitToFlightDeck('USS Nicholas', 'SH-60B', 'Perry FFG Seahawk 1', 1)
    SM.SetFlightDeckUnitLoadout('USS Nicholas', 'Perry FFG Seahawk 1', '1 AGM-119B;1 120 gallon tank;1 Mk-46 Mod5;25 Chaff-1;25 Chaff-1;5 DICASS (100) Sonobuoy;5 LOFAR (100) Sonobuoy;15 DIFAR (100) Sonobuoy;')
    
    unit = SM.GetDefaultUnit()
    unit.className = 'Oliver Hazard Perry FFGHM'
    unit.unitName = "USS McInerney"
    UI = SM.GetUnitInterface('USS Nimitz')
    leader_track = UI.GetTrackById(UI.GetPlatformId())
    lon_deg = 57.296*leader_track.Lon + -0.0941
    lat_deg = 57.296*leader_track.Lat + 0.0395
    unit.SetPosition(lon_deg, lat_deg, 0.0)
    unit.heading = 90.00
    unit.speed = 3.0
    SM.AddUnitToAlliance(unit, 1)
    SM.SetUnitLauncherItem(unit.unitName, 0, '20mm mark 244-0 ELC', 97)
    SM.SetUnitLauncherItem(unit.unitName, 1, '76mm HE-MOM', 80)
    SM.SetUnitLauncherItem(unit.unitName, 2, 'RIM-66L', 1)
    SM.SetUnitLauncherItem(unit.unitName, 3, 'Mk-46 Mod5', 3)
    SM.SetUnitLauncherItem(unit.unitName, 4, 'Mk-46 Mod5', 3)
    UI = SM.GetUnitInterface(unit.unitName)
    SM.AddToUnitMagazine("USS McInerney", 'Fuel', 28098)
    SM.AddToUnitMagazine("USS McInerney", 'Mk-46 Mod5', 19)
    SM.AddToUnitMagazine("USS McInerney", 'Mk-50', 1)
    SM.AddToUnitMagazine("USS McInerney", 'AGM-114 Hellfire', 8)
    SM.AddToUnitMagazine("USS McInerney", 'AGM-119B', 2)
    SM.AddToUnitMagazine("USS McInerney", '120 gallon tank', 2)
    SM.AddToUnitMagazine("USS McInerney", 'Chaff-1', 50)
    SM.AddToUnitMagazine("USS McInerney", 'Flare-1', 50)
    SM.AddToUnitMagazine("USS McInerney", 'DICASS (100) Sonobuoy', 105)
    SM.AddToUnitMagazine("USS McInerney", 'LOFAR (100) Sonobuoy', 105)
    SM.AddToUnitMagazine("USS McInerney", 'DIFAR (100) Sonobuoy', 315)
    SM.AddToUnitMagazine("USS McInerney", 'RIM-66L', 35)
    SM.AddToUnitMagazine("USS McInerney", 'RGM-84F Harpoon', 4)
    SM.AddToUnitMagazine("USS McInerney", '20mm mark 244-0 ELC', 523)
    SM.AddToUnitMagazine("USS McInerney", '76mm HE-MOM', 240)
    UI.AddTask('MissileWarning', 3.000000, 3)
    UI.AddTask('RefuelAllAircraft', 3.000000, 3)
    BB = UI.GetBlackboardInterface()
    leader_id = UI.LookupFriendlyId('USS Nimitz')
    UI.SetFormationLeader(leader_id)
    UI.SetFormationMode(2)
    UI.SetFormationPosition(9.995, 2.485, -2.705, 0.550)
    UI.SetFormationAltitudeOffset(0.0)
    UI.SetFormationUseNorthBearing(0)
    
    SM.AddUnitToFlightDeck('USS McInerney', 'SH-60B', 'Perry FFG Seahawk 101', 1)
    SM.SetFlightDeckUnitLoadout('USS McInerney', 'Perry FFG Seahawk 101', '1 AGM-119B;1 120 gallon tank;1 Mk-46 Mod5;25 Chaff-1;25 Chaff-1;5 DICASS (100) Sonobuoy;5 LOFAR (100) Sonobuoy;15 DIFAR (100) Sonobuoy;')
    
    unit = SM.GetDefaultUnit()
    unit.className = 'Sacramento AOEHM'
    unit.unitName = "Sacramento AOEHM"
    UI = SM.GetUnitInterface('USS Nimitz')
    leader_track = UI.GetTrackById(UI.GetPlatformId())
    lon_deg = 57.296*leader_track.Lon + -0.0413
    lat_deg = 57.296*leader_track.Lat + -0.0552
    unit.SetPosition(lon_deg, lat_deg, 0.0)
    unit.heading = 90.00
    unit.speed = 3.0
    SM.AddUnitToAlliance(unit, 1)
    SM.SetUnitLauncherItem(unit.unitName, 0, '20mm mark 244-0 ELC', 97)
    SM.SetUnitLauncherItem(unit.unitName, 1, '20mm mark 244-0 ELC', 97)
    SM.SetUnitLauncherItem(unit.unitName, 2, 'RIM-7P(v1)', 8)
    UI = SM.GetUnitInterface(unit.unitName)
    SM.AddToUnitMagazine("Sacramento AOEHM", '20mm mark 244-0 ELC', 1046)
    UI.AddTask('MissileWarning', 3.000000, 3)
    UI.AddTask('RefuelAllAircraft', 3.000000, 3)
    BB = UI.GetBlackboardInterface()
    leader_id = UI.LookupFriendlyId('USS Nimitz')
    UI.SetFormationLeader(leader_id)
    UI.SetFormationMode(2)
    UI.SetFormationPosition(7.323, 1.359, 2.157, 0.290)
    UI.SetFormationAltitudeOffset(0.0)
    UI.SetFormationUseNorthBearing(0)
    
    unit = SM.GetDefaultUnit()
    unit.className = 'Spruance DDG VLS 93'
    unit.unitName = "USS Cushing"
    UI = SM.GetUnitInterface('USS Nimitz')
    leader_track = UI.GetTrackById(UI.GetPlatformId())
    lon_deg = 57.296*leader_track.Lon + 0.0966
    lat_deg = 57.296*leader_track.Lat + -0.0089
    unit.SetPosition(lon_deg, lat_deg, 0.0)
    unit.heading = 90.00
    unit.speed = 3.0
    SM.AddUnitToAlliance(unit, 1)
    SM.SetUnitLauncherItem(unit.unitName, 0, 'RUM-139 Mod4 ASROC', 1)
    SM.SetUnitLauncherItem(unit.unitName, 1, 'BGM-109 TASM', 1)
    SM.SetUnitLauncherItem(unit.unitName, 2, 'BGM-109 TLAM', 1)
    SM.SetUnitLauncherItem(unit.unitName, 3, 'RIM-7P(v1)', 8)
    SM.SetUnitLauncherItem(unit.unitName, 4, '127mm mk 80 HE-PD mk 67', 20)
    SM.SetUnitLauncherItem(unit.unitName, 5, '127mm mk 80 HE-PD mk 67', 20)
    SM.SetUnitLauncherItem(unit.unitName, 6, '20mm mark 244-0 ELC', 97)
    SM.SetUnitLauncherItem(unit.unitName, 7, '20mm mark 244-0 ELC', 97)
    SM.SetUnitLauncherItem(unit.unitName, 8, 'RGM-84F Harpoon', 4)
    SM.SetUnitLauncherItem(unit.unitName, 9, 'RGM-84F Harpoon', 4)
    SM.SetUnitLauncherItem(unit.unitName, 10, 'RIM-116A RAM', 21)
    UI = SM.GetUnitInterface(unit.unitName)
    SM.AddToUnitMagazine("USS Cushing", 'Fuel', 65176)
    SM.AddToUnitMagazine("USS Cushing", 'Mk-46 Mod5', 23)
    SM.AddToUnitMagazine("USS Cushing", 'Mk-50', 2)
    SM.AddToUnitMagazine("USS Cushing", '120 gallon tank', 4)
    SM.AddToUnitMagazine("USS Cushing", 'AGM-114 Hellfire', 16)
    SM.AddToUnitMagazine("USS Cushing", 'AGM-119B', 4)
    SM.AddToUnitMagazine("USS Cushing", 'LOFAR (100) Sonobuoy', 263)
    SM.AddToUnitMagazine("USS Cushing", 'DICASS (100) Sonobuoy', 263)
    SM.AddToUnitMagazine("USS Cushing", 'DIFAR (100) Sonobuoy', 788)
    SM.AddToUnitMagazine("USS Cushing", 'RUM-139 Mod4 ASROC', 15)
    SM.AddToUnitMagazine("USS Cushing", 'BGM-109 TASM', 5)
    SM.AddToUnitMagazine("USS Cushing", 'BGM-109 TLAM', 38)
    SM.AddToUnitMagazine("USS Cushing", '20mm mark 244-0 ELC', 1046)
    SM.AddToUnitMagazine("USS Cushing", 'RIM-116A RAM', 42)
    SM.AddToUnitMagazine("USS Cushing", '127mm mk 80 HE-PD mk 67', 1200)
    UI.AddTask('MissileWarning', 3.000000, 3)
    UI.AddTask('RefuelAllAircraft', 3.000000, 3)
    BB = UI.GetBlackboardInterface()
    leader_id = UI.LookupFriendlyId('USS Nimitz')
    UI.SetFormationLeader(leader_id)
    UI.SetFormationMode(2)
    UI.SetFormationPosition(9.661, 2.404, 0.136, 0.391)
    UI.SetFormationAltitudeOffset(0.0)
    UI.SetFormationUseNorthBearing(0)
    
    SM.AddUnitToFlightDeck('USS Cushing', 'SH-60B', 'Spruance VLS 93 DDG Seahawk 1', 1)
    SM.SetFlightDeckUnitLoadout('USS Cushing', 'Spruance VLS 93 DDG Seahawk 1', '1 AGM-119B;1 120 gallon tank;1 Mk-46 Mod5;25 Chaff-1;25 Chaff-1;5 DICASS (100) Sonobuoy;5 LOFAR (100) Sonobuoy;15 DIFAR (100) Sonobuoy;')
    
    SM.AddUnitToFlightDeck('USS Cushing', 'SH-60B', 'Spruance VLS 93 DDG Seahawk 2', 1)
    SM.SetFlightDeckUnitLoadout('USS Cushing', 'Spruance VLS 93 DDG Seahawk 2', '1 AGM-119B;1 120 gallon tank;1 Mk-46 Mod5;25 Chaff-1;25 Chaff-1;5 DICASS (100) Sonobuoy;5 LOFAR (100) Sonobuoy;15 DIFAR (100) Sonobuoy;')
    
    unit = SM.GetDefaultUnit()
    unit.className = 'Ticonderoga CG Baseline 3'
    unit.unitName = "USS Gettysburg"
    UI = SM.GetUnitInterface('USS Nimitz')
    leader_track = UI.GetTrackById(UI.GetPlatformId())
    lon_deg = 57.296*leader_track.Lon + 0.0576
    lat_deg = 57.296*leader_track.Lat + 0.0717
    unit.SetPosition(lon_deg, lat_deg, 0.0)
    unit.heading = 90.00
    unit.speed = 3.0
    SM.AddUnitToAlliance(unit, 1)
    SM.SetUnitLauncherItem(unit.unitName, 0, 'RIM-156', 1)
    SM.SetUnitLauncherItem(unit.unitName, 1, 'RIM-66M', 1)
    SM.SetUnitLauncherItem(unit.unitName, 2, 'RIM-162A', 1)
    SM.SetUnitLauncherItem(unit.unitName, 3, '20mm mark 244-0 ELC', 97)
    SM.SetUnitLauncherItem(unit.unitName, 4, '20mm mark 244-0 ELC', 97)
    SM.SetUnitLauncherItem(unit.unitName, 5, 'RGM-84F Harpoon', 4)
    SM.SetUnitLauncherItem(unit.unitName, 6, 'RGM-84F Harpoon', 4)
    SM.SetUnitLauncherItem(unit.unitName, 7, '127mm mk 80 HE-PD mk 67', 20)
    SM.SetUnitLauncherItem(unit.unitName, 8, '127mm mk 80 HE-PD mk 67', 20)
    SM.SetUnitLauncherItem(unit.unitName, 9, 'Mk-46 Mod5', 3)
    SM.SetUnitLauncherItem(unit.unitName, 10, 'Mk-46 Mod5', 3)
    UI = SM.GetUnitInterface(unit.unitName)
    SM.AddToUnitMagazine("USS Gettysburg", 'Fuel', 56197)
    SM.AddToUnitMagazine("USS Gettysburg", 'Mk-46 Mod5', 33)
    SM.AddToUnitMagazine("USS Gettysburg", 'Mk-50', 3)
    SM.AddToUnitMagazine("USS Gettysburg", 'AGM-119B', 4)
    SM.AddToUnitMagazine("USS Gettysburg", 'AGM-114 Hellfire', 16)
    SM.AddToUnitMagazine("USS Gettysburg", '120 gallon tank', 4)
    SM.AddToUnitMagazine("USS Gettysburg", 'Chaff-1', 75)
    SM.AddToUnitMagazine("USS Gettysburg", 'Flare-1', 75)
    SM.AddToUnitMagazine("USS Gettysburg", 'LOFAR (100) Sonobuoy', 203)
    SM.AddToUnitMagazine("USS Gettysburg", 'DICASS (100) Sonobuoy', 203)
    SM.AddToUnitMagazine("USS Gettysburg", 'DIFAR (100) Sonobuoy', 608)
    SM.AddToUnitMagazine("USS Gettysburg", 'RIM-156', 19)
    SM.AddToUnitMagazine("USS Gettysburg", 'RIM-66M', 91)
    SM.AddToUnitMagazine("USS Gettysburg", 'RIM-162A', 39)
    SM.AddToUnitMagazine("USS Gettysburg", '20mm mark 244-0 ELC', 1046)
    SM.AddToUnitMagazine("USS Gettysburg", '127mm mk 80 HE-PD mk 67', 1200)
    UI.AddTask('MissileWarning', 3.000000, 3)
    UI.AddTask('RefuelAllAircraft', 3.000000, 3)
    BB = UI.GetBlackboardInterface()
    leader_id = UI.LookupFriendlyId('USS Nimitz')
    UI.SetFormationLeader(leader_id)
    UI.SetFormationMode(2)
    UI.SetFormationPosition(9.582, 2.521, -0.910, 0.440)
    UI.SetFormationAltitudeOffset(0.0)
    UI.SetFormationUseNorthBearing(0)
    
    SM.AddUnitToFlightDeck('USS Gettysburg', 'SH-60B', 'Tico Seahawk 1', 1)
    SM.SetFlightDeckUnitLoadout('USS Gettysburg', 'Tico Seahawk 1', '1 AGM-119B;1 120 gallon tank;1 Mk-46 Mod5;25 Chaff-1;25 Chaff-1;5 DICASS (100) Sonobuoy;5 LOFAR (100) Sonobuoy;15 DIFAR (100) Sonobuoy;')
    
    SM.AddUnitToFlightDeck('USS Gettysburg', 'SH-60B', 'Tico Seahawk 2', 1)
    SM.SetFlightDeckUnitLoadout('USS Gettysburg', 'Tico Seahawk 2', '1 AGM-119B;1 120 gallon tank;1 Mk-46 Mod5;25 Chaff-1;25 Chaff-1;5 DICASS (100) Sonobuoy;5 LOFAR (100) Sonobuoy;15 DIFAR (100) Sonobuoy;')
    
    ##############################
    ### Alliance 2 units
    ##############################

    unit = SM.GetDefaultUnit()
    unit.className = 'Su-27'
    unit.unitName = "Desert-15"
    unit.SetPosition(51.547581, 28.694471, 6015.5)
    unit.heading = 12.00
    unit.speed = 200.0
    SM.AddUnitToAlliance(unit, 2)
    SM.SetUnitLauncherItem(unit.unitName, 0, 'Kh-31P', 3)
    SM.SetUnitLauncherItem(unit.unitName, 1, 'R-77', 2)
    SM.SetUnitLauncherItem(unit.unitName, 2, 'Kh-31P', 4)
    SM.SetUnitLauncherItem(unit.unitName, 3, 'Flare-1', 25)
    SM.SetUnitLauncherItem(unit.unitName, 4, 'Chaff-1', 25)
    UI = SM.GetUnitInterface(unit.unitName)
    UI.AddTask('AirEvade', 3.000000, 3)
    UI.AddTask('EngageAll', 3.000000, 0)
    UI.AddTask('PatrolCircle', 1.000000, 0)
    UI.AddTask('RTB', 2.000000, 3)
    UI.AddTask('ReturnToBase', 2.000000, 0)
    BB = UI.GetBlackboardInterface()
    BB.Write('Bingo', '0.450000')
    BB.Write('Home', 'Esfahan AB')
    BB.Write('RTBtime', '5400.000000')
    BB.Write('StationAltitude', '5500.000000')
    BB.Write('StationLatitude', '0.582765')
    BB.Write('StationLongitude', '0.867429')
    UI.SetThrottle(0.500000)
    
    unit = SM.GetDefaultUnit()
    unit.className = 'Su-27'
    unit.unitName = "Desert-14"
    unit.SetPosition(52.915918, 30.685213, 10.0)
    unit.heading = 12.00
    unit.speed = 200.0
    SM.AddUnitToAlliance(unit, 2)
    SM.SetUnitLauncherItem(unit.unitName, 0, 'Kh-31P', 3)
    SM.SetUnitLauncherItem(unit.unitName, 1, 'R-77', 2)
    SM.SetUnitLauncherItem(unit.unitName, 2, 'Kh-31P', 4)
    SM.SetUnitLauncherItem(unit.unitName, 3, 'Flare-1', 25)
    SM.SetUnitLauncherItem(unit.unitName, 4, 'Chaff-1', 25)
    UI = SM.GetUnitInterface(unit.unitName)
    UI.AddTask('AirEvade', 3.000000, 3)
    UI.AddTask('EngageAll', 3.000000, 0)
    UI.AddTask('PatrolCircle', 1.000000, 0)
    UI.AddTask('RTB', 2.000000, 3)
    UI.AddTask('ReturnToBase', 2.000000, 0)
    BB = UI.GetBlackboardInterface()
    BB.Write('Bingo', '0.450000')
    BB.Write('Home', 'Esfahan AB')
    BB.Write('RTBtime', '5400.000000')
    BB.Write('StationAltitude', '5500.000000')
    BB.Write('StationLatitude', '0.582765')
    BB.Write('StationLongitude', '0.867429')
    UI.SetThrottle(0.500000)
    
    unit = SM.GetDefaultUnit()
    unit.className = 'Su-27'
    unit.unitName = "Desert-13"
    unit.SetPosition(51.753788, 31.946121, 10.0)
    unit.heading = 12.00
    unit.speed = 200.0
    SM.AddUnitToAlliance(unit, 2)
    SM.SetUnitLauncherItem(unit.unitName, 0, 'Kh-31P', 3)
    SM.SetUnitLauncherItem(unit.unitName, 1, 'R-77', 2)
    SM.SetUnitLauncherItem(unit.unitName, 2, 'Kh-31P', 4)
    SM.SetUnitLauncherItem(unit.unitName, 3, 'Flare-1', 25)
    SM.SetUnitLauncherItem(unit.unitName, 4, 'Chaff-1', 25)
    UI = SM.GetUnitInterface(unit.unitName)
    UI.AddTask('AirEvade', 3.000000, 3)
    UI.AddTask('EngageAll', 3.000000, 0)
    UI.AddTask('PatrolCircle', 1.000000, 0)
    UI.AddTask('RTB', 2.000000, 3)
    UI.AddTask('ReturnToBase', 2.000000, 0)
    BB = UI.GetBlackboardInterface()
    BB.Write('Bingo', '0.450000')
    BB.Write('Home', 'Esfahan AB')
    BB.Write('RTBtime', '5400.000000')
    BB.Write('StationAltitude', '5500.000000')
    BB.Write('StationLatitude', '0.582765')
    BB.Write('StationLongitude', '0.867429')
    UI.SetThrottle(0.500000)
    
    unit = SM.GetDefaultUnit()
    unit.className = 'Su-27'
    unit.unitName = "Desert-11"
    unit.SetPosition(48.848548, 30.507711, 9988.0)
    unit.heading = 12.00
    unit.speed = 200.0
    SM.AddUnitToAlliance(unit, 2)
    SM.SetUnitLauncherItem(unit.unitName, 0, 'Kh-31P', 3)
    SM.SetUnitLauncherItem(unit.unitName, 1, 'R-77', 2)
    SM.SetUnitLauncherItem(unit.unitName, 2, 'Kh-31P', 4)
    SM.SetUnitLauncherItem(unit.unitName, 3, 'Flare-1', 25)
    SM.SetUnitLauncherItem(unit.unitName, 4, 'Chaff-1', 25)
    UI = SM.GetUnitInterface(unit.unitName)
    UI.AddTask('AirEvade', 3.000000, 3)
    UI.AddTask('EngageAll', 2.000000, 0)
    UI.AddTask('PatrolCircle', 1.000000, 0)
    UI.AddTask('RTB', 2.000000, 3)
    BB = UI.GetBlackboardInterface()
    BB.Write('Bingo', '0.450000')
    BB.Write('Home', 'Esfahan AB')
    BB.Write('RTBtime', '5400.000000')
    BB.Write('StationAltitude', '5500.000000')
    BB.Write('StationLatitude', '0.510626')
    BB.Write('StationLongitude', '0.871716')
    UI.SetThrottle(0.500000)
    
    unit = SM.GetDefaultUnit()
    unit.className = 'Su-27'
    unit.unitName = "Desert-10"
    unit.SetPosition(51.885339, 31.002746, 10.0)
    unit.heading = 12.00
    unit.speed = 200.0
    SM.AddUnitToAlliance(unit, 2)
    SM.SetUnitLauncherItem(unit.unitName, 0, 'Kh-31P', 3)
    SM.SetUnitLauncherItem(unit.unitName, 1, 'R-77', 2)
    SM.SetUnitLauncherItem(unit.unitName, 2, 'Kh-31P', 4)
    SM.SetUnitLauncherItem(unit.unitName, 3, 'Flare-1', 25)
    SM.SetUnitLauncherItem(unit.unitName, 4, 'Chaff-1', 25)
    UI = SM.GetUnitInterface(unit.unitName)
    UI.AddTask('AirEvade', 3.000000, 3)
    UI.AddTask('EngageAll', 3.000000, 0)
    UI.AddTask('PatrolCircle', 1.000000, 0)
    UI.AddTask('RTB', 2.000000, 3)
    UI.AddTask('ReturnToBase', 2.000000, 0)
    BB = UI.GetBlackboardInterface()
    BB.Write('Bingo', '0.450000')
    BB.Write('Home', 'Esfahan AB')
    BB.Write('RTBtime', '5400.000000')
    BB.Write('StationAltitude', '5500.000000')
    BB.Write('StationLatitude', '0.582765')
    BB.Write('StationLongitude', '0.867429')
    UI.SetThrottle(0.500000)
    
    unit = SM.GetDefaultUnit()
    unit.className = 'Su-27'
    unit.unitName = "Desert-8"
    unit.SetPosition(50.350500, 31.460425, 10.0)
    unit.heading = 12.00
    unit.speed = 200.0
    SM.AddUnitToAlliance(unit, 2)
    SM.SetUnitLauncherItem(unit.unitName, 0, 'Kh-31P', 3)
    SM.SetUnitLauncherItem(unit.unitName, 1, 'R-77', 2)
    SM.SetUnitLauncherItem(unit.unitName, 2, 'Kh-31P', 4)
    SM.SetUnitLauncherItem(unit.unitName, 3, 'Flare-1', 25)
    SM.SetUnitLauncherItem(unit.unitName, 4, 'Chaff-1', 25)
    UI = SM.GetUnitInterface(unit.unitName)
    UI.AddTask('AirEvade', 3.000000, 3)
    UI.AddTask('EngageAll', 2.000000, 0)
    UI.AddTask('PatrolCircle', 1.000000, 0)
    UI.AddTask('RTB', 2.000000, 3)
    BB = UI.GetBlackboardInterface()
    BB.Write('Bingo', '0.450000')
    BB.Write('Home', 'Esfahan AB')
    BB.Write('RTBtime', '5400.000000')
    BB.Write('StationAltitude', '5500.000000')
    BB.Write('StationLatitude', '0.522373')
    BB.Write('StationLongitude', '0.880288')
    UI.SetThrottle(0.500000)
    
    unit = SM.GetDefaultUnit()
    unit.className = 'Su-27'
    unit.unitName = "Desert-7"
    unit.SetPosition(50.240893, 32.160981, 10.0)
    unit.heading = 12.00
    unit.speed = 200.0
    SM.AddUnitToAlliance(unit, 2)
    SM.SetUnitLauncherItem(unit.unitName, 0, 'Kh-31P', 3)
    SM.SetUnitLauncherItem(unit.unitName, 1, 'R-77', 2)
    SM.SetUnitLauncherItem(unit.unitName, 2, 'Kh-31P', 4)
    SM.SetUnitLauncherItem(unit.unitName, 3, 'Flare-1', 25)
    SM.SetUnitLauncherItem(unit.unitName, 4, 'Chaff-1', 25)
    UI = SM.GetUnitInterface(unit.unitName)
    UI.AddTask('AirEvade', 3.000000, 3)
    UI.AddTask('EngageAll', 3.000000, 0)
    UI.AddTask('PatrolCircle', 1.000000, 0)
    UI.AddTask('RTB', 2.000000, 3)
    UI.AddTask('ReturnToBase', 2.000000, 0)
    BB = UI.GetBlackboardInterface()
    BB.Write('Bingo', '0.450000')
    BB.Write('Home', 'Esfahan AB')
    BB.Write('RTBtime', '5400.000000')
    BB.Write('StationAltitude', '5500.000000')
    BB.Write('StationLatitude', '0.582765')
    BB.Write('StationLongitude', '0.867429')
    UI.SetThrottle(0.500000)
    
    unit = SM.GetDefaultUnit()
    unit.className = 'F-5E'
    unit.unitName = "Camel-9"
    unit.SetPosition(50.812418, 29.833798, 1361.8)
    unit.heading = 12.00
    unit.speed = 200.0
    SM.AddUnitToAlliance(unit, 2)
    SM.SetUnitLauncherItem(unit.unitName, 0, 'AIM-9M', 2)
    SM.SetUnitLauncherItem(unit.unitName, 1, 'AIM-9M', 2)
    SM.SetUnitLauncherItem(unit.unitName, 2, 'Mk-82', 6)
    UI = SM.GetUnitInterface(unit.unitName)
    UI.AddTask('AirEvade', 3.000000, 3)
    UI.AddTask('BombDatum', 3.000000, 0)
    UI.AddTask('EngageAll', 2.000000, 0)
    UI.AddTask('PatrolCircle', 1.000000, 0)
    UI.AddTask('RTB', 2.000000, 3)
    BB = UI.GetBlackboardInterface()
    BB.Write('Bingo', '0.450000')
    BB.Write('DatumLatitude', '0.517490')
    BB.Write('DatumLongitude', '0.880519')
    BB.Write('Home', 'Esfahan AB')
    BB.Write('RTBtime', '5400.000000')
    BB.Write('StationAltitude', '5500.000000')
    BB.Write('StationLatitude', '0.520337')
    BB.Write('StationLongitude', '0.882228')
    UI.SetThrottle(0.500000)
    
    unit = SM.GetDefaultUnit()
    unit.className = 'F-5E'
    unit.unitName = "Camel-8"
    unit.SetPosition(49.990167, 29.881296, 2763.8)
    unit.heading = 12.00
    unit.speed = 200.0
    SM.AddUnitToAlliance(unit, 2)
    SM.SetUnitLauncherItem(unit.unitName, 0, 'AIM-9M', 2)
    SM.SetUnitLauncherItem(unit.unitName, 1, 'AIM-9M', 2)
    SM.SetUnitLauncherItem(unit.unitName, 2, 'Mk-82', 6)
    UI = SM.GetUnitInterface(unit.unitName)
    UI.AddTask('AirEvade', 3.000000, 3)
    UI.AddTask('BombDatum', 3.000000, 0)
    UI.AddTask('EngageAll', 2.000000, 0)
    UI.AddTask('PatrolCircle', 1.000000, 0)
    UI.AddTask('RTB', 2.000000, 3)
    BB = UI.GetBlackboardInterface()
    BB.Write('Bingo', '0.450000')
    BB.Write('DatumLatitude', '0.517490')
    BB.Write('DatumLongitude', '0.880519')
    BB.Write('Home', 'Esfahan AB')
    BB.Write('RTBtime', '5400.000000')
    BB.Write('StationAltitude', '5500.000000')
    BB.Write('StationLatitude', '0.517123')
    BB.Write('StationLongitude', '0.877193')
    UI.SetThrottle(0.500000)
    
    unit = SM.GetDefaultUnit()
    unit.className = 'F-5E'
    unit.unitName = "Camel-7"
    unit.SetPosition(51.503119, 29.178850, 10.0)
    unit.heading = 12.00
    unit.speed = 200.0
    SM.AddUnitToAlliance(unit, 2)
    SM.SetUnitLauncherItem(unit.unitName, 0, 'AIM-9M', 2)
    SM.SetUnitLauncherItem(unit.unitName, 1, 'AIM-9M', 2)
    SM.SetUnitLauncherItem(unit.unitName, 2, 'Mk-82', 6)
    UI = SM.GetUnitInterface(unit.unitName)
    UI.AddTask('AirEvade', 3.000000, 3)
    UI.AddTask('EngageAll', 3.000000, 0)
    UI.AddTask('PatrolCircle', 1.000000, 0)
    UI.AddTask('RTB', 2.000000, 3)
    UI.AddTask('ReturnToBase', 2.000000, 0)
    BB = UI.GetBlackboardInterface()
    BB.Write('Bingo', '0.450000')
    BB.Write('Home', 'Esfahan AB')
    BB.Write('RTBtime', '5400.000000')
    BB.Write('StationAltitude', '5500.000000')
    BB.Write('StationLatitude', '0.559727')
    BB.Write('StationLongitude', '0.888198')
    UI.SetThrottle(0.500000)
    
    unit = SM.GetDefaultUnit()
    unit.className = 'F-5E'
    unit.unitName = "Camel-6"
    unit.SetPosition(51.536007, 29.862274, 10.0)
    unit.heading = 12.00
    unit.speed = 200.0
    SM.AddUnitToAlliance(unit, 2)
    SM.SetUnitLauncherItem(unit.unitName, 0, 'AIM-9M', 2)
    SM.SetUnitLauncherItem(unit.unitName, 1, 'AIM-9M', 2)
    SM.SetUnitLauncherItem(unit.unitName, 2, 'Mk-82', 6)
    UI = SM.GetUnitInterface(unit.unitName)
    UI.AddTask('AirEvade', 3.000000, 3)
    UI.AddTask('BombDatum', 3.000000, 0)
    UI.AddTask('EngageAll', 2.000000, 0)
    UI.AddTask('PatrolCircle', 1.000000, 0)
    UI.AddTask('RTB', 2.000000, 3)
    BB = UI.GetBlackboardInterface()
    BB.Write('Bingo', '0.450000')
    BB.Write('DatumLatitude', '0.517490')
    BB.Write('DatumLongitude', '0.880519')
    BB.Write('Home', 'Esfahan AB')
    BB.Write('RTBtime', '5400.000000')
    BB.Write('StationAltitude', '5500.000000')
    BB.Write('StationLatitude', '0.516205')
    BB.Write('StationLongitude', '0.884955')
    UI.SetThrottle(0.500000)
    
    unit = SM.GetDefaultUnit()
    unit.className = 'F-5E'
    unit.unitName = "Camel-5"
    unit.SetPosition(50.922083, 30.640637, 10.0)
    unit.heading = 12.00
    unit.speed = 200.0
    SM.AddUnitToAlliance(unit, 2)
    SM.SetUnitLauncherItem(unit.unitName, 0, 'AIM-9M', 2)
    SM.SetUnitLauncherItem(unit.unitName, 1, 'AIM-9M', 2)
    SM.SetUnitLauncherItem(unit.unitName, 2, 'Mk-82', 6)
    UI = SM.GetUnitInterface(unit.unitName)
    UI.AddTask('AirEvade', 3.000000, 3)
    UI.AddTask('BombDatum', 3.000000, 0)
    UI.AddTask('EngageAll', 2.000000, 0)
    UI.AddTask('PatrolCircle', 1.000000, 0)
    UI.AddTask('RTB', 2.000000, 3)
    BB = UI.GetBlackboardInterface()
    BB.Write('Bingo', '0.450000')
    BB.Write('DatumLatitude', '0.517490')
    BB.Write('DatumLongitude', '0.880519')
    BB.Write('Home', 'Esfahan AB')
    BB.Write('RTBtime', '5400.000000')
    BB.Write('StationAltitude', '5500.000000')
    BB.Write('StationLatitude', '0.523267')
    BB.Write('StationLongitude', '0.880417')
    UI.SetThrottle(0.500000)
    
    unit = SM.GetDefaultUnit()
    unit.className = 'F-5E'
    unit.unitName = "Camel-4"
    unit.SetPosition(50.998802, 29.662942, 1571.3)
    unit.heading = 12.00
    unit.speed = 200.0
    SM.AddUnitToAlliance(unit, 2)
    SM.SetUnitLauncherItem(unit.unitName, 0, 'AIM-9M', 2)
    SM.SetUnitLauncherItem(unit.unitName, 1, 'AIM-9M', 2)
    SM.SetUnitLauncherItem(unit.unitName, 2, 'Mk-82', 6)
    UI = SM.GetUnitInterface(unit.unitName)
    UI.AddTask('AirEvade', 3.000000, 3)
    UI.AddTask('BombDatum', 3.000000, 0)
    UI.AddTask('EngageAll', 2.000000, 0)
    UI.AddTask('PatrolCircle', 1.000000, 0)
    UI.AddTask('RTB', 2.000000, 3)
    BB = UI.GetBlackboardInterface()
    BB.Write('Bingo', '0.450000')
    BB.Write('DatumLatitude', '0.517490')
    BB.Write('DatumLongitude', '0.880519')
    BB.Write('Home', 'Esfahan AB')
    BB.Write('RTBtime', '5400.000000')
    BB.Write('StationAltitude', '5500.000000')
    BB.Write('StationLatitude', '0.516572')
    BB.Write('StationLongitude', '0.884220')
    UI.SetThrottle(0.500000)
    
    unit = SM.GetDefaultUnit()
    unit.className = 'F-5E'
    unit.unitName = "Camel-3"
    unit.SetPosition(50.615092, 30.090082, 10.0)
    unit.heading = 12.00
    unit.speed = 200.0
    SM.AddUnitToAlliance(unit, 2)
    SM.SetUnitLauncherItem(unit.unitName, 0, 'AIM-9M', 2)
    SM.SetUnitLauncherItem(unit.unitName, 1, 'AIM-9M', 2)
    SM.SetUnitLauncherItem(unit.unitName, 2, 'Mk-82', 6)
    UI = SM.GetUnitInterface(unit.unitName)
    UI.AddTask('AirEvade', 3.000000, 3)
    UI.AddTask('BombDatum', 3.000000, 0)
    UI.AddTask('EngageAll', 2.000000, 0)
    UI.AddTask('PatrolCircle', 1.000000, 0)
    UI.AddTask('RTB', 2.000000, 3)
    BB = UI.GetBlackboardInterface()
    BB.Write('Bingo', '0.450000')
    BB.Write('DatumLatitude', '0.517490')
    BB.Write('DatumLongitude', '0.880519')
    BB.Write('Home', 'Esfahan AB')
    BB.Write('RTBtime', '5400.000000')
    BB.Write('StationAltitude', '5500.000000')
    BB.Write('StationLatitude', '0.521163')
    BB.Write('StationLongitude', '0.880654')
    UI.SetThrottle(0.500000)
    
    unit = SM.GetDefaultUnit()
    unit.className = 'F-5E'
    unit.unitName = "Camel-2"
    unit.SetPosition(50.768587, 31.286131, 10.0)
    unit.heading = 12.00
    unit.speed = 200.0
    SM.AddUnitToAlliance(unit, 2)
    SM.SetUnitLauncherItem(unit.unitName, 0, 'AIM-9M', 2)
    SM.SetUnitLauncherItem(unit.unitName, 1, 'AIM-9M', 2)
    SM.SetUnitLauncherItem(unit.unitName, 2, 'Mk-82', 6)
    UI = SM.GetUnitInterface(unit.unitName)
    UI.AddTask('AirEvade', 3.000000, 3)
    UI.AddTask('BombDatum', 3.000000, 0)
    UI.AddTask('EngageAll', 2.000000, 0)
    UI.AddTask('PatrolCircle', 1.000000, 0)
    UI.AddTask('RTB', 2.000000, 3)
    BB = UI.GetBlackboardInterface()
    BB.Write('Bingo', '0.450000')
    BB.Write('DatumLatitude', '0.517490')
    BB.Write('DatumLongitude', '0.880519')
    BB.Write('Home', 'Esfahan AB')
    BB.Write('RTBtime', '5400.000000')
    BB.Write('StationAltitude', '5500.000000')
    BB.Write('StationLatitude', '0.521172')
    BB.Write('StationLongitude', '0.880747')
    UI.SetThrottle(0.500000)
    
    unit = SM.GetDefaultUnit()
    unit.className = 'E-2T'
    unit.unitName = "SandEye2-3"
    unit.SetPosition(48.068581, 33.272633, 10.0)
    unit.heading = 315.00
    unit.speed = 250.0
    SM.AddUnitToAlliance(unit, 2)
    UI = SM.GetUnitInterface(unit.unitName)
    UI.AddTask('AirEvade', 3.000000, 3)
    UI.AddTask('PatrolCircle', 1.000000, 0)
    UI.AddTask('RTB', 2.000000, 3)
    BB = UI.GetBlackboardInterface()
    BB.Write('StationAltitude', '1629.920044')
    BB.Write('StationLatitude', '0.571535')
    BB.Write('StationLongitude', '0.836850')
    
    unit = SM.GetDefaultUnit()
    unit.className = 'E-2T'
    unit.unitName = "SandEye2-2"
    unit.SetPosition(53.002034, 31.684967, 10.0)
    unit.heading = 315.00
    unit.speed = 250.0
    SM.AddUnitToAlliance(unit, 2)
    UI = SM.GetUnitInterface(unit.unitName)
    UI.AddTask('AirEvade', 3.000000, 3)
    UI.AddTask('PatrolCircle', 1.000000, 0)
    UI.AddTask('RTB', 2.000000, 3)
    BB = UI.GetBlackboardInterface()
    BB.Write('StationAltitude', '1629.920044')
    BB.Write('StationLatitude', '0.558090')
    BB.Write('StationLongitude', '0.918554')
    
    unit = SM.GetDefaultUnit()
    unit.className = 'S-300PMU'
    unit.unitName = "ISAM-1"
    unit.SetPosition(52.660000, 32.830000, 0.0)
    unit.heading = 0.00
    unit.speed = 0.0
    SM.AddUnitToAlliance(unit, 2)
    SM.SetUnitLauncherItem(unit.unitName, 0, '5V55RUD', 4)
    SM.SetUnitLauncherItem(unit.unitName, 1, '5V55RUD', 4)
    SM.SetUnitLauncherItem(unit.unitName, 2, '5V55RUD', 4)
    SM.SetUnitLauncherItem(unit.unitName, 3, '5V55RUD', 4)
    UI = SM.GetUnitInterface(unit.unitName)
    SM.AddToUnitMagazine("ISAM-1", '5V55RUD', 72)
    UI.AddTask('EngageAll', 3.000000, 0)
    UI.AddTask('Patrol', 2.000000, 0)
    BB = UI.GetBlackboardInterface()
    
    unit = SM.GetDefaultUnit()
    unit.className = 'Tien Kung-II'
    unit.unitName = "ISAM-2"
    unit.SetPosition(48.360000, 32.810000, 1.0)
    unit.heading = 0.00
    unit.speed = 0.0
    SM.AddUnitToAlliance(unit, 2)
    SM.SetUnitLauncherItem(unit.unitName, 0, 'Tien Kung-II SAM', 8)
    UI = SM.GetUnitInterface(unit.unitName)
    UI.AddTask('EngageAll', 3.000000, 0)
    UI.AddTask('Patrol', 2.000000, 0)
    BB = UI.GetBlackboardInterface()
    
    unit = SM.GetDefaultUnit()
    unit.className = 'S-300PMU'
    unit.unitName = "ISAM-3"
    unit.SetPosition(50.960000, 33.650000, 0.0)
    unit.heading = 0.00
    unit.speed = 0.0
    SM.AddUnitToAlliance(unit, 2)
    SM.SetUnitLauncherItem(unit.unitName, 0, '5V55RUD', 4)
    SM.SetUnitLauncherItem(unit.unitName, 1, '5V55RUD', 4)
    SM.SetUnitLauncherItem(unit.unitName, 2, '5V55RUD', 4)
    SM.SetUnitLauncherItem(unit.unitName, 3, '5V55RUD', 4)
    UI = SM.GetUnitInterface(unit.unitName)
    SM.AddToUnitMagazine("ISAM-3", '5V55RUD', 72)
    UI.AddTask('EngageAll', 3.000000, 0)
    UI.AddTask('Patrol', 2.000000, 0)
    BB = UI.GetBlackboardInterface()
    
    unit = SM.GetDefaultUnit()
    unit.className = 'S-300PMU'
    unit.unitName = "ISAM-4"
    unit.SetPosition(51.840000, 30.350000, -0.0)
    unit.heading = 0.00
    unit.speed = 0.0
    SM.AddUnitToAlliance(unit, 2)
    SM.SetUnitLauncherItem(unit.unitName, 0, '5V55RUD', 4)
    SM.SetUnitLauncherItem(unit.unitName, 1, '5V55RUD', 4)
    SM.SetUnitLauncherItem(unit.unitName, 2, '5V55RUD', 4)
    SM.SetUnitLauncherItem(unit.unitName, 3, '5V55RUD', 4)
    UI = SM.GetUnitInterface(unit.unitName)
    SM.AddToUnitMagazine("ISAM-4", '5V55RUD', 72)
    UI.AddTask('EngageAll', 3.000000, 0)
    UI.AddTask('Patrol', 2.000000, 0)
    BB = UI.GetBlackboardInterface()
    
    unit = SM.GetDefaultUnit()
    unit.className = 'Rapier-Towed'
    unit.unitName = "ISAM-5"
    unit.SetPosition(50.670000, 33.630000, 1.0)
    unit.heading = 0.00
    unit.speed = 0.0
    SM.AddUnitToAlliance(unit, 2)
    SM.SetUnitLauncherItem(unit.unitName, 0, 'Rapier-SAM', 4)
    UI = SM.GetUnitInterface(unit.unitName)
    SM.AddToUnitMagazine("ISAM-5", 'Rapier-SAM', 8)
    UI.AddTask('EngageAll', 3.000000, 0)
    UI.AddTask('Patrol', 2.000000, 0)
    BB = UI.GetBlackboardInterface()
    
    unit = SM.GetDefaultUnit()
    unit.className = 'Rapier-Towed'
    unit.unitName = "ISAM-6"
    unit.SetPosition(48.430000, 31.320000, 1.0)
    unit.heading = 0.00
    unit.speed = 0.0
    SM.AddUnitToAlliance(unit, 2)
    SM.SetUnitLauncherItem(unit.unitName, 0, 'Rapier-SAM', 4)
    UI = SM.GetUnitInterface(unit.unitName)
    SM.AddToUnitMagazine("ISAM-6", 'Rapier-SAM', 8)
    UI.AddTask('EngageAll', 3.000000, 0)
    UI.AddTask('Patrol', 2.000000, 0)
    BB = UI.GetBlackboardInterface()
    
    unit = SM.GetDefaultUnit()
    unit.className = 'Rapier-Towed'
    unit.unitName = "ISAM-7"
    unit.SetPosition(48.730000, 33.330000, 1.0)
    unit.heading = 0.00
    unit.speed = 0.0
    SM.AddUnitToAlliance(unit, 2)
    SM.SetUnitLauncherItem(unit.unitName, 0, 'Rapier-SAM', 4)
    UI = SM.GetUnitInterface(unit.unitName)
    SM.AddToUnitMagazine("ISAM-7", 'Rapier-SAM', 8)
    UI.AddTask('EngageAll', 3.000000, 0)
    UI.AddTask('Patrol', 2.000000, 0)
    BB = UI.GetBlackboardInterface()
    
    unit = SM.GetDefaultUnit()
    unit.className = 'Tien Kung-II'
    unit.unitName = "ISAM-8"
    unit.SetPosition(50.100000, 30.160000, 1.0)
    unit.heading = 0.00
    unit.speed = 0.0
    SM.AddUnitToAlliance(unit, 2)
    SM.SetUnitLauncherItem(unit.unitName, 0, 'Tien Kung-II SAM', 8)
    UI = SM.GetUnitInterface(unit.unitName)
    UI.AddTask('EngageAll', 3.000000, 0)
    UI.AddTask('Patrol', 2.000000, 0)
    BB = UI.GetBlackboardInterface()
    
    unit = SM.GetDefaultUnit()
    unit.className = 'Airstrip'
    unit.unitName = "Esfahan AB"
    unit.SetPosition(51.720000, 32.650000, 0.0)
    unit.heading = 225.00
    unit.speed = 0.0
    SM.AddUnitToAlliance(unit, 2)
    UI = SM.GetUnitInterface(unit.unitName)
    SM.AddToUnitMagazine("Esfahan AB", 'Fuel', 1000000)
    SM.AddToUnitMagazine("Esfahan AB", 'Chaff-1', 10110)
    SM.AddToUnitMagazine("Esfahan AB", 'Flare-1', 10110)
    SM.AddToUnitMagazine("Esfahan AB", '1520 Liter Tank', 100)
    SM.AddToUnitMagazine("Esfahan AB", 'FAB-100', 610)
    SM.AddToUnitMagazine("Esfahan AB", 'FAB-250', 310)
    SM.AddToUnitMagazine("Esfahan AB", 'FAB-500', 340)
    SM.AddToUnitMagazine("Esfahan AB", 'R-27R', 200)
    SM.AddToUnitMagazine("Esfahan AB", 'R-27T', 100)
    SM.AddToUnitMagazine("Esfahan AB", 'R-60M', 200)
    SM.AddToUnitMagazine("Esfahan AB", 'R-60MK', 100)
    SM.AddToUnitMagazine("Esfahan AB", 'R-60T', 100)
    SM.AddToUnitMagazine("Esfahan AB", 'R-60U', 100)
    SM.AddToUnitMagazine("Esfahan AB", 'R-73', 180)
    SM.AddToUnitMagazine("Esfahan AB", 'R-73M', 100)
    SM.AddToUnitMagazine("Esfahan AB", 'R-73M2', 100)
    SM.AddToUnitMagazine("Esfahan AB", 'R-73U', 20)
    SM.AddToUnitMagazine("Esfahan AB", 'AIM-54C', 100)
    SM.AddToUnitMagazine("Esfahan AB", 'AIM-7M', 200)
    SM.AddToUnitMagazine("Esfahan AB", 'AIM-9M', 200)
    SM.AddToUnitMagazine("Esfahan AB", 'Kh-22MP', 25)
    SM.AddToUnitMagazine("Esfahan AB", 'Kh-22M', 10)
    UI.AddTask('RefuelAllAircraft', 3.000000, 3)
    BB = UI.GetBlackboardInterface()
    
    SM.AddUnitToFlightDeck('Esfahan AB', 'MiG-29B', 'Wind-1', 1)
    SM.SetFlightDeckUnitLoadout('Esfahan AB', 'Wind-1', '1 1520 Liter Tank;2 R-27R;2 R-73U;2 R-73U;25 Flare-1;25 Chaff-1;')
    
    SM.AddUnitToFlightDeck('Esfahan AB', 'MiG-29B', 'Wind-2', 1)
    SM.SetFlightDeckUnitLoadout('Esfahan AB', 'Wind-2', '1 1520 Liter Tank;2 R-27R;2 R-73U;2 R-73U;25 Flare-1;25 Chaff-1;')
    
    SM.AddUnitToFlightDeck('Esfahan AB', 'MiG-29B', 'Wind-3', 1)
    SM.SetFlightDeckUnitLoadout('Esfahan AB', 'Wind-3', '1 1520 Liter Tank;2 R-27R;2 R-73U;2 R-73U;25 Flare-1;25 Chaff-1;')
    
    SM.AddUnitToFlightDeck('Esfahan AB', 'MiG-29B', 'Wind-4', 1)
    SM.SetFlightDeckUnitLoadout('Esfahan AB', 'Wind-4', '1 1520 Liter Tank;2 R-27R;2 R-73U;2 R-73U;25 Flare-1;25 Chaff-1;')
    
    SM.AddUnitToFlightDeck('Esfahan AB', 'MiG-29B', 'Wind-5', 1)
    SM.SetFlightDeckUnitLoadout('Esfahan AB', 'Wind-5', '1 1520 Liter Tank;2 R-27R;2 R-73U;2 R-73U;25 Flare-1;25 Chaff-1;')
    
    SM.AddUnitToFlightDeck('Esfahan AB', 'MiG-29B', 'Wind-6', 1)
    SM.SetFlightDeckUnitLoadout('Esfahan AB', 'Wind-6', '1 1520 Liter Tank;2 R-27R;2 R-73U;2 R-73U;25 Flare-1;25 Chaff-1;')
    
    SM.AddUnitToFlightDeck('Esfahan AB', 'MiG-29B', 'Wind-7', 1)
    SM.SetFlightDeckUnitLoadout('Esfahan AB', 'Wind-7', '1 1520 Liter Tank;2 R-27R;2 R-73U;2 R-73U;25 Flare-1;25 Chaff-1;')
    
    SM.AddUnitToFlightDeck('Esfahan AB', 'MiG-29B', 'Wind-8', 1)
    SM.SetFlightDeckUnitLoadout('Esfahan AB', 'Wind-8', '1 1520 Liter Tank;2 R-27R;2 R-73U;2 R-73U;25 Flare-1;25 Chaff-1;')
    
    SM.AddUnitToFlightDeck('Esfahan AB', 'MiG-29B', 'Wind-9', 1)
    SM.SetFlightDeckUnitLoadout('Esfahan AB', 'Wind-9', '1 1520 Liter Tank;2 R-27R;2 R-73U;2 R-73U;25 Flare-1;25 Chaff-1;')
    
    SM.AddUnitToFlightDeck('Esfahan AB', 'MiG-29B', 'Wind-10', 1)
    SM.SetFlightDeckUnitLoadout('Esfahan AB', 'Wind-10', '1 1520 Liter Tank;2 R-27R;2 R-73U;2 R-73U;25 Flare-1;25 Chaff-1;')
    
    SM.AddUnitToFlightDeck('Esfahan AB', 'MiG-29B', 'Wind-11', 1)
    SM.SetFlightDeckUnitLoadout('Esfahan AB', 'Wind-11', '1 1520 Liter Tank;2 R-27R;2 R-73U;2 R-73U;25 Flare-1;25 Chaff-1;')
    
    SM.AddUnitToFlightDeck('Esfahan AB', 'MiG-29B', 'Wind-12', 1)
    SM.SetFlightDeckUnitLoadout('Esfahan AB', 'Wind-12', '1 1520 Liter Tank;2 R-27R;2 R-73U;2 R-73U;25 Flare-1;25 Chaff-1;')
    
    SM.AddUnitToFlightDeck('Esfahan AB', 'MiG-29B', 'Wind-13', 1)
    SM.SetFlightDeckUnitLoadout('Esfahan AB', 'Wind-13', '1 1520 Liter Tank;2 R-27R;2 R-73U;2 R-73U;25 Flare-1;25 Chaff-1;')
    
    SM.AddUnitToFlightDeck('Esfahan AB', 'MiG-29B', 'Wind-14', 1)
    SM.SetFlightDeckUnitLoadout('Esfahan AB', 'Wind-14', '1 1520 Liter Tank;2 R-27R;2 R-73U;2 R-73U;25 Flare-1;25 Chaff-1;')
    
    SM.AddUnitToFlightDeck('Esfahan AB', 'MiG-29B', 'Wind-15', 1)
    SM.SetFlightDeckUnitLoadout('Esfahan AB', 'Wind-15', '1 1520 Liter Tank;2 R-27R;2 R-73U;2 R-73U;25 Flare-1;25 Chaff-1;')
    
    SM.AddUnitToFlightDeck('Esfahan AB', 'MiG-29B', 'Wind-16', 1)
    SM.SetFlightDeckUnitLoadout('Esfahan AB', 'Wind-16', '1 1520 Liter Tank;2 R-27R;2 R-73U;2 R-73U;25 Flare-1;25 Chaff-1;')
    
    SM.AddUnitToFlightDeck('Esfahan AB', 'MiG-29B', 'Wind-17', 1)
    SM.SetFlightDeckUnitLoadout('Esfahan AB', 'Wind-17', '1 1520 Liter Tank;2 R-27R;2 R-73U;2 R-73U;25 Flare-1;25 Chaff-1;')
    
    SM.AddUnitToFlightDeck('Esfahan AB', 'MiG-29B', 'Wind-18', 1)
    SM.SetFlightDeckUnitLoadout('Esfahan AB', 'Wind-18', '1 1520 Liter Tank;2 R-27R;2 R-73U;2 R-73U;25 Flare-1;25 Chaff-1;')
    
    SM.AddUnitToFlightDeck('Esfahan AB', 'MiG-29B', 'Wind-19', 1)
    SM.SetFlightDeckUnitLoadout('Esfahan AB', 'Wind-19', '1 1520 Liter Tank;2 R-27R;2 R-73U;2 R-73U;25 Flare-1;25 Chaff-1;')
    
    SM.AddUnitToFlightDeck('Esfahan AB', 'MiG-29B', 'Wind-20', 1)
    SM.SetFlightDeckUnitLoadout('Esfahan AB', 'Wind-20', '1 1520 Liter Tank;2 R-27R;2 R-73U;2 R-73U;25 Flare-1;25 Chaff-1;')
    
    SM.AddUnitToFlightDeck('Esfahan AB', 'F-14B', 'Storm-1', 2)
    SM.SetFlightDeckUnitLoadout('Esfahan AB', 'Storm-1', '32 20mm PGU;4 AIM-7F;2 AIM-9L;2 AIM-54A;25 Flare-1;25 Chaff-1;')
    
    SM.AddUnitToFlightDeck('Esfahan AB', 'F-14B', 'Storm-2', 2)
    SM.SetFlightDeckUnitLoadout('Esfahan AB', 'Storm-2', '32 20mm PGU;4 AIM-7F;2 AIM-9L;2 AIM-54A;25 Flare-1;25 Chaff-1;')
    
    SM.AddUnitToFlightDeck('Esfahan AB', 'F-14B', 'Storm-3', 2)
    SM.SetFlightDeckUnitLoadout('Esfahan AB', 'Storm-3', '32 20mm PGU;4 AIM-7F;2 AIM-9L;2 AIM-54A;25 Flare-1;25 Chaff-1;')
    
    SM.AddUnitToFlightDeck('Esfahan AB', 'F-14B', 'Storm-4', 2)
    SM.SetFlightDeckUnitLoadout('Esfahan AB', 'Storm-4', '32 20mm PGU;4 AIM-7F;2 AIM-9L;2 AIM-54A;25 Flare-1;25 Chaff-1;')
    
    SM.AddUnitToFlightDeck('Esfahan AB', 'F-14B', 'Storm-5', 2)
    SM.SetFlightDeckUnitLoadout('Esfahan AB', 'Storm-5', '32 20mm PGU;4 AIM-7F;2 AIM-9L;2 AIM-54A;25 Flare-1;25 Chaff-1;')
    
    SM.AddUnitToFlightDeck('Esfahan AB', 'F-14B', 'Storm-6', 2)
    SM.SetFlightDeckUnitLoadout('Esfahan AB', 'Storm-6', '32 20mm PGU;4 AIM-7F;2 AIM-9L;2 AIM-54A;25 Flare-1;25 Chaff-1;')
    
    SM.AddUnitToFlightDeck('Esfahan AB', 'F-14B', 'Storm-7', 2)
    SM.SetFlightDeckUnitLoadout('Esfahan AB', 'Storm-7', '32 20mm PGU;4 AIM-7F;2 AIM-9L;2 AIM-54A;25 Flare-1;25 Chaff-1;')
    
    SM.AddUnitToFlightDeck('Esfahan AB', 'F-14B', 'Storm-8', 2)
    SM.SetFlightDeckUnitLoadout('Esfahan AB', 'Storm-8', '32 20mm PGU;4 AIM-7F;2 AIM-9L;2 AIM-54A;25 Flare-1;25 Chaff-1;')
    
    SM.AddUnitToFlightDeck('Esfahan AB', 'F-14B', 'Storm-9', 1)
    SM.SetFlightDeckUnitLoadout('Esfahan AB', 'Storm-9', '32 20mm PGU;4 AIM-7F;2 AIM-9L;2 AIM-54A;25 Flare-1;25 Chaff-1;')
    
    SM.AddUnitToFlightDeck('Esfahan AB', 'F-14B', 'Storm-10', 1)
    SM.SetFlightDeckUnitLoadout('Esfahan AB', 'Storm-10', '32 20mm PGU;4 AIM-7F;2 AIM-9L;2 AIM-54A;25 Flare-1;25 Chaff-1;')
    
    SM.AddUnitToFlightDeck('Esfahan AB', 'F-14B', 'Storm-11', 1)
    SM.SetFlightDeckUnitLoadout('Esfahan AB', 'Storm-11', '32 20mm PGU;4 AIM-7F;2 AIM-9L;2 AIM-54A;25 Flare-1;25 Chaff-1;')
    
    SM.AddUnitToFlightDeck('Esfahan AB', 'F-14B', 'Storm-12', 1)
    SM.SetFlightDeckUnitLoadout('Esfahan AB', 'Storm-12', '32 20mm PGU;4 AIM-7F;2 AIM-9L;2 AIM-54A;25 Flare-1;25 Chaff-1;')
    FP = UI.GetFlightPortInfo()
    base_track = UI.GetTrackById(UI.GetPlatformId())
    
    mission_id = FP.AddGenericMission()
    FP.AddAircraftToMission(mission_id, 'Storm-1')
    FP.AddAircraftToMission(mission_id, 'Storm-2')
    FP.AddAircraftToMission(mission_id, 'Storm-3')
    FP.AddAircraftToMission(mission_id, 'Storm-4')
    FP.AddAircraftToMission(mission_id, 'Storm-5')
    FP.AddAircraftToMission(mission_id, 'Storm-6')
    FP.AddAircraftToMission(mission_id, 'Storm-7')
    FP.AddAircraftToMission(mission_id, 'Storm-8')
    FP.AddAircraftToMission(mission_id, 'Storm-9')
    FP.AddAircraftToMission(mission_id, 'Storm-10')
    FP.AddAircraftToMission(mission_id, 'Storm-11')
    FP.AddAircraftToMission(mission_id, 'Storm-12')
    FP.SetMissionLaunchTime(mission_id, '10:00:00+0m+R1.0')
    FP.SetMissionDatum(mission_id, 0.0000000, 0.0000000)
    FP.SetMissionLandingTarget(mission_id, '')
    FP.SetMissionWaveQuantity(mission_id, 4)
    FP.SetMissionType(mission_id, '')
    FP.SetMissionPatrolArea(mission_id, '-0.0288250,0.0125784,-0.0275346,0.0220158,0.0057857,0.0312745,0.0125701,0.0252366,')
    FP.SetMissionPatrolAnchor(mission_id, 'Esfahan AB', 2)
    FP.AddMissionWaypointAdvanced(mission_id, 0.9042920, 0.5690750, 4000.0, 200.0)
    FP.SetMissionWaypointTasks(mission_id, 0, 'WaitForGroup,EngageAll')
    FP.AddMissionWaypointAdvanced(mission_id, 0.8988980, 0.5497470, 5000.0, 300.0)
    FP.SetMissionWaypointTasks(mission_id, 1, 'AirPatrolArea,EngageAll')
    
    mission_id = FP.AddGenericMission()
    FP.AddAircraftToMission(mission_id, 'Wind-1')
    FP.AddAircraftToMission(mission_id, 'Wind-2')
    FP.AddAircraftToMission(mission_id, 'Wind-3')
    FP.AddAircraftToMission(mission_id, 'Wind-4')
    FP.AddAircraftToMission(mission_id, 'Wind-5')
    FP.AddAircraftToMission(mission_id, 'Wind-6')
    FP.AddAircraftToMission(mission_id, 'Wind-7')
    FP.AddAircraftToMission(mission_id, 'Wind-8')
    FP.AddAircraftToMission(mission_id, 'Wind-9')
    FP.AddAircraftToMission(mission_id, 'Wind-10')
    FP.AddAircraftToMission(mission_id, 'Wind-11')
    FP.AddAircraftToMission(mission_id, 'Wind-12')
    FP.SetMissionLaunchTime(mission_id, '11:00:00+0m')
    FP.SetMissionDatum(mission_id, 0.0000000, 0.0000000)
    FP.SetMissionLandingTarget(mission_id, '')
    FP.SetMissionWaveQuantity(mission_id, 4)
    FP.SetMissionType(mission_id, '')
    FP.SetMissionPatrolArea(mission_id, '0.8970430,0.5719616,0.9077772,0.5608488,0.9371099,0.5474962,0.9492580,0.5475794,')
    FP.AddMissionWaypointAdvanced(mission_id, 0.9054200, 0.5717920, 5000.0, 200.0)
    FP.SetMissionWaypointTasks(mission_id, 0, 'WaitForGroup,EngageAll')
    FP.AddMissionWaypointAdvanced(mission_id, 0.9206680, 0.5618240, 5000.0, 300.0)
    FP.SetMissionWaypointTasks(mission_id, 1, 'AirPatrolArea,EngageAll')
    
    mission_id = FP.AddGenericMission()
    FP.AddAircraftToMission(mission_id, 'Wind-13')
    FP.AddAircraftToMission(mission_id, 'Wind-14')
    FP.AddAircraftToMission(mission_id, 'Wind-15')
    FP.AddAircraftToMission(mission_id, 'Wind-16')
    FP.AddAircraftToMission(mission_id, 'Wind-17')
    FP.AddAircraftToMission(mission_id, 'Wind-18')
    FP.AddAircraftToMission(mission_id, 'Wind-19')
    FP.AddAircraftToMission(mission_id, 'Wind-20')
    FP.SetMissionLaunchTime(mission_id, '11:00:00+0m')
    FP.SetMissionDatum(mission_id, 0.0000000, 0.0000000)
    FP.SetMissionLandingTarget(mission_id, '')
    FP.SetMissionWaveQuantity(mission_id, 4)
    FP.SetMissionType(mission_id, 'Standby-AAW')
    FP.AddMissionWaypointAdvanced(mission_id, 0.9014620, 0.5713720, 6000.0, 200.0)
    FP.SetMissionWaypointTasks(mission_id, 0, 'WaitForGroup')
    FP.AddMissionWaypointAdvanced(mission_id, 0.9135410, 0.5581730, 6000.0, 0.0)
    FP.AddMissionWaypointAdvanced(mission_id, 0.8993750, 0.5659430, 7000.0, 300.0)
    FP.SetMissionWaypointTasks(mission_id, 2, 'BarrierPatrol,EngageAll,RTB')
    FP.AddMissionWaypointAdvanced(mission_id, 0.8969280, 0.5684880, 7000.0, 300.0)
    FP.AddMissionWaypointAdvanced(mission_id, 0.8905470, 0.5777170, 8000.0, 300.0)
    FP.AddMissionWaypointAdvanced(mission_id, 0.9017830, 0.5700150, 4000.0, 300.0)
    FP.SetMissionWaypointTasks(mission_id, 5, 'Land')
    
    unit = SM.GetDefaultUnit()
    unit.className = 'Airstrip'
    unit.unitName = "Shiraz AB"
    unit.SetPosition(52.500000, 29.650000, 15.0)
    unit.heading = 315.00
    unit.speed = 0.0
    SM.AddUnitToAlliance(unit, 2)
    UI = SM.GetUnitInterface(unit.unitName)
    SM.AddToUnitMagazine("Shiraz AB", 'Fuel', 1100000)
    SM.AddToUnitMagazine("Shiraz AB", 'AIM-9M', 56)
    SM.AddToUnitMagazine("Shiraz AB", 'AAM-SR', 32)
    SM.AddToUnitMagazine("Shiraz AB", 'R-27R', 24)
    SM.AddToUnitMagazine("Shiraz AB", 'R-60', 24)
    SM.AddToUnitMagazine("Shiraz AB", 'R-40R', 24)
    SM.AddToUnitMagazine("Shiraz AB", 'Mk-82', 172)
    SM.AddToUnitMagazine("Shiraz AB", 'AIM-7M', 100)
    SM.AddToUnitMagazine("Shiraz AB", 'Mk-84', 100)
    SM.AddToUnitMagazine("Shiraz AB", 'AGM-65D', 52)
    UI.AddTask('RefuelAllAircraft', 3.000000, 3)
    BB = UI.GetBlackboardInterface()
    
    SM.AddUnitToFlightDeck('Shiraz AB', 'F-5E', 'Sky-1', 2)
    SM.SetFlightDeckUnitLoadout('Shiraz AB', 'Sky-1', '2 AIM-9M;2 AIM-7M;4 AGM-65D;')
    
    SM.AddUnitToFlightDeck('Shiraz AB', 'F-5E', 'Sky-2', 2)
    SM.SetFlightDeckUnitLoadout('Shiraz AB', 'Sky-2', '2 AIM-9M;2 AIM-7M;4 AGM-65D;')
    
    SM.AddUnitToFlightDeck('Shiraz AB', 'F-5E', 'Sky-3', 2)
    SM.SetFlightDeckUnitLoadout('Shiraz AB', 'Sky-3', '2 AIM-9M;2 AIM-7M;4 AGM-65D;')
    
    SM.AddUnitToFlightDeck('Shiraz AB', 'F-5E', 'Sky-4', 2)
    SM.SetFlightDeckUnitLoadout('Shiraz AB', 'Sky-4', '2 AIM-9M;2 AIM-7M;4 AGM-65D;')
    
    SM.AddUnitToFlightDeck('Shiraz AB', 'F-5E', 'Sky-5', 2)
    SM.SetFlightDeckUnitLoadout('Shiraz AB', 'Sky-5', '2 AIM-9M;2 AIM-7M;4 AGM-65D;')
    
    SM.AddUnitToFlightDeck('Shiraz AB', 'F-5E', 'Sky-6', 2)
    SM.SetFlightDeckUnitLoadout('Shiraz AB', 'Sky-6', '2 AIM-9M;2 AIM-7M;4 AGM-65D;')
    
    SM.AddUnitToFlightDeck('Shiraz AB', 'F-5E', 'Sky-7', 1)
    SM.SetFlightDeckUnitLoadout('Shiraz AB', 'Sky-7', '2 AIM-9M;2 AIM-7M;4 AGM-65D;')
    
    SM.AddUnitToFlightDeck('Shiraz AB', 'F-5E', 'Sky-8', 1)
    SM.SetFlightDeckUnitLoadout('Shiraz AB', 'Sky-8', '2 AIM-9M;2 AIM-7M;4 AGM-65D;')
    
    SM.AddUnitToFlightDeck('Shiraz AB', 'F-5E', 'Sky-9', 1)
    SM.SetFlightDeckUnitLoadout('Shiraz AB', 'Sky-9', '2 AIM-9M;2 AIM-7M;4 AGM-65D;')
    
    SM.AddUnitToFlightDeck('Shiraz AB', 'F-5E', 'Sky-10', 1)
    SM.SetFlightDeckUnitLoadout('Shiraz AB', 'Sky-10', '2 AIM-9M;2 AIM-7M;4 AGM-65D;')
    
    SM.AddUnitToFlightDeck('Shiraz AB', 'F-5E', 'Sky-11', 1)
    SM.SetFlightDeckUnitLoadout('Shiraz AB', 'Sky-11', '2 AIM-9M;2 AIM-7M;4 AGM-65D;')
    
    SM.AddUnitToFlightDeck('Shiraz AB', 'F-5E', 'Sky-12', 1)
    SM.SetFlightDeckUnitLoadout('Shiraz AB', 'Sky-12', '2 AIM-9M;2 AIM-7M;4 AGM-65D;')
    FP = UI.GetFlightPortInfo()
    base_track = UI.GetTrackById(UI.GetPlatformId())
    
    mission_id = FP.AddGenericMission()
    FP.AddAircraftToMission(mission_id, 'Sky-7')
    FP.AddAircraftToMission(mission_id, 'Sky-8')
    FP.AddAircraftToMission(mission_id, 'Sky-9')
    FP.AddAircraftToMission(mission_id, 'Sky-10')
    FP.AddAircraftToMission(mission_id, 'Sky-11')
    FP.AddAircraftToMission(mission_id, 'Sky-12')
    FP.SetMissionLaunchTime(mission_id, '10:00:00+0m')
    FP.SetMissionDatum(mission_id, 0.0000000, 0.0000000)
    FP.SetMissionLandingTarget(mission_id, '')
    FP.SetMissionWaveQuantity(mission_id, 6)
    FP.SetMissionType(mission_id, '')
    
    mission_id = FP.AddGenericMission()
    FP.AddAircraftToMission(mission_id, 'Sky-2')
    FP.AddAircraftToMission(mission_id, 'Sky-3')
    FP.AddAircraftToMission(mission_id, 'Sky-1')
    FP.AddAircraftToMission(mission_id, 'Sky-4')
    FP.AddAircraftToMission(mission_id, 'Sky-5')
    FP.AddAircraftToMission(mission_id, 'Sky-6')
    FP.SetMissionLaunchTime(mission_id, '10:30:00+0m+R0.5')
    FP.SetMissionDatum(mission_id, 0.0000000, 0.0000000)
    FP.SetMissionLandingTarget(mission_id, '')
    FP.SetMissionWaveQuantity(mission_id, 2)
    FP.SetMissionType(mission_id, '')
    FP.SetMissionPatrolArea(mission_id, '0.9149202,0.5069469,0.8970641,0.5270270,0.8986753,0.5176291,0.9065010,0.5093165,')
    FP.AddMissionWaypointAdvanced(mission_id, 0.9147930, 0.5196150, 4000.0, 200.0)
    FP.SetMissionWaypointTasks(mission_id, 0, 'WaitForGroup,EngageAll')
    FP.AddMissionWaypointAdvanced(mission_id, 0.9083050, 0.5155330, 5000.0, 300.0)
    FP.SetMissionWaypointTasks(mission_id, 1, 'AirPatrolArea,EngageAll')
    
    unit = SM.GetDefaultUnit()
    unit.className = 'E-2T'
    unit.unitName = "SandEye1-1"
    unit.SetPosition(52.719000, 32.650000, 10.0)
    unit.heading = 315.00
    unit.speed = 250.0
    SM.AddUnitToAlliance(unit, 2)
    UI = SM.GetUnitInterface(unit.unitName)
    UI.AddTask('AirEvade', 3.000000, 3)
    UI.AddTask('Nav', 1.000000, 0)
    UI.AddNavWaypointAdvanced(0.920033, 0.569850, 0.000000, 0.000000)
    UI.AddTask('PatrolCircle', 1.000000, 0)
    UI.AddTask('RTB', 2.000000, 3)
    BB = UI.GetBlackboardInterface()
    BB.Write('StationAltitude', '1920.640015')
    BB.Write('StationLatitude', '0.569850')
    BB.Write('StationLongitude', '0.920033')
    
    unit = SM.GetDefaultUnit()
    unit.className = 'E-2T'
    unit.unitName = "SandEye2-1"
    unit.SetPosition(52.592942, 29.472376, 4120.8)
    unit.heading = 315.00
    unit.speed = 250.0
    SM.AddUnitToAlliance(unit, 2)
    UI = SM.GetUnitInterface(unit.unitName)
    UI.AddTask('AirEvade', 3.000000, 3)
    UI.AddTask('PatrolCircle', 1.000000, 0)
    UI.AddTask('RTB', 2.000000, 3)
    BB = UI.GetBlackboardInterface()
    BB.Write('StationAltitude', '1629.920044')
    BB.Write('StationLatitude', '0.517902')
    BB.Write('StationLongitude', '0.919327')
    
    unit = SM.GetDefaultUnit()
    unit.className = 'F-5E'
    unit.unitName = "Camel-1"
    unit.SetPosition(50.890000, 32.070000, 10.0)
    unit.heading = 12.00
    unit.speed = 200.0
    SM.AddUnitToAlliance(unit, 2)
    SM.SetUnitLauncherItem(unit.unitName, 0, 'AIM-9M', 2)
    SM.SetUnitLauncherItem(unit.unitName, 1, 'AIM-9M', 2)
    SM.SetUnitLauncherItem(unit.unitName, 2, 'Mk-82', 6)
    UI = SM.GetUnitInterface(unit.unitName)
    UI.AddTask('AirEvade', 3.000000, 3)
    UI.AddTask('EngageAll', 3.000000, 0)
    UI.AddTask('PatrolCircle', 1.000000, 0)
    UI.AddTask('RTB', 2.000000, 3)
    UI.AddTask('ReturnToBase', 2.000000, 0)
    BB = UI.GetBlackboardInterface()
    BB.Write('Bingo', '0.450000')
    BB.Write('Home', 'Esfahan AB')
    BB.Write('RTBtime', '5400.000000')
    BB.Write('StationAltitude', '5500.000000')
    BB.Write('StationLatitude', '0.559727')
    BB.Write('StationLongitude', '0.888198')
    UI.SetThrottle(0.500000)
    
    unit = SM.GetDefaultUnit()
    unit.className = 'Su-27'
    unit.unitName = "Desert-2"
    unit.SetPosition(49.290000, 32.450000, 10.0)
    unit.heading = 12.00
    unit.speed = 200.0
    SM.AddUnitToAlliance(unit, 2)
    SM.SetUnitLauncherItem(unit.unitName, 0, 'Kh-31P', 3)
    SM.SetUnitLauncherItem(unit.unitName, 1, 'R-77', 2)
    SM.SetUnitLauncherItem(unit.unitName, 2, 'Kh-31P', 4)
    SM.SetUnitLauncherItem(unit.unitName, 3, 'Flare-1', 25)
    SM.SetUnitLauncherItem(unit.unitName, 4, 'Chaff-1', 25)
    UI = SM.GetUnitInterface(unit.unitName)
    UI.AddTask('AirEvade', 3.000000, 3)
    UI.AddTask('EngageAll', 3.000000, 0)
    UI.AddTask('PatrolCircle', 1.000000, 0)
    UI.AddTask('RTB', 2.000000, 3)
    UI.AddTask('ReturnToBase', 2.000000, 0)
    BB = UI.GetBlackboardInterface()
    BB.Write('Bingo', '0.450000')
    BB.Write('Home', 'Shiraz AB')
    BB.Write('RTBtime', '5400.000000')
    BB.Write('StationAltitude', '5500.000000')
    BB.Write('StationLatitude', '0.566359')
    BB.Write('StationLongitude', '0.860273')
    UI.SetThrottle(0.500000)
    
    unit = SM.GetDefaultUnit()
    unit.className = 'MiG-25'
    unit.unitName = "Lightening-3"
    unit.SetPosition(48.710000, 31.890000, 4962.0)
    unit.heading = 12.00
    unit.speed = 200.0
    SM.AddUnitToAlliance(unit, 2)
    SM.SetUnitLauncherItem(unit.unitName, 0, 'R-60', 2)
    SM.SetUnitLauncherItem(unit.unitName, 1, 'R-60', 2)
    SM.SetUnitLauncherItem(unit.unitName, 2, 'Chaff-1', 25)
    SM.SetUnitLauncherItem(unit.unitName, 3, 'Flare-1', 25)
    UI = SM.GetUnitInterface(unit.unitName)
    UI.AddTask('AirEvade', 3.000000, 3)
    UI.AddTask('EngageAll', 3.000000, 0)
    UI.AddTask('PatrolCircle', 1.000000, 0)
    UI.AddTask('RTB', 2.000000, 3)
    UI.AddTask('ReturnToBase', 2.000000, 0)
    BB = UI.GetBlackboardInterface()
    BB.Write('Bingo', '0.450000')
    BB.Write('Home', 'Esfahan AB')
    BB.Write('RTBtime', '5400.000000')
    BB.Write('StationAltitude', '5500.000000')
    BB.Write('StationLatitude', '0.556585')
    BB.Write('StationLongitude', '0.850150')
    UI.SetThrottle(0.500000)
    
    unit = SM.GetDefaultUnit()
    unit.className = 'MiG-25'
    unit.unitName = "Lightening-4"
    unit.SetPosition(52.130000, 31.280000, 10.0)
    unit.heading = 12.00
    unit.speed = 200.0
    SM.AddUnitToAlliance(unit, 2)
    SM.SetUnitLauncherItem(unit.unitName, 0, 'R-60', 2)
    SM.SetUnitLauncherItem(unit.unitName, 1, 'R-60', 2)
    SM.SetUnitLauncherItem(unit.unitName, 2, 'Chaff-1', 25)
    SM.SetUnitLauncherItem(unit.unitName, 3, 'Flare-1', 25)
    UI = SM.GetUnitInterface(unit.unitName)
    UI.AddTask('AirEvade', 3.000000, 3)
    UI.AddTask('EngageAll', 2.000000, 0)
    UI.AddTask('PatrolCircle', 1.000000, 0)
    UI.AddTask('RTB', 2.000000, 3)
    BB = UI.GetBlackboardInterface()
    BB.Write('Bingo', '0.450000')
    BB.Write('Home', 'Shiraz AB')
    BB.Write('LandTarget', 'Shiraz AB')
    BB.Write('RTBtime', '5400.000000')
    BB.Write('StationAltitude', '5500.000000')
    BB.Write('StationLatitude', '0.544739')
    BB.Write('StationLongitude', '0.904586')
    UI.SetThrottle(0.500000)
    
    unit = SM.GetDefaultUnit()
    unit.className = 'Su-30MKK'
    unit.unitName = "Sand-5"
    unit.SetPosition(52.280000, 30.310000, 10.0)
    unit.heading = 12.00
    unit.speed = 200.0
    SM.AddUnitToAlliance(unit, 2)
    SM.SetUnitLauncherItem(unit.unitName, 0, 'Kh-29T', 4)
    SM.SetUnitLauncherItem(unit.unitName, 1, 'R-77', 2)
    SM.SetUnitLauncherItem(unit.unitName, 2, 'R-77', 4)
    SM.SetUnitLauncherItem(unit.unitName, 3, 'Flare-1', 25)
    SM.SetUnitLauncherItem(unit.unitName, 4, 'Chaff-1', 25)
    UI = SM.GetUnitInterface(unit.unitName)
    UI.AddTask('AirEvade', 3.000000, 3)
    UI.AddTask('EngageAll', 3.000000, 0)
    UI.AddTask('PatrolCircle', 1.000000, 0)
    UI.AddTask('RTB', 2.000000, 3)
    UI.AddTask('ReturnToBase', 2.000000, 0)
    BB = UI.GetBlackboardInterface()
    BB.Write('Bingo', '0.450000')
    BB.Write('Home', 'Shiraz AB')
    BB.Write('RTBtime', '5400.000000')
    BB.Write('StationAltitude', '5500.000000')
    BB.Write('StationLatitude', '0.529009')
    BB.Write('StationLongitude', '0.912458')
    UI.SetThrottle(0.500000)
    
    unit = SM.GetDefaultUnit()
    unit.className = 'Su-27'
    unit.unitName = "Desert-6"
    unit.SetPosition(49.700000, 33.390000, 10.0)
    unit.heading = 12.00
    unit.speed = 200.0
    SM.AddUnitToAlliance(unit, 2)
    SM.SetUnitLauncherItem(unit.unitName, 0, 'Kh-31P', 3)
    SM.SetUnitLauncherItem(unit.unitName, 1, 'R-77', 2)
    SM.SetUnitLauncherItem(unit.unitName, 2, 'Kh-31P', 4)
    SM.SetUnitLauncherItem(unit.unitName, 3, 'Flare-1', 25)
    SM.SetUnitLauncherItem(unit.unitName, 4, 'Chaff-1', 25)
    UI = SM.GetUnitInterface(unit.unitName)
    UI.AddTask('AirEvade', 3.000000, 3)
    UI.AddTask('EngageAll', 3.000000, 0)
    UI.AddTask('PatrolCircle', 1.000000, 0)
    UI.AddTask('RTB', 2.000000, 3)
    UI.AddTask('ReturnToBase', 2.000000, 0)
    BB = UI.GetBlackboardInterface()
    BB.Write('Bingo', '0.450000')
    BB.Write('Home', 'Esfahan AB')
    BB.Write('RTBtime', '5400.000000')
    BB.Write('StationAltitude', '5500.000000')
    BB.Write('StationLatitude', '0.582765')
    BB.Write('StationLongitude', '0.867429')
    UI.SetThrottle(0.500000)
    
    unit = SM.GetDefaultUnit()
    unit.className = 'MiG-25'
    unit.unitName = "Lightening-7"
    unit.SetPosition(52.470000, 32.540000, 10.0)
    unit.heading = 12.00
    unit.speed = 200.0
    SM.AddUnitToAlliance(unit, 2)
    SM.SetUnitLauncherItem(unit.unitName, 0, 'R-60', 2)
    SM.SetUnitLauncherItem(unit.unitName, 1, 'R-60', 2)
    SM.SetUnitLauncherItem(unit.unitName, 2, 'Chaff-1', 25)
    SM.SetUnitLauncherItem(unit.unitName, 3, 'Flare-1', 25)
    UI = SM.GetUnitInterface(unit.unitName)
    UI.AddTask('AirEvade', 3.000000, 3)
    UI.AddTask('EngageAll', 3.000000, 0)
    UI.AddTask('PatrolCircle', 1.000000, 0)
    UI.AddTask('RTB', 2.000000, 3)
    UI.AddTask('ReturnToBase', 2.000000, 0)
    BB = UI.GetBlackboardInterface()
    BB.Write('Bingo', '0.450000')
    BB.Write('Home', 'Esfahan AB')
    BB.Write('RTBtime', '5400.000000')
    BB.Write('StationAltitude', '5500.000000')
    BB.Write('StationLatitude', '0.567930')
    BB.Write('StationLongitude', '0.915774')
    UI.SetThrottle(0.500000)
    
    unit = SM.GetDefaultUnit()
    unit.className = 'MiG-25'
    unit.unitName = "Lightening-8"
    unit.SetPosition(52.120000, 32.650000, 10.0)
    unit.heading = 12.00
    unit.speed = 200.0
    SM.AddUnitToAlliance(unit, 2)
    SM.SetUnitLauncherItem(unit.unitName, 0, 'R-60', 2)
    SM.SetUnitLauncherItem(unit.unitName, 1, 'R-60', 2)
    SM.SetUnitLauncherItem(unit.unitName, 2, 'Chaff-1', 25)
    SM.SetUnitLauncherItem(unit.unitName, 3, 'Flare-1', 25)
    UI = SM.GetUnitInterface(unit.unitName)
    UI.AddTask('AirEvade', 3.000000, 3)
    UI.AddTask('EngageAll', 3.000000, 0)
    UI.AddTask('PatrolCircle', 1.000000, 0)
    UI.AddTask('RTB', 2.000000, 3)
    UI.AddTask('ReturnToBase', 2.000000, 0)
    BB = UI.GetBlackboardInterface()
    BB.Write('Bingo', '0.450000')
    BB.Write('Home', 'Esfahan AB')
    BB.Write('RTBtime', '5400.000000')
    BB.Write('StationAltitude', '5500.000000')
    BB.Write('StationLatitude', '0.569850')
    BB.Write('StationLongitude', '0.909666')
    UI.SetThrottle(0.500000)
    
    unit = SM.GetDefaultUnit()
    unit.className = 'Su-27'
    unit.unitName = "Desert-9"
    unit.SetPosition(49.670000, 31.190000, 2208.0)
    unit.heading = 12.00
    unit.speed = 200.0
    SM.AddUnitToAlliance(unit, 2)
    SM.SetUnitLauncherItem(unit.unitName, 0, 'Kh-31P', 3)
    SM.SetUnitLauncherItem(unit.unitName, 1, 'R-77', 2)
    SM.SetUnitLauncherItem(unit.unitName, 2, 'Kh-31P', 4)
    SM.SetUnitLauncherItem(unit.unitName, 3, 'Flare-1', 25)
    SM.SetUnitLauncherItem(unit.unitName, 4, 'Chaff-1', 25)
    UI = SM.GetUnitInterface(unit.unitName)
    UI.AddTask('AirEvade', 3.000000, 3)
    UI.AddTask('EngageAll', 2.000000, 0)
    UI.AddTask('PatrolCircle', 1.000000, 0)
    UI.AddTask('RTB', 2.000000, 3)
    BB = UI.GetBlackboardInterface()
    BB.Write('Bingo', '0.450000')
    BB.Write('Home', 'Esfahan AB')
    BB.Write('RTBtime', '5400.000000')
    BB.Write('StationAltitude', '5500.000000')
    BB.Write('StationLatitude', '0.516500')
    BB.Write('StationLongitude', '0.876002')
    UI.SetThrottle(0.500000)
    
    unit = SM.GetDefaultUnit()
    unit.className = 'F-5E'
    unit.unitName = "Camel-10"
    unit.SetPosition(49.310000, 33.080000, 10.0)
    unit.heading = 12.00
    unit.speed = 200.0
    SM.AddUnitToAlliance(unit, 2)
    SM.SetUnitLauncherItem(unit.unitName, 0, 'AIM-9M', 2)
    SM.SetUnitLauncherItem(unit.unitName, 1, 'AIM-9M', 2)
    SM.SetUnitLauncherItem(unit.unitName, 2, 'Mk-82', 6)
    UI = SM.GetUnitInterface(unit.unitName)
    UI.AddTask('AirEvade', 3.000000, 3)
    UI.AddTask('EngageAll', 3.000000, 0)
    UI.AddTask('PatrolCircle', 1.000000, 0)
    UI.AddTask('RTB', 2.000000, 3)
    UI.AddTask('ReturnToBase', 2.000000, 0)
    BB = UI.GetBlackboardInterface()
    BB.Write('Bingo', '0.450000')
    BB.Write('Home', 'Shiraz AB')
    BB.Write('RTBtime', '5400.000000')
    BB.Write('StationAltitude', '5500.000000')
    BB.Write('StationLatitude', '0.577355')
    BB.Write('StationLongitude', '0.860622')
    UI.SetThrottle(0.500000)
    
    unit = SM.GetDefaultUnit()
    unit.className = 'Mirage-F1'
    unit.unitName = "Dune-11"
    unit.SetPosition(51.940000, 30.330000, 10.0)
    unit.heading = 12.00
    unit.speed = 200.0
    SM.AddUnitToAlliance(unit, 2)
    SM.SetUnitLauncherItem(unit.unitName, 0, 'AIM-9M', 1)
    SM.SetUnitLauncherItem(unit.unitName, 1, 'AIM-9M', 1)
    SM.SetUnitLauncherItem(unit.unitName, 2, 'AIM-9M', 1)
    SM.SetUnitLauncherItem(unit.unitName, 3, 'AIM-9M', 1)
    SM.SetUnitLauncherItem(unit.unitName, 4, 'AIM-9M', 1)
    SM.SetUnitLauncherItem(unit.unitName, 5, 'AIM-9M', 1)
    SM.SetUnitLauncherItem(unit.unitName, 6, 'AM-39 Exocet', 1)
    UI = SM.GetUnitInterface(unit.unitName)
    UI.AddTask('AirEvade', 3.000000, 3)
    UI.AddTask('EngageAll', 3.000000, 0)
    UI.AddTask('PatrolCircle', 1.000000, 0)
    UI.AddTask('RTB', 2.000000, 3)
    UI.AddTask('ReturnToBase', 2.000000, 0)
    BB = UI.GetBlackboardInterface()
    BB.Write('Bingo', '0.450000')
    BB.Write('Home', 'Esfahan AB')
    BB.Write('RTBtime', '5400.000000')
    BB.Write('StationAltitude', '5500.000000')
    BB.Write('StationLatitude', '0.529358')
    BB.Write('StationLongitude', '0.906524')
    UI.SetThrottle(0.500000)
    
    unit = SM.GetDefaultUnit()
    unit.className = 'Su-27'
    unit.unitName = "Desert-12"
    unit.SetPosition(53.540000, 33.380000, 10.0)
    unit.heading = 12.00
    unit.speed = 200.0
    SM.AddUnitToAlliance(unit, 2)
    SM.SetUnitLauncherItem(unit.unitName, 0, 'Kh-31P', 3)
    SM.SetUnitLauncherItem(unit.unitName, 1, 'R-77', 2)
    SM.SetUnitLauncherItem(unit.unitName, 2, 'Kh-31P', 4)
    SM.SetUnitLauncherItem(unit.unitName, 3, 'Flare-1', 25)
    SM.SetUnitLauncherItem(unit.unitName, 4, 'Chaff-1', 25)
    UI = SM.GetUnitInterface(unit.unitName)
    UI.AddTask('AirEvade', 3.000000, 3)
    UI.AddTask('EngageAll', 3.000000, 0)
    UI.AddTask('PatrolCircle', 1.000000, 0)
    UI.AddTask('RTB', 2.000000, 3)
    UI.AddTask('ReturnToBase', 2.000000, 0)
    BB = UI.GetBlackboardInterface()
    BB.Write('Bingo', '0.450000')
    BB.Write('Home', 'Shiraz AB')
    BB.Write('RTBtime', '5400.000000')
    BB.Write('StationAltitude', '5500.000000')
    BB.Write('StationLatitude', '0.582591')
    BB.Write('StationLongitude', '0.934449')
    UI.SetThrottle(0.500000)
    
    unit = SM.GetDefaultUnit()
    unit.className = 'Su-30MKK'
    unit.unitName = "Sand-13"
    unit.SetPosition(53.270000, 33.400000, 10.0)
    unit.heading = 12.00
    unit.speed = 200.0
    SM.AddUnitToAlliance(unit, 2)
    SM.SetUnitLauncherItem(unit.unitName, 0, 'Kh-29T', 4)
    SM.SetUnitLauncherItem(unit.unitName, 1, 'R-77', 2)
    SM.SetUnitLauncherItem(unit.unitName, 2, 'R-77', 4)
    SM.SetUnitLauncherItem(unit.unitName, 3, 'Flare-1', 25)
    SM.SetUnitLauncherItem(unit.unitName, 4, 'Chaff-1', 25)
    UI = SM.GetUnitInterface(unit.unitName)
    UI.AddTask('AirEvade', 3.000000, 3)
    UI.AddTask('EngageAll', 3.000000, 0)
    UI.AddTask('PatrolCircle', 1.000000, 0)
    UI.AddTask('RTB', 2.000000, 3)
    UI.AddTask('ReturnToBase', 2.000000, 0)
    BB = UI.GetBlackboardInterface()
    BB.Write('Bingo', '0.450000')
    BB.Write('Home', 'Esfahan AB')
    BB.Write('RTBtime', '5400.000000')
    BB.Write('StationAltitude', '5500.000000')
    BB.Write('StationLatitude', '0.582940')
    BB.Write('StationLongitude', '0.929737')
    UI.SetThrottle(0.500000)
    
    unit = SM.GetDefaultUnit()
    unit.className = 'Mirage-F1'
    unit.unitName = "Dune-14"
    unit.SetPosition(48.810000, 33.270000, 10.0)
    unit.heading = 12.00
    unit.speed = 200.0
    SM.AddUnitToAlliance(unit, 2)
    SM.SetUnitLauncherItem(unit.unitName, 0, 'AIM-9M', 1)
    SM.SetUnitLauncherItem(unit.unitName, 1, 'AIM-9M', 1)
    SM.SetUnitLauncherItem(unit.unitName, 2, 'AIM-9M', 1)
    SM.SetUnitLauncherItem(unit.unitName, 3, 'AIM-9M', 1)
    SM.SetUnitLauncherItem(unit.unitName, 4, 'AIM-9M', 1)
    SM.SetUnitLauncherItem(unit.unitName, 5, 'AIM-9M', 1)
    SM.SetUnitLauncherItem(unit.unitName, 6, 'AM-39 Exocet', 1)
    UI = SM.GetUnitInterface(unit.unitName)
    UI.AddTask('AirEvade', 3.000000, 3)
    UI.AddTask('EngageAll', 3.000000, 0)
    UI.AddTask('PatrolCircle', 1.000000, 0)
    UI.AddTask('RTB', 2.000000, 3)
    UI.AddTask('ReturnToBase', 2.000000, 0)
    BB = UI.GetBlackboardInterface()
    BB.Write('Bingo', '0.450000')
    BB.Write('Home', 'Shiraz AB')
    BB.Write('RTBtime', '5400.000000')
    BB.Write('StationAltitude', '5500.000000')
    BB.Write('StationLatitude', '0.580671')
    BB.Write('StationLongitude', '0.851895')
    UI.SetThrottle(0.500000)
    
    unit = SM.GetDefaultUnit()
    unit.className = 'Pr 12341 Ovod-1'
    unit.unitName = "Iranian Patrol Boat"
    unit.SetPosition(50.164002, 29.402303, 0.0)
    unit.heading = 90.00
    unit.speed = 25.0
    SM.AddUnitToAlliance(unit, 2)
    SM.SetUnitLauncherItem(unit.unitName, 0, 'P-120 Malakhit', 3)
    SM.SetUnitLauncherItem(unit.unitName, 1, 'P-120 Malakhit', 3)
    SM.SetUnitLauncherItem(unit.unitName, 2, '9M33M', 2)
    SM.SetUnitLauncherItem(unit.unitName, 3, '76.2mm OS-62 FRAG', 152)
    SM.SetUnitLauncherItem(unit.unitName, 4, '30mm OF-84 HE-FRAG AK-630M', 59)
    UI = SM.GetUnitInterface(unit.unitName)
    SM.AddToUnitMagazine("Iranian Patrol Boat", '9M33M', 20)
    SM.AddToUnitMagazine("Iranian Patrol Boat", '30mm OF-84 HE-FRAG AK-630M76.2mm OS-62 FRAG', 152)
    UI.AddTask('MissileWarning', 3.000000, 3)
    UI.AddTask('Nav', 1.000000, 0)
    UI.AddNavWaypointAdvanced(0.864965, 0.511959, 0.000000, 0.000000)
    UI.AddNavWaypointAdvanced(0.874915, 0.509409, 0.000000, 0.000000)
    UI.SetNavLoopState(1)
    BB = UI.GetBlackboardInterface()
    
    unit = SM.GetDefaultUnit()
    unit.className = 'Pr 877M Paltus'
    unit.unitName = "Yushen"
    unit.SetPosition(50.434839, 29.133300, -17.6)
    unit.heading = 90.00
    unit.speed = 3.0
    SM.AddUnitToAlliance(unit, 2)
    SM.SetUnitLauncherItem(unit.unitName, 0, '9M32M Strela 3', 1)
    SM.SetUnitLauncherItem(unit.unitName, 1, 'SET-65M', 1)
    SM.SetUnitLauncherItem(unit.unitName, 2, 'SET-65M', 1)
    SM.SetUnitLauncherItem(unit.unitName, 3, 'SET-65M', 1)
    SM.SetUnitLauncherItem(unit.unitName, 4, 'SET-65M', 1)
    SM.SetUnitLauncherItem(unit.unitName, 5, '53-65M', 1)
    SM.SetUnitLauncherItem(unit.unitName, 6, '53-65M', 1)
    UI = SM.GetUnitInterface(unit.unitName)
    SM.AddToUnitMagazine("Yushen", 'SET-65M', 12)
    SM.AddToUnitMagazine("Yushen", '53-65M', 6)
    SM.AddToUnitMagazine("Yushen", '9M32M Strela 3', 8)
    UI.AddTask('EngageAll', 2.000000, 0)
    UI.AddTask('MissileWarning', 0.000000, 0)
    UI.AddTask('Nav', 1.000000, 0)
    UI.AddNavWaypointAdvanced(0.876100, 0.507163, 0.000000, 0.000000)
    UI.AddNavWaypointAdvanced(0.881430, 0.504684, 0.000000, 0.000000)
    UI.SetNavLoopState(1)
    UI.AddTask('SubEvade', 3.000000, 3)
    BB = UI.GetBlackboardInterface()
    
    ##############################
    ### Alliance 1 goals
    ##############################

    goal_temp = SM.DestroyGoal('ISAM-1')
    goal_21_0 = goal_temp

    goal_temp = SM.DestroyGoal('ISAM-2')
    goal_21_1 = goal_temp

    goal_temp = SM.DestroyGoal('ISAM-3')
    goal_21_2 = goal_temp

    goal_temp = SM.DestroyGoal('ISAM-4')
    goal_21_3 = goal_temp

    goal_temp = SM.DestroyGoal('ISAM-5')
    goal_21_4 = goal_temp

    goal_temp = SM.DestroyGoal('ISAM-6')
    goal_21_5 = goal_temp

    goal_temp = SM.DestroyGoal('ISAM-7')
    goal_21_6 = goal_temp

    goal_temp = SM.DestroyGoal('ISAM-8')
    goal_21_7 = goal_temp

    goal_temp = SM.TimeGoal()
    goal_temp.SetPassTimeout(59999999940.0)
    goal_temp.SetFailTimeout(10800.0)
    goal_21_8 = goal_temp

    goal_temp = SM.CompoundGoal(0)
    goal_temp.AddGoal(goal_21_0)
    goal_temp.AddGoal(goal_21_1)
    goal_temp.AddGoal(goal_21_2)
    goal_temp.AddGoal(goal_21_3)
    goal_temp.AddGoal(goal_21_4)
    goal_temp.AddGoal(goal_21_5)
    goal_temp.AddGoal(goal_21_6)
    goal_temp.AddGoal(goal_21_7)
    goal_temp.AddGoal(goal_21_8)
    
    SM.SetAllianceGoal(1, goal_temp)

    SM.SetAllianceROEByType(1, 2, 2, 2, 2)

    ##############################
    ### Alliance 2 goals
    ##############################

    goal_temp = SM.TimeGoal()
    goal_temp.SetPassTimeout(10800.0)
    goal_22_0 = goal_temp

    goal_temp = SM.ProtectGoal('ISAM-1')
    goal_23_0 = goal_temp

    goal_temp = SM.ProtectGoal('ISAM-2')
    goal_23_1 = goal_temp

    goal_temp = SM.ProtectGoal('ISAM-3')
    goal_23_2 = goal_temp

    goal_temp = SM.ProtectGoal('ISAM-4')
    goal_23_3 = goal_temp

    goal_temp = SM.ProtectGoal('ISAM-5')
    goal_23_4 = goal_temp

    goal_temp = SM.ProtectGoal('ISAM-6')
    goal_23_5 = goal_temp

    goal_temp = SM.ProtectGoal('ISAM-7')
    goal_23_6 = goal_temp

    goal_temp = SM.ProtectGoal('ISAM-8')
    goal_23_7 = goal_temp

    goal_temp = SM.CompoundGoal(1)
    goal_temp.AddGoal(goal_23_0)
    goal_temp.AddGoal(goal_23_1)
    goal_temp.AddGoal(goal_23_2)
    goal_temp.AddGoal(goal_23_3)
    goal_temp.AddGoal(goal_23_4)
    goal_temp.AddGoal(goal_23_5)
    goal_temp.AddGoal(goal_23_6)
    goal_temp.AddGoal(goal_23_7)
    
    goal_22_1 = goal_temp

    goal_temp = SM.CompoundGoal(0)
    goal_temp.AddGoal(goal_22_0)
    goal_temp.AddGoal(goal_22_1)
    
    SM.SetAllianceGoal(2, goal_temp)

    SM.SetAllianceROEByType(2, 2, 2, 2, 2)

    ##############################
    ### Overlay Graphics
    ##############################
    SM.OverlayText('Tehran', 51.4800, 35.8000, '0x000000FF')
    SM.OverlayText('Esfahan', 51.7200, 32.6500, '0x000000FF')
    SM.OverlayText('Shiraz', 52.5088, 29.6758, '0x000000FF')
    SM.OverlayText('Yazd', 54.2000, 31.9000, '0x000000FF')
    SM.OverlayText('Ganaveh', 50.4766, 29.6392, '0x000000FF')
    ##############################
    ### Randomization Info
    ##############################
