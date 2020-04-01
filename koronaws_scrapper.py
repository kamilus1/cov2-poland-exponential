from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from datetime import date
from time import sleep
class Koronaws:
    def __init__(self, driver="D:\chromedriver\chromedriver.exe"):
       options = Options()
       options.add_argument("--headless")
       options.add_argument(driver)
       self.driver = webdriver.Chrome(options=options)

    def get_infections(self):
        self.driver.get("https://korona.ws")
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.presence_of_all_elements_located((By.XPATH, '//div[@class="ah"]')))
        return element[1].text
    def update(self, csv_name="cov2.csv"):
        f = open(csv_name, "r")
        line = f.readlines()
        f.close()
        line = str(line[-1])
        line = line.split(";")
        old_cases = int(line[2])
        day = int(line[1])
        new_cases = int(self.get_infections())
        d = date.today()
        new_date = "{}-{}-{}".format(d.day, d.month, d.year)
        if new_cases != old_cases:
            day += 1
            f = open(csv_name, "a")
            f.write("\n{};{};{}".format(new_date, str(day), str(new_cases)))
            f.close()
if __name__ == '__main__':
    # u need to start it at least one time a day or keep it running on some server to get actual csv file of infections
    while True:
        K = Koronaws()
        K.update()
        K.driver.quit()
        del K
        sleep(3600)
