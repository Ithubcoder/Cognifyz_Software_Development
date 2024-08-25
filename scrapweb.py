from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time


# Function to fetch weather data using Selenium
def fetch_weather_data_selenium(location_code):
    try:
        # Set up the WebDriver (make sure to install WebDriver Manager)
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        url = f"https://weather.com/weather/today/l/UKXX0085"
        driver.get(url)

        # Wait for the page to fully load
        time.sleep(5)

        # Extract data
        temperature_element = driver.find_element(By.CLASS_NAME, "CurrentConditions--tempValue--3a50n")
        condition_element = driver.find_element(By.CLASS_NAME, "CurrentConditions--phraseValue--2xXSr")
        location_element = driver.find_element(By.CLASS_NAME, "CurrentConditions--location--1Ayv3")

        # Print data
        temperature = temperature_element.text
        condition = condition_element.text
        location_name = location_element.text

        driver.quit()
        return {
            "location": location_name,
            "temperature": temperature,
            "condition": condition
        }
    except Exception as e:
        print(f"An error occurred: {e}")
        return None


# Main function to run the interactive web scraper
def main():
    print("Welcome to the Weather Scraper!")
    location_code = input(
        "Enter the location code for which you want to fetch the weather (e.g., UKXX0085 for London): ")
    weather_data = fetch_weather_data_selenium(location_code)
    if weather_data:
        print("\nWeather Information:")
        print(f"Location: {weather_data['location']}")
        print(f"Temperature: {weather_data['temperature']}")
        print(f"Condition: {weather_data['condition']}")
    else:
        print("No data available.")


if __name__ == "__main__":
    main()
