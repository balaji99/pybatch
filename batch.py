import os
import logging
from datetime import datetime
import time


### BEGIN: Custom iterators and item processors

def display_file_information(file_path):
    """Display detailed information about a file."""
    try:
        file_stat = os.stat(file_path)
        logging.info(f"Processing file: {file_path}")
        print(f"File: {os.path.basename(file_path)}")
        print(f"Size: {file_stat.st_size} bytes")
        print(f"Last modified: {time.ctime(file_stat.st_mtime)}")
        print(f"Last accessed: {time.ctime(file_stat.st_atime)}")
        print(f"Mode: {file_stat.st_mode}")
        print("---")
        return True
    except Exception as e:
        logging.error(f"Error processing file {file_path}: {str(e)}")
        return False

def list_files(folder_path, config):
    """List all files in a folder, optionally including subdirectories."""
    logging.info(f"Listing files in folder: {folder_path}")
    recursive = config.get("recursive-sub-directories", False)
    
    if recursive:
        for root, _, files in os.walk(folder_path):
            for file in files:
                yield os.path.join(root, file)
    else:
        for item in os.listdir(folder_path):
            item_path = os.path.join(folder_path, item)
            if os.path.isfile(item_path):
                yield item_path

### END: Custom iterators and item processors


### BEGIN: Batch processing engine

# Set up logging
START_TIMESTAMP = datetime.now().strftime("%Y%m%d_%H%M%S")
LOG_FILENAME = f"batch-ops-{START_TIMESTAMP}.log"
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    handlers=[
        logging.FileHandler(LOG_FILENAME),
        logging.StreamHandler()
    ]
)

def batch_process():
    """Main batch processing function."""
    logging.info("Starting batch processing")
    try:
        for item in ITER_FUNCTION(**ITER_FUNCTION_CONFIG):
            if not ITEM_FUNCTION(item):
                logging.warning("Batch processing stopped due to ITEM_FUNCTION returning False")
                break
    except Exception as e:
        logging.error(f"Error during batch processing: {str(e)}")
    logging.info("Batch processing completed")

### END: Batch processing engine


### BEGIN: Global variables

# Set default values
ITEM_FUNCTION = display_file_information
ITER_FUNCTION = list_files
ITER_FUNCTION_CONFIG = {"recursive-sub-directories": False}

### END: Global variables


if __name__ == "__main__":
    batch_process()
