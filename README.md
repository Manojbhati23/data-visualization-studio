# 📊 Data Visualization Studio Pro

An interactive data visualization and analytics platform built with Python, Streamlit, and Matplotlib.

Users can upload CSV datasets, perform exploratory data analysis (EDA), generate interactive visualizations, create PDF reports, and run basic machine learning predictions.

---

## 🚀 Features

### 📁 Data Upload
- Upload CSV files
- Automatic dataset preview
- View rows and columns

### 📈 Data Visualization
- Line Charts
- Bar Charts
- Scatter Plots
- Histograms
- Box Plots
- Correlation Heatmaps
- 3D Scatter Plots

### 🔍 Exploratory Data Analysis (EDA)
- Dataset Summary
- Statistical Information
- Missing Value Detection
- Data Type Analysis

### 🤖 Machine Learning
- Linear Regression Demo
- Simple Prediction Engine

### 📄 Export
- Download Charts as PNG
- Generate PDF Reports

### ⚙️ DevOps
- Docker Support
- GitHub Actions CI/CD
- Git Version Control

---

## 🛠 Tech Stack

### Backend

- Python
- Pandas
- NumPy
- Scikit-Learn

### Visualization

- Matplotlib
- Seaborn

### Frontend

- Streamlit

### Reporting

- ReportLab

### DevOps

- Docker
- GitHub Actions

---

## 📂 Project Structure

```text
data-visualization-studio/
│
├── app.py
├── requirements.txt
├── README.md
├── Dockerfile
├── .gitignore
│
├── modules/
│   ├── charts.py
│   ├── eda.py
│   ├── export.py
│   └── ml.py
│
├── assets/
│
└── .github/
    └── workflows/
        └── python.yml
```

---

## 📦 Installation

Clone the repository:

```bash
git clone [https://github.com/Manojbhati23](https://github.com/Manojbhati23/data-visualization-studio)

cd data-visualization-studio
```

Create a virtual environment:

### Windows

```bash
python -m venv venv

venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv venv

source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## ▶️ Run Application

```bash
streamlit run app.py
```

Application will start at:

```text
http://localhost:8501
```

---

## 🧪 Sample Dataset

Create a file named:

```text
sample.csv
```

Example:

```csv
Month,Sales,Profit,Customers
Jan,100,20,50
Feb,120,30,55
Mar,150,45,60
Apr,170,50,70
May,220,70,95
Jun,260,85,100
```

Upload the file inside the application.

---

## 📊 Example Visualizations

### Line Chart

Shows trends over time.

### Scatter Plot

Displays relationships between variables.

### Heatmap

Displays correlations among numerical features.

### 3D Scatter Plot

Visualizes data across three dimensions.

---

## 🐳 Docker Support

Build Docker image:

```bash
docker build -t visualization-studio .
```

Run container:

```bash
docker run -p 8501:8501 visualization-studio
```

---

## 🔄 GitHub Actions

Continuous Integration is enabled using GitHub Actions.

The pipeline:

- Installs dependencies
- Validates Python code
- Runs automatically on every push

Workflow file:

```text
.github/workflows/python.yml
```

---

## 🚀 Deployment

### Streamlit Cloud

1. Push project to GitHub
2. Open Streamlit Cloud
3. Select repository
4. Choose:

```text
main
app.py
```

5. Deploy

---

## 🎯 Future Enhancements

- Real-time Stock Market Dashboard
- Interactive Plotly Graphs
- Forecasting Models
- User Authentication
- Database Integration
- AI-powered Data Insights
- Azure Deployment
- AWS Deployment
- Kubernetes Support

---

## 🤝 Contributing

Contributions are welcome.

1. Fork repository
2. Create feature branch
3. Commit changes
4. Push branch
5. Open Pull Request

---

## 📜 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

**Manoj Kumar**

GitHub: https://github.com/Manojbhati23
LinkedIn: https://www.linkedin.com/in/manoj-kumar-593436241/

---

### ⭐ If you found this project useful, please give it a star!
