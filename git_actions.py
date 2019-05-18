import requests


def login(endpoint, username, password):
    """
    :param endpoint:
    :param username:
    :param password:
    :return:
    """
    login = requests.get(endpoint, auth=(username, password))
    if login.status_code != 200:
        return login.status_code, 'Bad Credentials!!'
    else:
        return login.status_code, 'Authorization Successful!!'


def user_profile(current_user_url, username):
    """
    :param current_user_url:
    :param username:
    :return:
    """
    return requests.get(current_user_url.replace('{user}', '') + username)


def repos(user_repo_url, username):
    """
    :param user_repo_url:
    :param username:
    :return:
    """
    return requests.get(user_repo_url.replace('{user}', username))
