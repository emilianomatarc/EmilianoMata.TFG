import webbrowser

def generate(actions):
    f = open("./informe/InformePruebas.html","w")

    message  = "<html>"
    message += "<head></head>"
    message += "<body>"
    message += "<h1>Informe de Pruebas</h1>"

    message += "<h2>Paso 0. Antes de comenzar el caso de prueba.</h2>"
    message += """<img src="0.png" width="640" height="480">"""
    
    for idx, action in enumerate(actions):
        message += "<br><br><br>"
        message += "<h2>Paso "
        message += str(action.order)
        message += ". "
        message += str(action.name) + " "
        message += str(action.param1) 
        message += " " + str(action.param2) if action.param2 is not None else ""
        message += ".</h2>"

        message += """<img src=\"""" 
        message += str(action.order) 
        message += """.png" width="640" height="480">"""

    message += "<br><br><br>"
    message += "<h2>Paso N. Despues de finalizar caso de prueba.</h2>"
    message += """<img src="n.png" width="640" height="480">"""

    message += "</body>"
    message += "</html>"

    f.write(message)
    f.close()

    #webbrowser.open_new_tab('./informe/InformePruebas.html')