from dash import Dash, html
import carbon_dash
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from multiprocessing import Process

def run_app():
    app = Dash(__name__)
    app.layout = html.Div([
        carbon_dash.Dropdown(
            id='test-dropdown',
            items=['Option 1', 'Option 2'],
            label='Dropdown',
            title='Dropdown Title'
        )
    ])
    app.run(debug=False, port=8051)

def inspect():
    p = Process(target=run_app)
    p.start()
    time.sleep(5)
    
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(options=chrome_options)
    
    try:
        driver.get("http://127.0.0.1:8051")
        time.sleep(5)
        
        dropdown = driver.find_element("id", "test-dropdown")
        print(f"Dropdown HTML: {dropdown.get_attribute('outerHTML')}")
        
        # Carbon dropdown usually has a button or a div that handles clicks
        trigger = driver.find_element("xpath", "//*[@id='test-dropdown']//button")
        trigger.click()
        time.sleep(2)
        
        # Look for the menu
        menu = driver.find_elements("xpath", "//*[contains(@class, 'cds--list-box__menu')]")
        for m in menu:
            print(f"Menu HTML: {m.get_attribute('outerHTML')}")
            
        items = driver.find_elements("xpath", "//*[contains(@class, 'cds--list-box__menu-item')]")
        for i in items:
            print(f"Item HTML: {i.get_attribute('outerHTML')}")
            
    except Exception as e:
        print(f"Error: {e}")
    finally:
        driver.quit()
        p.terminate()

if __name__ == "__main__":
    inspect()
