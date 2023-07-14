import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


def first_test():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    driver = webdriver.Firefox()
    driver.get("https://www.saucedemo.com/")

    time.sleep(5)

    # Поиск элементов и присваивание к переменным.
    input_username = driver.find_element("user-name",By.CSS_SELECTOR, '[id="user-name"]', timeout=20)
    input_password = driver.find_element_by_name('password')
    login_button = driver.find_element_by_name('Войти')



    # Действия с формами
    input_username.send_value("A_Hapunov.")
    input_password.send_keys("A_Hapunov21")
    login_button.send_keys(Keys.RETURN)

    # Поиск и проверка попадания на главную страницу
    title_text = driver.find_element_by_xpath("//*[@id=\"header_container\"]/div[2]/span")
    if title_text.text == "АРМ ЦОД":
        print("Мы попали на главную страницу")
    else:
        print("Ошибка поиска элемента")

    time.sleep(30)


if __name__ == '__main__':
    first_test()