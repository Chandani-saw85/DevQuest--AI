# DevQuest Setup Guide

## System Requirements

### Windows
```batch
java -version
node -v
python --version
```

### Mac/Linux
```bash
java -version
node -v
python3 --version
```

## Installation

### 1. Java Backend

```bash
cd backend/java
./gradlew bootRun
```

**Expected Output:**
```
DevQuestApplication started successfully
Port: 8080
```

### 2. Python AI Engine

```bash
cd backend/python
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python app.py
```

**Expected Output:**
```
🤖 AI Engine running on http://localhost:5000
✅ AI services ready
```

### 3. React Frontend

```bash
cd frontend
npm install
npm start
```

**Browser opens:**
```
http://localhost:3000
```

## Verification

```bash
# Check Java (8080)
curl http://localhost:8080/api/v1/health

# Check Python (5000)
curl http://localhost:5000/api/health

# Check React (3000)
# Visit http://localhost:3000 in browser
```

## Troubleshooting

### Port Already in Use
```bash
# Mac/Linux
lsof -i :8080
kill -9 <PID>

# Windows
netstat -ano | findstr :8080
taskkill /PID <PID> /F
```

### Python Virtual Environment
```bash
# Activate
source venv/bin/activate  # Mac/Linux
venv\\Scripts\\activate     # Windows

# Deactivate
deactivate
```

### Clear Cache
```bash
# Python
find . -type d -name __pycache__ -exec rm -r {} +

# Node
rm -rf node_modules
npm install
```

## Next Steps

1. Open http://localhost:3000
2. Create account
3. Start Level 1
4. Get AI feedback
5. Climb the leaderboard!

Enjoy DevQuest! 🎮
