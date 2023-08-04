import os
import shutil
import argparse
import logging
import time

def sync_folders(source_folder, replica_folder):
    shutil.rmtree(replica_folder)
    shutil.copytree(source_folder, replica_folder)

def log_file_operation(operation, file_path):
    logging.info(f"{operation} {file_path}")

def sync_folders_periodically(source_folder, replica_folder, interval, log_file):
    logging.basicConfig(filename=log_file, level=logging.INFO)
    sync_folders(source_folder, replica_folder)
    log_file_operation("Sync", source_folder)
    while True:
        time.sleep(interval)
        sync_folders(source_folder, replica_folder)
        log_file_operation("Sync", source_folder)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Sync two folders periodically")
    parser.add_argument("source_folder", help="Path to the source folder")
    parser.add_argument("replica_folder", help="Path to the replica folder")
    parser.add_argument("interval", type=int, help="Interval in seconds")
    parser.add_argument("log_file", help="Path to the log file")
    args = parser.parse_args()
    sync_folders_periodically(args.source_folder, args.replica_folder, args.interval, args.log_file)
