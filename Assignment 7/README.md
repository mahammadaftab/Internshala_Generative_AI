# Assignment 7: Interactive Dall-E Image Generator

## 📋 Table of Contents
1. [Overview](#overview)
2. [Prerequisites](#prerequisites)
3. [Installation](#installation)
4. [Configuration](#configuration)
5. [How to Run](#how-to-run)
6. [Usage Guide](#usage-guide)
7. [Code Analysis](#code-analysis)
8. [API Endpoints](#api-endpoints)
9. [Features](#features)
10. [Troubleshooting](#troubleshooting)

---

## Overview

**Assignment 7** is a Flask-based web application that enables interactive image generation using OpenAI's **Dall-E 3** model. Users can enter text descriptions and generate AI-powered images without page refresh.

### Key Improvements
- ✅ **No Page Refresh** - AJAX-based interaction
- ✅ **Real-time Image Generation** - Using Dall-E-3
- ✅ **Copy Image URL** - Easy sharing functionality
- ✅ **Bootstrap UI** - Responsive and modern design
- ✅ **Interactive JavaScript** - Smooth user experience

---

## Prerequisites

### System Requirements
- **Python**: 3.8 or higher
- **pip**: Python package manager (comes with Python)
- **Internet Connection**: Required for OpenAI API calls
- **OpenAI API Key**: Free or paid account at https://platform.openai.com

### Check Your Environment
```bash
# Check Python version
python --version

# Check pip version
pip --version
```

### Required Packages
- Flask
- boltiotai (OpenAI wrapper)
- python-dotenv (optional, for environment variables)

---

## Installation

### Step 1: Navigate to Assignment 7 Directory
```bash
cd "C:\Users\mdaft\OneDrive\Desktop\GitHub Projects\Internshala_Generative_AI\Assignment 7"
```

### Step 2: Create Virtual Environment (Recommended)
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate

# On macOS/Linux:
source venv/bin/activate
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

Or install manually:
```bash
pip install Flask==3.0.0
pip install boltiotai==0.2.3
pip install python-dotenv==1.0.0
pip install requests==2.31.0
```

### Verify Installation
```bash
pip list
```

You should see:
- Flask 3.0.0
- boltiotai 0.2.3
- python-dotenv 1.0.0
- requests 2.31.0

---

## Configuration

### Getting Your OpenAI API Key

1. **Go to OpenAI Platform**: https://platform.openai.com
2. **Sign Up/Login**: Create or log into your account
3. **Navigate to API Keys**: https://platform.openai.com/api-keys
4. **Create New Secret Key**: Click "Create new secret key"
5. **Copy the Key**: Save it safely (you won't see it again!)

### Setting the API Key

#### Option 1: Windows Command Prompt (Temporary)
```bash
set OPENAI_API_KEY=sk-your-api-key-here
```

#### Option 2: Windows PowerShell (Temporary)
```powershell
$env:OPENAI_API_KEY="sk-your-api-key-here"
```

#### Option 3: Create .env File (Persistent)
Create a file named `.env` in the Assignment 7 folder:
```
OPENAI_API_KEY=sk-your-api-key-here
```

#### Option 4: Windows Environment Variables (System-wide)
1. Press `Win + X` → Select "System"
2. Click "Advanced system settings"
3. Click "Environment Variables"
4. Click "New" under User variables
5. Variable name: `OPENAI_API_KEY`
6. Variable value: `sk-your-api-key-here`
7. Click OK and restart terminal

#### Verify API Key is Set
```bash
# Windows Command Prompt
echo %OPENAI_API_KEY%

# Windows PowerShell
$env:OPENAI_API_KEY

# macOS/Linux
echo $OPENAI_API_KEY
```

Should output your API key (without displaying it fully).

---

## How to Run

### Method 1: Direct Execution

```bash
# 1. Navigate to Assignment 7 directory
cd "C:\Users\mdaft\OneDrive\Desktop\GitHub Projects\Internshala_Generative_AI\Assignment 7"

# 2. Activate virtual environment (if using one)
venv\Scripts\activate

# 3. Set API key (if not already set)
set OPENAI_API_KEY=sk-your-key-here

# 4. Run the application
python main.py
```

### Method 2: Using PowerShell

```powershell
# Set execution policy
Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned

# Activate virtual environment
.\.venv\Scripts\Activate.ps1

# Set API key
$env:OPENAI_API_KEY="sk-your-key-here"

# Run application
python main.py
```

### Expected Output

You should see:
```
 * Serving Flask app 'main'
 * Debug mode: on
 * Running on http://0.0.0.0:8080
 * Press CTRL+C to quit
```

### Open in Browser

Open your web browser and navigate to:
```
http://localhost:8080
```

You should see:
- "Custom Image Generator" heading
- Text input field with placeholder
- "Share with the Image" button
- Output card (initially empty)

---

## Usage Guide

### Step 1: Enter Image Description
```
Example prompts:
- "A serene mountain landscape at sunset"
- "A futuristic city with neon lights"
- "A cozy library with warm lighting"
- "A dragon flying over a castle"
```

### Step 2: Click "Share with the Image" Button
- Loading state appears
- Server calls Dall-E API
- Image is generated (takes ~10-30 seconds)

### Step 3: View Generated Image
- Image appears in the Output card
- Shows 300px height by default
- Can be copied using the "Copy" button

### Step 4: Copy Image URL (Optional)
- Click "Copy" button in card header
- URL is copied to clipboard
- Use `Ctrl+V` to paste elsewhere

### Step 5: Generate Another Image
- Clear the input field
- Enter a new description
- Click button again
- No page refresh occurs

---

## Code Analysis

### File Structure
```
main.py (Single file deployment)
├── Imports
│   ├── boltiotai.openai
│   ├── os
│   └── Flask
├── API Configuration
│   └── openai.api_key setup
├── Function: generate_tutorial()
│   └── Calls Dall-E API
├── Flask App Initialization
│   └── app = Flask(__name__)
├── Routes
│   ├── GET / (Main page)
│   ├── POST / (Handle form)
│   └── POST /generate (API endpoint)
├── HTML Template (Embedded)
│   ├── Form with input
│   ├── Display area
│   └── JavaScript code
└── Main Execution
    └── app.run()
```

### Code Breakdown

#### 1. **Imports and Configuration**
```python
from boltiotai import openai  # OpenAI API wrapper
import os                      # Access environment variables
from flask import Flask, render_template_string, request

# Set API key from environment variable
openai.api_key = os.environ['OPENAI_API_KEY']
```

#### 2. **Image Generation Function**
```python
def generate_tutorial(components):
    # Make API call to Dall-E
    response = openai.Images.create(
        prompt=components,          # User's description
        model="dall-e-3",           # Model version
        size="1024x1024",           # Output size
        response_format="url"       # Return URL instead of base64
    )
    
    # Extract image URL from response
    image_url = response['data'][0]['url']
    return image_url
```

#### 3. **Flask App Initialization**
```python
app = Flask(__name__)  # Create Flask application instance
```

#### 4. **Routes/Endpoints**

**Route 1: Main Page (GET)**
```python
@app.route('/', methods=['GET', 'POST'])
def hello():
    # GET: Display form
    # POST: Process form submission
    output = ""
    
    if request.method == 'POST':
        components = request.form['components']  # Get user input
        output = generate_tutorial(components)    # Generate image
    
    # Render HTML template with output
    return render_template_string(HTML_TEMPLATE, output=output)
```

**Route 2: Generate Image (POST)**
```python
@app.route('/generate', methods=['POST'])
def generate():
    components = request.form['components']
    return generate_tutorial(components)
```

#### 5. **Main Execution**
```python
if __name__ == '__main__':
    app.run(
        host='0.0.0.0',  # Accessible from any IP
        port=8080         # Port number
    )
```

#### 6. **HTML & JavaScript (Embedded)**

**Form Submission (AJAX)**
```javascript
async function generateTutorial() {
    // Get user input
    const components = document.querySelector('#components').value;
    const output = document.querySelector('#output');
    const imgElement = document.getElementById('myImage');
    
    // Send to backend via AJAX (no page refresh)
    const response = await fetch('/generate', {
        method: 'POST',
        body: new FormData(document.querySelector('#tutorial-form'))
    });
    
    // Get image URL from response
    const imageUrl = await response.text();
    
    // Display image
    imgElement.src = imageUrl;
    output.textContent = 'Generating an image for you...';
}
```

**Copy to Clipboard**
```javascript
function copyToClipboard() {
    const imgElement = document.getElementById('myImage');
    const imageUrl = imgElement.src;
    
    // Create temporary textarea
    const textarea = document.createElement('textarea');
    textarea.value = imageUrl;
    document.body.appendChild(textarea);
    
    // Select and copy
    textarea.select();
    document.execCommand('copy');
    
    // Clean up
    document.body.removeChild(textarea);
    alert('Copied to clipboard');
}
```

---

## API Endpoints

### 1. **GET / - Display Main Page**
- **URL**: `http://localhost:8080/`
- **Method**: GET
- **Response**: HTML page with form
- **Purpose**: Serve the user interface

### 2. **POST / - Submit Form (Traditional)**
- **URL**: `http://localhost:8080/`
- **Method**: POST
- **Parameters**: `components` (text input)
- **Response**: Full page reload with image
- **Purpose**: Traditional form submission

### 3. **POST /generate - AJAX Image Generation**
- **URL**: `http://localhost:8080/generate`
- **Method**: POST
- **Parameters**: `components` (text input)
- **Response**: Image URL (plain text)
- **Purpose**: Generate image without page refresh

---

## Features

### ✨ User Interface Features
- **Bootstrap Framework** - Professional styling
- **Responsive Design** - Works on desktop and mobile
- **Form Validation** - Required field validation
- **Loading Feedback** - User knows image is being generated

### 🚀 Technical Features
- **AJAX Implementation** - No page refresh
- **In-Memory Storage** - Fast response times
- **Error Handling** - Graceful error display
- **Copy Functionality** - Share images easily
- **Form Reuse** - Generate multiple images

### 🎨 Image Generation Features
- **Dall-E 3 Model** - Latest image generation
- **1024x1024 Resolution** - High quality output
- **Text to Image** - Any description becomes image
- **URL Format** - Easy sharing and storage

---

## Troubleshooting

### ❌ Error: "API key not set"
```
Error: openai.api_key is not set
```
**Solution**:
1. Verify API key is correct
2. Check environment variable is set: `echo %OPENAI_API_KEY%`
3. Restart terminal after setting
4. Try using .env file

### ❌ Error: "Module not found"
```
ModuleNotFoundError: No module named 'flask'
```
**Solution**:
```bash
pip install -r requirements.txt
# Or manually:
pip install Flask boltiotai
```

### ❌ Error: "Port already in use"
```
OSError: [Errno 48] Address already in use
```
**Solution**:
```python
# Edit main.py and change port:
app.run(host='0.0.0.0', port=9000)  # Change 8080 to 9000
```

### ❌ Error: "Connection timeout"
```
openai.error.APIConnectionError
```
**Solution**:
- Check internet connection
- Verify API key is valid
- Check OpenAI service status
- Retry the request

### ❌ Images not displaying
- Check browser console (F12) for errors
- Verify image URL is accessible
- Check CORS settings if using proxy
- Try different image size

### ⚠️ Slow image generation
- Normal: 10-30 seconds
- API may be busy - retry after a moment
- Complex prompts take longer
- Check API quota usage

### ✅ Still having issues?

1. **Check API Key**
   ```bash
   python -c "import os; print(os.environ.get('OPENAI_API_KEY', 'NOT SET'))"
   ```

2. **Test API Connection**
   ```python
   from boltiotai import openai
   import os
   openai.api_key = os.environ['OPENAI_API_KEY']
   print(openai.Models.list())  # Should show available models
   ```

3. **Check Requirements**
   ```bash
   pip list
   # Verify Flask and boltiotai are installed
   ```

4. **Review Error Logs**
   - Terminal output when running app
   - Browser console (F12 → Console tab)
   - Check for red error messages

---

## Example Workflow

### Session Example

```
1. Start Application
   └─ python main.py
   
2. Open Browser
   └─ http://localhost:8080
   
3. Generate Image 1
   Input: "A sunset over mountains"
   └─ Image displays in 15 seconds
   
4. Copy URL
   └─ Image URL copied to clipboard
   
5. Generate Image 2
   Input: "A futuristic city"
   └─ New image displays (no page refresh!)
   
6. Share Images
   └─ Paste URLs from clipboard anywhere
```

---

## Performance Tips

| Action | Time Expected |
|--------|---------------|
| Page Load | < 2 seconds |
| Image Generation | 10-30 seconds |
| Copy URL | < 1 second |
| Form Submit | Instant (AJAX) |

---

## Advanced Configuration

### Change Port Number
```python
# In main.py, change:
app.run(host='0.0.0.0', port=8080)
# To:
app.run(host='0.0.0.0', port=5000)
```

### Change Image Size
```python
# In generate_tutorial function:
size="1024x1024"  # Options: 512x512, 1024x1024, 1792x1024
```

### Enable/Disable Debug Mode
```python
# Current (Debug ON):
app.run(host='0.0.0.0', port=8080, debug=True)

# For production (Debug OFF):
app.run(host='0.0.0.0', port=8080, debug=False)
```

---

## Security Notes

⚠️ **Important Security Tips**

1. **Never hardcode API keys** - Always use environment variables
2. **Keep API key secret** - Don't share or commit to git
3. **Use .env files** - Add `.env` to `.gitignore`
4. **Restrict API key** - Set spending limits in OpenAI dashboard
5. **Monitor usage** - Check API usage regularly to avoid surprise charges

---

## Next Steps After Running

1. **Generate a few images** - Test the functionality
2. **Modify prompts** - Try different descriptions
3. **Copy and share URLs** - Test copy functionality
4. **Check API usage** - Monitor your OpenAI account
5. **Explore enhancements** - Add database, user accounts, etc.

---

## Summary

| Item | Details |
|------|---------|
| **Purpose** | Interactive Dall-E image generation |
| **Technology** | Flask + Dall-E API + JavaScript |
| **Port** | 8080 |
| **Dependencies** | Flask, boltiotai, python-dotenv |
| **API Key** | Required (from OpenAI) |
| **Installation Time** | ~2 minutes |
| **First Run** | ~1 minute setup |
| **Image Generation** | 10-30 seconds per image |

---

## For More Help

- **Flask Documentation**: https://flask.palletsprojects.com/
- **OpenAI API Docs**: https://platform.openai.com/docs/
- **Python Guide**: https://www.python.org/
- **Assignment Docs**: See DOCUMENTATION.md

---

**Happy Image Generating! 🎨**

Created for Assignment 7 - Internshala Generative AI Course
