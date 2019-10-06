from selenium import webdriver

browser = webdriver.Firefox(executable_path=r'D:\Downloads\geckodriver.exe')
browser.get('https://moodle.elab.fon.bg.ac.rs/login/index.php')
ime = browser.find_element_by_id("username")
lozinka = browser.find_element_by_id("password")

ime.send_keys("milosavljevicpedja15")
lozinka.send_keys("Elab.Rs.171")
lozinka.submit()


