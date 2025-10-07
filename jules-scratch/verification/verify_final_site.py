import os
from playwright.sync_api import sync_playwright, expect

def run_verification(playwright):
    browser = playwright.chromium.launch(headless=True)
    page = browser.new_page()

    base_path = "file://" + os.path.abspath(".")

    # --- Verification ---

    # 1. Index Page
    page.goto(f"{base_path}/index.html")
    expect(page).to_have_title("Data Engineering Topics")
    page.screenshot(path="jules-scratch/verification/01_final_index.png")

    # 2. AWS Section
    page.get_by_role("link", name="Explore AWS →").click()
    expect(page).to_have_title("AWS Topics")
    page.screenshot(path="jules-scratch/verification/02_final_aws_topics.png")

    page.get_by_role("link", name="Learn more →").first.click()
    expect(page).to_have_title("Amazon S3 Deep Dive")
    page.screenshot(path="jules-scratch/verification/03_final_s3_page.png")
    page.go_back()

    page.get_by_role("link", name="View Case Studies →").click()
    expect(page).to_have_title("AWS Case Studies")
    page.screenshot(path="jules-scratch/verification/04_final_aws_case_studies.png")

    page.get_by_role("link", name="View Case Study →").first.click()
    expect(page).to_have_title("Case Study: Netflix's Resilient Data Platform with WAL")
    page.locator(".mermaid").scroll_into_view_if_needed()
    page.wait_for_timeout(1500) # Wait for mermaid to render
    page.screenshot(path="jules-scratch/verification/05_final_netflix_wal_case_study.png")

    # 3. Azure Section
    page.goto(f"{base_path}/index.html")
    page.get_by_role("link", name="Explore Azure →").click()
    expect(page).to_have_title("Azure Topics")
    page.screenshot(path="jules-scratch/verification/06_final_azure_topics.png")

    page.get_by_role("link", name="Learn more →").first.click()
    expect(page).to_have_title("Azure Data Lake Storage (ADLS) Gen2 Deep Dive")
    page.screenshot(path="jules-scratch/verification/07_final_adls_page.png")
    page.go_back()

    page.get_by_role("link", name="View Case Studies →").click()
    expect(page).to_have_title("Azure Case Studies")
    page.screenshot(path="jules-scratch/verification/08_final_azure_case_studies.png")

    page.get_by_role("link", name="View Case Study →").first.click()
    expect(page).to_have_title("Case Study: AI-Powered Personalization at ASOS with Azure")
    page.locator(".mermaid").scroll_into_view_if_needed()
    page.wait_for_timeout(1500) # Wait for mermaid to render
    page.screenshot(path="jules-scratch/verification/09_final_azure_personalization_case_study.png")

    # 4. Databricks Enriched Content
    page.goto(f"{base_path}/databricks_topics.html")
    page.get_by_role("link", name="Learn more →").first.click()
    expect(page).to_have_title("Databricks Explained")
    page.screenshot(path="jules-scratch/verification/10_final_databricks_enriched.png")

    # 5. SQL Enriched Content & New Case Study
    page.goto(f"{base_path}/sql_topics.html")
    page.locator("div.card:has-text('SQL Querying & Tuning')").get_by_role("link", name="Learn more →").click()
    expect(page).to_have_title("SQL Querying & Tuning for Large Datasets")
    page.screenshot(path="jules-scratch/verification/11_final_sqltuning_enriched.png")
    page.go_back()

    page.get_by_role("link", name="View Case Studies →").click()
    expect(page).to_have_title("SQL Case Studies")
    page.screenshot(path="jules-scratch/verification/12_final_sql_case_studies.png")

    page.get_by_role("link", name="View Case Study →").first.click()
    expect(page).to_have_title("Case Study: Scaling MySQL at Shopify with Vitess")
    page.locator(".mermaid").scroll_into_view_if_needed()
    page.wait_for_timeout(1500) # Wait for mermaid to render
    page.screenshot(path="jules-scratch/verification/13_final_shopify_case_study.png")

    browser.close()

with sync_playwright() as playwright:
    run_verification(playwright)