from selenium import webdriver
from selenium.webdriver.support.ui import Select
import pyfiglet
from os import system
import time
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Configurar las opciones de Chrome
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--log-level=3")

# Inicializar WebDriver con Service
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

driver.set_window_size(1024, 650)

def loop2():
    time.sleep(60)
    try:
        driver.find_element("xpath", "/html/body/main/div/div/div[2]/div/div[1]/div[3]/div/div/button").click()
    except:
        print("You didn't solve the captcha yet")
        loop2()
    
    time.sleep(2)
    try:
        driver.find_element("xpath", "/html/body/main/div/div/div[2]/form/div/input").send_keys(vidUrl)
    except:
        print("Delay")
        driver.refresh()
        loop2()
    
    time.sleep(2)
    driver.find_element("xpath", '//button[@type="submit"]').click()
    time.sleep(2)
    
    try:
        driver.find_element("xpath", "/html/body/main/div/div/div[2]/div/div/div/h5/button[2]").click()
    except:
        print("Either failed to input or can't find the button. Need to retry")
        driver.refresh()
        loop2()
    
    time.sleep(2)
    print("Views success delivered!")
    driver.refresh()
    time.sleep(250)
    loop2()

vidUrl = "YOUR_URL"  # Cambia YOUR_URL a la URL de tu video de TikTok
username = "YOUR_USERNAME"  # Cambia YOUR_USERNAME a tu nombre de usuario de TikTok

# Limpiar la terminal y mostrar el banner
system("cls")
tiktod = pyfiglet.figlet_format("TIKTOD V2", font="slant")
print(tiktod)
print("Author: https://github.com/kangoka")
print("")

# Configuración del modo automático
auto = 2  # 2 para auto views

if auto == 2:
    driver.get("https://homedecoratione.com/")
    loop2()
