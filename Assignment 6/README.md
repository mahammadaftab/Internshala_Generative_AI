# Assignment 6: Exploring AI Artistry - Python Implementation

## Objective
Explore various AI image generation tools including Dall-E, Midjourney, Playground.ai, and DreamStudio. Generate different images using these tools and compare their outputs.

## Features

This Python Flask application provides:

### 1. **Web Interface**
   - Interactive tabs for different sections
   - Real-time image generation with Dall-E
   - Tool information display
   - Comparison table
   - Analysis and recommendations

### 2. **Dall-E Integration**
   - Generate images using OpenAI's Dall-E API
   - Custom prompt input
   - Image gallery with history
   - Quality and interpretation tracking

### 3. **Tools Comparison**
   - Detailed information on Dall-E, Midjourney, Playground.ai, and DreamStudio
   - Feature comparison
   - Rating system
   - Detailed analysis and recommendations

### 4. **Data Export**
   - Export comparison report as JSON
   - Track generated images and metadata
   - Store generation timestamps

## Installation

### Prerequisites
- Python 3.8+
- OpenAI API key (set as environment variable `OPENAI_API_KEY`)

### Setup Steps

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Set your OpenAI API key:**
   ```bash
   # On Windows
   set OPENAI_API_KEY=your_api_key_here
   
   # On macOS/Linux
   export OPENAI_API_KEY=your_api_key_here
   ```

3. **Run the application:**
   ```bash
   python main.py
   ```

4. **Access the web interface:**
   Open your browser and navigate to `http://localhost:8080`

## Usage

### Generate Images
1. Go to the "Dall-E" tab
2. Enter a detailed prompt describing the image you want to generate
3. Click "Generate Image"
4. Wait for the image to be generated
5. View the result and your generation history

### View Tool Information
1. Click the "Tools Info" tab
2. Browse detailed information about each AI tool
3. See features, creators, and quality ratings

### Compare Tools
1. Click the "Comparison" tab
2. View the comparison table with ratings
3. See detailed analysis for different use cases

### Export Report
Access the JSON report at: `http://localhost:8080/export_report`

## API Endpoints

- `GET /` - Main web interface
- `POST /generate_dalle` - Generate image with Dall-E
  - Body: `{prompt: "your prompt here"}`
- `GET /get_images/<tool>` - Get generated images for a tool
- `GET /get_tools_info` - Get all tools information
- `GET /export_report` - Export comparison report as JSON

## Tool Comparisons

### Dall-E
- **Creator:** OpenAI
- **Quality:** ⭐⭐⭐⭐⭐
- **Best for:** Professional use, high-quality output
- **Unique features:** ChatGPT integration, multiple sizes, editing tools

### Midjourney
- **Creator:** Midjourney Inc.
- **Quality:** ⭐⭐⭐⭐⭐
- **Best for:** Professional design, artistic outputs
- **Unique features:** Discord integration, upscaling, style control

### Playground.ai
- **Creator:** Playground Inc.
- **Quality:** ⭐⭐⭐⭐
- **Best for:** Beginners, fast generation
- **Unique features:** Web interface, multiple models, real-time preview

### DreamStudio
- **Creator:** Stability AI
- **Quality:** ⭐⭐⭐⭐
- **Best for:** Advanced customization, fine control
- **Unique features:** ControlNet, advanced parameters, edit mode

## Recommendations

- **For Most Users:** Dall-E - Best balance of quality and usability
- **For Professional Design:** Midjourney - Superior artistic output
- **For Beginners:** Playground.ai - Most user-friendly
- **For Customization:** DreamStudio - Most advanced control

## Notes

- Requires valid OpenAI API key with Dall-E access
- API calls will incur costs based on OpenAI pricing
- Generation time varies based on API load
- Images are stored in memory (not persisted to disk by default)

## File Structure

```
Assignment 6/
├── main.py           # Main Flask application
├── requirements.txt  # Python dependencies
└── README.md        # This file
```

## Error Handling

- Invalid prompts are rejected with error messages
- API errors are caught and displayed to the user
- Detailed logging available in console

## Future Enhancements

- Add database storage for images
- Implement caching system
- Add more AI tools integration
- Create detailed analytics dashboard
- Export reports as PDF/HTML
- Add image comparison features

## License

This is an educational project for the Internshala Generative AI course.
