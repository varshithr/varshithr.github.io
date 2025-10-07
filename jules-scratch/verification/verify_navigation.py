import os
from playwright.sync_api import sync_playwright, expect

def run_verification(playwright):
    browser = playwright.chromium.launch(headless=True)
    page = browser.new_page()

    base_path = "file://" + os.path.abspath(".")

    # 1. Verify index.html
    page.goto(f"{base_path}/index.html")
    expect(page).to_have_title("Data Engineering Topics")
    page.screenshot(path="jules-scratch/verification/01_index_page.png")

    # 2. Verify GCP Navigation and Content
    page.get_by_role("link", name="Explore GCP →").click()
    expect(page).to_have_title("GCP Topics")
    page.screenshot(path="jules-scratch/verification/02_gcp_topics.png")

    page.get_by_role("link", name="View Case Studies →").click()
    expect(page).to_have_title("GCP Case Studies")
    page.screenshot(path="jules-scratch/verification/03_gcp_case_studies.png")
    page.go_back()

    page.get_by_role("link", name="Learn more →").first.click()
    expect(page).to_have_title("BigQuery Visual Deep Dive")
    expect(page.get_by_role("link", name="Back to GCP Topics")).to_be_visible()
    page.screenshot(path="jules-scratch/verification/04_bigquery_page.png")

    # 3. Verify AWS Navigation and Content
    page.goto(f"{base_path}/index.html")
    page.get_by_role("link", name="Explore AWS →").click()
    expect(page).to_have_title("AWS Topics")
    page.screenshot(path="jules-scratch/verification/05_aws_topics.png")

    page.get_by_role("link", name="Learn more →").click()
    expect(page).to_have_title("AWS Data Engineering Overview")
    page.screenshot(path="jules-scratch/verification/06_aws_overview.png")
    page.go_back()

    page.get_by_role("link", name="View Case Studies →").click()
    expect(page).to_have_title("AWS Case Studies")
    page.screenshot(path="jules-scratch/verification/07_aws_case_studies.png")

    # 4. Verify Azure Navigation and Content
    page.goto(f"{base_path}/index.html")
    page.get_by_role("link", name="Explore Azure →").click()
    expect(page).to_have_title("Azure Topics")
    page.screenshot(path="jules-scratch/verification/08_azure_topics.png")

    page.get_by_role("link", name="Learn more →").click()
    expect(page).to_have_title("Azure Data Engineering Overview")
    page.screenshot(path="jules-scratch/verification/09_azure_overview.png")
    page.go_back()

    page.get_by_role("link", name="View Case Studies →").click()
    expect(page).to_have_title("Azure Case Studies")
    page.screenshot(path="jules-scratch/verification/10_azure_case_studies.png")

    # 5. Verify Databricks Navigation
    page.goto(f"{base_path}/index.html")
    page.get_by_role("link", name="Explore Databricks →").click()
    expect(page).to_have_title("Databricks Topics")
    page.screenshot(path="jules-scratch/verification/11_databricks_topics.png")

    # 6. Verify SQL Navigation
    page.goto(f"{base_path}/index.html")
    page.get_by_role("link", name="Explore SQL →").click()
    expect(page).to_have_title("SQL Topics")
    page.screenshot(path="jules-scratch/verification/12_sql_topics.png")

    browser.close()

with sync_playwright() as playwright:
    run_verification(playwright)