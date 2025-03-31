import re
import json
from src.regex_patterns import PATTERNS
from src.file_handler import read_file, save_report

class SensitiveDataScanner:
    def __init__(self):
        self.results = []

    def scan_repository(self, filepath):
        content = read_file(filepath)
        for pattern_name, pattern in PATTERNS.items():
            if re.search(pattern, content):
                self.results.append({"file": filepath, "issue": pattern_name})

        save_report(self.results)
