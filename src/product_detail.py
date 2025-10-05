from src.page_listing import scrape_noon_products
import os
from pathlib import Path
import json
from datetime import datetime
import requests
from bs4 import BeautifulSoup

class noon_scrape:
    def __init__(self,search_query:str,max_pages: int = None):
        self.headers = {
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'en-US,en;q=0.9',
            'cache-control': 'max-age=0',
            'priority': 'u=0, i',
            'sec-ch-ua': '"Chromium";v="140", "Not=A?Brand";v="24", "Google Chrome";v="140"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36',
        }
        self.payload = {}

        
        self.session_path = os.path.join(os.getcwd(), "session")
        os.makedirs(self.session_path, exist_ok=True)
        current_time = datetime.now().strftime("%Y%m%d_%H%M%S")
        self.file_name = f"{search_query}_{current_time}.json"
        self.json_path = os.path.join(self.session_path, self.file_name)

        scrape_noon_products(search_query, self.json_path,max_pages)

        with open(self.json_path, "r", encoding="utf-8") as f:
            self.json_data = json.load(f)



    def product_metadata(self):
        for i, product in enumerate(self.json_data):
            url = product["product_url"]
            soup = self.fetch_product_details(url)
            if not soup:
                continue

            categories = soup.find_all("a", class_="Breadcrumb_breadcrumb__74hod")
            categories_list = [cat.get_text(strip=True) for cat in categories]
            product["category"] = " > ".join(categories_list[1:]) if categories_list else ""

            star_rating = soup.find("span", class_="RatingPreviewStarV2_text__XseM1")
            product["review_rating"] = star_rating.text.strip() if star_rating else ""

            no_of_reviews = soup.find("div", class_="RatingPreviewStarV2_countCtr__41zXF")
            product["no_of_reviews"] = no_of_reviews.text.strip() if no_of_reviews else ""

            ranking = soup.find("div", class_="Nudges_nudgeText__cWC9q Nudges_isPdp__uEFfk")
            if ranking and ranking.text.strip() != "Free Delivery":
                product["ranking"] = ranking.text.strip()
            else:
                product["ranking"] = ""

            project_overview = soup.find("div", class_="OverviewTab_overviewDescriptionCtr__d5ELj")
            product["product_overview"] = project_overview.text.strip() if project_overview else ""

            highlights_div = soup.find("div", class_=lambda c: c and "OverviewTab_highlightsCtr" in c)
            if highlights_div:
                highlights = [li.get_text(strip=True) for li in highlights_div.find_all("li")]
                product["highlights"] = "\n".join(highlights)
            else:
                product["highlights"] = ""

        return self.json_data

    def fetch_product_details(self, url):
        response = requests.get(url, headers=self.headers)
        if response.status_code == 200:
            return BeautifulSoup(response.text, "html.parser")
        else:
            print(f"Failed to fetch product details for URL: {url} (status: {response.status_code})")
            return None

 

if __name__ == "__main__":
    scraper = noon_scrape()
    scraper.product_metadata()
    print("\n Scraping and metadata extraction completed successfully!")
    print(f"Final JSON file saved at: {scraper.json_path}")