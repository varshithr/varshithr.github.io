# Data Engineering Guides - Build System
.PHONY: build clean install dev serve help

# Default target
help:
	@echo "Data Engineering Guides Build System"
	@echo ""
	@echo "Available targets:"
	@echo "  install    Install Python dependencies"
	@echo "  build      Build the website"
	@echo "  clean      Clean build artifacts"
	@echo "  dev        Build with verbose logging"
	@echo "  serve      Serve the built website locally"
	@echo "  help       Show this help message"

# Install dependencies
install:
	pip install -r requirements.txt

# Build the website
build:
	python src/build_system.py

# Clean build artifacts
clean:
	rm -f build.log

# Development build with verbose logging
dev:
	python src/build_system.py --verbose

# Serve locally (requires Python 3.7+)
serve:
	python -m http.server 8000

# Full rebuild
rebuild: clean build

# Install and build
setup: install build