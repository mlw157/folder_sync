# folder_sync
This is a Python tool that synchronizes the contents of a source directory to a replica directory at regular intervals.

## Running with Python
First ensure that you have Python installed in your system.
### Usage
**Clone the repository:**
```bash
git clone https://github.com/mlw157/folder_sync.git
cd folder_sync
```
**Run the script:**
```bash
python app.py <source_path> <replica_path> <interval_seconds> <log_file_path>
```

## Running with Docker
### Installing
### Option 1: Build from Source
**Clone the repository:**
```bash
git clone https://github.com/mlw157/folder_sync.git
cd folder_sync
```
**Build the Docker image locally:**
```bash
docker build -t folder-synchronizer .
```
### Option 2: Pull the Docker Image from GitHub Container Registry
```bash
docker pull ghcr.io/mlw157/folder-synchronizer:1
```
```bash
docker tag docker pull ghcr.io/mlw157/folder-synchronizer:1t folder-synchronizer:1
```
### Usage
**Run the docker container**
```bash
docker run -v /path/to/source:/source -v /path/to/replica:/replica -v /path/to/log_file.log:/app/log_file.log  folder-synchronizer:1 /source /replica 5 /app/log_file.log
```
Replace /path/to/source, /path/to/replica, and /path/to/log_file.log with the actual paths on your host machine.
> **Note**: When running folder_sync with docker, the log file already needs to be created on your host machine, otherwise it will create a folder

## Running Tests
**Install pytest**
```bash
pip install pytest
```
**Run tests** <br>
Navigate to the project root directory and execute:
```bash
pytest
```
