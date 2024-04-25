class MiniDatabase:
    def __init__(self):
        self.data = []

    def insert(self, record):
        if isinstance(record, dict):
            self.data.append(record)
        else:
            raise ValueError("Record must be a dictionary")

    def update(self, identifier, key, value):
        updated = False
        for record in self.data:
            if record.get(identifier[0]) == identifier[1]:
                record[key] = value
                updated = True
        return updated

    def query(self, key, value):
        result = []
        for record in self.data:
            if record.get(key) == value:
                result.append(record)
        return result