from selenium import webdriver
import time

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# Variable Declaration
meta_get_started_btn = '//button[text()="Get Started"]'
meta_import_wallet__btn = '//button[text()="Import wallet"]'
meta_no_thanks_btn = '//button[text()="No Thanks"]'
open_sea_url = "window.open('https://opensea.io/collection/hand-painting-unique-style')"
sign_in_btn = '//button[text()="Sign"]'
complete_listing_btn = '//button[text()="Complete listing"]'
image_upload_chk = '//*[@id="media"]'
agreement_checkbox = '.first-time-flow__terms'
import_btn = '//button[text()="Import"]'
meta_next_btn = '//button[text()="Next"]'
meta_connect_btn = '//button[text()="Connect"]'

EXTENSION_PACK = r'C:\Users\amuly\Downloads\image-dataset-generator-main\image-dataset-generator-main\metamask.crx'
opt = webdriver.ChromeOptions()
opt.add_extension(EXTENSION_PACK)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=opt)


# TODO:   Update the below locators and the url to the desired collection also add doc strings

def switch_to_child_window(driver):
    """
    Switch to child window
    Args:
        driver: webdriver instance
    Returns: None
    """
    p = driver.current_window_handle
    chwd = driver.window_handles
    driver.maximize_window()
    for w in chwd:
        # switch focus to child window
        if w != p:
            driver.switch_to.window(w)
    time.sleep(5)


def meta_mask_login(driver):
    """
    Login to MetaMask and import the wallet
    Args:
        driver: webdriver instance
    Returns:None

    """
    driver.find_element(By.XPATH, meta_get_started_btn).click()
    driver.find_element(By.XPATH, meta_import_wallet__btn).click()
    driver.find_element(By.XPATH, meta_no_thanks_btn).click()
    time.sleep(5)
    inputs = driver.find_elements(By.XPATH, '//input')
    inputs[0].send_keys("16 digits secret code")
    inputs[1].send_keys("NEW_PASSWORD")
    inputs[2].send_keys("NEW_PASSWORD")
    driver.find_element(By.CSS_SELECTOR, agreement_checkbox).click()
    driver.find_element(By.XPATH, import_btn).click()
    time.sleep(10)


def opening_open_sea(driver):
    """
    Open the open sea page and opens the collection
    Args:
        driver: Web driver instance
    Returns:None
    """
    driver.execute_script(open_sea_url)
    time.sleep(20)
    window1 = driver.window_handles[2]
    driver.switch_to.window(window1)
    driver.find_element(By.XPATH, "//a[contains(@class, 'NavItem') and contains(@href, 'create')]").click()
    time.sleep(5)
    meta_mask_btn = driver.find_element(By.XPATH, '//*[@id="main"]/div/div/div/div[2]/ul/li[1]/button')
    meta_mask_btn.click()
    time.sleep(10)
    open_sea_window = driver.window_handles[2]
    driver.switch_to.window(open_sea_window)
    time.sleep(5)
    meta_mask_btn.click()
    time.sleep(5)
    switch_to_child_window(driver)
    time.sleep(5)
    driver.find_element(By.XPATH, meta_next_btn).click()
    driver.find_element(By.XPATH, meta_connect_btn).click()
    driver.switch_to.window(open_sea_window)
    time.sleep(10)
    driver.get('https://opensea.io/collections/hand-painting-unique-style')
    driver.find_element(By.XPATH, '//*[@id="main"]/div/div/div[1]/ul/li[1]/a/span').click()
    time.sleep(5)
    driver.find_element(By.XPATH, '//*[@id="main"]/div/div/section/div/div/div[1]/div/a').click()
    time.sleep(5)


def add_item_open_sea(driver, backgrounds='0'):
    """
    Add an item to the collection
    Args:
        driver:
        backgrounds: Here we can pass the number of background to be added to the collection
        eg: I have images names as generated1, generated2 and soon
    Returns:None

    """
    time.sleep(15)
    driver.find_element(By.XPATH, '//*[@id="main"]/div/div/div[1]/span/a').click()
    time.sleep(5)
    switch_to_child_window(driver)

    try:
        for i in range(5):
            result = driver.find_element(By.XPATH, '//*[@id="app-content"]/div/div[2]/div/div[3]/button[2]')
            if result:
                driver.find_element(By.XPATH, '//*[@id="app-content"]/div/div[2]/div/div[3]/button[2]').click()
                time.sleep(5)
    except:
        pass
    open_sea_window = driver.window_handles[2]
    driver.switch_to.window(open_sea_window)
    time.sleep(5)
    driver.find_element(By.XPATH, image_upload_chk).send_keys(
        fr"C:\Users\amuly\Downloads\image-dataset-generator-main\image-dataset-generator-main\generated\generated{backgrounds}.png")
    time.sleep(5)
    driver.find_element(By.XPATH, '//*[@id="name"]').send_keys(f'AI Generated Images #{backgrounds}/5879')
    time.sleep(10)

    driver.find_element(By.XPATH, '//*[@id="main"]/div/div/section/div[2]/form/div[9]/div[1]/span/button').click()
    time.sleep(10)

    for i in range(5):
        try:
            for i in range(5):
                result = driver.find_element(
                    By.CLASS_NAME,
                    'Iconreact__Icon-sc-1gugx8q-0.Modalreact__StyledIcon-sc-xyql9f-1.irnoQt.byuytI.material-icons')
                if result:
                    driver.find_element_by(
                        By.CLASS_NAME,
                        'Iconreact__Icon-sc-1gugx8q-0.Modalreact__StyledIcon-sc-xyql9f-1.irnoQt.byuytI.material-icons').click()
                    time.sleep(5)
        except:
            pass
    driver.find_element(By.XPATH, '//*[@id="main"]/div/div/div[1]/div/span[2]/a').click()
    time.sleep(5)
    set_price_open_sea(driver)


def set_price_open_sea(driver):
    """
    Set the price of the item and list in open sea market
    Args:
        driver: Web driver instance
    Returns:None

    """
    time.sleep(10)
    driver.find_element(
        By.XPATH,
        '//*[@id="main"]/div/div/div[3]/div/div[2]/div/div[1]/form/div[1]/div/div[2]/div/div/div[2]/input').send_keys(
        0.023)
    time.sleep(10)
    driver.find_element(By.XPATH, complete_listing_btn).click()
    time.sleep(10)
    driver.find_element(By.XPATH, sign_in_btn).click()
    time.sleep(10)
    switch_to_child_window(driver)

    try:
        for i in range(5):
            result = driver.find_element(By.XPATH, sign_in_btn)
            if result:
                driver.find_element(By.XPATH, sign_in_btn).click()
                time.sleep(5)
    except:
        pass

    open_sea_window = driver.window_handles[2]
    driver.switch_to.window(open_sea_window)
    time.sleep(10)
    for i in range(5):
        try:
            for i in range(5):
                result = driver.find_element(
                    By.CLASS_NAME,
                    'Iconreact__Icon-sc-1gugx8q-0.Modalreact__StyledIcon-sc-xyql9f-1.irnoQt.byuytI.material-icons')
                if result:
                    driver.find_element(
                        By.CLASS_NAME,
                        'Iconreact__Icon-sc-1gugx8q-0.Modalreact__StyledIcon-sc-xyql9f-1.irnoQt.byuytI.material-icons').click()
                    time.sleep(5)
        except:
            pass
    driver.find_element(
        By.CLASS_NAME,
        'styles__StyledLink-sc-l6elh8-0.ekTmzq.Blockreact__Block-sc-1xf18x6-0.Buttonreact__StyledButton-sc-glfma3-0.bhqEJb.gIDfxn').click()


if __name__ == '__main__':
    switch_to_child_window(driver)
    meta_mask_login(driver)
    opening_open_sea(driver)
    for i in range(1, 5879):
        print(i)
        add_item_open_sea(driver, backgrounds=str(i))
    time.sleep(5)
    driver.quit()
    print('Done')
