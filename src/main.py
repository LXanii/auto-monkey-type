import pyautogui, time, pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

def get_screenshot():
    print("Getting Screenshot...")
    pyautogui.click(929, 555) # click on
    pyautogui.click(957,693) # click out
    pyautogui.screenshot('test.png', region=(365, 510, 1190, 118)) # 2nd is up and down yuh + 4 down - 4 up
    pyautogui.click(929, 555)

def turn_gray(file_name, x):
    if x:
        get_screenshot()
    image = Image.open(file_name)
    grayscale = image.convert('L')
    grayscale.save("read_image.jpg")
    print("New Image saved Successfully")

def get_words():
    print("Collecting Words...")
    words = []
    result = pytesseract.image_to_string('read_image.jpg')
    for i in result.replace("\n", " "):
        words.append(i)
    string = ''
    for i in words:
        string += i
    print("Typing Words...")
    return string.lower()

def main():
    turn_gray('test.png', True)
    pyautogui.typewrite(get_words(), interval=0.02)

time.sleep(2)
while True:
    main()
    while pyautogui.locateOnScreen('char.png', confidence=0.65) == None:
        print("Getting Continious Screenshot...")
        print(pyautogui.locateOnScreen('char.png', confidence=0.65))
        pyautogui.click(957,693)
        pyautogui.screenshot('test.png', region=(365, 550, 1190, 118))
        pyautogui.click(929, 555)
        turn_gray('test.png', False)
        pyautogui.typewrite(get_words(), interval=0.02)
        if pyautogui.locateOnScreen('char.png', confidence=0.65) != None:
            break
    print("\nStarting New Game\n")
    pyautogui.click(929, 555)
    pyautogui.press('esc')
    pyautogui.click(957,693)