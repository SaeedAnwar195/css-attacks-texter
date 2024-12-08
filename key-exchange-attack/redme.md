# Overview
This script, key-exchange-intercepter.py, demonstrates a simulated key exchange interception attack. It generates a malicious RSA key pair, encodes the public key in Base64, and sends it to a target endpoint to replace legitimate keys during a key exchange process. This is intended for educational and research purposes only and should not be used maliciously or without permission.

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
python  key-exchange-intercepter.py
```
