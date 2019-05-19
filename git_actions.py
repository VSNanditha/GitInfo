import requests
from requests.auth import HTTPBasicAuth


def login(endpoint, username, password):
    """
    :param endpoint: endpoint url
    :param username: github userid
    :param password: github password
    :return: login request status code and message
    """
    login = requests.get(endpoint, auth=HTTPBasicAuth(username, password))
    if login.status_code != 200:
        return login.status_code, 'Bad Credentials!!'
    else:
        return login.status_code, 'Authorization Successful!!'


def user_profile(current_user_url, username):
    """
    :param current_user_url: endpoint to user profile
    :param username: github userid
    :return: user profile data
    """
    return requests.get(current_user_url.replace('{user}', '') + username)


def repos(user_repo_url, username):
    """
    :param user_repo_url: endpoint to user repository list
    :param username: github username
    :return: user repository list
    """
    return requests.get(user_repo_url.replace('{user}', username))
