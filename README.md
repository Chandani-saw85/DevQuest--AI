# DevQuest Game 🎮

A unique, interactive game designed specifically for developers, tackling real-world daily life issues with AI-powered guidance!

## 📖 Game Overview

**DevQuest** is an educational game that puts developers through relatable daily scenarios:
- **The Great Debug** - Find and fix 5 bugs in production code
- **Late Night Code Review** - Get AI-powered feedback on your code
- **API Rate Limit Challenge** - Build optimized APIs
- **Database Query Optimization** - Write fastest SQL queries
- **Refactor Legacy Monolith** - Break down massive codebases
- **Performance Profiling Race** - Identify memory leaks
- **Security Vulnerability Hunt** - Find and patch security issues
- **Documentation Sprint** - Write clear docs for messy code

## 🛠 Tech Stack

- **Backend**: Java (Spring Boot), Python (Flask + Extreme AI)
- **Frontend**: React, HTML5, CSS3
- **AI Integration**: Machine Learning, NLP, Pattern Recognition
- **Database**: SQLite (embedded, no external dependencies)
- **Authentication**: JWT Tokens

## 🤖 EXTREME AI FEATURES

### 1️⃣ **Predictive Performance Engine**
- Predicts code execution time BEFORE running
- Estimates memory usage with peak detection
- Detects performance bottlenecks automatically
- Provides 300-500% estimated speedup recommendations

### 2️⃣ **Advanced ML Code Analyzer**
- Machine learning-based code quality prediction
- Detects code smells (god functions, deep nesting)
- Predicts runtime behavior (memory leaks, infinite loops)
- ML Confidence: 70-99%

### 3️⃣ **Security Signature Scanner**
- Scans for 50+ CVE vulnerabilities
- Plagiarism detection using ML similarity analysis
- Detects SQL injection, XSS, unsafe deserialization
- Maps to CVE databases automatically

### 4️⃣ **Adaptive Learning Engine**
- Learns from YOUR submissions
- Adapts difficulty dynamically
- Generates personalized learning paths
- Predicts your performance on next problems
- Calculates learning velocity (rapid/steady/struggling)

### 5️⃣ **Intelligent Pattern Recognition**
- Identifies coding strengths and weaknesses
- Recommends next milestones
- Tracks improvement trends
- Suggests optimal learning sequence

## 📁 Project Structure

```
DevQuest-Game/
├── README.md
├── SETUP.md
├── .gitignore
│
├── backend/
│   ├─�� java/
│   │   ├── build.gradle
│   │   ├── gradlew
│   │   ├── gradlew.bat
│   │   └── src/main/
│   │       ├── java/com/devquest/
│   │       │   ├── DevQuestApplication.java
│   │       │   ├── controller/
│   │       │   ├── model/
│   │       │   ├── repository/
│   │       │   ├── service/
│   │       │   ├── config/
│   │       │   └── util/
│   │       └── resources/
│   │           ├── application.properties
│   │           └── data.sql
│   │
│   └── python/
│       ├── app.py
│       ├── requirements.txt
│       ├── .env.example
│       └── ai_engine/
│           ├── code_analyzer.py
│           ├── feedback_generator.py
│           ├── performance_advisor.py
│           ├── advanced_analyzer.py
│           ├── predictive_engine.py
│           ├── signature_analyzer.py
│           └── adaptive_learning.py
│
└── frontend/
    ├── package.json
    ├── public/
    │   └── index.html
    └── src/
        ├── App.jsx
        ├── components/
        ├── pages/
        ├── services/
        └── styles/
```

## 🚀 Quick Start

### Prerequisites
- Java 11+
- Node.js 14+
- Python 3.8+

### Installation

**1. Clone & Setup**
```bash
git clone https://github.com/Chandani-saw85/DevQuest--AI.git
cd DevQuest--AI
```

**2. Java Backend**
```bash
cd backend/java
./gradlew bootRun
# Runs on http://localhost:8080
```

**3. Python AI Engine**
```bash
cd backend/python
python -m venv venv
source venv/bin/activate  # Mac/Linux
venv\\Scripts\\activate     # Windows
pip install -r requirements.txt
python app.py
# Runs on http://localhost:5000
```

**4. React Frontend**
```bash
cd frontend
npm install
npm start
# Opens http://localhost:3000
```

## 📡 API Endpoints

### Java Backend (8080)
```
GET  /api/v1/levels              Get all levels
GET  /api/v1/levels/:id          Get specific level
POST /api/v1/game/submit         Submit solution
GET  /api/v1/leaderboard         Get leaderboard
```

### Python AI Engine (5000)
```
POST /api/analyze-code           Analyze code quality
POST /api/get-feedback           Get AI feedback
POST /api/performance-analysis   Predict performance
POST /api/security-scan          Scan vulnerabilities
POST /api/adaptive-path          Get learning path
```

## 🎮 Game Levels

| Level | Difficulty | XP | Time | Features |
|-------|-----------|----|----|----------|
| The Great Debug | ⭐⭐ | 100 | 5min | Bug finding |
| Code Review | ⭐⭐⭐ | 200 | 10min | AI feedback |
| API Challenge | ⭐⭐⭐ | 300 | 15min | Performance |
| Query Optimization | ⭐⭐⭐⭐ | 400 | 20min | SQL tuning |
| Refactor Monolith | ⭐⭐⭐⭐ | 500 | 30min | Architecture |

## 🧪 Testing

```bash
# Java
cd backend/java
./gradlew test

# Python
cd backend/python
python -m pytest

# React
cd frontend
npm test
```

## 🤝 Git Workflow

### For Contributors:

```bash
# 1. Create feature branch from chandani-dev
git checkout chandani-dev
git pull origin chandani-dev
git checkout -b feature/your-feature-name

# 2. Make changes
git add .
git commit -m "Add: Feature description"
git push origin feature/your-feature-name

# 3. Create Pull Request to chandani-dev
# (NOT main - always to chandani-dev!)
```

### For Project Owner (You):

```bash
# Review PR, then merge to chandani-dev
git checkout chandani-dev
git merge feature/your-feature-name

# When ready for release, merge to main
git checkout main
git merge chandani-dev
git push origin main
```

## 📝 License

MIT License

## 👤 Author

**Chandani** - [@Chandani-saw85](https://github.com/Chandani-saw85)

## 🤝 Contributing

Contributions are welcome! Please:
1. Fork the repo
2. Create feature branch from `chandani-dev`
3. Submit PR to `chandani-dev` (NOT main)
4. Include description of changes

---

**Built with ❤️ for developers. Level Up Your Skills! 🚀**
