import google.cloud.bigquery as bigquery
import pytest

from app.insert_records import insert_csv_to_bigquery


@pytest.fixture
def mock_client(mocker):
    return mocker.patch.object(bigquery, "Client")


@pytest.fixture
def mock_table_ref(mocker):
    return mocker.Mock(spec=bigquery.TableReference)


def test_insert_csv_to_bigquery(mocker, mock_client, mock_table_ref):
    # Set up mock file
    csv_data = "id,user_id,date,amount,store\n1,1,2022-01-01,1000,store1\n2,2,2022-01-02,2000,store2\n"
    m = mocker.mock_open(read_data=csv_data)
    mocker.patch("builtins.open", m)

    # Call function
    insert_csv_to_bigquery(mock_client, "test.csv", mock_table_ref)

    # Assert that job was created and executed correctly
    mock_client.return_value.load_table_from_file.assert_called_once_with(
        m(), mock_table_ref, job_config=mocker.ANY
    )
    job_config = mock_client.return_value.load_table_from_file.call_args[1][
        "job_config"
    ]
    assert job_config.schema == [
        bigquery.SchemaField("id", "INTEGER"),
        bigquery.SchemaField("user_id", "INTEGER"),
        bigquery.SchemaField("date", "DATE"),
        bigquery.SchemaField("amount", "INTEGER"),
        bigquery.SchemaField("store", "STRING"),
    ]
    assert job_config.skip_leading_rows == 1
    assert job_config.source_format == bigquery.SourceFormat.CSV
