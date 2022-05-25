import requests


class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_to, file_from):
        get_upload_def_url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        headers = {'Content-type': 'application/json', 'Authorization': f'OAuth {self.token}'}
        params = {'path': file_to, 'overwrite': 'true'}

        upload_url_json = requests.get(get_upload_def_url, headers=headers, params=params).json()
        href = upload_url_json.get('href')

        with open(file_from, 'rb') as upload_file:
            upload_put = requests.put(href, data=upload_file)
            if upload_put.status_code == 201:
                print('Загрузка успешно осуществлена')
            else:
                print(f'Error {upload_put.status_code}')


if __name__ == '__main__':
    path_to_file = ...
    user_token = ...
    uploader = YaUploader(user_token)
    uploader.upload('/Netology_HW/test', path_to_file)
