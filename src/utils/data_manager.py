import json
import os

class DataManager:
    """ShadowLogic's data management module, responsible for session and scan data persistence."""
    
    def __init__(self, data_dir=".shadowlogic_data"):
        self.data_dir = data_dir
        if not os.path.exists(self.data_dir):
            os.makedirs(self.data_dir)

    def save_session(self, session_id, data):
        """Saves session data."""
        filepath = os.path.join(self.data_dir, f"{session_id}.json")
        with open(filepath, 'w') as f:
            json.dump(data, f, indent=4)

    def load_session(self, session_id):
        """Loads session data."""
        filepath = os.path.join(self.data_dir, f"{session_id}.json")
        if os.path.exists(filepath):
            with open(filepath, 'r') as f:
                return json.load(f)
        return None

    def list_sessions(self):
        """Lists all saved sessions."""
        return [f.replace(".json", "") for f in os.listdir(self.data_dir) if f.endswith(".json")]
