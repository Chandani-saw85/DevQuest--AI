class CodeSignatureAnalyzer:
    """EXTREME AI: Vulnerability scanning and plagiarism detection"""
    
    def __init__(self):
        self.known_patterns = self._load_patterns()
    
    def _load_patterns(self):
        """Load known vulnerability patterns"""
        return {
            "insecure_hash": ["md5", "sha1"],
            "sql_injection_risk": ["+ str(", "f-string with query"],
            "xss_risk": ["innerHTML", "document.write"],
            "insecure_deserialization": ["pickle.loads", "ObjectInputStream"]
        }
    
    def scan_vulnerabilities(self, code):
        """Scan code for known vulnerabilities"""
        vulnerabilities = []
        
        dangerous_functions = {
            'eval': {'severity': 'CRITICAL', 'msg': 'Code execution vulnerability'},
            'exec': {'severity': 'CRITICAL', 'msg': 'Code execution vulnerability'},
            'pickle.loads': {'severity': 'CRITICAL', 'msg': 'Unsafe deserialization'},
            'yaml.load': {'severity': 'CRITICAL', 'msg': 'Use yaml.safe_load()'},
        }
        
        for func, info in dangerous_functions.items():
            if func in code:
                vulnerabilities.append({
                    "type": func,
                    "severity": info['severity'],
                    "message": info['msg'],
                    "line": self._find_line(code, func)
                })
        
        if any(x in code for x in ['password=', 'api_key=']):
            vulnerabilities.append({
                "type": "hardcoded_secret",
                "severity": "CRITICAL",
                "message": "Hardcoded credentials found"
            })
        
        return vulnerabilities
    
    def analyze_code_similarity(self, code1, code2):
        """Compare code snippets for similarity (plagiarism detection)"""
        norm1 = self._normalize_code(code1)
        norm2 = self._normalize_code(code2)
        
        common = len(set(norm1) & set(norm2))
        total = len(set(norm1) | set(norm2))
        similarity = (common / total * 100) if total > 0 else 0
        
        return {
            "similarity_percent": round(similarity, 2),
            "is_plagiarism": similarity > 80,
            "confidence": min(95, similarity * 0.9)
        }
    
    def _normalize_code(self, code):
        """Normalize code for comparison"""
        lines = code.split('\n')
        normalized = []
        
        for line in lines:
            if '#' in line:
                line = line[:line.index('#')]
            line = ' '.join(line.split())
            if line:
                normalized.append(line)
        
        return ' '.join(normalized)
    
    def _find_line(self, code, func):
        """Find line number of function"""
        for i, line in enumerate(code.split('\n')):
            if func in line:
                return i + 1
        return -1
