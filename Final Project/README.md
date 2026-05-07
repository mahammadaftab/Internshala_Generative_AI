# EduGenie: AI-Powered Educational Content Creator

## Overview

EduGenie is a web-based AI tool that dynamically generates comprehensive educational content based on user-provided course titles. Using OpenRouter's AI models, it creates structured course materials including objectives, syllabi, learning outcomes aligned with Bloom's Taxonomy, assessment methods, and recommended readings.

## Features

- **Simple Web Interface**: Clean, responsive UI built with Bootstrap
- **AI-Powered Content Generation**: Leverages OpenRouter's API for high-quality educational content
- **Bloom's Taxonomy Alignment**: Learning outcomes follow cognitive levels (Remember, Understand, Apply, Analyze, Evaluate, Create)
- **Structured Output**: Organized content sections for easy curriculum planning
- **Error Handling**: Robust error handling for API failures and user input validation
- **Data Privacy**: No user data storage; all processing happens in real-time

## Technology Stack

- **Backend**: Python Flask
- **Frontend**: HTML5, CSS3, JavaScript (ES6+)
- **AI API**: OpenRouter (compatible with OpenAI API)
- **Styling**: Bootstrap 5
- **Icons**: Font Awesome

## Quick Start

1. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Set your OpenRouter API key**:
   ```bash
   # On Windows PowerShell
   $env:OPENROUTER_API_KEY = "your-openrouter-api-key-here"

   # On Linux/macOS
   export OPENROUTER_API_KEY="your-openrouter-api-key-here"
   ```

3. **Run the application**:
   ```bash
   python app.py
   ```

4. **Open your browser** and go to `http://localhost:5000`

5. **Test the application**:
   ```bash
   python test.py
   ```

## API Endpoint

### POST /generate_content

Generates educational content based on a course title.

**Request Body:**
```json
{
  "course_title": "Introduction to Data Science"
}
```

**Response:**
```json
{
  "content": "Generated educational content here..."
}
```

**Error Response:**
```json
{
  "error": "Error message"
}
```

## Content Structure

The generated content includes:

1. **Course Objective**: Clear statement of learning goals
2. **Sample Syllabus**: 4-6 main topics/modules
3. **Learning Outcomes**: 3 measurable outcomes aligned with Bloom's Taxonomy
4. **Assessment Methods**: 2-3 evaluation strategies
5. **Recommended Readings**: 3-5 relevant resources

## Bloom's Taxonomy Alignment

Learning outcomes are designed to cover different cognitive levels:
- **Remember**: Recall facts and basic concepts
- **Understand**: Explain ideas and concepts
- **Apply**: Use information in new situations
- **Analyze**: Draw connections among ideas
- **Evaluate**: Justify a stand or decision
- **Create**: Produce new or original work

## Testing

### Unit Testing

Run the Flask application and test the following scenarios:

1. **Valid Input**: Enter "Python Programming" and verify structured output
2. **Empty Input**: Submit empty form and check error handling
3. **API Error**: Test with invalid API key to verify error messages
4. **Network Issues**: Simulate network problems

### Manual Testing Checklist

- [ ] UI loads correctly on different browsers
- [ ] Form validation works for empty inputs
- [ ] Loading indicator appears during API calls
- [ ] Generated content displays properly
- [ ] Error messages are user-friendly
- [ ] Content aligns with Bloom's Taxonomy
- [ ] Responsive design on mobile devices

### Sample Test Cases

1. **Course Title**: "Web Development Fundamentals"
   - Verify syllabus includes HTML, CSS, JavaScript
   - Check learning outcomes cover practical skills

2. **Course Title**: "Environmental Science"
   - Ensure content covers ecological concepts
   - Validate assessment methods are appropriate

## Security Considerations

- API keys are stored as environment variables
- No user data is persisted on the server
- CORS is enabled for cross-origin requests
- Input validation prevents malicious payloads

## Deployment

For production deployment:

1. Set `debug=False` in `app.py`
2. Use a production WSGI server (e.g., Gunicorn)
3. Configure proper environment variables
4. Set up HTTPS
5. Implement rate limiting for API calls

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests for new functionality
5. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- OpenAI for providing the GPT API
- Bootstrap for the UI framework
- Flask for the web framework