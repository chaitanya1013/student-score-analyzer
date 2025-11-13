# 📊 Student Score Analyzer (Python + Docker)

A simple and clean Python project that analyzes student scores and calculates:

- Highest score  
- Lowest score  
- Average score  
- Total students  

This project is fully containerized with Docker and demonstrates **Python development, modular coding, error handling, and containerization** — ideal for DevOps learning and portfolio building.

---

## 🚀 Features

- Reads student score data from a text file  
- Validates student data format  
- Calculates useful statistics  
- Shows execution timestamp  
- Dockerized for consistent and portable execution  
- Clean and modular folder structure  

---

## 📁 Project Structure

student-score-analyzer/
│
├── app/
│ ├── analyzer.py # Main Python script
│ ├── utils.py # Reusable data parsing + logic
│ └── data.txt # Input dataset
│
├── Dockerfile # Docker build instructions
└── .gitignore # Ignored files

---

## 🧪 Sample Input (data.txt)

Aman,85
Riya,92
Karan,76
Sneha,88
John,95

---

## 💻 Run Locally (Without Docker)

Make sure Python 3 is installed.

```sh
python3 app/analyzer.py

```

🐳 Docker Setup
Build Docker Image

docker build -t score-analyzer .

Run Docker Container

docker run --rm score-analyzer

Expected Output

📊 Student Score Analyzer
🕒 Execution Time: 2025-11-12 11:23:45

Total Students: 5
Highest Score: 95
Lowest Score: 76
Average Score: 87.2

✔️ Analysis Completed Successfully!


🛠 Tools & Technologies Used
Python 3.12 (slim)
Docker
Modular Python programming
Error handling & data validation

🤝 Contribution
Contributions are welcome!
If you want to improve the analyzer or convert it to a REST API using Flask, feel free to fork the repo and open a pull request.

📄 License
This project is open-source and available under the MIT License.

⭐ Future Enhancements
Convert to Flask API (/analyze)
Add database (MySQL/PostgreSQL) with Docker Compose
Auto CI/CD using GitHub Actions
Add unit tests (pytest)
