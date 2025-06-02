
# 🚀 Network API Test Automation with Cisco SD-WAN

This is an end-to-end **API Test Automation project** that integrates SDET and DevNet skills by automating Cisco SD-WAN APIs using Python, Pytest, Allure, and GitHub Actions. It covers real-world test scenarios, reporting, CI/CD, and reusable code modules.

---

## 📁 Project Structure

```bash
network-api-testing/
│
├── auth.py                # Handles authentication and token retrieval
├── api_helper.py          # Core API logic for inventory fetching, etc.
├── get_inventory.py       # Manual inventory fetch script
├── logger_config.py       # Centralized logging setup
├── requirements.txt       # Python dependencies
│
├── tests/
│   ├── test_inventory.py  # Positive tests for SD-WAN device inventory
│   ├── test_negative.py   # Negative tests (e.g., invalid auth, endpoints)
│   └── test_token.py      # Token validation tests
│
├── .github/
│   └── workflows/
│       └── api-tests.yml  # GitHub Actions workflow file
│
├── allure-results/        # Temporary test result files
├── report.html            # HTML report generated via pytest
└── README.md              # You're here!
```

---

## 🔧 Tech Stack & Tools

| Area               | Tool / Tech                  |
|--------------------|------------------------------|
| Language           | Python 3.11                   |
| Framework          | Pytest                        |
| API Client         | Requests                      |
| Reporting          | Pytest-HTML, Allure           |
| CI/CD              | GitHub Actions                |
| Target Platform    | Cisco SD-WAN Sandbox          |
| Logging            | Python's `logging` module     |

---

## 🧪 How to Run Tests Locally

### 🔹 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 🔹 2. Run All Tests
```bash
pytest tests/
```

### 🔹 3. Generate HTML Report
```bash
pytest --html=report.html --self-contained-html
```

### 🔹 4. Generate Allure Report (Optional)
```bash
pytest --alluredir=allure-results
allure serve allure-results
```

---

## 🛠️ GitHub Actions CI Setup

Tests run automatically on every push to `main` via this workflow:  
📄 `.github/workflows/api-tests.yml`

### ✅ CI Jobs Include:
- Set up Python and dependencies
- Run API tests
- Upload HTML + JSON reports
- (Optional) Run Allure CLI report generation *(commented)*

### 🔐 GitHub Secrets Used:
| Secret Name         | Description                        |
|---------------------|------------------------------------|
| `SDWAN_USERNAME`    | Cisco sandbox username             |
| `SDWAN_PASSWORD`    | Cisco sandbox password             |
| `SDWAN_BASE_URL`    | Base URL of vManage                |

---

## 📸 Screenshots

### ✅ Allure Report - Overview
![Allure Overview](screenshots/allure-overview.png)

### 📊 Allure Test Case View
![Allure Test Case](screenshots/allure-testcase.png)

### 💡 Pytest HTML Report
![Pytest HTML](screenshots/html-report.png)

> Replace `/screenshots/*.png` with your real screenshots.

---

## 📌 Key Features

- ✔️ Token-based authentication
- ✔️ Inventory validation and JSON checks
- ✔️ Negative tests for robustness
- ✔️ Token header handling (`X-XSRF-TOKEN`)
- ✔️ Modular reusable Python components
- ✔️ CI with reporting artifacts
- ✔️ Centralized logging

---

## 👤 Author

**Vishal Yadav**  
🔗 LinkedIn / Portfolio / GitHub (Insert links if public)
