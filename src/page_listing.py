import requests
import json
import time

def scrape_noon_products(query, output_file,max_pages=None):
    BASE_URL = "https://www.noon.com/_svc/catalog/api/v3/u/search?q={}&limit=50&page={}"

    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-US,en;q=0.9',
        'cache-control': 'no-cache, max-age=0, must-revalidate, no-store',
        'referer': f'https://www.noon.com/uae-en/search/?q={query}',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36'
    }
    
    products = []
    page = 1

    while True:  
        if max_pages and page > max_pages:   # stop if reached limit
            break
        url = BASE_URL.format(query, page)
        print(f"Fetching page {page} for query '{query}'...")

        response = requests.get(url, headers=headers)
        if response.status_code != 200:
            print(f"Failed at page {page}, status: {response.status_code}")
            break

        data = response.json()
        hits = data.get('hits', [])

        if not hits:
            break

        for hit in hits:
            sku = hit.get('sku', '')
            brand = hit.get('brand', '')
            product_name = hit.get('name', '')
            offer_code = hit.get('offer_code', '')

            product_url = f"https://www.noon.com/uae-en/{hit.get('url', '')}/{sku}/p/?o={offer_code}"

            price = hit.get('price', '')
            sale_price = hit.get('sale_price', '')

            image_key = hit.get('image_key', '')
            main_image_url = f"https://f.nooncdn.com/p/{image_key}.jpg?width=800" if image_key else ''

            image_keys = hit.get('image_keys', [])
            all_images = [f"https://f.nooncdn.com/p/{img_key}.jpg?width=800" for img_key in image_keys]

            products.append({
                'sku': sku,
                'brand': brand,
                'product_name': product_name,
                'product_url': product_url,
                'price': price,
                'sale_price': sale_price,
                'main_image_url': main_image_url,
                'all_image_urls': all_images
            })

        page += 1
        time.sleep(1)

    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(products, f, indent=2, ensure_ascii=False)

    print(f"Extracted {len(products)} products across {page-1} pages to {output_file}")


if __name__ == "__main__":
    search_query = input("Enter search term (e.g. mobiles, laptops, watches): ").strip()
    num_pages = input("Enter number of pages to scrape (leave blank for all): ").strip()
    num_pages = int(num_pages) if num_pages else None
    file_name = "extracted.json"

    scrape_noon_products(search_query, file_name,num_pages)
