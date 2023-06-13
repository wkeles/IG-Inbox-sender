from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver

driver = webdriver.Chrome()

driver.get('https://instagram.com')

wait = WebDriverWait(driver, 10)

try:
    cookie_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Tüm çerezlere izin ver')]")))
    
    driver.execute_script("arguments[0].click();", cookie_button)
except:

    pass

username = input("Kullanıcı adınızı girin: ")
password = input("Şifrenizi girin: ")

username_input = driver.find_element(By.XPATH, "//input[@name='username']")
password_input = driver.find_element(By.XPATH, "//input[@name='password']")
username_input.send_keys(username)
password_input.send_keys(password)
password_input.send_keys(Keys.ENTER)

try:
    factor_code_input = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@name='verificationCode']")))
    factor_code = input("Faktör kodunu girin: ")
    factor_code_input.send_keys(factor_code)
    factor_code_input.send_keys(Keys.ENTER)
except:

    pass

wait = WebDriverWait(driver, 10)

try:
    
    cookie_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Şimdi Değil')]")))

    cookie_button.click()

except:

    pass

driver.get("https://instagram.com/direct/inbox/")

try:
    message_text = "Merhaba! Bu otomatik bir mesajdır."

    conversations = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//a[@role='link' and @href='/direct/t/']")))

    for conversation in conversations:
        conversation.click()

        message_input = wait.until(EC.element_to_be_clickable((By.XPATH, "//textarea[@placeholder='Mesaj gönder']")))

        message_input.send_keys(message_text)
        message_input.send_keys(Keys.ENTER)

    print("Tüm mesajlar başarıyla gönderildi.")

except Exception as e:
    print("Mesaj gönderme hatası:", str(e))

finally:
    driver.quit()