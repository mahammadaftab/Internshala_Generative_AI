from flask import Flask, request, jsonify, render_template
import requests
import os
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# OpenRouter API configuration
OPENROUTER_API_KEY = os.getenv('OPENROUTER_API_KEY')
OPENROUTER_URL = "https://openrouter.ai/api/v1/chat/completions"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_content', methods=['POST'])
def generate_content():
    try:
        data = request.get_json()
        course_title = data.get('course_title', '').strip()

        if not course_title:
            return jsonify({'error': 'Course title is required'}), 400

        # Create the prompt for OpenAI
        prompt = f"""
        Generate educational content for a course titled: "{course_title}"

        Please provide the following structured content:

        1. Course Objective: A clear, concise statement of what students will achieve.

        2. Sample Syllabus: Outline the main topics/modules for the course (4-6 modules).

        3. Three Measurable Learning Outcomes: Write outcomes that align with Bloom's Taxonomy levels (Remember, Understand, Apply, Analyze, Evaluate, Create). Make them specific and measurable.

        4. Assessment Methods: Suggest 2-3 assessment methods that evaluate the learning outcomes.

        5. Recommended Readings: List 3-5 books, articles, or online resources relevant to the course.

        Ensure the content is educational, appropriate, and follows best practices in curriculum design.
        """

        # Call OpenRouter API using requests
        headers = {
            'Authorization': f'Bearer {OPENROUTER_API_KEY}',
            'Content-Type': 'application/json'
        }

        data = {
            'model': 'openai/gpt-3.5-turbo',
            'messages': [
                {"role": "system", "content": "You are an expert educational content creator who designs high-quality course materials."},
                {"role": "user", "content": prompt}
            ],
            'max_tokens': 1500,
            'temperature': 0.7
        }

        api_response = requests.post(OPENROUTER_URL, headers=headers, json=data)
        api_response.raise_for_status()  # Raise exception for bad status codes

        response = api_response.json()
        generated_content = response['choices'][0]['message']['content'].strip()

        return jsonify({'content': generated_content})

    except requests.exceptions.RequestException as e:
        return jsonify({'error': f'API request error: {str(e)}'}), 500
    except Exception as e:
        return jsonify({'error': f'Server error: {str(e)}'}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)