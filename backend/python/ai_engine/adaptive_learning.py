class AdaptiveLearningEngine:
    """EXTREME AI: Learns from user submissions and adapts"""
    
    def __init__(self):
        self.user_profiles = {}
    
    def analyze_user_performance(self, user_id, submissions):
        """Analyze user's coding patterns and skill level"""
        if not submissions:
            return {"skill_level": "beginner", "confidence": 0}
        
        return {
            "total_submissions": len(submissions),
            "success_rate": self._calculate_success_rate(submissions),
            "average_score": self._calculate_average_score(submissions),
            "improvement_trend": self._calculate_trend(submissions),
            "skill_level": self._determine_skill_level(submissions),
            "strengths": self._identify_strengths(submissions),
            "weaknesses": self._identify_weaknesses(submissions),
            "learning_velocity": self._calculate_learning_velocity(submissions),
            "recommended_path": self._generate_learning_path(submissions)
        }
    
    def _calculate_success_rate(self, submissions):
        """Calculate success rate"""
        if not submissions:
            return 0
        successful = sum(1 for s in submissions if s.get('passed', False))
        return (successful / len(submissions)) * 100
    
    def _calculate_average_score(self, submissions):
        """Calculate average score"""
        if not submissions:
            return 0
        scores = [s.get('score', 0) for s in submissions]
        return sum(scores) / len(scores) if scores else 0
    
    def _calculate_trend(self, submissions):
        """Calculate performance trend"""
        if len(submissions) < 3:
            return "insufficient_data"
        recent = submissions[-5:]
        scores = [s.get('score', 0) for s in recent]
        if len(scores) < 2:
            return "stable"
        improvements = sum(1 for i in range(1, len(scores)) if scores[i] > scores[i-1])
        if improvements > len(scores) * 0.6:
            return "improving"
        elif improvements < len(scores) * 0.4:
            return "declining"
        else:
            return "stable"
    
    def _determine_skill_level(self, submissions):
        """Determine skill level"""
        avg_score = self._calculate_average_score(submissions)
        if avg_score >= 85:
            return "expert"
        elif avg_score >= 70:
            return "advanced"
        elif avg_score >= 55:
            return "intermediate"
        elif avg_score >= 40:
            return "beginner"
        else:
            return "novice"
    
    def _identify_strengths(self, submissions):
        """Identify coding strengths"""
        strengths = []
        for submission in submissions[-10:]:
            if submission.get('score', 0) >= 80:
                if submission.get('problem_type'):
                    strengths.append(submission.get('problem_type'))
        return strengths if strengths else ["fundamentals"]
    
    def _identify_weaknesses(self, submissions):
        """Identify weak areas"""
        weaknesses = []
        for submission in submissions[-10:]:
            if submission.get('score', 0) < 50:
                if submission.get('problem_type'):
                    weaknesses.append(submission.get('problem_type'))
        return weaknesses if weaknesses else ["none_identified"]
    
    def _calculate_learning_velocity(self, submissions):
        """Calculate learning speed"""
        if len(submissions) < 5:
            return "insufficient_data"
        recent_scores = [s.get('score', 0) for s in submissions[-5:]]
        old_scores = [s.get('score', 0) for s in submissions[-10:-5]]
        if not old_scores:
            return "new_learner"
        recent_avg = sum(recent_scores) / len(recent_scores)
        old_avg = sum(old_scores) / len(old_scores)
        improvement = recent_avg - old_avg
        if improvement > 15:
            return "rapid"
        elif improvement > 5:
            return "steady"
        else:
            return "stable"
    
    def _generate_learning_path(self, submissions):
        """Generate personalized learning path"""
        skill_level = self._determine_skill_level(submissions)
        paths = {
            "novice": ["arrays", "strings", "loops"],
            "beginner": ["data_structures", "sorting"],
            "intermediate": ["trees", "graphs"],
            "advanced": ["dynamic_programming", "recursion"],
            "expert": ["system_design", "optimization"]
        }
        return paths.get(skill_level, paths["beginner"])
