"""
Centralized path management system for the website.
Handles all URL and file path calculations.
"""

import os
from pathlib import Path
from typing import Dict, List


class PathManager:
    """Manages all paths and URLs for the website."""

    def __init__(self, base_dir: Path = None):
        self.base_dir = base_dir or Path(__file__).parent.parent
        self.site_root = self.base_dir

    def get_relative_path(self, from_path: Path, to_path: Path) -> str:
        """Calculate relative path from one file to another."""
        try:
            rel_path = os.path.relpath(to_path, from_path.parent)
            # Normalize path separators for web
            return rel_path.replace('\\', '/')
        except ValueError:
            # Fallback if paths are on different drives (Windows)
            return str(to_path).replace('\\', '/')

    def get_navigation_paths(self, current_file: Path) -> Dict[str, str]:
        """Get navigation paths relative to current file."""
        rel_path = current_file.relative_to(self.site_root)
        directory_parts = len(rel_path.parts) - 1

        # Calculate prefix to get back to root
        prefix = '../' * directory_parts

        return {
            'home_link': f'{prefix}index.html',
            'aws_link': f'{prefix}aws/',
            'gcp_link': f'{prefix}gcp/',
            'azure_link': f'{prefix}azure/',
            'databricks_link': f'{prefix}databricks/',
            'sql_link': f'{prefix}sql/',
            'case_studies_link': f'{prefix}case_studies.html',
            'learn_concepts_link': f'{prefix}learn_concepts/',
            'about_link': f'{prefix}aboutme.html',
            'css_path': f'{prefix}assets/styles.css',
            'js_path': f'{prefix}assets/scripts.js'
        }

    def get_asset_paths(self, current_file: Path) -> Dict[str, str]:
        """Get asset paths relative to current file."""
        nav_paths = self.get_navigation_paths(current_file)
        return {
            'css_path': nav_paths['css_path'],
            'js_path': nav_paths['js_path']
        }

    def get_section_info(self, current_file: Path) -> Dict[str, str]:
        """Get section-specific information based on file location."""
        rel_path = current_file.relative_to(self.site_root)

        # Determine which section we're in
        path_parts = rel_path.parts
        if len(path_parts) > 0:
            section = path_parts[0]
            if section == 'aws':
                return {
                    'brand_text': 'AWS',
                    'brand_gradient': 'gradient-aws',
                    'section_color': '#FF9900'
                }
            elif section == 'gcp':
                return {
                    'brand_text': 'GCP',
                    'brand_gradient': 'gradient-gcp',
                    'section_color': '#4285F4'
                }
            elif section == 'azure':
                return {
                    'brand_text': 'Azure',
                    'brand_gradient': 'gradient-azure',
                    'section_color': '#0078D4'
                }
            elif section == 'databricks':
                return {
                    'brand_text': 'Databricks',
                    'brand_gradient': 'gradient-databricks',
                    'section_color': '#FF3621'
                }
            elif section == 'sql':
                return {
                    'brand_text': 'SQL',
                    'brand_gradient': 'gradient-sql',
                    'section_color': '#336791'
                }
            elif section == 'learn_concepts':
                return {
                    'brand_text': 'Learn',
                    'brand_gradient': 'gradient-learn',
                    'section_color': '#10B981'
                }

        # Default (root level)
        return {
            'brand_text': 'Home',
            'brand_gradient': 'gradient-text',
            'section_color': '#58508d'
        }

    def get_breadcrumb(self, current_file: Path) -> List[Dict[str, str]]:
        """Generate breadcrumb navigation."""
        rel_path = current_file.relative_to(self.site_root)
        path_parts = rel_path.parts

        breadcrumbs = [{
            'text': 'Home',
            'url': self.get_navigation_paths(current_file)['home_link']
        }]

        current_path = self.site_root
        for i, part in enumerate(path_parts[:-1]):  # Exclude the filename
            current_path = current_path / part
            if part in ['aws', 'gcp', 'azure', 'databricks', 'sql', 'learn_concepts']:
                # This is a section
                section_info = self.get_section_info(current_path / 'index.html')
                breadcrumbs.append({
                    'text': section_info['brand_text'],
                    'url': f"{'../' * (len(path_parts) - i - 1)}{part}/"
                })

        return breadcrumbs

    def get_canonical_url(self, current_file: Path) -> str:
        """Get canonical URL for the current page."""
        rel_path = current_file.relative_to(self.site_root)

        # Convert markdown files to HTML paths
        if rel_path.suffix == '.md':
            if rel_path.name == 'index.md':
                url_path = str(rel_path.parent)
                if url_path == '.':
                    return '/'
                return f'/{url_path}/'
            else:
                # Convert .md to .html
                html_path = rel_path.with_suffix('.html')
                return f'/{html_path}'
        elif rel_path.suffix == '.html':
            # For HTML files
            if rel_path.name == 'index.html':
                url_path = str(rel_path.parent)
                if url_path == '.':
                    return '/'
                return f'/{url_path}/'
            else:
                return f'/{rel_path}'

        # Fallback
        return f'/{rel_path}'