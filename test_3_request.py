from methods_api import get_username


def test_right_userdata_in_json(username):
    assert get_username() == username, 'Username is wrong'