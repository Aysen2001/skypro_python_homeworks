import pytest
from ProjectApi import ProjectApi

api = ProjectApi("https://ru.yougile.com")


# GET /api-v2/projects - получить список


def test_positive_get_proj():
    get_project = api.get_project()
    get_proj = len(get_project)
    assert get_proj == 2


@pytest.mark.xfail
def test_negative_get_proj():
    get_project = api.get_project()
    get_proj = len(get_project)
    assert get_proj == 0


# POST /api-v2/projects - создать проект


def test_positive_cr_proj():
    list_bef = api.get_project()
    len_bef_project = list_bef["paging"]["count"]

    title = "Создать новый проект"
    api.create_project(title)

    list_af = api.get_project()
    len_af_project = list_af["paging"]["count"]

    assert len_af_project - len_bef_project == 1


@pytest.mark.xfail
def test_negative_cr_proj():
    list_bef = api.get_project()
    len_bef_project = list_bef["paging"]["count"]

    title = ""
    api.create_project(title)

    list_af = api.get_project()
    len_af_project = list_af["paging"]["count"]

    assert len_af_project - len_bef_project == 1


# GET /api-v2/projects/{id} - получить проект по id


def test_positive_get_proj_id():
    title = "Проект с новым id"
    id_proj_new = api.create_project(title)
    id = id_proj_new["id"]
    project_id = api.get_project_id(id)

    assert project_id["id"] == id
    assert project_id["title"] == title


@pytest.mark.xfail
def test_negative_get_proj_id():
    title = "Проект с новым другим id"
    id_proj_new = api.create_project(title)
    id = id_proj_new["id"]
    project_id = api.get_project_id(id)

    assert project_id["id"] == "123"
    assert project_id["title"] == "Ошибочное название"


# PUT /api-v2/projects/{id} - изменить проект по id


def test_positive_put_proj_id():
    title = "Новый проект для смены названия"
    new_proj = api.create_project(title)
    id = new_proj["id"]

    title = "Меняем название"
    put_proj_id = api.put_project_id(title, id)

    my_proj = api.get_project_id(id)

    assert put_proj_id["id"] == id
    assert my_proj["title"] == "Меняем название"


@pytest.mark.xfail
def test_negative_put_proj_id():
    title = "Новый проект для смены названия"
    new_proj = api.create_project(title)
    id = new_proj["id"]

    title = "Меняем название"
    api.put_project_id(title, id)

    my_proj = api.get_project_id(id)

    assert my_proj["title"] == "Новый проект для смены названия"
