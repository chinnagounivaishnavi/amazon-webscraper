from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def amazon_login(driver):
    try:
        # Navigate to Amazon
        driver.get("https://www.amazon.in")

        # Wait for the "Sign-In" button
        sign_in_button = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.ID, "nav-link-accountList"))
        )
        sign_in_button.click()

        # Wait for the email input field
        email_input = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.ID, "ap_email"))
        )
        email_input.send_keys("your_email@example.com")
        driver.find_element(By.ID, "continue").click()

        # Wait for the password input field
        password_input = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.ID, "ap_password"))
        )
        password_input.send_keys("your_password")
        driver.find_element(By.ID, "signInSubmit").click()

        print("Login successful!")

    except Exception as e:
        print(f"Error during login: {e}")


# Main function
def main():
    driver = webdriver.Chrome()
    try:
        amazon_login(driver)
    finally:
        driver.quit()

if __name__ == "__main__":
    main()
