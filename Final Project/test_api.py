#!/usr/bin/env python3
"""
Test script for EduGenie API endpoint
"""

import requests
import json
import time

def test_api():
    """Test the generate_content API endpoint"""

    # Wait a moment for Flask to start
    time.sleep(2)

    url = 'http://localhost:5000/generate_content'
    data = {'course_title': 'Introduction to Python Programming'}

    try:
        print("Testing API endpoint...")
        response = requests.post(url, json=data, timeout=30)
        print(f"Status Code: {response.status_code}")

        if response.status_code == 200:
            result = response.json()
            print("✅ Success!")
            print("Content preview:")
            print(result['content'][:200] + "...")
        else:
            error = response.json()
            print("❌ Error:", error.get('error', 'Unknown error'))

    except requests.exceptions.RequestException as e:
        print(f"❌ Request failed: {e}")
    except Exception as e:
        print(f"❌ Unexpected error: {e}")

if __name__ == "__main__":
    test_api()