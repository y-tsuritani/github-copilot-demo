import csv
import re


def find_names(file_path: str) -> list:
    """
    ファイルを読み込んで、日本人の名前を抽出する関数

    Args:
        file_path: ファイルパス

    Return:
        名前のリスト

    """
    names = []
    with open(file_path, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            for item in row:
                matches = re.findall(r"氏名：(.+)", item)
                names.extend(matches)
    return names


def find_phone_numbers(file_path: str) -> list:
    """
    ファイルを読み込んで、電話番号を抽出する関数

    Args:
        file_path: ファイルパス

    Return:
        電話番号のリスト

    """
    phone_numbers = []
    with open(file_path, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            for item in row:
                matches = re.findall(r"\d{2,4}-\d{2,4}-\d{4}", item)
                phone_numbers.extend(matches)
    return phone_numbers


def find_postal_codes(file_path: str) -> list:
    """
    ファイルを読み込んで、郵便番号を抽出する関数

    Args:
        file_path: ファイルパス

    Return:
        郵便番号のリスト

    """
    postal_codes = []
    with open(file_path, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            for item in row:
                matches = re.findall(r"\d{3}-\d{4}", item)
                postal_codes.extend(matches)
    return postal_codes


def find_emails(file_path: str) -> list:
    """
    ファイルを読み込んで、メールアドレスを抽出する関数

    Args:
        file_path: ファイルパス

    Return:
        メールアドレスのリスト

    """
    emails = []
    with open(file_path, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            for item in row:
                matches = re.findall(r"\w+@\w+\.\w+", item)
                emails.extend(matches)
    return emails


# ファイルを読み込んで日本の住所を抽出する関数
def find_addresses(file_path: str) -> list:
    """
    ファイルを読み込んで、日本の住所を抽出する関数

    Args:
        file_path: ファイルパス

    Return:
        住所のリスト

    """
    addresses = []
    with open(file_path, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            for item in row:
                matches = re.findall(
                    r"([^\x01-\x7Eぁ-んァ-ン一-龥]+[都道府県市区町村][^\x01-\x7Eぁ-んァ-ン一-龥]+[市区町村][^\x01-\x7Eぁ-んァ-ン一-龥]+[0-9-]+)",
                    item,
                )
                addresses.extend(matches)
    return addresses


# 住所の文字列を座標に変換する関数
def address_to_coordinate(address: str) -> tuple:
    """
    住所の文字列を座標に変換する関数

    Args:
        address: 住所の文字列

    Return:
        座標のタプル

    """
    import json

    import requests

    url = "https://www.geocoding.jp/api/"
    payload = {"q": address}
    result = requests.get(url, params=payload)
    result = json.loads(result.text)
    coordinate = (result["coordinate"]["lat"], result["coordinate"]["lng"])
    return coordinate


# 座標のタプルを距離に変換する関数
def coordinate_to_distance(coordinate1: tuple, coordinate2: tuple) -> float:
    """
    座標のタプルを距離に変換する関数

    Args:
        coordinate1: 座標のタプル1
        coordinate2: 座標のタプル2

    Return:
        距離

    """
    import math

    lat1 = math.radians(coordinate1[0])
    lon1 = math.radians(coordinate1[1])
    lat2 = math.radians(coordinate2[0])
    lon2 = math.radians(coordinate2[1])

    r = 6378.137
    x = r * math.cos(lat1) * math.cos(lon1) - r * math.cos(lat2) * math.cos(lon2)
    y = r * math.cos(lat1) * math.sin(lon1) - r * math.cos(lat2) * math.sin(lon2)
    z = r * math.sin(lat1) - r * math.sin(lat2)
    distance = math.sqrt(x**2 + y**2 + z**2)
    return distance
