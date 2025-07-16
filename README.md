# Reddit User Persona Analyzer

This project analyzes Reddit user data to generate detailed user personas using AI-powered analysis.

---

## ✨ Features

- 🔍 Scrapes Reddit user data using **PRAW (Python Reddit API Wrapper)**.
- 🤖 Analyzes user data with **Gemini API** to generate rich user personas.
- 🖥️ Provides a **CLI interface** and a **Streamlit-based web frontend**.
- 🔐 Supports secure configuration via **environment variables** and **Streamlit secrets**.

---

## 📦 Installation

### 1. Clone the repository:

```bash
git clone <repository-url>
cd reddit
````

### 2. Create a virtual environment and activate it:

```bash
conda create --name reddit python=3.10 -y
conda activate reddit
```

### 3. Install dependencies:

```bash
pip install -r requirements.txt
```

---

## ⚙️ Configuration

You can provide credentials either via a `.env` file or through Streamlit secrets.

### Required credentials:

* `CLIENT_ID`: Reddit API client ID
* `CLIENT_SECRET`: Reddit API client secret
* `USER_AGENT`: User agent string for Reddit API
* `GOOGLE_API_KEY`: API key for Gemini AI service

### For Streamlit:

Create a file at `.streamlit/secrets.toml` with the following:

```toml
CLIENT_ID = "your_client_id"
CLIENT_SECRET = "your_client_secret"
USER_AGENT = "your_user_agent"
GOOGLE_API_KEY = "your_gemini_api_key"
```

---

## 🚀 Usage

### Command Line Interface

Run the script with a Reddit user URL:

```bash
python main.py --url https://www.reddit.com/user/username
```

### Streamlit Frontend

Launch the web app:

```bash
streamlit run streamlit_app.py
```

Then, enter the Reddit user URL in the interface to generate the persona.

---

## 🗂️ Project Structure

```
reddit/
├── analyzer.py             # AI analysis of scraped Reddit data
├── app.py                  # Streamlit frontend
├── config.py               # Environment variable and secrets loader
├── main.py                 # CLI entry point
├── persona.py              # Persona generation logic
├── scraper.py              # Reddit data scraping logic
├── .streamlit/
│   └── secrets.toml        # Secrets for Streamlit app
├── requirements.txt        # Python dependencies
└── output/                 # Directory for generated persona text files
```

---

## 📄 License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.

---

## 🤝 Contributing

Feel free to open issues or submit pull requests for improvements!
