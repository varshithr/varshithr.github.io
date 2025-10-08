from playwright.sync_api import sync_playwright, expect
import os

def run_verification(playwright):
    browser = playwright.chromium.launch(headless=True)
    page = browser.new_page()

    base_dir = os.path.abspath(os.path.dirname(__file__) + '/../../')

    def path(file):
        return f"file://{base_dir}/{file}"

    # 1. Verify main index page and navigation to all topic pages
    page.goto(path("index.html"))
    expect(page).to_have_title("Data Engineering Topics")
    page.screenshot(path="jules-scratch/verification/01_final_index.png")

    page.get_by_role("link", name="Explore AWS →").click()
    expect(page).to_have_title("AWS Topics")
    page.screenshot(path="jules-scratch/verification/02_final_aws_topics.png")

    page.get_by_role("link", name="Learn more →").first.click()
    expect(page).to_have_title("Amazon S3 Deep Dive")
    page.screenshot(path="jules-scratch/verification/03_final_s3_page.png")

    page.goto(path("aws/index.html"))
    page.get_by_role("link", name="View Case Studies →").click()
    expect(page).to_have_title("AWS Case Studies")
    page.screenshot(path="jules-scratch/verification/04_final_aws_case_studies.png")

    page.get_by_role("link", name="View Case Study →").first.click()
    expect(page).to_have_title("Case Study: Netflix's Resilient Data Platform with WAL")
    page.screenshot(path="jules-scratch/verification/05_final_netflix_wal_case_study.png")

    page.goto(path("index.html"))
    page.get_by_role("link", name="Explore Azure →").click()
    expect(page).to_have_title("Azure Topics")
    page.screenshot(path="jules-scratch/verification/06_final_azure_topics.png")

    page.get_by_role("link", name="Learn more →").first.click()
    expect(page).to_have_title("Azure Data Lake Storage (ADLS) Gen2 Deep Dive")
    page.screenshot(path="jules-scratch/verification/07_final_adls_page.png")

    page.goto(path("azure/index.html"))
    page.get_by_role("link", name="View Case Studies →").click()
    expect(page).to_have_title("Azure Case Studies")
    page.screenshot(path="jules-scratch/verification/08_final_azure_case_studies.png")

    page.get_by_role("link", name="View Case Study →").first.click()
    expect(page).to_have_title("Case Study: AI-Powered Personalization at ASOS with Azure")
    page.screenshot(path="jules-scratch/verification/09_final_azure_personalization_case_study.png")

    # 10. Verify Databricks and SQL sections, including enriched content from user
    page.goto(path("index.html"))
    page.get_by_role("link", name="Explore Databricks →").click()
    page.locator(".card", has_text="Databricks & Lakehouse").get_by_role("link").click()
    expect(page).to_have_title("Databricks Explained")
    page.screenshot(path="jules-scratch/verification/10_final_databricks_enriched.png")

    page.goto(path("index.html"))
    page.get_by_role("link", name="Explore SQL →").click()
    page.locator(".card", has_text="SQL Querying & Tuning").get_by_role("link").click()
    expect(page).to_have_title("SQL Querying & Tuning for Large Datasets")
    page.screenshot(path="jules-scratch/verification/11_final_sqltuning_enriched.png")

    page.goto(path("sql/index.html"))
    page.get_by_role("link", name="View Case Studies →").click()
    expect(page).to_have_title("SQL Case Studies")
    page.screenshot(path="jules-scratch/verification/12_final_sql_case_studies.png")

    page.get_by_role("link", name="View Case Study →").first.click()
    expect(page).to_have_title("Case Study: Scaling MySQL at Shopify with Vitess")
    page.screenshot(path="jules-scratch/verification/13_final_shopify_case_study.png")

    browser.close()

with sync_playwright() as playwright:
    run_verification(playwright)