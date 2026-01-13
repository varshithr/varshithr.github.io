# Data Engineering Guides - Build System

This document describes the new build system for the Data Engineering Guides website.

## Overview

The website has been restructured with a modern build system that:

- Uses Jinja2 templating to eliminate code duplication
- Provides centralized path management
- Includes comprehensive error handling and logging
- Generates SEO-optimized pages with proper metadata
- Implements accessibility best practices
- Uses a consistent design system

## Directory Structure

```
├── assets/                 # Static assets (CSS, JS, images)
├── content/                # Source content (Markdown/HTML pages)
├── src/
│   ├── templates/          # Jinja2 templates and components
│   │   ├── components/     # Reusable HTML components
│   │   └── *.html          # Page templates
│   └── *.py               # Build system and utilities
├── config.py              # Build configuration
├── requirements.txt       # Python dependencies
├── Makefile              # Build commands
├── *.html                # Built pages (GitHub.io root)
├── sitemap.xml           # Generated sitemap
└── robots.txt            # Generated robots.txt
```

**Note**: This project builds directly to the root directory for GitHub.io compatibility. Built files are excluded from version control via `.gitignore`.

## Quick Start

1. Install dependencies:
   ```bash
   make install
   ```

2. Build the website:
   ```bash
   make build
   ```

3. Serve locally:
   ```bash
   make serve
   ```

## Build Commands

- `make install` - Install Python dependencies
- `make build` - Build the website
- `make dev` - Build with verbose logging
- `make clean` - Clean build artifacts
- `make serve` - Serve the built website locally
- `make rebuild` - Full clean rebuild

## Key Improvements

### 1. Template System
- Shared HTML templates eliminate duplication
- Consistent navigation across all pages
- Modular components for headers, footers, etc.

### 2. Path Management
- Centralized path calculation system
- Automatic relative path generation
- Consistent URL structure

### 3. SEO & Accessibility
- Automatic meta tag generation
- Open Graph and Twitter card support
- ARIA labels and semantic HTML
- Skip links for keyboard navigation

### 4. Design System
- Consistent color palette and styling
- CSS custom properties for theming
- Responsive design with mobile-first approach

### 5. Error Handling
- Comprehensive logging
- Build failure reporting
- Graceful error recovery

## Configuration

Edit `config.py` to customize:

- Site metadata (name, description, author)
- Directory paths
- Build settings
- SEO defaults

## Adding New Content

1. Place content in `content/` directory
2. Use Markdown (`.md`) or HTML (`.html`) files
3. Add YAML frontmatter for page-specific metadata
4. Run `make build` to generate pages in root directory

Example YAML frontmatter:
```yaml
title: My Page Title
description: Page description for SEO
keywords: [keyword1, keyword2]
```

## GitHub.io Configuration

This project is configured for GitHub.io deployment:

- Built files are placed in the repository root
- GitHub Pages serves from the root directory
- Built files are excluded from git via `.gitignore`
- Source files remain tracked for version control

## Migration Notes

The old build system (`build_concepts.py`) is still available but deprecated. The new system provides:

- Better error handling
- More features (SEO, accessibility)
- Cleaner architecture
- Easier maintenance

## Troubleshooting

Check `build.log` for detailed error information when builds fail.

Common issues:
- Missing dependencies: Run `make install`
- Permission errors: Check file permissions
- Template errors: Check Jinja2 syntax in templates