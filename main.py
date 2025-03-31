import logging
from src.scanner import SensitiveDataScanner

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

if __name__ == "__main__":
    logging.info("Starting the sensitive data scan...")
    
    scanner = SensitiveDataScanner()
    
    try:
        scanner.scan_repository("data/sample.txt")  # Replace with actual repo files
        logging.info("Scan completed successfully.")
    except Exception as e:
        logging.error(f"Error during scan: {e}")
