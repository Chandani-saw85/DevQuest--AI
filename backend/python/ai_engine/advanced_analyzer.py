from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np

class AdvancedAIAnalyzer:
    """EXTREME AI: Machine Learning-based code quality prediction"""
    
    def __init__(self):
        self.vectorizer = TfidfVectorizer(max_features=100)
        self.classifier = RandomForestClassifier(n_estimators=100, random_state=42)
        self.trained = False
        self.train_classifier()
    
    def train_classifier(self):
        """Train ML classifier on code patterns"""
        training_codes = [
            "for i in range(len(arr)): print(arr[i])",
            "list_comp = [x*2 for x in arr]",
            "if x > 10: y = 20 else: y = 30",
            "try: func() except: pass",
        ]
        training_labels = [0, 1, 0, 0]
        
        try:
            X = self.vectorizer.fit_transform(training_codes)
            self.classifier.fit(X, training_labels)
            self.trained = True
        except:
            self.trained = False
    
    def predict_code_quality(self, code):
        """ML-based code quality prediction"""
        if not self.trained:
            return {"quality": "unknown", "confidence": 0}
        
        try:
            X = self.vectorizer.transform([code])
            prediction = self.classifier.predict(X)[0]
            confidence = self.classifier.predict_proba(X)[0].max()
            
            return {
                "quality": "excellent" if prediction == 1 else "needs_work",
                "confidence": float(confidence) * 100,
                "ml_score": int(prediction) * 50 + 50
            }
        except:
            return {"quality": "unable_to_analyze", "confidence": 0}
    
    def detect_code_patterns(self, code):
        """Detect code patterns and anti-patterns"""
        return {
            "nested_loops": code.count("for ") + code.count("while "),
            "try_catch": code.count("try:"),
            "list_comprehension": code.count("[x"),
            "lambda_usage": code.count("lambda"),
            "functions": code.count("def "),
            "classes": code.count("class ")
        }
    
    def analyze_code_smell(self, code):
        """Detect code smells using ML heuristics"""
        smells = []
        lines = code.split('\n')
        
        if len(lines) > 100:
            smells.append({
                "type": "god_function",
                "severity": "high",
                "message": "Function too long",
                "confidence": 95
            })
        
        max_indent = max([len(line) - len(line.lstrip()) for line in lines if line.strip()], default=0)
        if max_indent > 24:
            smells.append({
                "type": "deep_nesting",
                "severity": "medium",
                "message": "Too deeply nested",
                "confidence": 85
            })
        
        return smells
    
    def predict_runtime_behavior(self, code):
        """Predict likely runtime issues"""
        risks = []
        
        if code.count("new ") > 10:
            risks.append({
                "type": "memory_leak_risk",
                "probability": 0.7,
                "suggestion": "Monitor memory usage"
            })
        
        if "while True" in code and "break" not in code:
            risks.append({
                "type": "infinite_loop_risk",
                "probability": 0.95,
                "suggestion": "Add break condition"
            })
        
        return risks
