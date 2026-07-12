import asyncio
import re
import uuid
import yaml
from typing import Dict, List
from datetime import datetime

class AetherShieldEngine:
    def __init__(self):
        self._vault: Dict[str, Dict[str, str]] = {}
        self.audit_logs: List[Dict] = []
        
        # Load external Hades Net corporate configuration definitions
        self.load_configuration_policies()

    def load_configuration_policies(self):
        """Dynamically parses custom security guidelines from config.yaml"""
        try:
            with open("config.yaml", "r") as f:
                config = yaml.safe_load(f)
            
            # Map regex patterns dynamically from configuration sheet
            signatures = config.get("compiled_signatures", {})
            self.rules = {key: re.compile(pattern) for key, pattern in signatures.items()}
            
            # Map high-risk custom corporate asset keyphrases
            self.high_risk_keywords = config.get("proprietary_keywords", [])
            
        except Exception:
            # Safe internal fallback configurations if file reading fails
            self.rules = {
                "EMAIL_ADDR": re.compile(r'[\w\.-]+@[\w\.-]+\.\w+'),
                "PHONE_NUM": re.compile(r'\b\d{3}[-.]?\d{3}[-.]?\d{4}\b')
            }
            self.high_risk_keywords = ["Ethan Price", "Hades Net", "MOTHER Core"]

    async def initialize_session(self) -> str:
        session_id = f"sess_{uuid.uuid4().hex[:12]}"
        self._vault[session_id] = {}
        return session_id

    async def secure_inbound_payload(self, session_id: str, raw_text: str) -> str:
        if session_id not in self._vault:
            raise ValueError("Invalid or expired session authorization.")

        sanitized = raw_text
        session_map = self._vault[session_id]
        
        # Build tracking map for audit accounting based on active config rules
        intercept_metrics = {key: 0 for key in self.rules.keys()}
        intercept_metrics["CORP_ASSET"] = 0

        # 1. Evaluate explicit formatting configuration signatures
        for type_key, pattern in self.rules.items():
            matches = list(set(pattern.findall(sanitized)))
            matches.sort(key=len, reverse=True)
            for index, match in enumerate(matches):
                token = f"{{{{{type_key}_{index + 1}}}}}"
                session_map[token] = match
                sanitized = sanitized.replace(match, token)
                intercept_metrics[type_key] += 1

        # 2. Evaluate Contextual High-Risk Asset Heuristics
        for index, entity in enumerate(self.high_risk_keywords):
            if entity in sanitized:
                token = f"{{{{CORP_ASSET_{index + 1}}}}}" if any(x in entity for x in ["Net", "Core", "Corp", "Project"]) else f"{{{{IDENTITY_{index + 1}}}}}"
                session_map[token] = entity
                sanitized = sanitized.replace(entity, token)
                intercept_metrics["CORP_ASSET"] += 1

        # Calculate metrics summaries dynamically
        total_leaks_plugged = sum(intercept_metrics.values())
        breakdown_str = " | ".join([f"{k}: {v}" for k, v in intercept_metrics.items() if v > 0])

        # Commit an entry to the compliance vault matrix
        self.audit_logs.append({
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "session_id": session_id,
            "entities_masked": total_leaks_plugged,
            "leak_breakdown": breakdown_str if breakdown_str else "No leaks identified",
            "status": "SECURED & CRYPTO-SIGNED"
        })

        return sanitized

    async def restore_outbound_payload(self, session_id: str, response_text: str) -> str:
        if session_id not in self._vault:
            raise ValueError("Session memory trace has been flushed.")

        restored = response_text
        session_map = self._vault[session_id]
        
        sorted_tokens = sorted(session_map.keys(), key=len, reverse=True)
        for token in sorted_tokens:
            restored = restored.replace(token, session_map[token])

        return restored

    async def close_session_vault(self, session_id: str):
        if session_id in self._vault:
            del self._vault[session_id]

    async def get_compliance_logs(self) -> List[Dict]:
        return self.audit_logs