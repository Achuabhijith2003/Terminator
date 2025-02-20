class MemoryManager:
    def __init__(self):
        self.memory = []

    def save_memory(self, data):
        self.memory.append(data)

    def retrieve_memory(self):
        return self.memory

    def clear_memory(self):
        self.memory.clear()