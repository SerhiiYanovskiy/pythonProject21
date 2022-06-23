import requests
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

PROXY = "write proxi"
API_KEY = "write aoi_key 2capcha"
data_sitekey = "6LcbmroaAAAAANQ34XOxul9o_UgaJ6dkdq62Xey6"


def data_from_file():
    with open("data.csv", "r") as file:
        for line in file.readlines():
            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_argument('--proxy-server=%s' % PROXY)
            driver = webdriver.Chrome()
            email = (line.split(":"))[0]
            password = (line.split(":"))[1]
            full_name = email.split("@")[0]
            driver.set_window_position(0, 0)
            driver.set_window_size(1920, 1080)
            driver.get(f"https://dashboard.stripe.com/register")
            time.sleep(2)
            driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/div[2]/div[2]/div[1]/div/div/form/div/div/div[1]/div/div/div[2]/div/div/div/div/div/div/div[1]/input").send_keys(email)
            driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/div[2]/div[2]/div[1]/div/div/form/div/div/div[2]/div/div/div[2]/div/div/div/div/div/div/div[1]/input").send_keys(full_name)
            time.sleep(4)
            driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/div[2]/div[2]/div[1]/div/div/form/div/div/div[4]/div/div[2]/div/div/div/div/div/div[1]/div/div/div/div[1]/input").send_keys(password)
            driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/div[2]/div[2]/div[1]/div/div/form/div/div/div[5]/div/div/div/div/div/div/div/div[1]/div/div[1]/div/input").click()
            driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/div[2]/div[2]/div[1]/div/div/form/div/div/div[6]/div/div/div/div/div/div/div[2]").click()
            time.sleep(2)
            driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/div[2]/div[2]/div[1]/div/div/form/div/div/div[6]/div/div/div/div/div/div/div[1]/button/div/div[2]").click()
            time.sleep(3)
            driver.quit()






def pars_yahoo():
    with open("data.csv", "r") as file:
        for line in file.readlines():
            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_argument('--proxy-server=%s' % PROXY)
            driver = webdriver.Chrome()
            data_sitekey = "6LcbmroaAAAAANQ34XOxul9o_UgaJ6dkdq62Xey6"
            email = (line.split(":"))[0]
            password = (line.split(":"))[1]
            driver.set_window_position(0, 0)
            driver.set_window_size(1920, 1080)
            driver.get(f"https://login.yahoo.com/?.lang=en-US&src=homepage&.done=https%3A%2F%2Fwww.yahoo.com%2F&pspid=2023538075&activity=ybar-signin")
            time.sleep(2)
            driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[1]/div[2]/div[2]/form/div[1]/div[3]/input").send_keys(email)
            time.sleep(10)
            driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[1]/div[2]/div[2]/form/div[2]/input").click()
            time.sleep(10)
            page_url = driver.current_url
            u1 = f"https://2captcha.com/in.php?key={API_KEY}&method=userrecaptcha&googlekey={data_sitekey}&pageurl={page_url}&json=1&invisible=1"
            r1 = requests.get(u1)
            print(r1.json())
            rid = r1.json().get("request")
            u2 = f"https://2captcha.com/res.php?key={API_KEY}&action=get&id={int(rid)}&json=1"
            time.sleep(5)
            while True:
                r2 = requests.get(u2)
                print(r2.json())
                if r2.json().get("status") == 1:
                    form_tokon = r2.json().get("request")
                    break
                time.sleep(5)
            wirte_tokon_js = f'document.getElementById("g-recaptcha-response").innerHTML="{form_tokon}";'
            submit_js = 'document.getElementById("recaptcha-demo-form").submit();'
            driver.execute_script(wirte_tokon_js)
            time.sleep(3)
            driver.execute_script(submit_js)
            time.sleep(10)
            driver.find_element_by_xpath("/html/body/div[1]/div/form/button").click()
            time.sleep(2)
            driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[1]/div[2]/div[2]/form/div[2]/input").send_keys(password)
            driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[1]/div[2]/div[2]/form/div[3]/button").click()
            page_url = driver.current_url
            u1 = f"https://2captcha.com/in.php?key={API_KEY}&method=userrecaptcha&googlekey={data_sitekey}&pageurl={page_url}&json=1&invisible=1"
            r1 = requests.get(u1)
            print(r1.json())
            rid = r1.json().get("request")
            u2 = f"https://2captcha.com/res.php?key={API_KEY}&action=get&id={int(rid)}&json=1"
            time.sleep(5)
            while True:
                r2 = requests.get(u2)
                print(r2.json())
                if r2.json().get("status") == 1:
                    form_tokon = r2.json().get("request")
                    break
                time.sleep(5)
            driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[1]/div[2]/div[2]/form/div[3]/button").click()
            driver.find_element_by_xpath("/html/body/header/div[2]/div/div/div/div/div[3]/div/div[3]/div[3]/div/a/span[1]").click()
            driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div/div/div[2]/div/div[1]/ul/li[2]").click()
            driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div[2]/div[2]/ul/li/div/div[2]/div[1]/div[2]/div/div/div/div/table/tbody/tr[1]/td/table/tbody/tr/td/table[4]/tbody/tr[1]/td[2]/table/tbody/tr/td/a").click()



data_from_file()
data_from_file()

