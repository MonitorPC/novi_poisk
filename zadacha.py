import requests


def get_spn(adres):
    toponym_to_find = adres

    geocoder_api_server = "http://geocode-maps.yandex.ru/1.x/"

    geocoder_params = {
        "apikey": "40d1649f-0493-4b70-98ba-98533de7710b",
        "geocode": toponym_to_find,
        "format": "json"}

    response = requests.get(geocoder_api_server, params=geocoder_params)

    # Преобразуем ответ в json-объект
    json_response = response.json()
    # Получаем первый топоним из ответа геокодера.
    toponym = json_response["response"]["GeoObjectCollection"][
        "featureMember"][0]["GeoObject"]

    corner = toponym["boundedBy"]["Envelope"]

    delta = [str(abs(float(corner["lowerCorner"].split(' ')[0]) - float(corner["upperCorner"].split(' ')[0]))),
             str(abs(float(corner["lowerCorner"].split(' ')[1]) - float(corner["upperCorner"].split(' ')[1])))]

    return delta
