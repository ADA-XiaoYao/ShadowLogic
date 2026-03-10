import json
import os

class DataManager:
    """ShadowLogic 的数据管理模块，负责会话和扫描数据的持久化。"""
    
    def __init__(self, data_dir=".shadowlogic_data"):
        self.data_dir = data_dir
        if not os.path.exists(self.data_dir):
            os.makedirs(self.data_dir)

    def save_session(self, session_id, data):
        """保存会话数据。"""
        filepath = os.path.join(self.data_dir, f"{session_id}.json")
        with open(filepath, 'w') as f:
            json.dump(data, f, indent=4)

    def load_session(self, session_id):
        """加载会话数据。"""
        filepath = os.path.join(self.data_dir, f"{session_id}.json")
        if os.path.exists(filepath):
            with open(filepath, 'r') as f:
                return json.load(f)
        return None

    def list_sessions(self):
        """列出所有已保存的会话。"""
        return [f.replace(".json", "") for f in os.listdir(self.data_dir) if f.endswith(".json")]
