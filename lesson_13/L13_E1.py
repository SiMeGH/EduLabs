import requests as requests


def get_country_ids_and_probabilities(name: str) -> dict[float, str]:
    nationalize_url: str = "https://api.nationalize.io/"
    request_url: str = nationalize_url + f"?name={name}"
    response = requests.get(request_url)
    if response.status_code != 200:
        raise Exception("ERROR. Bad response from \'nationalize\'.")
    response_dict: dict = response.json()
    prob_and_id_dict: dict[float, str] = {}
    for country_id in response_dict["country"]:
        prob_and_id_dict[country_id["probability"]] = country_id["country_id"]
    return prob_and_id_dict


def find_highest_probability_country(id_and_prob_dict: dict[float, str]) -> str:
    if not id_and_prob_dict:
        raise Exception("ERROR. Name is invalid.")
    max_prob: float = 0
    for prob in id_and_prob_dict:
        if prob > max_prob:
            max_prob = prob
    return id_and_prob_dict[max_prob]


def get_country_name_from_code(code: str) -> str:
    restcountries_url: str = "https://restcountries.com/v3.1/alpha/"
    request_url: str = restcountries_url + code
    response = requests.get(request_url)
    if response.status_code != 200:
        raise Exception("ERROR. Bad response from \'restcountries\'.")
    response_dict: dict = response.json()
    return response_dict[0]["name"]["common"]


if __name__ == '__main__':
    try:
        my_name: str = input("Enter a name: ").lower().strip()
        id_and_prob: dict = get_country_ids_and_probabilities(my_name)
        country_code: str = find_highest_probability_country(id_and_prob)
        country_name: str = get_country_name_from_code(country_code)
        print(f"The most likely country to have the name \'{my_name}\' is \'{country_name}\'")
    except Exception as error:
        print(error)
