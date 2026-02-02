# 📦 Noon Scraper

A Python-based scraper to fetch product listings and details from [Noon.com](https://www.noon.com), with support for both **CLI mode** and **FastAPI** for API access.

---

## 🔧 Installation & Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/BairagiP/noon-scraper.git
   cd noon_scraper
   ```

2. **Create & activate a virtual environment**
   ```bash
   python -m venv venv
   venv\Scripts\activate   # On Windows
   # source venv/bin/activate  # On Linux/Mac
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

---

## ▶️ Running the Project

### Run with FastAPI

Start the API server:
```bash
uvicorn app:app --reload
```

Open your browser at:  
👉 [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

Example API Call

```bash
POST http://127.0.0.1:8000/scrape?query=mobiles&pages=3
```
Example Response
```bash 
{
  "extracted_data": [
    {
      "title": "Apple MacBook Air M1",
      "price": "AED 3,999",
      "rating": "4.8",
      "reviews": "125",
      "category": "Electronics & Mobiles > Laptops"
    }
  ]
}
```
## 🛠 Requirements
- Python 3.8+  
- FastAPI  
- Uvicorn  
- Requests  
- BeautifulSoup4  

## 📌 Notes

CLI mode saves data to extracted.json.

API mode returns structured JSON responses.


## Running Published Code

 will be added in future
