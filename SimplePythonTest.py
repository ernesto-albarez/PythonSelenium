from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.mercadolibre.com.ar")
driver.maximize_window()

searchBox = driver.find_element_by_xpath("//*[@class='nav-search-input']")
searchBox.clear()
searchBox.send_keys("huevo de pascuas")

searchButton = driver.find_element_by_xpath("//*[@class='nav-icon-search']")
searchButton.click()

driver.find_element_by_xpath("//*[@id='searchResults']/li[1]//*[@class='main-title']").click()

driver.close()

