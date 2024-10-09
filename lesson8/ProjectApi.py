import requests
import requests.auth


class ProjectApi:

    def __init__(self, url):
        self.url = url

    def bearer_auth(
            self,
            login='',       # введите логин
            password=''     # введите пароль
            ):
        profil = {
            'login': login,
            'password': password
        }

        auth_profil = requests.post(
            self.url+'/api-v2/auth/companies', json=profil)
        id_company = auth_profil.json()
        id_comp = id_company['content'][0]['id']

        body_key = {
            'login': login,
            'password': password,
            'companyId': id_comp
        }

        my_key = requests.post(
            self.url+'/api-v2/auth/keys/get',
            json=body_key
            )
        return my_key.json()[0]['key']

    def my_headers_key(self):
        my_headers = {}
        key_header = self.bearer_auth()
        my_headers = {
            "Content-Type": "application/json",
            "Authorization": "Bearer " + key_header
            }
        return my_headers

    def create_project(self, title):
        name_project = {"title": title}
        new_project = requests.post(
            self.url + "/api-v2/projects",
            json=name_project,
            headers=self.my_headers_key()
            )
        return new_project.json()

    def get_project(self):
        get_project = requests.get(
            self.url + "/api-v2/projects",
            headers=self.my_headers_key()
            )
        return get_project.json()

    def get_project_id(self, id):
        get_project_id = requests.get(
            self.url + "/api-v2/projects/" + str(id),
            headers=self.my_headers_key()
            )
        return get_project_id.json()

    def put_project_id(self, title, id):
        new_name = {"title": title}
        put_project_id = requests.put(
            self.url + "/api-v2/projects/" + str(id),
            json=new_name,
            headers=self.my_headers_key()
            )
        return put_project_id.json()
