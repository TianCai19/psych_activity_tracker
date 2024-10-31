# memory.py

import json
import os
import uuid
from datetime import datetime, timedelta
import config
import streamlit as st

class MemoryManager:
    def __init__(self, storage_file='memory.json'):
        self.storage_file = storage_file
        if 'memory_buffer' not in st.session_state:
            st.session_state.memory_buffer = self.load_memory()

    def load_memory(self):
        if os.path.exists(self.storage_file):
            with open(self.storage_file, 'r', encoding='utf-8') as f:
                return json.load(f)
        return []

    def save_memory(self):
        with open(self.storage_file, 'w', encoding='utf-8') as f:
            json.dump(st.session_state.memory_buffer, f, ensure_ascii=False, indent=4)

    def add_record(self, user_input):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        record_id = str(uuid.uuid4())
        entry = {
            "id": record_id,
            "timestamp": timestamp,
            "content": user_input
        }
        st.session_state.memory_buffer.append(entry)
        self.save_memory()
        return record_id

    def remove_record(self, record_id):
        initial_length = len(st.session_state.memory_buffer)
        st.session_state.memory_buffer = [entry for entry in st.session_state.memory_buffer if entry["id"] != record_id]
        if len(st.session_state.memory_buffer) < initial_length:
            self.save_memory()
            return True
        return False

    def get_all_records(self):
        return st.session_state.memory_buffer

    def clean_old_entries(self):
        cutoff = datetime.now() - timedelta(days=config.MEMORY_RETENTION_DAYS)
        new_history = []
        for entry in st.session_state.memory_buffer:
            try:
                timestamp_str = entry["timestamp"]
                timestamp = datetime.strptime(timestamp_str, "%Y-%m-%d %H:%M:%S")
                if timestamp >= cutoff:
                    new_history.append(entry)
            except (ValueError, KeyError):
                # 如果格式不正确，保留该条记录
                new_history.append(entry)
        st.session_state.memory_buffer = new_history
        self.save_memory()


class ConversationManager:
    def __init__(self, storage_file='conversations.json'):
        self.storage_file = storage_file
        if 'conversation_buffer' not in st.session_state:
            st.session_state.conversation_buffer = self.load_conversations()

    def load_conversations(self):
        if os.path.exists(self.storage_file):
            with open(self.storage_file, 'r', encoding='utf-8') as f:
                return json.load(f)
        return []

    def save_conversations(self):
        with open(self.storage_file, 'w', encoding='utf-8') as f:
            json.dump(st.session_state.conversation_buffer, f, ensure_ascii=False, indent=4)

    def add_conversation(self, user_input, feedback):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        conversation_id = str(uuid.uuid4())
        entry = {
            "id": conversation_id,
            "timestamp": timestamp,
            "user_input": user_input,
            "feedback": feedback
        }
        st.session_state.conversation_buffer.append(entry)
        self.save_conversations()
        return conversation_id

    def remove_conversation(self, conversation_id):
        initial_length = len(st.session_state.conversation_buffer)
        st.session_state.conversation_buffer = [
            entry for entry in st.session_state.conversation_buffer if entry["id"] != conversation_id
        ]
        if len(st.session_state.conversation_buffer) < initial_length:
            self.save_conversations()
            return True
        return False

    def get_all_conversations(self):
        return st.session_state.conversation_buffer

    def clean_old_conversations(self):
        cutoff = datetime.now() - timedelta(days=config.MEMORY_RETENTION_DAYS)
        new_history = []
        for entry in st.session_state.conversation_buffer:
            try:
                timestamp_str = entry["timestamp"]
                timestamp = datetime.strptime(timestamp_str, "%Y-%m-%d %H:%M:%S")
                if timestamp >= cutoff:
                    new_history.append(entry)
            except (ValueError, KeyError):
                new_history.append(entry)
        st.session_state.conversation_buffer = new_history
        self.save_conversations()