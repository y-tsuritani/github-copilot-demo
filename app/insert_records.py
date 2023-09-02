# .db/data/data.csv に格納されているデータをbigqueryのテーブルに挿入する関数を定義しています。
# import google.cloud.bigquery as bigquery
from google.cloud import bigquery


def insert_csv_to_bigquery(
    client: bigquery.Client, filepath: str, table_ref: bigquery.TableReference
) -> None:
    """Inserts data from a CSV file into a BigQuery table.

    Args:
        client (google.cloud.bigquery.client.Client): A BigQuery client object.
        filepath (str): The path to the CSV file to insert.
        table_ref (google.cloud.bigquery.table.TableReference): A reference to the destination table.

    Returns:
        None: This function does not return anything.

    Raises:
        google.cloud.exceptions.GoogleCloudError: If the job fails for any reason.
    """
    # Set up job configuration
    job_config = bigquery.LoadJobConfig(
        schema=[
            bigquery.SchemaField("id", "INTEGER"),
            bigquery.SchemaField("user_id", "INTEGER"),
            bigquery.SchemaField("date", "DATE"),
            bigquery.SchemaField("amount", "INTEGER"),
            bigquery.SchemaField("store", "STRING"),
            # Add more schema fields as needed
        ],
        skip_leading_rows=1,
        source_format=bigquery.SourceFormat.CSV,
    )

    # Load data from CSV file into table
    with open(filepath, "rb") as source_file:
        job = client.load_table_from_file(source_file, table_ref, job_config=job_config)

    # Wait for job to complete
    job.result()

    print(f"Loaded {job.output_rows} rows into {table_ref.table_id}.")


file_path = "./db/data/data.csv"

# Set up BigQuery client
client = bigquery.Client()

# Set up table reference
dataset_name = "GITHUB_COPILOT_DEMO"
table_id = "transactions"
table_ref = client.dataset("GITHUB_COPILOT_DEMO").table(table_id)

# Insert data from CSV file into table
insert_csv_to_bigquery(client, file_path, table_ref)
