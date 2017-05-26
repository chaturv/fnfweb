import os


def get_db_credentials():
    env = os.getenv('FNF_ENV')
    f_props = open('./properties/{env}.properties'.format(env=env), 'r')
    props = {}
    for line in f_props:
        splits = line.split('=')
        k = splits[0].replace('\n', '')
        v = splits[1].replace('\n', '')
        props[k] = v
    f_props.close()

    f_user_file = open(props['USER_FILE_PATH'], 'r')
    props['USER'] = f_user_file.readline().replace('\n', '')
    f_user_file.close()

    f_passwd_file = open(props['PASSWORD_FILE_PATH'], 'r')
    props['PASSWORD'] = f_passwd_file.readline().replace('\n', '')
    f_passwd_file.close()

    return props
