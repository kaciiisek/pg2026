import sys
import requests


def download_url_and_get_all_hrefs(url):
    """
    Funkce stahne url predanou v parametru url pomoci volani response =
    requests.get(),
    zkontroluje navratovy kod response.status_code, ktery musi byt 200,
    pokud ano, najdete ve stazenem obsahu stranky response.text
    vsechny vyskyt
    <a href="url">odkaz</a> a z nich nactete url, ktere vratite jako
    seznam pomoci return
    """
    hrefs = []

    response = requests.get(url)

    if response.status_code == 200:
        content = response.text
        start = 0

        while True:
            pos = content.find('<a href="', start)

            if pos == -1:
                break

            url_start = pos + len('<a href="')
            url_end = content.find('"', url_start)

            hrefs.append(content[url_start:url_end])

            start = url_end

    return hrefs


if __name__ == "__main__":
    try:
        url = sys.argv[1]
        print(download_url_and_get_all_hrefs(url))
    # osetrete potencialni chyby pomoci vetve except
    except Exception as e:
        print(f"Program skoncil chybou: {e}")
