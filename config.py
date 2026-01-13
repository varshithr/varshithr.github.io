"""
Configuration file for the Data Engineering Guides website build system.
"""

import os
from pathlib import Path


class Config:
    """Main configuration class."""

    def __init__(self):
        self.project_root = Path(__file__).parent

        # Directory structure
        self.source_dir = self.project_root / "content"
        self.templates_dir = self.project_root / "src" / "templates"
        self.assets_dir = self.project_root / "assets"
        self.output_dir = self.project_root  # GitHub.io serves from root

        # Build settings
        self.clean_build = True
        self.verbose_logging = False

        # Site settings
        self.site_name = "Data Engineering Guides"
        self.site_description = "Comprehensive data engineering concepts, services, and best practices across major cloud platforms."
        self.site_url = "https://varshithr.github.io"
        self.site_author = "Varshith Ramachandra Manchikanti"

        # SEO settings
        self.default_keywords = [
            "data engineering", "cloud platforms", "AWS", "GCP", "Azure",
            "Databricks", "distributed systems", "SRE", "big data"
        ]

    @property
    def markdown_extensions(self):
        """Default markdown extensions to use."""
        return [
            'markdown.extensions.extra',
            'markdown.extensions.codehilite',
            'markdown.extensions.tables',
            'markdown.extensions.toc',
            'markdown.extensions.fenced_code'
        ]

    @property
    def markdown_extension_configs(self):
        """Configuration for markdown extensions."""
        return {
            'markdown.extensions.codehilite': {'use_pygments': False}
        }


# Global config instance
config = Config()