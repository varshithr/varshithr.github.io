#!/bin/bash
set -e

# Create the output directory if it doesn't exist
mkdir -p learn

# Loop through all Markdown files in the source directory
find learn_concepts/docs -name "*.md" | while read file; do
  # Get the relative path of the file
  relative_path=${file#learn_concepts/docs/}

  # Set the output path for the HTML file and convert to lowercase
  output_path="learn/$relative_path"
  output_path=$(echo "${output_path//.md/.html}" | tr '[:upper:]' '[:lower:]')

  # Create the output directory for the HTML file
  mkdir -p "$(dirname "$output_path")"

  # Convert the Markdown file to HTML using pandoc and replace .md links
  export BODY=$(pandoc -f markdown -t html "$file" | sed 's/\.md/\.html/g')

  # Get the title from the first line of the Markdown file
  export TITLE=$(head -n 1 "$file" | sed 's/# //')

  # Use envsubst to perform the template substitution
  envsubst < scripts/template.html > "$output_path"

  echo "Generated $output_path"
done

echo "Build finished successfully."
