class Utils(object):
    def __init__(self, func):
        self.func = func

    def id(self):
        return Utils(self.func['id'])

    def data(self):
        return Utils(self.func['data'])

    def __repr__(self):
        return repr(self.func)

    def __getitem__(self, item):
        return Utils(self.func[item])

    def __setitem__(self, key, value):
        k = self.func[key] = value

        return k


