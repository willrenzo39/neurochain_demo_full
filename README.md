# 🧠 NeuroChain: AI-Powered Supply Chain Forecasting

Welcome to the **NeuroChain** demo — an AI-enhanced, real-time demand forecasting dashboard built using **Streamlit**, **Prophet**, and **Docker**. This app is designed for showcasing intelligent SAP S/4HANA-integrated supply chain scenarios and building AI confidence for small to mid-sized businesses.

---

## 🚀 Features

- Upload your own historical sales CSV file
- Generate future demand forecasts using Meta’s Prophet model
- Interactive dashboards powered by Plotly
- Containerized with Docker for fast and reproducible deployment
- Deploy-ready on Render or Heroku

---

## 🗂️ Project Structure

```bash
neurochain_demo/
├── app/
│   └── main.py               # Streamlit application logic
├── requirements.txt          # Python dependencies
├── Dockerfile                # Docker container definition
└── README.md                 # You're reading it
```

---

## 📦 Installation (Local)

1. **Clone the repo**
   ```bash
   git clone https://github.com/your-username/neurochain_demo.git
   cd neurochain_demo
   ```

2. **Create and activate a virtual environment (optional but recommended)**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the app**
   ```bash
   streamlit run app/main.py
   ```

---

## 🐳 Docker Deployment

1. **Build the Docker image**
   ```bash
   docker build -t neurochain-demo .
   ```

2. **Run the container**
   ```bash
   docker run -p 8501:8501 neurochain-demo
   ```

Then open [http://localhost:8501](http://localhost:8501) in your browser.

---

## 🌐 Deploying to Render

1. Push your project to a **GitHub repo**
2. Go to [Render.com](https://render.com)
3. Create a **New Web Service**
4. Select:
   - Runtime: **Docker**
   - Branch: `main`
   - Port: `8501`
   - Leave build/start commands empty
5. Wait for 3–5 min for the app to go live

---

## 📄 Data Format

Your input CSV should have **two columns**:
```csv
ds,y
2024-01-01,150
2024-01-02,180
...
```

- `ds`: Date (YYYY-MM-DD)
- `y`: Historical sales or demand value

---

## 🧠 Future Roadmap

- Integration with SAP OData APIs
- Inventory optimization module (via reinforcement learning)
- Real-time IoT sensor inputs
- Alert engine and auto-ordering triggers

---

## 🤝 Contact

For collaboration or enterprise inquiries:

**Renzo**  
📧 your-email@example.com  
🔗 [LinkedIn](https://linkedin.com/in/your-profile)