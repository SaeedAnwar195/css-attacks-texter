# Overview
This script demonstrates a potential concept for monitoring GitHub authentication token exchanges by injecting a JavaScript snippet into a target webpage. The injection overrides the browser's `localStorage.setItem` method to capture and send access tokens to an external server.

## Steps to run the script

### Step 1: Create a virtual environment
```bash
python3 -m venv env
```
### Step 2: Activate the virtual environment
```bash
source env/bin/activate
```

### Step 3: Install requirements
```bash
pip install -r requiremets.txt
```

### Step 4: Run the Script
```bash
python  github-token-harvest.py
```
