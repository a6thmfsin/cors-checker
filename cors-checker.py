#!/usr/bin/python3

import requests

def read_urls_from_file(file_path):
    with open(file_path, "r") as file:
        urls = file.readlines()
    urls = [url.strip() for url in urls]
    return urls

headers = {
    "Origin": "https://google.com",
    "Referer": "https://google.com" #you can ofc change google to your collaborator url aswell
}

def check_acao(urls, header_name):
    acao_file_name = f"{header_name.lower()}-acao.txt"
    with open(acao_file_name, "w") as f:
        for url in urls:
            try:
                response = requests.get(url, headers={header_name: headers[header_name]})
                if "Access-Control-Allow-Credentials" in response.headers:
                    f.write(f"{url}\n")
            except requests.exceptions.RequestException as e:
                print(f"error{url}: {e}")

if __name__ == "__main__":
    input_file_path = input("input endpoints: ")
    urls = read_urls_from_file(input_file_path)
    check_acao(urls, "Origin")
    check_acao(urls, "Referer")
