#!/usr/bin/env python3
"""
Build script to convert Markdown files in learn_concepts/ to HTML pages.
Preserves Mermaid diagrams, converts internal links, and applies site styling.
"""

import os
import re
import html
import markdown
from pathlib import Path
from typing import Dict, Tuple, List
from html.parser import HTMLParser

# Base directory for the project
BASE_DIR = Path(__file__).parent
LEARN_CONCEPTS_DIR = BASE_DIR / "learn_concepts"
DOCS_DIR = LEARN_CONCEPTS_DIR / "docs"

# HTML template based on site's existing design
HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="en" class="scroll-smooth">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;900&display=swap" rel="stylesheet">
    <script src="https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.min.js"></script>
    <style>
        body {{
            font-family: 'Inter', sans-serif;
            background-color: #F0F4F8;
            color: #1E293B;
        }}
        .gradient-text {{
            background: linear-gradient(90deg, #58508d, #bc5090);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }}
        .content {{
            background-color: white;
            border-radius: 0.75rem;
            padding: 2rem;
            box-shadow: 0 10px 15px -3px rgb(0 0 0 / 0.05), 0 4px 6px -4px rgb(0 0 0 / 0.05);
            margin-top: 2rem;
        }}
        .content h1 {{
            font-size: 2.5rem;
            font-weight: 900;
            margin-bottom: 1rem;
            color: #1E293B;
        }}
        .content h2 {{
            font-size: 2rem;
            font-weight: 700;
            margin-top: 2rem;
            margin-bottom: 1rem;
            color: #1E293B;
            border-bottom: 2px solid #E5E7EB;
            padding-bottom: 0.5rem;
        }}
        .content h3 {{
            font-size: 1.5rem;
            font-weight: 600;
            margin-top: 1.5rem;
            margin-bottom: 0.75rem;
            color: #1E293B;
        }}
        .content h4 {{
            font-size: 1.25rem;
            font-weight: 600;
            margin-top: 1rem;
            margin-bottom: 0.5rem;
            color: #1E293B;
        }}
        .content p {{
            margin-bottom: 1rem;
            line-height: 1.7;
        }}
        .content ul, .content ol {{
            margin-bottom: 1rem;
            padding-left: 2rem;
        }}
        .content li {{
            margin-bottom: 0.5rem;
            line-height: 1.6;
        }}
        .content code {{
            background-color: #F3F4F6;
            padding: 0.2rem 0.4rem;
            border-radius: 0.25rem;
            font-family: 'Courier New', monospace;
            font-size: 0.9em;
        }}
        .content pre {{
            background-color: #1E293B;
            color: #F0F4F8;
            padding: 1rem;
            border-radius: 0.5rem;
            overflow-x: auto;
            margin-bottom: 1rem;
        }}
        .content pre code {{
            background-color: transparent;
            padding: 0;
            color: inherit;
        }}
        .content blockquote {{
            border-left: 4px solid #58508d;
            padding-left: 1rem;
            margin-left: 0;
            margin-bottom: 1rem;
            color: #4B5563;
            font-style: italic;
        }}
        .content table {{
            width: 100%;
            border-collapse: collapse;
            margin-bottom: 1rem;
        }}
        .content th {{
            background-color: #F3F4F6;
            padding: 0.75rem;
            text-align: left;
            font-weight: 600;
            border: 1px solid #E5E7EB;
        }}
        .content td {{
            padding: 0.75rem;
            border: 1px solid #E5E7EB;
        }}
        .content tr:nth-child(even) {{
            background-color: #F9FAFB;
        }}
        .content a {{
            color: #58508d;
            text-decoration: underline;
        }}
        .content a:hover {{
            color: #bc5090;
        }}
        .content hr {{
            border: none;
            border-top: 2px solid #E5E7EB;
            margin: 2rem 0;
        }}
        .mermaid {{
            margin: 2rem 0;
            text-align: center;
            background-color: white;
            padding: 1rem;
            border-radius: 0.5rem;
        }}
        .sidebar {{
            position: fixed;
            top: 80px;
            left: 0;
            height: calc(100vh - 80px);
            width: 280px;
            background-color: white;
            border-right: 1px solid #E5E7EB;
            overflow-y: auto;
            transition: transform 0.3s ease;
            z-index: 40;
            box-shadow: 2px 0 4px rgba(0, 0, 0, 0.05);
        }}
        .sidebar.collapsed {{
            transform: translateX(-100%);
        }}
        .sidebar-toggle {{
            position: fixed;
            top: 90px;
            left: 20px;
            z-index: 50;
            background-color: white;
            border: 1px solid #E5E7EB;
            border-radius: 0.5rem;
            padding: 0.5rem;
            cursor: pointer;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
            display: none;
        }}
        .sidebar-toggle:hover {{
            background-color: #F3F4F6;
        }}
        .sidebar-content {{
            padding: 1.5rem;
        }}
        .sidebar-title {{
            font-size: 1.125rem;
            font-weight: 700;
            color: #1E293B;
            margin-bottom: 1rem;
            padding-bottom: 0.5rem;
            border-bottom: 2px solid #E5E7EB;
        }}
        .sidebar-nav {{
            list-style: none;
            padding: 0;
            margin: 0;
        }}
        .sidebar-nav li {{
            margin-bottom: 0.5rem;
        }}
        .sidebar-nav a {{
            display: block;
            padding: 0.5rem 0.75rem;
            color: #4B5563;
            text-decoration: none;
            border-radius: 0.375rem;
            transition: all 0.2s;
            font-size: 0.875rem;
        }}
        .sidebar-nav a:hover {{
            background-color: #F3F4F6;
            color: #58508d;
        }}
        .sidebar-nav a.active {{
            background-color: #EEF2FF;
            color: #58508d;
            font-weight: 600;
        }}
        .sidebar-nav .level-1 {{
            padding-left: 0.75rem;
            font-weight: 600;
            color: #1E293B;
        }}
        .sidebar-nav .level-2 {{
            padding-left: 1.5rem;
            color: #4B5563;
        }}
        .sidebar-nav .level-3 {{
            padding-left: 2.25rem;
            color: #6B7280;
            font-size: 0.8125rem;
        }}
        .sidebar-nav .level-4 {{
            padding-left: 3rem;
            color: #9CA3AF;
            font-size: 0.75rem;
        }}
        .main-content {{
            margin-left: 280px;
            transition: margin-left 0.3s ease;
        }}
        .main-content.no-sidebar {{
            margin-left: 0;
        }}
        @media (max-width: 1024px) {{
            .sidebar {{
                transform: translateX(-100%);
            }}
            .sidebar.expanded {{
                transform: translateX(0);
            }}
            .sidebar-toggle {{
                display: block;
            }}
            .main-content {{
                margin-left: 0;
            }}
        }}
    </style>
</head>
<body class="antialiased">
    <header class="bg-white sticky top-0 z-50 shadow-md">
        <nav class="container mx-auto px-4 sm:px-6 py-4 flex justify-between items-center">
            <div class="text-xl sm:text-2xl font-bold text-gray-800">
                <a href="{home_link}" class="flex items-center">
                    <svg class="w-6 h-6 mr-2" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg"><path d="M10.707 2.293a1 1 0 00-1.414 0l-7 7a1 1 0 001.414 1.414L4 10.414V17a1 1 0 001 1h2a1 1 0 001-1v-2a1 1 0 011-1h2a1 1 0 011 1v2a1 1 0 001 1h2a1 1 0 001-1v-6.586l.293.293a1 1 0 001.414-1.414l-7-7z"></path></svg>
                    <span class="gradient-text">Data Engineering Concepts</span>
                </a>
            </div>
            <ul class="flex space-x-4 sm:space-x-6 text-gray-600 font-medium text-sm sm:text-base">
                <li><a href="{case_studies_link}" class="hover:text-[#bc5090] font-semibold">Case Studies</a></li>
                <li><a href="{about_link}" class="hover:text-[#bc5090] font-semibold">About Me</a></li>
            </ul>
        </nav>
    </header>
    {sidebar_toggle}
    {sidebar}
    <main class="main-content{main_content_class}container mx-auto px-4 sm:px-6 lg:px-8 py-12">
        <div class="content">
{content}
        </div>
    </main>
    <footer class="bg-gray-800 text-white text-center p-6 mt-16">
        <p>&copy; 2025 Data Engineering Guides. An illustrative web application.</p>
    </footer>
    <script>
        mermaid.initialize({{ startOnLoad: true, theme: 'default' }});
        
        // Sidebar toggle functionality
        document.addEventListener('DOMContentLoaded', function() {{
            const sidebar = document.getElementById('sidebar');
            const sidebarToggle = document.getElementById('sidebarToggle');
            const mainContent = document.querySelector('.main-content');
            
            // Toggle sidebar
            if (sidebarToggle) {{
                sidebarToggle.addEventListener('click', function() {{
                    sidebar.classList.toggle('expanded');
                }});
            }}
            
            // Close sidebar when clicking outside on mobile
            document.addEventListener('click', function(event) {{
                if (window.innerWidth <= 1024) {{
                    if (!sidebar.contains(event.target) && !sidebarToggle.contains(event.target)) {{
                        sidebar.classList.remove('expanded');
                    }}
                }}
            }});
            
            // Update active link on scroll
            const headings = document.querySelectorAll('.content h1, .content h2, .content h3, .content h4');
            const sidebarLinks = document.querySelectorAll('.sidebar-nav a');
            
            function updateActiveLink() {{
                let current = '';
                headings.forEach(heading => {{
                    const rect = heading.getBoundingClientRect();
                    if (rect.top <= 100) {{
                        current = heading.id;
                    }}
                }});
                
                sidebarLinks.forEach(link => {{
                    link.classList.remove('active');
                    if (link.getAttribute('href') === '#' + current) {{
                        link.classList.add('active');
                    }}
                }});
            }}
            
            window.addEventListener('scroll', updateActiveLink);
            updateActiveLink();
            
            // Smooth scroll for sidebar links
            sidebarLinks.forEach(link => {{
                link.addEventListener('click', function(e) {{
                    const href = this.getAttribute('href');
                    if (href.startsWith('#')) {{
                        e.preventDefault();
                        const target = document.querySelector(href);
                        if (target) {{
                            const headerOffset = 80;
                            const elementPosition = target.getBoundingClientRect().top;
                            const offsetPosition = elementPosition + window.pageYOffset - headerOffset;
                            
                            window.scrollTo({{
                                top: offsetPosition,
                                behavior: 'smooth'
                            }});
                            
                            // Close sidebar on mobile after click
                            if (window.innerWidth <= 1024) {{
                                sidebar.classList.remove('expanded');
                            }}
                        }}
                    }}
                }});
            }});
        }});
    </script>
</body>
</html>
"""


def calculate_relative_path(from_path: Path, to_path: Path) -> str:
    """Calculate relative path from one file to another."""
    try:
        rel_path = os.path.relpath(to_path, from_path.parent)
        # Normalize path separators for web
        return rel_path.replace('\\', '/')
    except ValueError:
        # Fallback if paths are on different drives (Windows)
        return str(to_path).replace('\\', '/')


def get_navigation_links(file_path: Path) -> Dict[str, str]:
    """Calculate navigation links based on file depth."""
    depth = len(file_path.relative_to(BASE_DIR).parts) - 1
    
    if depth == 1:  # Root level (learn_concepts/index.html)
        return {
            'home_link': 'index.html',
            'case_studies_link': 'case_studies.html',
            'about_link': 'aboutme.html'
        }
    else:
        # Calculate how many levels up to root
        up_levels = depth - 1
        prefix = '../' * up_levels
        return {
            'home_link': f'{prefix}index.html',
            'case_studies_link': f'{prefix}case_studies.html',
            'about_link': f'{prefix}aboutme.html'
        }


def convert_markdown_links(content: str, current_file: Path, all_md_files: Dict[str, Path]) -> str:
    """Convert Markdown links to HTML links."""
    # Pattern to match markdown links: [text](path.md) or [text](../path.md)
    pattern = r'\[([^\]]+)\]\(([^)]+\.md)(?:#[^)]+)?\)'
    
    def replace_link(match):
        link_text = match.group(1)
        link_path = match.group(2)
        
        # Handle anchor links (preserve them)
        anchor_match = re.search(r'#([^)]+)$', match.group(0))
        anchor = f'#{anchor_match.group(1)}' if anchor_match else ''
        
        # Resolve relative path
        if link_path.startswith('http://') or link_path.startswith('https://'):
            # External link, keep as is
            return match.group(0)
        
        # Resolve relative path from current file
        if link_path.startswith('/'):
            # Absolute path from root
            target_path = BASE_DIR / link_path.lstrip('/')
        else:
            # Relative path
            target_path = (current_file.parent / link_path).resolve()
        
        # Check if target exists in our markdown files
        target_md = target_path.with_suffix('.md')
        if target_md.exists() and target_md in all_md_files.values():
            # Convert to HTML link
            html_path = target_path.with_suffix('.html')
            rel_path = calculate_relative_path(current_file, html_path)
            return f'[{link_text}]({rel_path}{anchor})'
        else:
            # Keep original link (might be external or not yet converted)
            return match.group(0)
    
    # First pass: convert .md links
    content = re.sub(pattern, replace_link, content)
    
    # Second pass: convert any remaining .md references in the HTML output
    # This handles links that were already processed by markdown but need .md -> .html
    content = re.sub(r'href="([^"]+\.md)(#[^"]+)?">', r'href="\1.html\2">', content)
    content = re.sub(r'href="([^"]+\.md)">', r'href="\1.html">', content)
    
    return content


class HeadingExtractor(HTMLParser):
    """Extract headings from HTML content."""
    def __init__(self):
        super().__init__()
        self.headings = []
        self.current_tag = None
        self.current_text = []
        self.current_id = None
    
    def handle_starttag(self, tag, attrs):
        if tag in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']:
            self.current_tag = tag
            self.current_text = []
            # Extract id attribute
            self.current_id = None
            for attr, value in attrs:
                if attr == 'id':
                    self.current_id = value
                    break
    
    def handle_endtag(self, tag):
        if tag == self.current_tag:
            text = ' '.join(self.current_text).strip()
            if text and self.current_id:
                level = int(tag[1])  # Extract number from h1, h2, etc.
                self.headings.append({
                    'level': level,
                    'text': text,
                    'id': self.current_id
                })
            self.current_tag = None
            self.current_text = []
    
    def handle_data(self, data):
        if self.current_tag:
            self.current_text.append(data)


def generate_sidebar_nav(html_content: str) -> Tuple[str, str, str]:
    """Generate sidebar navigation from headings in HTML content.
    Returns: (sidebar_html, sidebar_toggle_html, main_content_class)
    """
    parser = HeadingExtractor()
    parser.feed(html_content)
    headings = parser.headings
    
    if not headings:
        return ('', '', 'no-sidebar')
    
    nav_items = []
    for heading in headings:
        level = heading['level']
        text = html.escape(heading['text'])
        heading_id = heading['id']
        level_class = f'level-{level}'
        nav_items.append(f'                <li><a href="#{heading_id}" class="{level_class}">{text}</a></li>')
    
    sidebar_html = f'''    <aside class="sidebar" id="sidebar">
        <div class="sidebar-content">
            <div class="sidebar-title">Table of Contents</div>
            <ul class="sidebar-nav">
{chr(10).join(nav_items)}
            </ul>
        </div>
    </aside>'''
    
    sidebar_toggle_html = '''    <button class="sidebar-toggle" id="sidebarToggle" aria-label="Toggle sidebar">
        <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16"></path>
        </svg>
    </button>'''
    
    return (sidebar_html, sidebar_toggle_html, ' ')


def convert_markdown_to_html(md_file: Path, all_md_files: Dict[str, Path]) -> str:
    """Convert a single Markdown file to HTML."""
    with open(md_file, 'r', encoding='utf-8') as f:
        md_content = f.read()
    
    # Extract Mermaid blocks and store them
    mermaid_pattern = r'```mermaid\n(.*?)\n```'
    mermaid_blocks = []
    
    def extract_mermaid(match):
        diagram_code = match.group(1).strip()
        placeholder = f'MERMAID_{len(mermaid_blocks)}'
        mermaid_blocks.append(diagram_code)
        return f'\n\n{placeholder}\n\n'
    
    md_content = re.sub(mermaid_pattern, extract_mermaid, md_content, flags=re.DOTALL)
    
    # Convert markdown links
    md_content = convert_markdown_links(md_content, md_file, all_md_files)
    
    # Configure markdown extensions
    md_extensions = [
        'markdown.extensions.extra',
        'markdown.extensions.codehilite',
        'markdown.extensions.tables',
        'markdown.extensions.toc',
        'markdown.extensions.fenced_code'
    ]
    
    # Convert markdown to HTML
    html_content = markdown.markdown(
        md_content, 
        extensions=md_extensions,
        extension_configs={
            'markdown.extensions.codehilite': {'use_pygments': False}
        }
    )
    
    # Replace Mermaid placeholders with actual divs
    for i, diagram_code in enumerate(mermaid_blocks):
        placeholder = f'MERMAID_{i}'
        # Handle various ways markdown might have wrapped it
        # Try most specific patterns first
        html_content = re.sub(
            f'<p><strong>{re.escape(placeholder)}</strong></p>',
            f'<div class="mermaid">\n{diagram_code}\n</div>',
            html_content
        )
        html_content = re.sub(
            f'<p>{re.escape(placeholder)}</p>',
            f'<div class="mermaid">\n{diagram_code}\n</div>',
            html_content
        )
        html_content = re.sub(
            f'<strong>{re.escape(placeholder)}</strong>',
            f'<div class="mermaid">\n{diagram_code}\n</div>',
            html_content
        )
        # Final fallback - direct replacement
        html_content = html_content.replace(placeholder, f'<div class="mermaid">\n{diagram_code}\n</div>')
    
    # Also handle any Mermaid blocks that markdown converted to code blocks
    html_content = re.sub(
        r'<pre><code class="language-mermaid">(.*?)</code></pre>',
        lambda m: f'<div class="mermaid">\n{html.unescape(m.group(1).strip())}\n</div>',
        html_content,
        flags=re.DOTALL
    )
    
    # Fix any HTML entities and clean up Mermaid diagrams
    def fix_mermaid_content(match):
        content = match.group(1)
        # Unescape HTML entities
        content = html.unescape(content)
        # Remove any leading dashes and clean up whitespace
        lines = []
        for line in content.split('\n'):
            stripped = line.strip()
            # Skip empty lines and lines that are just dashes
            if stripped and not (stripped.startswith('-') and len(stripped) == 1):
                # Remove leading dash if present (markdown list item)
                if stripped.startswith('-'):
                    stripped = stripped[1:].strip()
                lines.append(stripped)
        return f'<div class="mermaid">\n' + '\n'.join(lines) + '\n</div>'
    
    html_content = re.sub(
        r'<div class="mermaid">(.*?)</div>',
        fix_mermaid_content,
        html_content,
        flags=re.DOTALL
    )
    
    # Get title from first h1 or filename
    title_match = re.search(r'<h1>(.*?)</h1>', html_content)
    if title_match:
        title = title_match.group(1).strip()
        # Remove HTML tags from title
        title = re.sub(r'<[^>]+>', '', title)
    else:
        title = md_file.stem.replace('-', ' ').title()
    
    # Generate sidebar navigation
    sidebar_html, sidebar_toggle_html, main_content_class = generate_sidebar_nav(html_content)
    
    # Get navigation links
    nav_links = get_navigation_links(md_file.with_suffix('.html'))
    
    # Format final HTML
    final_html = HTML_TEMPLATE.format(
        title=title,
        content=html_content,
        sidebar=sidebar_html,
        sidebar_toggle=sidebar_toggle_html,
        main_content_class=main_content_class,
        **nav_links
    )
    
    return final_html


def find_all_markdown_files() -> Dict[str, Path]:
    """Find all markdown files in learn_concepts directory."""
    md_files = {}
    for md_file in LEARN_CONCEPTS_DIR.rglob('*.md'):
        # Use relative path as key
        rel_path = md_file.relative_to(BASE_DIR)
        md_files[str(rel_path)] = md_file
    return md_files


def build_all_html_files():
    """Build all HTML files from Markdown files."""
    print("Finding all Markdown files...")
    all_md_files = find_all_markdown_files()
    print(f"Found {len(all_md_files)} Markdown files")
    
    # Create index.html for learn_concepts root if README.md exists
    readme_path = LEARN_CONCEPTS_DIR / "README.md"
    if readme_path.exists():
        print(f"Building index.html from {readme_path}")
        html_content = convert_markdown_to_html(readme_path, all_md_files)
        index_path = LEARN_CONCEPTS_DIR / "index.html"
        with open(index_path, 'w', encoding='utf-8') as f:
            f.write(html_content)
        print(f"  Created: {index_path}")
    
    # Process docs directory
    if DOCS_DIR.exists():
        # Create index.html for docs if INDEX.md exists
        index_md = DOCS_DIR / "INDEX.md"
        if index_md.exists():
            print(f"Building docs/index.html from {index_md}")
            html_content = convert_markdown_to_html(index_md, all_md_files)
            index_html = DOCS_DIR / "index.html"
            with open(index_html, 'w', encoding='utf-8') as f:
                f.write(html_content)
            print(f"  Created: {index_html}")
        
        # Process all other markdown files
        for md_file in DOCS_DIR.rglob('*.md'):
            if md_file.name == 'README.md':
                # Convert README.md to index.html in its directory
                html_content = convert_markdown_to_html(md_file, all_md_files)
                index_html = md_file.parent / "index.html"
                with open(index_html, 'w', encoding='utf-8') as f:
                    f.write(html_content)
                print(f"  Created: {index_html}")
            elif md_file.name != 'INDEX.md':
                # Convert other .md files to .html
                html_content = convert_markdown_to_html(md_file, all_md_files)
                html_file = md_file.with_suffix('.html')
                with open(html_file, 'w', encoding='utf-8') as f:
                    f.write(html_content)
                print(f"  Created: {html_file}")
    
    print("\nBuild complete!")


if __name__ == '__main__':
    build_all_html_files()

