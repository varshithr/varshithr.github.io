from playwright.sync_api import sync_playwright
import os

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # Create a directory for the screenshots if it doesn't exist
        os.makedirs("jules-scratch/verification", exist_ok=True)

        # Get the path to the current working directory
        base_path = os.getcwd()

        # List of all HTML files to capture
        html_files = []
        for root, _, files in os.walk("."):
            if "layouts" in root:
                continue
            for file in files:
                if file.endswith(".html"):
                    html_files.append(os.path.join(root, file))

        for file_path in html_files:
            # Navigate to the local HTML file
            page.goto(f"file://{os.path.join(base_path, file_path)}")

            # Take a screenshot
            screenshot_path = f"jules-scratch/verification/{os.path.splitext(os.path.basename(file_path))[0]}.png"
            page.screenshot(path=screenshot_path)
            print(f"Screenshot saved to {screenshot_path}")

        browser.close()

if __name__ == "__main__":
    run()
