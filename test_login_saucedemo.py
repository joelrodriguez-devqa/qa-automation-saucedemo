from selenium import webdriver
from selenium.webdriver.common.by import By
import time

#INICIO
print("Iniciando prueba automatizada...")

driver = webdriver.Chrome()

driver.get("https://www.saucedemo.com/")
time.sleep(1)

# Login
driver.find_element(By.NAME, "user-name").send_keys("standard_user")
driver.find_element(By.NAME, "password").send_keys("secret_sauce")
time.sleep(1)

driver.find_element(By.NAME, "login-button").click()

# Verificar que entramos correctamente
if "inventory" in driver.current_url:
    print("Login exitoso")
else:
    print("Login fallido")

#Buscar productos
products = driver.find_elements(By.CLASS_NAME, "inventory_item")

print(f"Se encontraron {len(products)} productos")

if len(products) > 0:
    print("La página cargó correctamente")
else:
    print("Error: no hay productos")

#FINAL
print("Prueba finalizada")

time.sleep(5)

driver.quit()
