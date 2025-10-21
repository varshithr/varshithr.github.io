from playwright.sync_api import sync_playwright
import os

def run(playwright):
    browser = playwright.chromium.launch()
    page = browser.new_page()

    base_url = "file:///app/"
    screenshot_dir = "jules-scratch/verification/"

    # List of pages to visit and screenshot
    pages_to_verify = [
        "index.html",
        "aboutme.html",
        "case_studies.html",
        "gcp/index.html",
        "gcp/bigquery.html",
        "gcp/bigtable.html",
        "gcp/cloud_storage.html",
        "gcp/composer.html",
        "gcp/dataflow.html",
        "gcp/dataproc.html",
        "gcp/gke.html",
        "gcp/case_studies/index.html",
        "gcp/case_studies/case_study_bigquery.html",
        "gcp/case_studies/case_study_dataflow.html",
        "gcp/case_studies/case_study_genomics.html",
        "gcp/case_studies/case_study_geospatial.html",
        "gcp/case_studies/case_study_netflix_looker.html",
        "aws/index.html",
        "aws/s3.html",
        "aws/redshift.html",
        "aws/emr.html",
        "aws/kinesis.html",
        "aws/glue.html",
        "aws/case_studies/index.html",
        "aws/case_studies/case_study_aws_dwh.html",
        "aws/case_studies/case_study_aws_ml.html",
        "aws/case_studies/case_study_aws_streaming.html",
        "aws/case_studies/case_study_netflix_wal.html",
        "azure/index.html",
        "azure/synapse.html",
        "azure/adls_gen2.html",
        "azure/adls.html",
        "azure/data_factory.html",
        "azure/event_hubs.html",
        "azure/case_studies/index.html",
        "azure/case_studies/case_study_azure_iot.html",
        "azure/case_studies/case_study_azure_personalization.html",
        "azure/case_studies/case_study_azure_synapse.html",
        "databricks/index.html",
        "databricks/databricks_platform.html",
        "databricks/delta_lake.html",
        "databricks/lakeflow.html",
        "databricks/agent_bricks.html",
        "databricks/case_studies/index.html",
        "databricks/case_studies/autoloader.html",
        "databricks/case_studies/case_study_adobe_delta.html",
        "sql/index.html",
        "sql/advanced_sql.html",
        "sql/dim_model.html",
        "sql/spark_internals.html",
        "sql/sqltuning.html",
        "sql/case_studies/index.html",
        "sql/case_studies/case1.html",
        "sql/case_studies/case_study_shopify_vitess.html",
        "sql/case_studies/customer_cohort.html",
    ]

    for rel_path in pages_to_verify:
        url = f"{base_url}{rel_path}"
        screenshot_path = os.path.join(screenshot_dir, rel_path.replace("/", "_").replace(".html", ".png"))

        page.goto(url)
        page.screenshot(path=screenshot_path)
        print(f"Captured screenshot of {url} at {screenshot_path}")

    browser.close()

with sync_playwright() as playwright:
    run(playwright)
