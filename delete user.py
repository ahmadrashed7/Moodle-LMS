import datetime
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
s = Service(executable_path='./chromedriver')

driver = webdriver.Chrome(service=s)


def setUp():
    driver.maximize_window()

    driver.implicitly_wait(30)

    driver.get('http://52.33.5.136/')

    if driver.current_url == 'http://52.33.5.136/' and driver.title == 'Moodle Test Server 2':
        print(f'We\'re at Moodle homepage -- {driver.current_url}')
        print(f'We\'re seeing title message -- "Software Quality Assurance Testing"')
    else:
        print(f'We\'re not at the Moodle homepage. Check your code!')
        driver.close()
        driver.quit()


def teardown():
    if driver is not None:
        print(f'--------------------------------------')
        print(f'Test Completed at: {datetime.datetime.now()}')
        driver.close()
        driver.quit()


def log_in():
    if driver.current_url == 'http://52.33.5.136/':
        driver.find_element(By.LINK_TEXT, 'Log in').click()
        if driver.current_url == 'http://52.33.5.136/login/index.php':
            driver.find_element(By.ID, 'username').send_keys('admin')
            sleep(0.25)
            driver.find_element(By.ID, 'password').send_keys('Moodle$erver002!#')
            sleep(0.25)
            driver.find_element(By.ID, 'loginbtn').click()
            if driver.title == 'Dashboard' and driver.current_url == 'http://52.33.5.136/my/':
                assert driver.current_url == 'http://52.33.5.136/my/'
                print(f'Log in successfully. Dashboard is present')
            else:
                print(f'We are not at the Dashboard. Try again')


def delete_user():
    driver.find_element(By.LINK_TEXT, "Site administration").click()
    sleep(0.25)
    assert driver.find_element(By.LINK_TEXT, 'Users')
    driver.find_element(By.LINK_TEXT, 'Users').click()
    driver.find_element(By.LINK_TEXT, 'Browse list of users').click()
    sleep(0.25)
    driver.find_element(By.XPATH, "//i[@title='Delete']").click()
    sleep(0.25)
    driver.find_element(By.XPATH, '/html/body/div[2]/div[4]/div/div[3]/div/section/div/div/div/div[3]/div/div[1]/form/button').click()
    sleep(0.25)
    if driver.current_url == "http://52.33.5.136/admin/user.php?sort=name&dir=ASC&perpage=30&page=0":
        for x in range(10): # it will run 10 times and delete 10 users.
            driver.find_element(By.XPATH, "//i[@title='Delete']").click()
            driver.find_element(By.XPATH, '/html/body/div[2]/div[4]/div/div[3]/div/section/div/div/div/div[''3]/div/div[1]/form/button').click()
            print('user deleted successfully')


setUp()
log_in()
delete_user()
teardown()
