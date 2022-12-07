import numpy as np
import cv2
import pyautogui
import pygetwindow as gw
import time
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\\Tesseract-OCR\\tesseract.exe'


def execute(actions):
    window = _launchAppToTest("Supercharger SRL")
    time.sleep(1)

    x, y, w, h = _getWindowSizeAndPosition(window)
    screen = _takeScreenShot(x + 10, y + 10, w - 10, h - 10)
    _saveScreenShoot(screen, "./informe/0.png")

    step = 1
    for action in actions:
        time.sleep(2)
        x, y, w, h = _getWindowSizeAndPosition(window)
        screen = _takeScreenShot(x + 10, y + 10, w - 10, h - 10)
        _saveScreenShoot(screen, "./log/step" + str(step) + ".png")
        if action.name == "PresionarBoton":
            _PresionarBoton(screen, action, x, y)
        elif action.name == "EscribirCampoTexto":
            _EscribirCampoTexto(screen, action, x, y, w, h)
        elif action.name == "BuscarTexto":
            
            _BuscarTexto(screen, action, x, y, w, h)

        step += 1

    x, y, w, h = _getWindowSizeAndPosition(window)
    screen = _takeScreenShot(x + 10, y + 10, w - 10, h - 10)
    _saveScreenShoot(screen, "./informe/n.png")

    _minimizeAppToTest("Supercharger SRL")


def _findTextOnScreen(screen, textToFind):
    gray = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
    _saveScreenShoot(gray, "./internal/1.gray.png")
    
    ret, thresh1 = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU | cv2.THRESH_BINARY_INV)
    _saveScreenShoot(thresh1, "./internal/2.thresh1.png")
    
    #rect_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (18, 18))
    rect_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (10, 10))
    _saveScreenShoot(rect_kernel, "./internal/3.rect_kernel.png")

    #dilation = cv2.dilate(thresh1, rect_kernel, iterations = 1)
    dilation = cv2.dilate(thresh1, rect_kernel, iterations = 1)
    _saveScreenShoot(dilation, "./internal/4.dilation.png")

    contours, hierarchy = cv2.findContours(dilation, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    # print(contours)
    
    step = 1
    for cnt in contours:
        x, y, w, h = cv2.boundingRect(cnt)
        cropped = screen[y:y + h, x:x + w]
        filename = "./log/contour" + str(step) + ".png"
        _saveScreenShoot(cropped, filename)
        textExtracted = pytesseract.image_to_string(cropped).strip()
        if textExtracted == textToFind:
            return x, y, w, h
        
        step += 1

    return 0,  0, 0, 0

def _PresionarBoton(screen, action, x0, y0):
    x, y, w, h = _findTextOnScreen(screen, action.param1)
    cv2.rectangle(screen, (x, y), (x + w, y + h), (0, 0, 255), 2)
    _saveScreenShoot(screen, "./informe/" + str(action.order) + ".png")

    cx = (x + x + w) // 2  
    cy = (y + y + h) // 2
    pyautogui.click(x0 + cx, y0 + cy)

def _EscribirCampoTexto(screen, action, x, y, w, h):

    if action.param1 == "Nombre":
        pyautogui.click(1395, 508)
        pyautogui.write(action.param2)
        screen = _takeScreenShot(x + 10, y + 10, w - 10, h - 10)
        cv2.rectangle(screen, (920, 460), (1165, 495), (0, 0, 255), 2)
        _saveScreenShoot(screen, "./informe/" + str(action.order) + ".png")
        
    
    if action.param1 == "Apellido":
        pyautogui.click(1395, 568)
        pyautogui.write(action.param2)
        screen = _takeScreenShot(x + 10, y + 10, w - 10, h - 10)
        cv2.rectangle(screen, (920, 520), (1165, 555), (0, 0, 255), 2)
        _saveScreenShoot(screen, "./informe/" + str(action.order) + ".png")
    
    if action.param1 == "DNI":
        pyautogui.click(1395, 628)
        pyautogui.write(action.param2)
        screen = _takeScreenShot(x + 10, y + 10, w - 10, h - 10)
        cv2.rectangle(screen, (920, 580), (1165, 615), (0, 0, 255), 2)
        _saveScreenShoot(screen, "./informe/" + str(action.order) + ".png")

    if action.param1 == "Telefono":
        pyautogui.click(1395, 688)
        pyautogui.write(action.param2)
        screen = _takeScreenShot(x + 10, y + 10, w - 10, h - 10)
        cv2.rectangle(screen, (920, 640), (1165, 675), (0, 0, 255), 2)
        _saveScreenShoot(screen, "./informe/" + str(action.order) + ".png")


    if action.param1 == "Domicilio":
        pyautogui.click(1395, 748)
        pyautogui.write("Salta 202")
        screen = _takeScreenShot(x + 10, y + 10, w - 10, h - 10)
        cv2.rectangle(screen, (920, 700), (1165, 735), (0, 0, 255), 2)
        _saveScreenShoot(screen, "./informe/" + str(action.order) + ".png")


def _BuscarTexto(screen, action, x, y, w, h):
    x, y, w, h = _findTextOnScreen(screen, action.param1)
    cv2.rectangle(screen, (x, y), (x + w, y + h), (0, 0, 255), 2)
    _saveScreenShoot(screen, "./informe/" + str(action.order) + ".png")


def _minimizeAllWindows():
    for window in gw.getAllWindows():
        window.minimize()
    

def _getWindowByTitle(title):
    return gw.getWindowsWithTitle(title)[0]


def _activeWindow(window):
    window.restore()
    window.activate()

def _getWindowSizeAndPosition(window):
    return window.left, window.top, window.width, window.height


def _launchAppToTest(AppName):
    _minimizeAllWindows()
    window = _getWindowByTitle(AppName)
    _activeWindow(window)
    return window
        

def _takeScreenShot(x, y, w, h):
    screenshot =  pyautogui.screenshot(region=(x, y, w, h))
    return cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)


def _saveScreenShoot(screenshot, filename):
    cv2.imwrite(filename, screenshot)


def _minimizeAppToTest(appName):
    window = gw.getWindowsWithTitle(appName)[0]
    window.minimize()