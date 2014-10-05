

def RefuelAllAircraft(TI):
    UI = TI.GetPlatformInterface()
    FP = UI.GetFlightPortInfo()
    if (not FP.IsValid()):
        UI.DisplayMessage('No flightport')
        TI.EndTask()

    TI.SetUpdateInterval(60)

    nUnits = FP.GetUnitCount()
    for n in range(0, nUnits):
        unitStatus = FP.GetUnitStatus(n)
        unitName = unitStatus.name
        unitLoc = unitStatus.current_loc
        UI_n = FP.GetUnitPlatformInterface(n)
        if (UI_n.GetFuel() < 1.0) and (not UI_n.IsRefueling()) and (not UI_n.MaintenanceHold()) and (UI_n.GetWeightMargin() > 10):
            #UI_n.DisplayMessage('Refueling %s' % unitName)
            #UI_n.LoadOther('Fuel')   -LoadOther was changed, now requires quantity to stock.  Determine fuel need before attempting to load.
            name = UI_n.GetPlatformClass()
            if UI_n.HasThrottle():
                fuel_capacity = UI.QueryDatabase('air',name,'FuelCapacity_kg')
            else:
                fuel_capacity = UI.QueryDatabase('simple_air',name,'FuelCapacity_kg')
            fuel_capacity = float(fuel_capacity.GetString(0))
            fuel_qty = int((1 - UI_n.GetFuel()) * fuel_capacity + 1)
            UI_n.LoadOther('Fuel', fuel_qty)
            return # only start one refueling at a time
            


def MaintainCAP(TI):
    UI = TI.GetPlatformInterface()
    FP = UI.GetFlightPortInfo()
    if (not FP.IsValid()):
        UI.DisplayMessage('No flightport')
        TI.EndTask()


######## FlightPort scripts #####
##def BuildFlightPortPanel(UserPanel, FlightPortInfo, UnitInfo):
##    # UnitInfo.DisplayMessage('BuildFlightPortPanelCalled')
##    UserPanel.Clear()
##    UserPanel.SetTitle('Flight Deck Control')
##
##    # draw buttons for heading row
##    UserPanel.AddItem('Unit Type','',10,10,80,12)
##    UserPanel.BoldLastItem()
##    UserPanel.AddItem('Location','',90,10,50,12)
##    UserPanel.BoldLastItem() 
##    UserPanel.AddItem('Dest','',140,10,50,12)
##    UserPanel.BoldLastItem() 
##    UserPanel.AddItem('Move','',190,10,60,12)
##    UserPanel.BoldLastItem() 
##    UserPanel.AddItem('','',250,10,40,12)
##    UserPanel.AddItem('','',290,10,40,12)   
##    nUnits = FlightPortInfo.GetUnitCount()
##    rowy = 22
##    startx = 10
##    for n in range(0, nUnits):
##        rowx = startx
##        # two buttons for unit info
##        unitStatus = FlightPortInfo.GetUnitStatus(n)
##        unitName = unitStatus.name
##        unitLoc = unitStatus.current_loc
##        if (unitStatus.atDestination):
##            unitGoalLoc = '---'
##        else:
##            unitGoalLoc = unitStatus.goal_loc
##            
##        bwidth = 80
##        UserPanel.AddItem(unitName,'',rowx,rowy,bwidth,12)
##        rowx = rowx + bwidth
##        bwidth = 50
##        UserPanel.AddItem(unitLoc,'',rowx,rowy,bwidth,12)
##        rowx = rowx + bwidth
##        UserPanel.AddItem(unitGoalLoc,'',rowx,rowy,bwidth,12)
##        rowx = rowx + bwidth        
##        # buttons to move units to different positions on flight deck
##        # hangar
##        bwidth = 20
##        UserPanel.AddItemWithParam('H','MoveToHangar',n,rowx,rowy,bwidth,12)
##        rowx = rowx + bwidth
##        # Ready (on deck)
##        UserPanel.AddItemWithParam('D','MoveToReady',n,rowx,rowy,bwidth,12)
##        rowx = rowx + bwidth
##        # Runway
##        UserPanel.AddItemWithParam('R','MoveToRunway',n,rowx,rowy,bwidth,12)
##        rowx = rowx + bwidth
##        # Op time
##        bwidth = 40 
##        if (unitStatus.isIdle == 0):
##            current_time = FlightPortInfo.GetCurrentTime()
##            op_time = unitStatus.ready_time
##            delta = op_time - current_time
##            str = '%04.0f' % delta
##        else:
##            str = ''
##        UserPanel.AddItem(str,'',rowx,rowy,bwidth,12)
##        rowx = rowx + bwidth
##        # Launch
##        bwidth = 40        
##        if (unitStatus.runway != -1):
##            cmdstr = 'LaunchRunway%d' % unitStatus.runway
##            UserPanel.AddItem('Launch',cmdstr,rowx,rowy,bwidth,12)
##        else:
##            UserPanel.AddItem('','',rowx,rowy,bwidth,12)
##        rowx = rowx + bwidth
##        
##        rowy = rowy + 12
##
##def LaunchRunway0(FlightPort):
##    LaunchRunway(FlightPort, 0)
##
##def LaunchRunway1(FlightPort):
##    LaunchRunway(FlightPort, 1)
##
##def LaunchRunway2(FlightPort):
##    LaunchRunway(FlightPort, 2)
##
##def LaunchRunway(FlightPort, n):
##    FlightPort.Launch(n)
##
##def MoveToHangar(FlightPort, n):
##    FlightPort.SetDestination(n, 0)  # 0 = Hangar
##
##def MoveToReady(FlightPort, n):
##    FlightPort.SetDestination(n, 1)  # 1 = Ready
##
##def MoveToRunway(FlightPort, n):
##    FlightPort.SetDestination(n, 3)  # 2 = Runway
