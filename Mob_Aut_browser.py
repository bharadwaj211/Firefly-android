from appium import webdriver
from appium.options.android import UiAutomator2Options
import time

# -----------------------------
# Set options for Chrome browser
# -----------------------------
options = UiAutomator2Options()
options.platformName = "Android"
options.automationName = "UiAutomator2"
options.deviceName = "RZ8M429KRFP"
options.udid = "RZ8M429KRFP"
options.browserName = "Chrome" 

# -----------------------------
# Connect to Appium server
# -----------------------------
driver = webdriver.Remote("http://127.0.0.1:4723", options=options)

# -----------------------------
# Open multiple URLs
# -----------------------------
urls = [
    "https://www.google.com",
    "https://www.openai.com",
    "https://www.github.com",
    "https://www.shuttershock.com
]

for url in urls:
    driver.get(url)
    print(f"Opened: {url}")
    time.sleep(5)  # wait 5 seconds to load

# -----------------------------
# Quit the session
# -----------------------------
driver.quit()
print("Browser automation completed successfully.")
