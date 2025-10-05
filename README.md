# 📦 Noon Scraper

A Python-based scraper to fetch product listings and details from [Noon.com](https://www.noon.com), with support for both **CLI mode** and **FastAPI** for API access.

---

## 🔧 Installation & Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/<your-username>/noon-scraper.git
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



## 🛠 Requirements
- Python 3.8+  
- FastAPI  
- Uvicorn  
- Requests  
- BeautifulSoup4  
