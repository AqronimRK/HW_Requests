import requests


def get_heroes_id_list(heroes_list):
    heroes_id_list = []
    for hero in heroes_list:
        reference_uri = f'https://superheroapi.com/api/2619421814940190/search/{hero}'
        search_request = requests.get(reference_uri).json()['results']
        req_id_list = [search_request[i]['id'] for i in range(len(search_request)) if search_request[i]['name'] == hero]
        heroes_id_list.append(req_id_list[0])
    return heroes_id_list


def get_intelligence_heroes(heroes_name):
    id_list = get_heroes_id_list(heroes_name)
    hero_dict = {}
    for hero in id_list:
        reference_uri = f'https://superheroapi.com/api/2619421814940190/{hero}/powerstats'
        intel_req = requests.get(reference_uri).json()
        hero_dict[int(intel_req['intelligence'])] = intel_req['name']
    print(f'Самый умный из {", ".join(heroes_name)} это {hero_dict[max(hero_dict.keys())]} с интеллектом: '
          f'{max(hero_dict.keys())}')


get_intelligence_heroes(['Hulk', 'Captain America', 'Thanos'])
