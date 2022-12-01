from action import Action
def parse(rawActions):

    order = 1
    actionList = []
    for rawAction in rawActions:
        stripped = rawAction.strip()
        splitted = stripped.split()

        actionName   = splitted[0].strip() if len(splitted) >= 1 else None 
        actionParam1 = splitted[1].strip() if len(splitted) >= 2 else None 
        actionParam2 = splitted[2].strip() if len(splitted) >= 3 else None 

        if actionName == None:
            continue
        elif actionName.startswith("#"):
            continue
        elif actionName.startswith("PresionarBoton") and actionParam1 is not None:
            actionList.append(Action(order, actionName, actionParam1, None))    
        elif actionName.startswith("EscribirCampoTexto") and actionParam1 is not None and actionParam2 is not None:
            actionList.append(Action(order, actionName, actionParam1, actionParam2))    
        elif actionName.startswith("BuscarTexto") and actionParam1 is not None:
            actionList.append(Action(order, actionName, actionParam1, None))    
        else:
            print("TestCase: incorrect format")
            actionList = []
            break

        order += 1
    
    return actionList