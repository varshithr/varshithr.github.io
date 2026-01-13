#!/usr/bin/env python3
"""
Modern build system for Data Engineering Guides website.
Uses Jinja2 templating, proper error handling, and centralized configuration.
"""

import os
import sys
import json
import shutil
import logging
import re
from pathlib import Path
from typing import Dict, List, Optional, Any
from datetime import datetime

import markdown
import yaml
from jinja2 import Environment, FileSystemLoader, TemplateNotFound

from path_manager import PathManager
from config import config


class BuildConfig:
    """Configuration for the build system."""
    def __init__(self, verbose=False, clean=True):
        self.project_root = config.project_root
        self.source_dir = config.source_dir
        self.output_dir = config.output_dir
        self.templates_dir = config.templates_dir
        self.assets_dir = config.assets_dir
        self.verbose = verbose
        self.clean = clean


class BuildError(Exception):
    """Custom exception for build errors."""
    pass


class BuildSystem:
    """Main build system class."""

    def __init__(self, config: BuildConfig):
        self.config = config
        self.path_manager = PathManager(config.project_root)
        self.setup_logging()
        self.setup_jinja()

    def setup_logging(self):
        """Set up logging configuration."""
        # Ensure output directory exists
        self.config.output_dir.mkdir(parents=True, exist_ok=True)

        level = logging.DEBUG if self.config.verbose else logging.INFO
        logging.basicConfig(
            level=level,
            format='%(asctime)s - %(levelname)s - %(message)s',
            handlers=[
                logging.StreamHandler(),
                logging.FileHandler(self.config.output_dir / 'build.log', mode='w')
            ]
        )
        self.logger = logging.getLogger(__name__)

    def setup_jinja(self):
        """Set up Jinja2 environment."""
        self.jinja_env = Environment(
            loader=FileSystemLoader(self.config.templates_dir),
            trim_blocks=True,
            lstrip_blocks=True,
            autoescape=True
        )

        # Add custom filters
        self.jinja_env.filters['basename'] = lambda x: Path(x).name
        self.jinja_env.filters['dirname'] = lambda x: str(Path(x).parent)

    def load_page_config(self, page_path: Path) -> Dict[str, Any]:
        """Load configuration for a specific page."""
        # If it's already a YAML file, load it directly
        if page_path.suffix == '.yaml':
            try:
                with open(page_path, 'r', encoding='utf-8') as f:
                    config = yaml.safe_load(f) or {}
                    # Remove content from config as it's handled separately
                    config.pop('content', None)
                    return config
            except Exception as e:
                self.logger.warning(f"Failed to load config for {page_path}: {e}")
                return {}

        # Look for a separate YAML config file
        config_file = page_path.with_suffix('.yaml')
        if config_file.exists():
            try:
                with open(config_file, 'r', encoding='utf-8') as f:
                    return yaml.safe_load(f) or {}
            except Exception as e:
                self.logger.warning(f"Failed to load config for {page_path}: {e}")
                return {}

        # Default config
        return {
            'title': page_path.stem.replace('-', ' ').title(),
            'description': 'Data engineering concepts and guides',
            'keywords': ['data engineering', 'cloud', 'distributed systems']
        }

    def render_template(self, template_name: str, context: Dict[str, Any]) -> str:
        """Render a Jinja2 template with context."""
        try:
            template = self.jinja_env.get_template(template_name)
            return template.render(**context)
        except TemplateNotFound:
            raise BuildError(f"Template '{template_name}' not found")
        except Exception as e:
            raise BuildError(f"Template rendering failed: {e}")

    def process_markdown_file(self, md_file: Path) -> str:
        """Convert markdown file to HTML."""
        try:
            with open(md_file, 'r', encoding='utf-8') as f:
                md_content = f.read()

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

            return html_content

        except Exception as e:
            raise BuildError(f"Failed to process markdown file {md_file}: {e}")

    def process_yaml_file(self, yaml_file: Path) -> str:
        """Process YAML file with content."""
        try:
            with open(yaml_file, 'r', encoding='utf-8') as f:
                yaml_content = yaml.safe_load(f)

            # Extract content from YAML
            content = yaml_content.get('content', '')

            # Clean up content - remove common leading whitespace from YAML block scalar
            if content:
                lines = content.split('\n')
                # Find the minimum indentation of non-empty lines
                non_empty_lines = [line for line in lines if line.strip()]
                if non_empty_lines:
                    min_indent = min(len(line) - len(line.lstrip()) for line in non_empty_lines if line.strip())
                    # Remove the common indentation
                    cleaned_lines = []
                    for line in lines:
                        if line.strip():  # Non-empty line
                            cleaned_lines.append(line[min_indent:] if len(line) > min_indent else line.lstrip())
                        else:  # Empty line
                            cleaned_lines.append('')
                    content = '\n'.join(cleaned_lines)

            # Process content as markdown if it contains markdown-like syntax
            if content and ('#' in content or '*' in content or '[' in content):
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
                    content,
                    extensions=md_extensions,
                    extension_configs={
                        'markdown.extensions.codehilite': {'use_pygments': False}
                    }
                )
                return html_content
            else:
                # Return content as-is (assuming it's already HTML)
                return content

        except Exception as e:
            raise BuildError(f"Failed to process YAML file {yaml_file}: {e}")

    def build_page(self, source_file: Path, template: str = 'base.html') -> str:
        """Build a single page."""
        try:
            # Load page configuration
            page_config = self.load_page_config(source_file)

            # Determine output path for path calculations
            if source_file.name in ['index.yaml', 'index.md'] and 'pages' in source_file.parts:
                # Root index files should be treated as root index.html for path calculations
                temp_output_file = self.config.project_root / 'index.html'
            else:
                # Normal path calculation for relative URLs
                rel_path = source_file.relative_to(self.config.source_dir)
                if source_file.suffix in ['.md', '.yaml']:
                    temp_output_file = self.config.project_root / rel_path.with_suffix('.html')
                else:
                    temp_output_file = self.config.project_root / rel_path

            # Get path information
            nav_paths = self.path_manager.get_navigation_paths(temp_output_file)
            section_info = self.path_manager.get_section_info(temp_output_file)

            # Handle breadcrumbs - for root index, no breadcrumbs
            try:
                breadcrumbs = self.path_manager.get_breadcrumb(temp_output_file)
            except ValueError:
                # If breadcrumb calculation fails (e.g., for root paths), use empty list
                breadcrumbs = []

            canonical_url = self.path_manager.get_canonical_url(temp_output_file)

            # Process content based on file type
            if source_file.suffix == '.md':
                content_html = self.process_markdown_file(source_file)
            elif source_file.suffix == '.yaml':
                content_html = self.process_yaml_file(source_file)
            elif source_file.suffix == '.html':
                # For existing HTML files, we might need to extract content
                # For now, just read as-is
                with open(source_file, 'r', encoding='utf-8') as f:
                    content_html = f.read()
            else:
                raise BuildError(f"Unsupported file type: {source_file.suffix}")

            # Build context
            context = {
                **page_config,
                **nav_paths,
                **section_info,
                'content': content_html,
                'breadcrumbs': breadcrumbs,
                'canonical_url': canonical_url,
                'build_time': datetime.now().isoformat(),
                'source_file': str(source_file.relative_to(self.config.source_dir))
            }

            # Render template
            return self.render_template(template, context)

        except Exception as e:
            raise BuildError(f"Failed to build page {source_file}: {e}")

    def copy_assets(self):
        """Copy static assets and HTML files to output directory."""
        try:
            # Copy assets
            if self.config.assets_dir.exists():
                target_dir = self.config.output_dir / 'assets'
                # Don't copy if source and target are the same
                if target_dir != self.config.assets_dir:
                    if target_dir.exists():
                        shutil.rmtree(target_dir)
                    shutil.copytree(self.config.assets_dir, target_dir)
                    self.logger.info(f"Copied assets to {target_dir}")
                else:
                    self.logger.debug(f"Assets directory is already in target location: {target_dir}")

            # Copy HTML files directly
            for html_file in self.config.source_dir.rglob('*.html'):
                # Skip files in templates, components, src, and venv directories
                # Also skip pages/index.html since it's handled by YAML build
                if not any(part in ['templates', 'components', 'src', 'venv']
                          for part in html_file.parts) and not (html_file.name == 'index.html' and 'pages' in html_file.parts):
                    # Calculate relative path and create output path
                    rel_path = html_file.relative_to(self.config.source_dir)

                    # Special handling for root pages (pages/ directory)
                    if str(rel_path).startswith('pages/'):
                        # Remove the pages/ prefix for root output
                        rel_path = rel_path.relative_to('pages')

                    output_file = self.config.output_dir / rel_path

                    # Create output directory
                    output_file.parent.mkdir(parents=True, exist_ok=True)

                    # Copy the file
                    shutil.copy2(html_file, output_file)

                    # Post-process HTML files to update headers/footers for consistency
                    if output_file != self.config.output_dir / 'index.html':  # Don't modify the template-generated index.html
                        self.post_process_html_file(output_file)

                    self.logger.debug(f"Copied HTML file: {rel_path}")

            # Special handling: copy learn_concepts directory as a whole and post-process its HTML files
            learn_concepts_src = self.config.source_dir / 'learn_concepts'
            learn_concepts_dst = self.config.output_dir / 'learn_concepts'
            if learn_concepts_src.exists():
                # Remove existing directory if it exists
                if learn_concepts_dst.exists():
                    shutil.rmtree(learn_concepts_dst)
                # Copy the entire directory
                shutil.copytree(learn_concepts_src, learn_concepts_dst)
                self.logger.info(f"Copied learn_concepts directory to {learn_concepts_dst}")

                # Post-process all HTML files in the copied learn_concepts directory
                for html_file in learn_concepts_dst.rglob('*.html'):
                    self.post_process_html_file(html_file)

        except Exception as e:
            raise BuildError(f"Failed to copy assets: {e}")

    def post_process_html_file(self, html_file: Path):
        """Post-process HTML files to update headers/footers for consistency."""
        try:
            with open(html_file, 'r', encoding='utf-8') as f:
                content = f.read()

            # Generate new header and footer with context
            rel_path = html_file.relative_to(self.config.output_dir)
            path_parts = str(rel_path).split('/')

            # Determine section for branding
            section = None
            if len(path_parts) > 0 and path_parts[0] in ['aws', 'gcp', 'azure', 'databricks', 'sql', 'learn_concepts']:
                section = path_parts[0]

            # Set up context for template rendering
            depth = len(path_parts) - 1
            prefix = '../' * depth if depth > 0 else './'

            # Build navigation links - current section links to itself
            context = {
                'home_link': prefix,
                'aws_link': './' if section == 'aws' else prefix + 'aws/',
                'gcp_link': './' if section == 'gcp' else prefix + 'gcp/',
                'azure_link': './' if section == 'azure' else prefix + 'azure/',
                'databricks_link': './' if section == 'databricks' else prefix + 'databricks/',
                'sql_link': './' if section == 'sql' else prefix + 'sql/',
                'case_studies_link': prefix + 'case_studies.html',
                'learn_concepts_link': prefix + 'learn_concepts/',
                'about_link': prefix + 'aboutme.html',
                'section': section,  # Add section for conditional sidebar toggle
            }

            # Set section-specific branding
            if section == 'aws':
                context.update({
                    'brand_text': 'AWS',
                    'brand_gradient': 'gradient-aws'
                })
            elif section == 'gcp':
                context.update({
                    'brand_text': 'GCP',
                    'brand_gradient': 'gradient-gcp'
                })
            elif section == 'azure':
                context.update({
                    'brand_text': 'Azure',
                    'brand_gradient': 'gradient-azure'
                })
            elif section == 'databricks':
                context.update({
                    'brand_text': 'Databricks',
                    'brand_gradient': 'gradient-databricks'
                })
            elif section == 'sql':
                context.update({
                    'brand_text': 'SQL',
                    'brand_gradient': 'gradient-sql'
                })
            elif section == 'learn_concepts':
                context.update({
                    'brand_text': 'Learn',
                    'brand_gradient': 'gradient-learn'
                })
            else:
                context.update({
                    'brand_text': 'Home',
                    'brand_gradient': 'gradient-text'
                })

            # Render new header and footer
            new_header = self.render_template('components/header.html', context)
            new_footer = self.render_template('components/footer.html', context)

            # Replace old header and footer
            # Look for header pattern (from <header> to </header>)
            header_pattern = r'<header[^>]*>.*?</header>'
            content = re.sub(header_pattern, new_header, content, flags=re.DOTALL | re.IGNORECASE)

            # Look for footer pattern (from <footer> to </footer>)
            footer_pattern = r'<footer[^>]*>.*?</footer>'
            content = re.sub(footer_pattern, new_footer, content, flags=re.DOTALL | re.IGNORECASE)

            # Add or update CSS link to point to root assets
            if '/assets/styles.css' not in content:
                # Add CSS link after the last link/preconnect in head
                css_link = '<link rel="stylesheet" href="/assets/styles.css">'
                # Insert after the last link tag in head
                head_end_pattern = r'(\s*)(</head>)'
                content = re.sub(head_end_pattern, f'\\1    {css_link}\\1\\2', content, count=1)

            # Remove inline <style> tags to prevent conflicts with new CSS
            style_pattern = r'<style[^>]*>.*?</style>'
            content = re.sub(style_pattern, '', content, flags=re.DOTALL | re.IGNORECASE)

            # Update body class for sticky footer (add flexbox classes if not present)
            body_pattern = r'<body([^>]*)class="([^"]*)"([^>]*)>'
            def update_body_class(match):
                attrs_before = match.group(1)
                classes = match.group(2)
                attrs_after = match.group(3)
                # Add flexbox classes if not already present
                if 'min-h-screen' not in classes:
                    classes += ' min-h-screen'
                if 'flex' not in classes:
                    classes += ' flex'
                if 'flex-col' not in classes:
                    classes += ' flex-col'
                return f'<body{attrs_before}class="{classes}"{attrs_after}>'
            content = re.sub(body_pattern, update_body_class, content)

            # Update main class for sticky footer (add flex-1 if not present)
            main_pattern = r'<main([^>]*)class="([^"]*)"([^>]*)>'
            def update_main_class(match):
                attrs_before = match.group(1)
                classes = match.group(2)
                attrs_after = match.group(3)
                # Add flex-1 if not already present
                if 'flex-1' not in classes and 'flex-grow' not in classes:
                    classes += ' flex-1'
                return f'<main{attrs_before}class="{classes}"{attrs_after}>'
            content = re.sub(main_pattern, update_main_class, content)

            # Write back the updated content
            with open(html_file, 'w', encoding='utf-8') as f:
                f.write(content)

            self.logger.debug(f"Post-processed HTML file: {html_file}")

        except Exception as e:
            self.logger.warning(f"Failed to post-process {html_file}: {e}")

    def find_source_files(self) -> List[Path]:
        """Find all source files to build."""
        source_files = []

        # Find Markdown and YAML files (HTML files will be copied directly)
        for file_path in self.config.source_dir.rglob('*.md'):
            if not any(part in ['templates', 'components', 'src', 'venv', 'learn_concepts']
                      for part in file_path.parts):
                source_files.append(file_path)

        for file_path in self.config.source_dir.rglob('*.yaml'):
            # Skip files in templates, components, src, venv, and learn_concepts directories
            if not any(part in ['templates', 'components', 'src', 'venv', 'learn_concepts']
                      for part in file_path.parts):
                source_files.append(file_path)

        return source_files

    def build_all_pages(self):
        """Build all pages."""
        source_files = self.find_source_files()
        self.logger.info(f"Found {len(source_files)} source files to build")

        built_pages = []
        errors = []

        for source_file in source_files:
            try:
                self.logger.debug(f"Building {source_file}")

                # Determine output path
                rel_path = source_file.relative_to(self.config.source_dir)

                # Special handling for root index files
                if source_file.name in ['index.md', 'index.yaml'] and 'pages' in source_file.parts:
                    # Root index files should output to root index.html
                    output_file = self.config.output_dir / 'index.html'
                elif source_file.suffix == '.md':
                    # Convert .md to .html
                    output_file = self.config.output_dir / rel_path.with_suffix('.html')
                elif source_file.suffix == '.yaml':
                    # Convert .yaml to .html
                    output_file = self.config.output_dir / rel_path.with_suffix('.html')
                else:
                    output_file = self.config.output_dir / rel_path

                # Create output directory
                output_file.parent.mkdir(parents=True, exist_ok=True)

                # Build page
                html_content = self.build_page(source_file)

                # Write output
                with open(output_file, 'w', encoding='utf-8') as f:
                    f.write(html_content)

                built_pages.append(output_file)
                self.logger.debug(f"Built {output_file}")

            except Exception as e:
                error_msg = f"Failed to build {source_file}: {e}"
                self.logger.error(error_msg)
                errors.append(error_msg)

        self.logger.info(f"Successfully built {len(built_pages)} pages")
        if errors:
            self.logger.error(f"Encountered {len(errors)} errors during build")
            for error in errors:
                self.logger.error(f"  - {error}")

        return built_pages, errors

    def generate_sitemap(self, built_pages: List[Path]):
        """Generate sitemap.xml."""
        try:
            base_url = config.site_url

            sitemap_entries = []
            for page in built_pages:
                rel_path = page.relative_to(self.config.output_dir)
                url_path = str(rel_path).replace('index.html', '').replace('.html', '/')
                if url_path.endswith('/'):
                    url_path = url_path[:-1] if url_path != '/' else url_path

                # Ensure proper URL construction with leading slash
                if not url_path.startswith('/'):
                    url_path = f"/{url_path}"
                full_url = f"{base_url.rstrip('/')}{url_path}"

                sitemap_entries.append({
                    'url': full_url,
                    'lastmod': datetime.now().strftime('%Y-%m-%d'),
                    'changefreq': 'weekly',
                    'priority': '0.8' if url_path == '/' else '0.6'
                })

            # Render sitemap template
            context = {'entries': sitemap_entries}
            sitemap_content = self.render_template('sitemap.xml', context)

            # Write sitemap
            sitemap_path = self.config.output_dir / 'sitemap.xml'
            with open(sitemap_path, 'w', encoding='utf-8') as f:
                f.write(sitemap_content)

            self.logger.info(f"Generated sitemap at {sitemap_path}")

        except Exception as e:
            self.logger.error(f"Failed to generate sitemap: {e}")

    def generate_robots_txt(self):
        """Generate robots.txt."""
        try:
            robots_content = self.render_template('robots.txt', {})
            robots_path = self.config.output_dir / 'robots.txt'
            with open(robots_path, 'w', encoding='utf-8') as f:
                f.write(robots_content)
            self.logger.info(f"Generated robots.txt at {robots_path}")
        except Exception as e:
            self.logger.error(f"Failed to generate robots.txt: {e}")

    def clean_output_dir(self):
        """Clean built files from output directory."""
        try:
            if self.config.output_dir == self.config.project_root:  # Output to root (GitHub.io)
                # Selective cleaning for root output - only remove known built files
                built_files = [
                    "index.html", "aboutme.html", "case_studies.html",  # Main pages
                    "example.html",  # Example page
                    "sitemap.xml", "robots.txt",  # Generated files
                ]

                # Remove specific built files if they exist
                for filename in built_files:
                    file_path = self.config.output_dir / filename
                    if file_path.exists():
                        file_path.unlink()
                        self.logger.debug(f"Removed built file: {file_path}")

                # Remove assets directory if it exists (but not the source assets)
                assets_dir = self.config.output_dir / "assets"
                if assets_dir.exists() and assets_dir.is_dir():
                    # Check if this is a copied assets dir (not the source)
                    if not (self.config.assets_dir / "styles.css").exists() or \
                       assets_dir != self.config.assets_dir:
                        shutil.rmtree(assets_dir)
                        self.logger.debug(f"Removed copied assets directory: {assets_dir}")

                # Remove any HTML files that don't exist in source directories
                for html_file in self.config.output_dir.glob("*.html"):
                    # Skip if it's in a source directory
                    if any(parent.name in ['content', 'src'] for parent in html_file.parents):
                        continue
                    # Skip documentation files
                    if html_file.name in ['BUILD_README.md', 'README.md']:
                        continue
                    # Remove if it's likely a built file (not in our known source locations)
                    html_file.unlink()
                    self.logger.debug(f"Removed built HTML file: {html_file}")

            else:
                # Original behavior for subdirectory output
                if self.config.output_dir.exists():
                    shutil.rmtree(self.config.output_dir)
                self.config.output_dir.mkdir(parents=True)

            self.logger.info(f"Cleaned built files from output directory: {self.config.output_dir}")
        except Exception as e:
            raise BuildError(f"Failed to clean output directory: {e}")

    def build(self) -> bool:
        """Run the full build process."""
        try:
            self.logger.info("Starting build process...")

            if self.config.clean:
                self.clean_output_dir()

            self.copy_assets()
            built_pages, errors = self.build_all_pages()

            if built_pages:
                self.generate_sitemap(built_pages)
                self.generate_robots_txt()

            success = len(errors) == 0
            if success:
                self.logger.info("Build completed successfully!")
            else:
                self.logger.error(f"Build completed with {len(errors)} errors")

            return success

        except Exception as e:
            self.logger.error(f"Build failed: {e}")
            return False


def main():
    """Main entry point."""
    import argparse

    parser = argparse.ArgumentParser(description='Build Data Engineering Guides website')
    parser.add_argument('--verbose', '-v', action='store_true', help='Verbose logging')
    parser.add_argument('--no-clean', action='store_true', help='Don\'t clean output directory')

    args = parser.parse_args()

    build_config = BuildConfig(
        verbose=args.verbose,
        clean=not args.no_clean
    )

    builder = BuildSystem(build_config)
    success = builder.build()

    sys.exit(0 if success else 1)


if __name__ == '__main__':
    main()