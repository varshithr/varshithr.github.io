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
    <link rel="stylesheet" href="{css_path}">
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
    <script src="{scripts_path}"></script>
    {progress_script}
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
    # Get relative path from BASE_DIR
    rel_path = file_path.relative_to(BASE_DIR)
    # Count directory levels (excluding filename)
    # For learn_concepts/docs/01-foundations/file.html -> 3 directories
    directory_parts = len(rel_path.parts) - 1

    if directory_parts == 1:  # Root level (learn_concepts/index.html)
        return {
            'home_link': '../index.html',
            'case_studies_link': '../case_studies.html',
            'about_link': '../aboutme.html',
            'css_path': 'assets/styles.css',
            'scripts_path': 'assets/scripts.js'
        }
    else:
        # Calculate how many levels up to root from the file's directory
        # For learn_concepts/docs/01-foundations/file.html:
        #   File is in: learn_concepts/docs/01-foundations/
        #   Need to go up 3 levels: ../../../ to reach root
        up_levels = directory_parts
        prefix = '../' * up_levels
        assets_prefix = '../' * (up_levels - 1) + 'assets/'
        return {
            'home_link': f'{prefix}index.html',
            'case_studies_link': f'{prefix}case_studies.html',
            'about_link': f'{prefix}aboutme.html',
            'css_path': f'{assets_prefix}styles.css',
            'scripts_path': f'{assets_prefix}scripts.js'
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
            # Special handling for README.md -> index.html
            if target_path.name == 'README':
                html_path = target_path.parent / 'index.html'
            else:
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

    # Third pass: convert README.html to index.html
    content = re.sub(r'href="([^"]*)/README\.html([^"]*)">', r'href="\1/index.html\2">', content)
    content = re.sub(r'href="README\.html([^"]*)">', r'href="index.html\1">', content)
    
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
    
    sidebar_html = f'''    <div class="sidebar-overlay" id="sidebarOverlay"></div>
    <aside class="sidebar" id="sidebar">
        <div class="sidebar-header">
            <div class="sidebar-title">Table of Contents</div>
            <button class="sidebar-close" id="sidebarClose" aria-label="Close sidebar">
                <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path>
                </svg>
            </button>
        </div>
        <div class="sidebar-content">
            <ul class="sidebar-nav">
{chr(10).join(nav_items)}
            </ul>
        </div>
    </aside>'''
    
    sidebar_toggle_html = '''    <button class="sidebar-toggle mobile" id="sidebarToggleMobile" aria-label="Toggle sidebar">
        <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16"></path>
        </svg>
    </button>
    <button class="sidebar-toggle desktop" id="sidebarToggleDesktop" aria-label="Toggle sidebar">
        <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16"></path>
        </svg>
    </button>'''
    
    return (sidebar_html, sidebar_toggle_html, ' ')


def process_progress_checkboxes(content: str) -> str:
    """Convert markdown checkboxes to HTML checkboxes with unique IDs."""
    import hashlib
    
    # Pattern to match markdown checkboxes with link: - [ ] [text](url)
    # This captures the full line including the link
    pattern = r'- \[([ x])\]\s*\[([^\]]+)\]\(([^)]+)\)'
    
    def replace_checkbox_with_link(match):
        checked = match.group(1).strip() == 'x'
        link_text = match.group(2)
        link_url = match.group(3)
        # Generate ID based on link URL (most stable identifier)
        checkbox_id = f'progress-{hashlib.md5(link_url.encode()).hexdigest()[:12]}'
        checked_attr = 'checked' if checked else ''
        # Return checkbox followed by the original link structure
        # The markdown processor will handle the link conversion
        return f'<input type="checkbox" class="progress-checkbox" id="{checkbox_id}" data-progress-item data-link-url="{link_url}" {checked_attr}> '
    
    # Pattern for checkboxes without links: - [ ] text
    pattern_no_link = r'- \[([ x])\]([^\n]+)'
    
    def replace_checkbox_no_link(match):
        checked = match.group(1).strip() == 'x'
        text = match.group(2).strip()
        # Generate ID based on text content
        checkbox_id = f'progress-{hashlib.md5(text.encode()).hexdigest()[:12]}'
        checked_attr = 'checked' if checked else ''
        return f'<input type="checkbox" class="progress-checkbox" id="{checkbox_id}" data-progress-item {checked_attr}> {text}'
    
    # First replace checkboxes with links
    content = re.sub(pattern, replace_checkbox_with_link, content)
    # Then replace remaining checkboxes without links
    content = re.sub(pattern_no_link, replace_checkbox_no_link, content)
    
    return content


def convert_markdown_to_html(md_file: Path, all_md_files: Dict[str, Path]) -> str:
    """Convert a single Markdown file to HTML."""
    with open(md_file, 'r', encoding='utf-8') as f:
        md_content = f.read()
    
    # Check if this is PROGRESS.md - process checkboxes specially
    is_progress_file = md_file.name == 'PROGRESS.md'
    
    # Extract Mermaid blocks and store them
    mermaid_pattern = r'```mermaid\n(.*?)\n```'
    mermaid_blocks = []
    
    def extract_mermaid(match):
        diagram_code = match.group(1).strip()
        placeholder = f'MERMAID_{len(mermaid_blocks)}'
        mermaid_blocks.append(diagram_code)
        return f'\n\n{placeholder}\n\n'
    
    md_content = re.sub(mermaid_pattern, extract_mermaid, md_content, flags=re.DOTALL)
    
    # Store checkbox data for PROGRESS.md to process after markdown conversion
    checkbox_data = []
    if is_progress_file:
        # Extract checkbox information before markdown conversion
        checkbox_pattern = r'- \[([ x])\]\s*\[([^\]]+)\]\(([^)]+)\)'
        for match in re.finditer(checkbox_pattern, md_content):
            checked = match.group(1).strip() == 'x'
            link_text = match.group(2)
            link_url = match.group(3)
            import hashlib
            checkbox_id = f'progress-{hashlib.md5(link_url.encode()).hexdigest()[:12]}'
            checkbox_data.append({
                'id': checkbox_id,
                'checked': checked,
                'link_url': link_url,
                'link_text': link_text
            })
    
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
    
    # Process checkboxes for PROGRESS.html after markdown conversion
    if is_progress_file and checkbox_data:
        # Replace [ ] or [x] text in list items with actual checkboxes
        checkbox_index = [0]  # Use list to allow modification in nested function
        
        def replace_in_li(match):
            if checkbox_index[0] < len(checkbox_data):
                cb_data = checkbox_data[checkbox_index[0]]
                checked_attr = 'checked' if cb_data['checked'] else ''
                checkbox_html = f'<input type="checkbox" class="progress-checkbox" id="{cb_data["id"]}" data-progress-item data-link-url="{cb_data["link_url"]}" {checked_attr}>'
                checkbox_index[0] += 1
                return f'<li>{checkbox_html} '
            return match.group(0)
        
        html_content = re.sub(r'<li>\[([ x])\]\s*', replace_in_li, html_content)
    
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
    
    # Add progress tracking script if this is PROGRESS.html
    progress_script = ''
    if is_progress_file:
        # Calculate path to progress.js relative to current file
        nav_links = get_navigation_links(md_file.with_suffix('.html'))
        progress_path = nav_links['scripts_path'].replace('scripts.js', 'progress.js')
        progress_script = f'<script src="{progress_path}"></script>'
    
    # Format final HTML
    final_html = HTML_TEMPLATE.format(
        title=title,
        content=html_content,
        sidebar=sidebar_html,
        sidebar_toggle=sidebar_toggle_html,
        main_content_class=main_content_class,
        progress_script=progress_script,
        **nav_links
    )
    
    # Insert progress script before closing body tag
    if progress_script:
        final_html = final_html.replace('</body>', progress_script + '\n</body>')
    
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

