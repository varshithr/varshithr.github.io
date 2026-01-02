#!/bin/bash

# Exit immediately if a command exits with a non-zero status.
set -e

# --- Configuration ---
SRC_DIR="learn_concepts/docs"
DEST_DIR="learn"
TEMPLATE_FILE="scripts/template.html"

# --- Helper Functions ---
function print_info() {
    echo "INFO: $1"
}

function print_error() {
    echo "ERROR: $1" >&2
    exit 1
}

# --- Dependency Check ---
if ! command -v pandoc &> /dev/null; then
    print_info "pandoc not found. Attempting to install..."
    # Add installation command for your OS, e.g., for Debian/Ubuntu:
    if [ -f /etc/debian_version ]; then
        sudo apt-get update && sudo apt-get install -y pandoc
    # For macOS with Homebrew:
    elif [[ "$OSTYPE" == "darwin"* ]]; then
        brew install pandoc
    else
        print_error "Unsupported OS. Please install pandoc manually."
    fi
fi

# --- Main Script ---

# 1. Clean and recreate the destination directory
print_info "Cleaning up destination directory: $DEST_DIR"
rm -rf "$DEST_DIR"
mkdir -p "$DEST_DIR"

# 2. Find all markdown files and process them
find "$SRC_DIR" -name "*.md" | while read -r md_file; do
    # 3. Determine output path, converting to lowercase
    relative_path="${md_file#$SRC_DIR/}"
    html_file="$DEST_DIR/$(echo "${relative_path%.md}.html" | tr '[:upper:]' '[:lower:]')"

    # 4. Create destination directory for the HTML file
    mkdir -p "$(dirname "$html_file")"

    print_info "Processing: $md_file -> $html_file"

    # 5. Extract title from the first H1 heading and remove newlines
    title=$(grep -m 1 '^# ' "$md_file" | sed 's/# //' | tr -d '\n')
    if [ -z "$title" ]; then
        title=$(basename "${md_file%.md}")
    fi

    # 6. Calculate relative paths
    depth=$(echo "$relative_path" | awk -F/ '{print NF-1}')
    rel_path=$(printf '../'%.0s $(seq 1 $depth))
    css_path=$(printf '../'%.0s $(seq 1 $depth))"learn/css"

    # 7. Convert Markdown to HTML using pandoc with the template and title
    pandoc "$md_file" \
        -o "$html_file" \
        --template="$TEMPLATE_FILE" \
        --standalone \
        --toc \
        --toc-depth=2 \
        --katex \
        --metadata title="$title" \
        --variable=rel_path:"$rel_path" \
        --variable=css_path:"$css_path"

    # 7. Post-process the HTML
    # - Replace .md links with .html
    # - Remove newlines from the <title> tag
    perl -i -p -e 's/\.md"/.html"/g' "$html_file"
    perl -i -0777 -pe 's|<title>\s*([^<]*?)\s*</title>|<title>$1</title>|g' "$html_file"
done

print_info "Build complete. HTML files are in the '$DEST_DIR' directory."
