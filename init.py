import argparse
import configparser
import getpass

import git_actions


def _read_config():
    config = configparser.ConfigParser()
    config.read('config.ini')
    return config


def _argument_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-u', '--username', type=str, required=True)
    # parser.add_argument('-p', '--password', type=str, required=True)
    return parser.parse_args()


def _get_user_info(user_data):
    """
    :param user_data:
    :return:
    """
    for key, value in user_data.items():
        print(key, value, sep=': ')


def _get_usr_repos(repo_list):
    """
    :param repo_list:
    :return:
    """
    for repo in repo_list:
        print(repo['name'], repo['html_url'], sep=': ')


if __name__ == '__main__':
    config = _read_config()
    args = _argument_parser()

    password = getpass.getpass("Enter password for user {} ".format(args.username))

    endpoint = config['DEFAULT']['ENDPOINT']
    user_profile = config['DEFAULT']['USER_PROFILE']
    repos = config['DEFAULT']['REPOS']

    git_login = git_actions.login(endpoint, args.username, password)

    if git_login[0] != 200:
        print(git_login[1])
        exit()

    print(git_login[1])
    user_profile = git_actions.user_profile(user_profile, args.username)
    _get_user_info(user_profile.json())

    repos_list = git_actions.repos(repos, args.username)
    _get_usr_repos(repos_list.json())
