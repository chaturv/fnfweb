import os


class AppProperties:
    def __init__(self):
        self.props = {}

        env = os.getenv('FNF_ENV')
        f_props = open('./properties/{env}.properties'.format(env=env), 'r')

        for line in f_props:
            splits = line.split('=')
            k = self._remove_newline(splits[0])
            v = self._remove_newline(splits[1])
            self.props[k] = v
        f_props.close()

    def get_db_credentials(self):
        f = open(self.props['USER_FILE_PATH'], 'r')
        self.props['USER'] = self._remove_newline(f.readline())
        f.close()

        f = open(self.props['PASSWORD_FILE_PATH'], 'r')
        self.props['PASSWORD'] = self._remove_newline(f.readline())
        f.close()

        return self.props

    def get_secret_key(self):
        f = open(self.props['SECRET_KEY_FILE_PATH'], 'r')
        return self._remove_newline(f.readline())

    def _remove_newline(self, x):
        return x.replace('\n', '')
