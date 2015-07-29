# Created on 07/17/15 22:43:23
from math import *
from random import *
from UnitCommands import *

def CreateScenario(SM):

    SM.SetScenarioDescription("""Enter description of scenario.\n""")
    SM.SetScenarioName("""Clutter Initial Test""")
    SM.CreateAlliance(1, 'USA')
    SM.SetAllianceDefaultCountry(1, 'USA')
    SM.SetAlliancePlayable(1, 1)
    SM.CreateAlliance(2, 'Germany')
    SM.SetAllianceDefaultCountry(2, 'Germany')
    SM.SetAlliancePlayable(2, 1)
    SM.SetUserAlliance(2)

    SM.SetDateTime(1990,4,13,0,0,0)
    SM.SetStartTheater(0.529166, 50.470833) # (lon, lat) in degrees, negative is West or South
    SM.SetScenarioLoaded(1)

    SM.SetSeaState(3)

    SM.SetSVP('0.000000,1515.000000,200.000000,1500.000000,300.000000,1510.000000,500.000000,1520.000000,5000.000000,1600.000000')

    ####################
    SM.SetSimpleBriefing(1, """No briefing found""")

    ####################
    SM.SetSimpleBriefing(2, """No briefing found""")

    ##############################
    ### Alliance 1 units
    ##############################

    unit = SM.GetDefaultUnit()
    unit.className = 'Oliver Hazard Perry FFGHM'
    unit.unitName = "USS Lewis B. Puller"
    unit.SetPosition(0.665433, 50.666372, 0.0)
    unit.heading = 90.00
    unit.speed = 29.0
    unit.cost = 0.0
    SM.AddUnitToAlliance(unit, 1)
    SM.SetUnitLauncherItem(unit.unitName, 0, '20mm mark 244-0 ELC', 97)
    SM.SetUnitLauncherItem(unit.unitName, 1, '76mm HE-MOM', 80)
    SM.SetUnitLauncherItem(unit.unitName, 2, 'RIM-66L', 1)
    SM.SetUnitLauncherItem(unit.unitName, 3, 'Mk-46 Mod5', 3)
    SM.SetUnitLauncherItem(unit.unitName, 4, 'Mk-46 Mod5', 3)
    UI = SM.GetUnitInterface(unit.unitName)
    SM.AddToUnitMagazine("USS Lewis B. Puller", '120 gallon tank', 2)
    SM.AddToUnitMagazine("USS Lewis B. Puller", 'AGM-114 Hellfire', 8)
    SM.AddToUnitMagazine("USS Lewis B. Puller", 'Chaff-1', 50)
    SM.AddToUnitMagazine("USS Lewis B. Puller", 'DICASS (85) Sonobuoy', 105)
    SM.AddToUnitMagazine("USS Lewis B. Puller", 'DIFAR (85) Sonobuoy', 315)
    SM.AddToUnitMagazine("USS Lewis B. Puller", 'Flare-1', 50)
    SM.AddToUnitMagazine("USS Lewis B. Puller", 'Fuel', 28058)
    SM.AddToUnitMagazine("USS Lewis B. Puller", 'LOFAR (85) Sonobuoy', 105)
    SM.AddToUnitMagazine("USS Lewis B. Puller", 'Mk-46 Mod5', 22)
    SM.AddToUnitMagazine("USS Lewis B. Puller", 'RGM-84D Harpoon', 4)
    SM.AddToUnitMagazine("USS Lewis B. Puller", 'RIM-66L', 35)
    SM.AddToUnitMagazine("USS Lewis B. Puller", '20mm mark 244-0 ELC', 523)
    SM.AddToUnitMagazine("USS Lewis B. Puller", '76mm HE-MOM', 240)
    UI.SetSensorState(4, 1)
    UI.SetSensorState(5, 1)
    UI.SetSensorState(9, 1)
    UI.SetSensorState(10, 1)
    UI.AddTask('MissileWarning', 3.000000, 3)
    UI.AddTask('PointDefense', 3.000000, 3)
    UI.AddTask('RefuelAllAircraft', 3.000000, 3)
    BB = UI.GetBlackboardInterface()
    
    SM.AddUnitToFlightDeck('USS Lewis B. Puller', 'SH-60B', 'Perry FFG Seahawk 1', 1)
    SM.SetFlightDeckUnitLoadout('USS Lewis B. Puller', 'Perry FFG Seahawk 1', '4 AGM-114 Hellfire;1 120 gallon tank;1 120 gallon tank;25 Chaff-1;25 Chaff-1;5 DICASS (100) Sonobuoy;5 LOFAR (100) Sonobuoy;15 DIFAR (100) Sonobuoy;')
    
    ##############################
    ### Alliance 2 units
    ##############################

    unit = SM.GetDefaultUnit()
    unit.className = 'Tiger Type 148 (1991) FACM'
    unit.unitName = "S55 Alk"
    unit.SetPosition(1.000098, 50.499927, 0.0)
    unit.heading = -36.55
    unit.speed = 28.8
    unit.cost = 0.0
    SM.AddUnitToAlliance(unit, 2)
    SM.SetUnitLauncherItem(unit.unitName, 0, 'MM-38 Exocet', 2)
    SM.SetUnitLauncherItem(unit.unitName, 1, 'MM-38 Exocet', 2)
    SM.SetUnitLauncherItem(unit.unitName, 2, '76mm HE-MOM', 80)
    SM.SetUnitLauncherItem(unit.unitName, 3, '40mm HE-T', 50)
    SM.SetUnitLauncherItem(unit.unitName, 4, 'Silverdog/Wolke Chaff', 6)
    SM.SetUnitLauncherItem(unit.unitName, 5, 'Hotdog Flare', 6)
    SM.SetUnitLauncherItem(unit.unitName, 6, 'Silverdog/Wolke Chaff', 6)
    SM.SetUnitLauncherItem(unit.unitName, 7, 'Hotdog Flare', 6)
    UI = SM.GetUnitInterface(unit.unitName)
    SM.AddToUnitMagazine("S55 Alk", '40mm HE-T', 500)
    SM.AddToUnitMagazine("S55 Alk", '76mm HE-MOM', 240)
    SM.AddToUnitMagazine("S55 Alk", 'Silverdog/Wolke Chaff', 120)
    UI.SetSensorState(1, 1)
    UI.SetSensorState(6, 1)
    UI.SetSensorState(7, 1)
    UI.AddTask('EngageAll', 2.000000, 0)
    UI.AddTask('MissileWarning', 3.000000, 3)
    UI.AddTask('Nav', 1.000000, 0)
    UI.AddNavWaypointAdvanced(0.013550, 0.884714, 0.000000, 0.000000)
    UI.AddTask('PointDefense', 3.000000, 3)
    BB = UI.GetBlackboardInterface()
    
    ##############################
    ### Alliance 1 goals
    ##############################

    goal_temp = SM.TimeGoal()
    goal_temp.SetPassTimeout(36000.0)
    goal_temp.SetFailTimeout(59940.0)
    SM.SetAllianceGoal(1, goal_temp)

    SM.SetAllianceROEByType(1, 2, 2, 2, 2)

    ##############################
    ### Alliance 2 goals
    ##############################

    goal_temp = SM.TimeGoal()
    goal_temp.SetPassTimeout(36000.0)
    goal_temp.SetFailTimeout(59940.0)
    SM.SetAllianceGoal(2, goal_temp)

    SM.SetAllianceROEByType(2, 2, 2, 2, 2)

    ##############################
    ### Overlay Graphics
    ##############################
    ##############################
    ### Randomization Info
    ##############################
    SM.SetIncludeProbability('B-244', 1.000000)
    SM.AddRandomBox('B-244', 1.1088, 1.2830, 50.9586, 51.0115)
    SM.SetIncludeProbability('B-247', 1.000000)
    SM.AddRandomBox('B-247', 1.2194, 1.4316, 50.8291, 50.9169)
    SM.SetIncludeProbability('B-307', 1.000000)
    SM.AddRandomBox('B-307', 1.1276, 1.2971, 50.7459, 50.8381)
    SM.SetIncludeProbability('K-479', 1.000000)
    SM.AddRandomBox('K-479', 1.3183, 1.5278, 50.9593, 51.0173)
