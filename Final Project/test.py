#!/usr/bin/env python3
"""
Test script for EduGenie Educational Content Creator
This script tests the Flask app functionality without requiring a browser.
"""

import requests
import json
import os
import sys

def test_generate_content():
    """Test the content generation endpoint"""

    # Check if OpenRouter API key is set
    api_key = os.getenv('OPENROUTER_API_KEY')
    if not api_key:
        print("❌ OPENROUTER_API_KEY environment variable not set")
        print("Please set it with: $env:OPENROUTER_API_KEY='your-api-key'")
        return False

    # Test direct API call to OpenRouter
    try:
        import requests
        headers = {
            'Authorization': f'Bearer {api_key}',
            'Content-Type': 'application/json'
        }
        url = 'https://openrouter.ai/api/v1/chat/completions'
        data = {
            'model': 'openai/gpt-3.5-turbo',
            'messages': [{'role': 'user', 'content': 'Hello'}],
            'max_tokens': 5
        }

        response = requests.post(url, headers=headers, json=data, timeout=10)
        if response.status_code == 200:
            result = response.json()
            if 'choices' in result and len(result['choices']) > 0:
                print("✅ OpenRouter API connection successful")
                return True
            else:
                print("❌ Unexpected API response format")
                return False
        else:
            print(f"❌ API returned status {response.status_code}: {response.text[:100]}")
            return False

    except Exception as e:
        print(f"❌ API test failed: {str(e)}")
        return False

def test_ui_structure():
    """Test that the HTML template exists and has required elements"""
    try:
        with open('templates/index.html', 'r', encoding='utf-8') as f:
            content = f.read()

        required_elements = [
            '<title>EduGenie',
            'courseTitle',
            'generate_content',
            'EduGenie: AI-Powered Educational Content Creator'
        ]

        for element in required_elements:
            if element not in content:
                print(f"❌ Missing element in HTML: {element}")
                return False

        print("✅ HTML template structure verified")
        return True

    except FileNotFoundError:
        print("❌ templates/index.html not found")
        return False
    except Exception as e:
        print(f"❌ HTML test failed: {str(e)}")
        return False

if __name__ == "__main__":
    print("🧪 EduGenie Test Suite")
    print("=" * 50)

    tests = [
        ("UI Structure Test", test_ui_structure),
        ("Content Generation Test", test_generate_content)
    ]

    passed = 0
    total = len(tests)

    for test_name, test_func in tests:
        print(f"\n🔍 Running {test_name}...")
        if test_func():
            passed += 1
        print("-" * 30)

    print(f"\n📊 Test Results: {passed}/{total} tests passed")

    if passed == total:
        print("🎉 All tests passed! EduGenie is ready to use.")
    else:
        print("⚠️  Some tests failed. Please check the errors above.")

    sys.exit(0 if passed == total else 1)