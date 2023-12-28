from urllib.request import urlopen
import json
import requests

boxer_name = "Cung Le"

url = f"https://script.google.com/macros/s/AKfycbwFKTo7z55NfBapOwEIQCyc59oLC1rofk4CZh79nf39lhKm0Inl2Mtw2KFU3xeKDmBU/exec?boxer_name={boxer_name}"

try:
    response = requests.get(url)
    response.raise_for_status()

    boxer_info = response.json()

except requests.exceptions.HTTPError as err:
    print(f"Lỗi: {err}")
except requests.exceptions.RequestException as err:
    print(f"Lỗi kết nối: {err}")
print(f"Thông tin võ sĩ: Tên: {boxer_info['data'][0]['boxer_name']} , Tuổi: {boxer_info['data'][0]['boxer_age']} , Chiều cao: {boxer_info['data'][0]['boxer_height']} , Cân nặng: {boxer_info['data'][0]['boxer_weight']} , Nơi ở hiện tại: {boxer_info['data'][0]['boxer_location']} , Quê quán: {boxer_info['data'][0]['boxer_hometown']}")
