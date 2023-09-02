import pytest

from myapp.find_personal_info import (
    find_addresses,
    find_emails,
    find_names,
    find_phone_numbers,
    find_postal_codes,
)


@pytest.fixture
def sample_file(tmp_path):
    file_path = tmp_path / "sample.csv"
    with open(file_path, "w") as file:
        file.write("住所：東京都渋谷区神南1-2-3\n")
        file.write("住所：大阪府大阪市北区梅田2-3-4\n")
        file.write("住所：福岡県福岡市博多区博多駅前1-2-3\n")
        file.write("氏名：山田太郎\n")
        file.write("氏名：鈴木花子\n")
        file.write("090-1234-5678\n")
        file.write("03-1234-5678\n")
        file.write("0120-123-456\n")
        file.write("100-0001\n")
        file.write("530-0001\n")
        file.write("810-0001\n")
        file.write("メールアドレス：test@example.com\n")
        file.write("メールアドレス：test2@example.com\n")
    return file_path


def test_find_addresses(sample_file):
    addresses = find_addresses(sample_file)
    assert len(addresses) == 3
    assert addresses[0] == "東京都渋谷区神南1-2-3"
    assert addresses[1] == "大阪府大阪市北区梅田2-3-4"
    assert addresses[2] == "福岡県福岡市博多区博多駅前1-2-3"


def test_find_emails(sample_file):
    emails = find_emails(sample_file)
    assert len(emails) == 2
    assert emails[0] == "test@example.com"
    assert emails[1] == "test2@example.com"


def test_find_names(sample_file):
    names = find_names(sample_file)
    assert len(names) == 2
    assert names[0] == "山田太郎"
    assert names[1] == "鈴木花子"


def test_find_phone_numbers(sample_file):
    phone_numbers = find_phone_numbers(sample_file)
    assert len(phone_numbers) == 3
    assert phone_numbers[0] == "090-1234-5678"
    assert phone_numbers[1] == "03-1234-5678"
    assert phone_numbers[2] == "0120-123-456"


def test_find_postal_codes(sample_file):
    postal_codes = find_postal_codes(sample_file)
    assert len(postal_codes) == 3
    assert postal_codes[0] == "100-0001"
    assert postal_codes[1] == "530-0001"
    assert postal_codes[2] == "810-0001"
