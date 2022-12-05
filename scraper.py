# C:\Users\nemanja.novakovic\Desktop\Learning
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

DRIVER_PATH = "C:\\Users\\nemanja.novakovic\\Desktop\\Learning\\ecommerce\\django-shop"
ser = Service(DRIVER_PATH)
op = webdriver.ChromeOptions()
op.add_argument('--headless')
op.add_argument('--disable-gpu')
driver = webdriver.Chrome()
driver.get('https://www.drustveneigre.rs/drustvene-igre?limit=200')
timeout = 7

try:
    element_present = EC.presence_of_element_located((By.CLASS_NAME, 'product-layout'))
    WebDriverWait(driver, timeout).until(element_present)
    driver.maximize_window()

    scroll_pause_time = 1 # You can set your own pause time. My laptop is a bit slow so I use 1 sec
    screen_height = driver.execute_script("return window.screen.height;")   # get the screen height of the web
    i = 1

    while True:
    # scroll one screen height each time
        driver.execute_script("window.scrollTo(0, {screen_height}*{i});".format(screen_height=screen_height, i=i))  
        i += 1
        time.sleep(scroll_pause_time)
        # update scroll height each time after scrolled, as the scroll height can change after we scrolled the page
        scroll_height = driver.execute_script("return document.body.scrollHeight;")  
        # Break the loop when the height we need to scroll to is larger than the total scroll height
        if (screen_height) * i > scroll_height:
            break

    mipl_games = []
    games_ = []
    bad_tags = ["BESTSELER", "NOVO", "Na stanju", "-25 %", "Din", "USKORO", "NA STANJU"]

# if "Došli ste do kraja kataloga" in driver.page_source:
    # driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    all_el = driver.find_elements(By.CLASS_NAME, 'product-layout')
    links = [i.find_element(By.CLASS_NAME, "product-img").get_attribute('href') for i in all_el]
    games_ = [i.text.split("\n") for i in all_el]
    images = [i.find_element(By.CLASS_NAME, "img-first").get_attribute('src') for i in all_el]
    for g in games_:
        if g[0] == "NEMA NA STANJU":
            g[0], g[1], g[-1] = g[1], int(float(g[-1][:-3].replace("," ,""))), g[0]
        #Add only relevant information and exclude information that matches bad_tags array
        mipl_games.append([ele for ele in g if ele not in bad_tags])
        for gn in range(len(mipl_games)):
            if mipl_games[gn][0] == "NEMA NA STANJU":
                mipl_games[gn][0], mipl_games[gn][1], mipl_games[gn][-1] = mipl_games[gn][1], \
                                                                            int(float(mipl_games[gn][-1][:-3].replace(",", ""))), \
                                                                            mipl_games[gn][0]
            # removing link el from IN STOCK games so that it can be appended to the so it can match the OUT OF STOCK games info order
            if len(mipl_games[gn]) > 2 and mipl_games[gn][-1] != "NEMA NA STANJU":
                del mipl_games[gn][-1]
            mipl_games[gn].append(links[gn])
    # Adding IN STOCK information ( that does not exist in data originaly)
    for i in range(len(mipl_games)):
        if mipl_games[i][2] != 'NEMA NA STANJU':
            mipl_games[i].insert(2, 'NA STANJU')
            mipl_games[i][1] = int(float(mipl_games[i][1][:-3].replace(",", "")))
    #appending image link at the end of the game info 
    for i in range(len(images)):
        mipl_games[i].append(images[i])
    final_games_dict = {}
    for i in range(len(mipl_games)):
        game = {}
        game['title'] = mipl_games[i][0]
        game['price'] = mipl_games[i][1]
        game['status'] = mipl_games[i][2]
        if mipl_games[i][2] == 'NA STANJU':
            game['status'] = True
        else:
            game['status'] = False
        game['image'] = mipl_games[i][-1]
        final_games_dict[i] = game
except TimeoutException:
    print('TimeoutException')