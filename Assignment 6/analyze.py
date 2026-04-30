#!/usr/bin/env python3
"""
Assignment 6: CLI Tool for AI Artistry Analysis
Command-line interface for analyzing and comparing AI image generation tools.
"""

import argparse
import json
from analyzer import AIToolAnalyzer


def main():
    parser = argparse.ArgumentParser(
        description="AI Artistry Comparison Tool - Analyze and compare AI image generation tools",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python analyze.py --ranking              # Show tool rankings
  python analyze.py --best-for professional_design
  python analyze.py --export json          # Export report as JSON
  python analyze.py --export html          # Export report as HTML
  python analyze.py --full-analysis        # Generate complete analysis
        """
    )
    
    parser.add_argument(
        '--ranking',
        action='store_true',
        help='Show overall ranking of tools'
    )
    
    parser.add_argument(
        '--best-for',
        type=str,
        help='Show best tool for a specific use case (e.g., professional_design, beginners)'
    )
    
    parser.add_argument(
        '--export',
        type=str,
        choices=['json', 'html'],
        help='Export detailed report in specified format'
    )
    
    parser.add_argument(
        '--full-analysis',
        action='store_true',
        help='Generate complete analysis report'
    )
    
    parser.add_argument(
        '--tool-info',
        type=str,
        help='Get detailed information about a specific tool (dalle, midjourney, playground, dreamstudio)'
    )
    
    args = parser.parse_args()
    analyzer = AIToolAnalyzer()
    
    if args.ranking:
        print("\n" + "="*60)
        print("AI IMAGE GENERATION TOOLS - OVERALL RANKINGS")
        print("="*60)
        rankings = analyzer.get_overall_ranking()
        for idx, rank in enumerate(rankings, 1):
            print(f"\n{idx}. {rank['tool']} - {rank['average_score']}/5.0")
            print("   Metrics:")
            for metric, score in rank['metrics'].items():
                if metric != 'name':
                    print(f"   - {metric.replace('_', ' ').title()}: {score}/5.0")
    
    elif args.best_for:
        print("\n" + "="*60)
        print(f"BEST TOOL FOR: {args.best_for.replace('_', ' ').upper()}")
        print("="*60)
        use_cases = analyzer.get_best_use_cases()
        if args.best_for in use_cases:
            print(f"\nRecommended: {use_cases[args.best_for]}")
        else:
            print(f"\nUse cases available: {', '.join(use_cases.keys())}")
    
    elif args.tool_info:
        print("\n" + "="*60)
        print(f"TOOL INFORMATION - {args.tool_info.upper()}")
        print("="*60)
        
        analysis = analyzer._generate_detailed_analysis()
        if args.tool_info in analysis:
            tool_analysis = analysis[args.tool_info]
            print(f"\nBest for: {tool_analysis['best_for']}")
            print("\nStrengths:")
            for strength in tool_analysis['strengths']:
                print(f"  ✓ {strength}")
            print("\nWeaknesses:")
            for weakness in tool_analysis['weaknesses']:
                print(f"  ✗ {weakness}")
        else:
            print(f"Tool not found. Available tools: dalle, midjourney, playground, dreamstudio")
    
    elif args.export:
        sample_generations = {
            "dalle": [],
            "midjourney": [],
            "playground": [],
            "dreamstudio": []
        }
        report = analyzer.generate_comparison_report(sample_generations)
        
        if args.export == 'json':
            filename = analyzer.export_report_json(report)
            print(f"✓ Report exported to: {filename}")
        elif args.export == 'html':
            filename = analyzer.export_report_html(report)
            print(f"✓ Report exported to: {filename}")
    
    elif args.full_analysis:
        print("\n" + "="*60)
        print("COMPLETE AI ARTISTRY ANALYSIS")
        print("="*60)
        
        # Show rankings
        print("\n1. OVERALL RANKINGS")
        print("-" * 60)
        for idx, rank in enumerate(analyzer.get_overall_ranking(), 1):
            print(f"{idx}. {rank['tool']}: {rank['average_score']}/5.0")
        
        # Show best use cases
        print("\n2. BEST TOOLS FOR DIFFERENT USE CASES")
        print("-" * 60)
        for use_case, tool in analyzer.get_best_use_cases().items():
            print(f"  • {use_case.replace('_', ' ').title()}: {tool}")
        
        # Show detailed analysis
        print("\n3. DETAILED ANALYSIS")
        print("-" * 60)
        analysis = analyzer._generate_detailed_analysis()
        for tool_key, tool_analysis in analysis.items():
            print(f"\n{tool_key.upper()}:")
            print(f"Best for: {tool_analysis['best_for']}")
            print("Strengths:")
            for s in tool_analysis['strengths'][:3]:
                print(f"  ✓ {s}")
            print("Weaknesses:")
            for w in tool_analysis['weaknesses'][:2]:
                print(f"  ✗ {w}")
        
        # Recommendation
        print("\n" + "="*60)
        print("RECOMMENDATION")
        print("="*60)
        print("""
For most users, Dall-E is recommended due to:
  • Exceptional image quality and consistency
  • Excellent prompt interpretation
  • Seamless ChatGPT integration
  • User-friendly interface
  • Good balance of all metrics

However, choose based on your specific needs:
  • Professional Design → Midjourney
  • Beginners → Playground.ai
  • Advanced Customization → DreamStudio
  • General Use → Dall-E
        """)
    
    else:
        # Show help by default
        parser.print_help()


if __name__ == '__main__':
    main()
