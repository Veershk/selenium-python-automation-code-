import pytest
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager


@pytest.fixture(scope="class")
def browserInvoke(request):
    option = webdriver.EdgeOptions()
    option.add_experimental_option("detach", True)
    driver = webdriver.Edge(options=option, service=Service(EdgeChromiumDriverManager().install()))
    driver.get("https://rahulshettyacademy.com/client/")
    driver.maximize_window()
    request.cls.driver = driver
    yield
    # driver.quit()
