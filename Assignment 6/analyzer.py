"""
Assignment 6: AI Artistry Comparison Analysis Module
This module provides utilities for analyzing and comparing AI image generation tools.
"""

import json
from datetime import datetime
from typing import Dict, List, Any


class AIToolAnalyzer:
    """Analyzer for comparing AI image generation tools"""
    
    def __init__(self):
        self.tools_data = {
            "dalle": {
                "name": "Dall-E",
                "image_quality": 4.8,
                "prompt_interpretation": 4.9,
                "ease_of_use": 4.2,
                "speed": 4.0,
                "customization": 4.0,
                "cost_value": 3.5
            },
            "midjourney": {
                "name": "Midjourney",
                "image_quality": 4.9,
                "prompt_interpretation": 4.8,
                "ease_of_use": 3.2,
                "speed": 3.0,
                "customization": 4.5,
                "cost_value": 3.5
            },
            "playground": {
                "name": "Playground.ai",
                "image_quality": 4.1,
                "prompt_interpretation": 4.0,
                "ease_of_use": 4.8,
                "speed": 4.9,
                "customization": 3.5,
                "cost_value": 4.3
            },
            "dreamstudio": {
                "name": "DreamStudio",
                "image_quality": 4.4,
                "prompt_interpretation": 4.2,
                "ease_of_use": 3.5,
                "speed": 3.8,
                "customization": 4.9,
                "cost_value": 4.0
            }
        }
    
    def get_best_tool(self, criteria: str) -> str:
        """Get the best tool for a specific criteria"""
        best_tool = None
        best_score = 0
        
        for tool_key, metrics in self.tools_data.items():
            score = metrics.get(criteria, 0)
            if score > best_score:
                best_score = score
                best_tool = tool_key
        
        return best_tool
    
    def get_overall_ranking(self) -> List[Dict[str, Any]]:
        """Get overall ranking of tools by average score"""
        rankings = []
        
        for tool_key, metrics in self.tools_data.items():
            # Calculate average score
            scores = [v for k, v in metrics.items() if k != "name"]
            avg_score = sum(scores) / len(scores)
            
            rankings.append({
                "tool": metrics["name"],
                "key": tool_key,
                "average_score": round(avg_score, 2),
                "metrics": metrics
            })
        
        # Sort by average score
        rankings.sort(key=lambda x: x["average_score"], reverse=True)
        return rankings
    
    def get_best_use_cases(self) -> Dict[str, str]:
        """Get best tool for different use cases"""
        return {
            "professional_design": self.tools_data[self.get_best_tool("customization")]["name"],
            "beginners": self.tools_data[self.get_best_tool("ease_of_use")]["name"],
            "overall_quality": self.tools_data[self.get_best_tool("image_quality")]["name"],
            "speed": self.tools_data[self.get_best_tool("speed")]["name"],
            "cost_value": self.tools_data[self.get_best_tool("cost_value")]["name"],
            "prompt_understanding": self.tools_data[self.get_best_tool("prompt_interpretation")]["name"]
        }
    
    def generate_comparison_report(self, image_generations: Dict[str, List[Dict]]) -> Dict[str, Any]:
        """Generate a detailed comparison report"""
        report = {
            "timestamp": datetime.now().isoformat(),
            "title": "AI Image Generation Tools - Comprehensive Comparison",
            "executive_summary": {
                "recommendation": "Dall-E is recommended for most users due to excellent balance of quality, ease of use, and integration with ChatGPT.",
                "rankings": self.get_overall_ranking(),
                "best_use_cases": self.get_best_use_cases()
            },
            "detailed_analysis": self._generate_detailed_analysis(),
            "image_generation_stats": self._generate_stats(image_generations)
        }
        return report
    
    def _generate_detailed_analysis(self) -> Dict[str, str]:
        """Generate detailed analysis for each tool"""
        analysis = {
            "dalle": {
                "strengths": [
                    "Exceptional image quality and consistency",
                    "Excellent prompt interpretation",
                    "Seamless ChatGPT integration",
                    "Multiple editing tools (outpainting, inpainting)",
                    "Multiple size options"
                ],
                "weaknesses": [
                    "Higher subscription cost",
                    "Can struggle with specific character consistency",
                    "Limited free tier"
                ],
                "best_for": "Professional users seeking high-quality, consistent results with AI assistance"
            },
            "midjourney": {
                "strengths": [
                    "Highly artistic and stylized outputs",
                    "Excellent for design professionals",
                    "Strong community and support",
                    "Superior upscaling and refinement",
                    "Great style parameter control"
                ],
                "weaknesses": [
                    "Discord-based interface unintuitive for beginners",
                    "Slower generation speed",
                    "Requires subscription for consistent use",
                    "Steeper learning curve"
                ],
                "best_for": "Professional designers and artists seeking highly polished, artistic outputs"
            },
            "playground": {
                "strengths": [
                    "Most intuitive web interface",
                    "Fastest generation speed",
                    "Multiple AI models available",
                    "Perfect for beginners",
                    "Good community features"
                ],
                "weaknesses": [
                    "Variable output quality depending on model",
                    "Limited advanced customization",
                    "Free tier has usage restrictions",
                    "Less artistic consistency than competitors"
                ],
                "best_for": "Beginners and casual users wanting quick, easy image generation"
            },
            "dreamstudio": {
                "strengths": [
                    "Highly customizable parameters",
                    "ControlNet for precision control",
                    "Good balance of speed and quality",
                    "Open-source foundation",
                    "Advanced editing capabilities"
                ],
                "weaknesses": [
                    "Steep learning curve for advanced features",
                    "Requires parameter tweaking for optimal results",
                    "Less artistic consistency than Midjourney",
                    "Technical approach may intimidate beginners"
                ],
                "best_for": "Advanced users wanting fine-grained control and customization"
            }
        }
        return analysis
    
    def _generate_stats(self, image_generations: Dict[str, List[Dict]]) -> Dict[str, Any]:
        """Generate statistics about image generations"""
        stats = {
            "total_images_generated": sum(len(v) for v in image_generations.values()),
            "breakdown_by_tool": {
                tool: len(images) for tool, images in image_generations.items()
            }
        }
        return stats
    
    def export_report_json(self, report: Dict, filename: str = "ai_comparison_report.json"):
        """Export report as JSON file"""
        with open(filename, 'w') as f:
            json.dump(report, f, indent=2)
        return filename
    
    def export_report_html(self, report: Dict, filename: str = "ai_comparison_report.html") -> str:
        """Export report as HTML"""
        html = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <title>{report['title']}</title>
            <style>
                body {{ font-family: Arial, sans-serif; margin: 20px; }}
                h1 {{ color: #667eea; }}
                h2 {{ color: #764ba2; }}
                table {{ border-collapse: collapse; width: 100%; margin: 20px 0; }}
                th, td {{ border: 1px solid #ddd; padding: 10px; text-align: left; }}
                th {{ background-color: #667eea; color: white; }}
                .tool-section {{ background: #f8f9fa; padding: 15px; margin: 15px 0; border-radius: 5px; }}
                .strength {{ color: green; }}
                .weakness {{ color: red; }}
                ul {{ margin: 10px 0; }}
            </style>
        </head>
        <body>
            <h1>{report['title']}</h1>
            <p>Generated: {report['timestamp']}</p>
            
            <h2>Executive Summary</h2>
            <p>{report['executive_summary']['recommendation']}</p>
            
            <h2>Overall Rankings</h2>
            <table>
                <tr>
                    <th>Rank</th>
                    <th>Tool</th>
                    <th>Average Score</th>
                </tr>
        """
        
        for idx, ranking in enumerate(report['executive_summary']['rankings'], 1):
            html += f"""
                <tr>
                    <td>{idx}</td>
                    <td>{ranking['tool']}</td>
                    <td>{ranking['average_score']}/5.0</td>
                </tr>
            """
        
        html += """
            </table>
            
            <h2>Best Use Cases</h2>
            <ul>
        """
        
        for use_case, tool in report['executive_summary']['best_use_cases'].items():
            html += f"<li><strong>{use_case.replace('_', ' ').title()}:</strong> {tool}</li>"
        
        html += """
            </ul>
            
            <h2>Detailed Analysis</h2>
        """
        
        for tool_key, analysis in report['detailed_analysis'].items():
            html += f"""
            <div class="tool-section">
                <h3>{tool_key.upper()}</h3>
                <h4>Strengths:</h4>
                <ul>
            """
            for strength in analysis['strengths']:
                html += f"<li class='strength'>{strength}</li>"
            html += """
                </ul>
                <h4>Weaknesses:</h4>
                <ul>
            """
            for weakness in analysis['weaknesses']:
                html += f"<li class='weakness'>{weakness}</li>"
            html += f"""
                </ul>
                <p><strong>Best for:</strong> {analysis['best_for']}</p>
            </div>
            """
        
        html += """
        </body>
        </html>
        """
        
        with open(filename, 'w') as f:
            f.write(html)
        return filename


# Example usage
if __name__ == "__main__":
    analyzer = AIToolAnalyzer()
    
    # Get overall ranking
    print("Overall Rankings:")
    for rank in analyzer.get_overall_ranking():
        print(f"{rank['tool']}: {rank['average_score']}/5.0")
    
    # Get best use cases
    print("\nBest Tools for Different Use Cases:")
    for use_case, tool in analyzer.get_best_use_cases().items():
        print(f"{use_case}: {tool}")
    
    # Generate and export report
    sample_generations = {
        "dalle": [{"prompt": "A sunset", "quality": "Excellent"}],
        "midjourney": [],
        "playground": [],
        "dreamstudio": []
    }
    
    report = analyzer.generate_comparison_report(sample_generations)
    print("\nReport generated successfully!")
