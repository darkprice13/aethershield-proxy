import re
import yaml
import uuid

class AetherShieldEngine:
    def __init__(self):
        # Explicitly initialize data stores to prevent runtime AttributeErrors
        self._vault = {}
        self.audit_logs = []
        self.keywords = []
        self.signatures = {}
        self.load_config()

    def load_config(self):
        """Safely loads institutional data compliance parameters from config.yaml"""
        try:
            with open("config.yaml", "r") as f:
                config = yaml.safe_load(f)
                if config:
                    self.keywords = config.get("proprietary_keywords", [])
                    self.signatures = config.get("compiled_signatures", {})
        except Exception:
            # Safe local fallback arrays if configuration is unreadable
            self.keywords = []
            self.signatures = {}

    async def initialize_session(self) -> str:
        session_id = str(uuid.uuid4())[:8]
        self._vault[session_id] = {}
        return session_id

    async def secure_inbound_payload(self, session_id: str, raw_text: str) -> str:
        if session_id not in self._vault:
            self._vault[session_id] = {}
        
        sanitized = raw_text
        session_map = self._vault[session_id]

        # 1. Parse regular expression financial signatures (Cards, IBANs, Routing Codes)
        for key, pattern in self.signatures.items():
            try:
                matches = re.findall(pattern, sanitized)
                for i, match in enumerate(set(matches)):
                    token = f"{{{{{key}_{i+1}}}}}"
                    session_map[token] = match
                    sanitized = sanitized.replace(match, token)
            except Exception:
                continue

        # 2. Parse proprietary structural phrases
        for i, keyword in enumerate(self.keywords):
            if keyword in sanitized:
                token = f"{{{{CORP_ASSET_{i+1}}}}}"
                session_map[token] = keyword
                sanitized = sanitized.replace(keyword, token)

        return sanitized

    async def restore_outbound_payload(self, session_id: str, response_text: str) -> str:
        if session_id not in self._vault:
            raise ValueError("Session memory trace has been flushed.")
        
        restored = response_text
        session_map = self._vault[session_id]
        
        # Sort tokens by length descending to prevent partial replacement bugs
        sorted_tokens = sorted(session_map.keys(), key=len, reverse=True)
        for token in sorted_tokens:
            restored = restored.replace(token, session_map[token])
            
        return restored

    async def close_session_vault(self, session_id: str):
        if session_id in self._vault:
            del self._vault[session_id]

    # Native Python 3.9+ lowercase typing eliminates external dependency requirements
    async def get_compliance_logs(self) -> list[dict]:
        return self.audit_logs