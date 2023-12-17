from playwright.sync_api import sync_playwright

# Function to scrape text content from a web page using Playwright
def scrape(url, selector):
    # Launch a Playwright instance and perform scraping
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(url)
        text_raw = page.locator(selector)
        text = text_raw.first.text_content().lower()
        browser.close()
        return text

# Function to identify weather front based on extracted text
def front_searcher(front_name):
    if 'hidegfront' in front_name:
        return 'hidegfront 🥶'
    elif 'melegfront' in front_name:
        return 'melegfront 🥵'
    elif 'kettősfront' in front_name:
        return 'kettősfront 🤕'
    else:
        return 'nincs front 😊'

# Scrape weather front information from two different URLs
front_name1 = scrape(
    'https://www.hazipatika.com/orvosmeteorologia',
    '.o-humanMeteoDay__frontEffectBox span')
front_name2 = scrape(
    'https://www.idokep.hu/elorejelzes/Budapest', 
    '.forecast-box-text')

# Determine weather fronts using the front_searcher function
f1 = front_searcher(front_name1)
f2 = front_searcher(front_name2)

# Output the identified weather fronts
print(f1)
print(f2)
