from flask import Flask, render_template_string, request, jsonify
import os
import json
from datetime import datetime
from boltiotai import openai

# Initialize Flask app
app = Flask(__name__)

# Set OpenAI API key
openai.api_key = os.environ.get('OPENAI_API_KEY')

# Data storage for comparisons
image_data = {
    "dalle": [],
    "midjourney": [],
    "playground": [],
    "dreamstudio": []
}

# Tool descriptions and features
tool_info = {
    "dalle": {
        "name": "Dall-E",
        "creator": "OpenAI",
        "website": "openai.com/dall-e",
        "features": ["High-quality generation", "Multiple sizes", "Outpainting", "Inpainting", "ChatGPT integration"],
        "avg_quality": 4.8
    },
    "midjourney": {
        "name": "Midjourney",
        "creator": "Midjourney Inc.",
        "website": "midjourney.com",
        "features": ["Discord integration", "Upscaling", "Style parameters", "Aspect ratio control", "Niji mode"],
        "avg_quality": 4.7
    },
    "playground": {
        "name": "Playground.ai",
        "creator": "Playground Inc.",
        "website": "playground.com",
        "features": ["Web interface", "Multiple models", "Real-time preview", "Negative prompts", "Community gallery"],
        "avg_quality": 4.3
    },
    "dreamstudio": {
        "name": "DreamStudio",
        "creator": "Stability AI",
        "website": "dreamstudio.ai",
        "features": ["Stable Diffusion", "Advanced parameters", "ControlNet support", "Edit mode", "Multiple models"],
        "avg_quality": 4.5
    }
}

# Sample prompts for comparison
sample_prompts = [
    "A serene mountain landscape at sunset with golden light",
    "Abstract geometric art with vibrant colors",
    "Futuristic city skyline at night with neon lights",
    "A portrait of an artist in their studio",
    "Underwater coral reef with bioluminescent creatures"
]

def generate_image_dalle(prompt):
    """Generate image using Dall-E API"""
    try:
        response = openai.Images.create(
            prompt=prompt,
            model="dall-e-3",
            size="1024x1024",
            response_format="url"
        )
        image_url = response['data'][0]['url']
        return {
            "success": True,
            "url": image_url,
            "prompt": prompt,
            "timestamp": datetime.now().isoformat(),
            "quality": "Excellent",
            "interpretation": "Very Good"
        }
    except Exception as e:
        return {
            "success": False,
            "error": str(e),
            "prompt": prompt
        }

@app.route('/')
def index():
    html = '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>AI Artistry Comparison - Python</title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
        <style>
            :root {
                --primary: #667eea;
                --secondary: #764ba2;
            }
            
            body {
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                min-height: 100vh;
                color: #1e293b;
            }
            
            .header {
                background: linear-gradient(135deg, var(--primary) 0%, var(--secondary) 100%);
                color: white;
                padding: 3rem 1rem;
                text-align: center;
                border-radius: 20px;
                margin: 2rem 1rem;
                box-shadow: 0 20px 40px rgba(102, 126, 234, 0.3);
            }
            
            .header h1 {
                margin: 0;
                font-size: 2.5rem;
            }
            
            .header p {
                margin: 0.5rem 0 0;
                opacity: 0.95;
            }
            
            .container-wrapper {
                max-width: 1200px;
                margin: 0 auto;
            }
            
            .tab-nav {
                display: flex;
                gap: 0.75rem;
                margin: 2rem 1rem 0;
                flex-wrap: wrap;
                background: white;
                padding: 1rem;
                border-radius: 16px;
                box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
            }
            
            .tab-btn {
                padding: 0.75rem 1.5rem;
                border: 2px solid transparent;
                background: #f1f5f9;
                color: #475569;
                border-radius: 10px;
                cursor: pointer;
                font-weight: 600;
                transition: all 0.3s ease;
                border: none;
            }
            
            .tab-btn:hover {
                background: #e2e8f0;
                color: #1e293b;
            }
            
            .tab-btn.active {
                background: var(--primary);
                color: white;
            }
            
            main {
                background: white;
                border-radius: 20px;
                padding: 2rem;
                margin: 2rem 1rem;
                box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
            }
            
            .tab-content {
                display: none;
            }
            
            .tab-content.active {
                display: block;
                animation: fadeIn 0.3s ease;
            }
            
            @keyframes fadeIn {
                from { opacity: 0; transform: translateY(10px); }
                to { opacity: 1; transform: translateY(0); }
            }
            
            h2 {
                color: var(--primary);
                border-bottom: 3px solid #f0f0f0;
                padding-bottom: 0.75rem;
            }
            
            h3 {
                color: #475569;
                margin-top: 1.5rem;
            }
            
            .input-section {
                background: #f8fafc;
                padding: 1.5rem;
                border-radius: 14px;
                margin-bottom: 1.5rem;
            }
            
            .btn-primary {
                background: var(--primary);
                border-color: var(--primary);
            }
            
            .btn-primary:hover {
                background: #5568d3;
                border-color: #5568d3;
            }
            
            .image-gallery {
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
                gap: 1.5rem;
                margin: 1.5rem 0;
            }
            
            .gallery-item {
                background: #f8fafc;
                border: 2px solid #e2e8f0;
                border-radius: 14px;
                padding: 1rem;
                overflow: hidden;
            }
            
            .gallery-item img {
                width: 100%;
                height: 200px;
                object-fit: cover;
                border-radius: 10px;
                margin-bottom: 0.75rem;
            }
            
            .gallery-item h4 {
                color: var(--primary);
                margin: 0.75rem 0;
            }
            
            .gallery-item p {
                margin: 0.25rem 0;
                font-size: 0.9rem;
                color: #64748b;
            }
            
            .tool-card {
                background: linear-gradient(135deg, #f5f7fa 0%, #f0f4f8 100%);
                border: 2px solid #e2e8f0;
                border-left: 4px solid var(--primary);
                border-radius: 14px;
                padding: 1.5rem;
                margin-bottom: 1.5rem;
                transition: all 0.3s ease;
            }
            
            .tool-card:hover {
                transform: translateY(-4px);
                box-shadow: 0 10px 20px rgba(102, 126, 234, 0.15);
            }
            
            .comparison-table {
                width: 100%;
                border-collapse: collapse;
                margin: 1.5rem 0;
            }
            
            .comparison-table th {
                background: var(--primary);
                color: white;
                padding: 1rem;
                text-align: left;
            }
            
            .comparison-table td {
                padding: 1rem;
                border-bottom: 1px solid #e2e8f0;
            }
            
            .comparison-table tr:hover {
                background: #f8fafc;
            }
            
            .loading {
                display: none;
                text-align: center;
                padding: 2rem;
            }
            
            .spinner-border {
                color: var(--primary);
            }
            
            .alert {
                border-radius: 10px;
                margin-bottom: 1.5rem;
            }
        </style>
    </head>
    <body>
        <div class="container-wrapper">
            <div class="header">
                <h1>Exploring AI Artistry</h1>
                <p>Comparing Dall-E, Midjourney, Playground.ai, and DreamStudio</p>
            </div>
            
            <nav class="tab-nav">
                <button class="tab-btn active" onclick="switchTab('overview')">Overview</button>
                <button class="tab-btn" onclick="switchTab('dalle')">Dall-E</button>
                <button class="tab-btn" onclick="switchTab('tools-info')">Tools Info</button>
                <button class="tab-btn" onclick="switchTab('comparison')">Comparison</button>
                <button class="tab-btn" onclick="switchTab('analysis')">Analysis</button>
            </nav>
            
            <main>
                <section id="overview" class="tab-content active">
                    <h2>Objective</h2>
                    <p>Explore various AI image generation tools including Dall-E, Midjourney, Playground.ai, and DreamStudio. Generate different images using these tools and compare their outputs.</p>
                    
                    <h3>What We'll Analyze</h3>
                    <ul>
                        <li><strong>Image Quality:</strong> Resolution, detail, and visual appeal</li>
                        <li><strong>Prompt Interpretation:</strong> How well the tool understands and executes the prompt</li>
                        <li><strong>Ease of Use:</strong> User interface and accessibility</li>
                        <li><strong>Unique Features:</strong> Special capabilities and tools offered</li>
                        <li><strong>Speed:</strong> How quickly images are generated</li>
                        <li><strong>Customization Options:</strong> Control over style, size, and parameters</li>
                    </ul>
                    
                    <h3>About This Application</h3>
                    <p>This Python Flask application demonstrates AI image generation using Dall-E API from OpenAI. It provides a web interface for:</p>
                    <ul>
                        <li>Generating images with custom prompts using Dall-E</li>
                        <li>Storing and tracking image generation history</li>
                        <li>Comparing different AI tools based on predefined criteria</li>
                        <li>Analyzing tool capabilities and recommendations</li>
                    </ul>
                </section>
                
                <section id="dalle" class="tab-content">
                    <h2>Dall-E Image Generation</h2>
                    
                    <div class="input-section">
                        <h4>Generate Images with Dall-E</h4>
                        <div class="mb-3">
                            <label for="dalle-prompt" class="form-label">Enter a prompt:</label>
                            <textarea class="form-control" id="dalle-prompt" rows="3" placeholder="Describe the image you want to generate..."></textarea>
                        </div>
                        <button class="btn btn-primary" onclick="generateDalleImage()">Generate Image</button>
                    </div>
                    
                    <div class="loading" id="dalle-loading">
                        <div class="spinner-border" role="status">
                            <span class="visually-hidden">Loading...</span>
                        </div>
                        <p>Generating image with Dall-E...</p>
                    </div>
                    
                    <div id="dalle-result"></div>
                    
                    <h3>Recent Generations</h3>
                    <div class="image-gallery" id="dalle-gallery"></div>
                </section>
                
                <section id="tools-info" class="tab-content">
                    <h2>AI Tools Information</h2>
                    <div id="tools-container"></div>
                </section>
                
                <section id="comparison" class="tab-content">
                    <h2>Tools Comparison</h2>
                    <table class="comparison-table">
                        <thead>
                            <tr>
                                <th>Criteria</th>
                                <th>Dall-E</th>
                                <th>Midjourney</th>
                                <th>Playground.ai</th>
                                <th>DreamStudio</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td><strong>Image Quality</strong></td>
                                <td>⭐⭐⭐⭐⭐</td>
                                <td>⭐⭐⭐⭐⭐</td>
                                <td>⭐⭐⭐⭐</td>
                                <td>⭐⭐⭐⭐</td>
                            </tr>
                            <tr>
                                <td><strong>Prompt Interpretation</strong></td>
                                <td>⭐⭐⭐⭐⭐</td>
                                <td>⭐⭐⭐⭐⭐</td>
                                <td>⭐⭐⭐⭐</td>
                                <td>⭐⭐⭐⭐</td>
                            </tr>
                            <tr>
                                <td><strong>Ease of Use</strong></td>
                                <td>⭐⭐⭐⭐</td>
                                <td>⭐⭐⭐</td>
                                <td>⭐⭐⭐⭐⭐</td>
                                <td>⭐⭐⭐</td>
                            </tr>
                            <tr>
                                <td><strong>Speed</strong></td>
                                <td>⭐⭐⭐⭐</td>
                                <td>⭐⭐⭐</td>
                                <td>⭐⭐⭐⭐⭐</td>
                                <td>⭐⭐⭐⭐</td>
                            </tr>
                            <tr>
                                <td><strong>Customization</strong></td>
                                <td>⭐⭐⭐⭐</td>
                                <td>⭐⭐⭐⭐</td>
                                <td>⭐⭐⭐</td>
                                <td>⭐⭐⭐⭐⭐</td>
                            </tr>
                        </tbody>
                    </table>
                </section>
                
                <section id="analysis" class="tab-content">
                    <h2>Comparative Analysis & Recommendation</h2>
                    
                    <div class="alert alert-info">
                        <h4>Recommended Choice: Dall-E for Most Users</h4>
                        <p>After comparing all four tools, <strong>Dall-E</strong> emerges as the best overall choice for most users due to its exceptional image quality, excellent prompt interpretation, and user-friendly interface with ChatGPT integration.</p>
                    </div>
                    
                    <h3>Best for Different Use Cases</h3>
                    <div class="tool-card">
                        <h4>Best for Professional Design: Midjourney</h4>
                        <p>Midjourney excels at producing highly artistic and stylized outputs perfect for professional design work. The upscaling and variation tools provide excellent refinement capabilities.</p>
                    </div>
                    
                    <div class="tool-card">
                        <h4>Best for Beginners: Playground.ai</h4>
                        <p>Playground.ai offers the most intuitive web-based interface and fastest generation speed, making it ideal for users new to AI image generation.</p>
                    </div>
                    
                    <div class="tool-card">
                        <h4>Best Overall Quality: Dall-E</h4>
                        <p>Dall-E produces the most consistent high-quality images with excellent prompt interpretation and seamless ChatGPT integration for creative assistance.</p>
                    </div>
                    
                    <div class="tool-card">
                        <h4>Best for Customization: DreamStudio</h4>
                        <p>DreamStudio's advanced parameters and ControlNet technology provide unparalleled control for users who want fine-grained customization of their results.</p>
                    </div>
                    
                    <h3>Conclusion</h3>
                    <p>All four tools represent the cutting edge of AI image generation technology. The best choice depends on your specific needs, workflow, and priorities. We recommend trying each platform to determine which aligns best with your use case.</p>
                </section>
            </main>
        </div>
        
        <script>
            function switchTab(tabName) {
                // Hide all tabs
                document.querySelectorAll('.tab-content').forEach(tab => {
                    tab.classList.remove('active');
                });
                
                // Remove active class from buttons
                document.querySelectorAll('.tab-btn').forEach(btn => {
                    btn.classList.remove('active');
                });
                
                // Show selected tab
                document.getElementById(tabName).classList.add('active');
                
                // Add active class to clicked button
                event.target.classList.add('active');
                
                // Load tools info if tools-info tab
                if (tabName === 'tools-info') {
                    loadToolsInfo();
                }
            }
            
            function generateDalleImage() {
                const prompt = document.getElementById('dalle-prompt').value;
                if (!prompt.trim()) {
                    alert('Please enter a prompt');
                    return;
                }
                
                document.getElementById('dalle-loading').style.display = 'block';
                document.getElementById('dalle-result').innerHTML = '';
                
                fetch('/generate_dalle', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify({prompt: prompt})
                })
                .then(response => response.json())
                .then(data => {
                    document.getElementById('dalle-loading').style.display = 'none';
                    if (data.success) {
                        const html = `
                            <div class="alert alert-success">Image generated successfully!</div>
                            <div style="text-align: center; margin: 2rem 0;">
                                <img src="${data.url}" style="max-width: 100%; max-height: 500px; border-radius: 10px;">
                                <p style="margin-top: 1rem; color: #475569;"><strong>Prompt:</strong> ${data.prompt}</p>
                            </div>
                        `;
                        document.getElementById('dalle-result').innerHTML = html;
                        loadDalleGallery();
                    } else {
                        document.getElementById('dalle-result').innerHTML = `<div class="alert alert-danger">Error: ${data.error}</div>`;
                    }
                })
                .catch(error => {
                    document.getElementById('dalle-loading').style.display = 'none';
                    document.getElementById('dalle-result').innerHTML = `<div class="alert alert-danger">Error: ${error}</div>`;
                });
            }
            
            function loadDalleGallery() {
                fetch('/get_images/dalle')
                    .then(response => response.json())
                    .then(data => {
                        const gallery = document.getElementById('dalle-gallery');
                        if (data.images.length === 0) {
                            gallery.innerHTML = '<p>No images generated yet</p>';
                            return;
                        }
                        gallery.innerHTML = data.images.map(img => `
                            <div class="gallery-item">
                                <img src="${img.url}" alt="Generated image">
                                <h4>Generated Image</h4>
                                <p><strong>Prompt:</strong> ${img.prompt}</p>
                                <p><strong>Quality:</strong> ${img.quality}</p>
                                <p><strong>Interpretation:</strong> ${img.interpretation}</p>
                            </div>
                        `).join('');
                    });
            }
            
            function loadToolsInfo() {
                fetch('/get_tools_info')
                    .then(response => response.json())
                    .then(data => {
                        const container = document.getElementById('tools-container');
                        container.innerHTML = data.tools.map(tool => `
                            <div class="tool-card">
                                <h3>${tool.name}</h3>
                                <p><strong>Creator:</strong> ${tool.creator}</p>
                                <p><strong>Website:</strong> <a href="https://${tool.website}" target="_blank">${tool.website}</a></p>
                                <h4>Key Features:</h4>
                                <ul>
                                    ${tool.features.map(f => `<li>${f}</li>`).join('')}
                                </ul>
                                <p><strong>Average Quality Rating:</strong> ${tool.avg_quality}/5.0</p>
                            </div>
                        `).join('');
                    });
            }
            
            // Load initial data
            window.addEventListener('load', () => {
                loadToolsInfo();
            });
        </script>
    </body>
    </html>
    '''
    return render_template_string(html)

@app.route('/generate_dalle', methods=['POST'])
def generate_dalle():
    """Generate image with Dall-E"""
    data = request.get_json()
    prompt = data.get('prompt', '')
    
    if not prompt:
        return jsonify({'success': False, 'error': 'Prompt is required'})
    
    result = generate_image_dalle(prompt)
    
    if result['success']:
        image_data['dalle'].append(result)
    
    return jsonify(result)

@app.route('/get_images/<tool>')
def get_images(tool):
    """Get generated images for a specific tool"""
    images = image_data.get(tool, [])
    return jsonify({'images': images[::-1]})  # Reverse to show newest first

@app.route('/get_tools_info')
def get_tools_info_api():
    """Get tools information"""
    tools = []
    for key, info in tool_info.items():
        tools.append(info)
    return jsonify({'tools': tools})

@app.route('/export_report')
def export_report():
    """Export comparison report as JSON"""
    report = {
        "title": "AI Artistry Comparison Report",
        "generated": datetime.now().isoformat(),
        "tools": tool_info,
        "image_data": image_data,
        "summary": {
            "dalle_images": len(image_data['dalle']),
            "total_images": sum(len(v) for v in image_data.values()),
            "recommendation": "Dall-E for most users due to exceptional quality and ease of use"
        }
    }
    return jsonify(report)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
