class Base62:
    def __init__(self):
        self.alphabets = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
        self.mapping = {v: i for i, v in enumerate(self.alphabets)}

    def encode_url(self, no):
        string = ''
        if no == 0:
            return '0'

        while no > 0:
            string = self.alphabets[no % 62] + string
            no = no // 62

        return string
