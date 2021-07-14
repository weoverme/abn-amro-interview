MAPPING = {
    2: {
        "name": "CLIENT TYPE", "length": 4, "char_start": 4, "char_end": 7
    },
    3: {
        "name": "CLIENT NAME","length": 4, "char_start": 8, "char_end":11
    },
    4: {
        "name": "ACCOUNT NUMBER","length": 4, "char_start": 12, "char_end":15
    },
    5: {
        "name": "SUBACCOUNT NUMBER","length": 4, "char_start": 16, "char_end":19
    },
    7: {
        "name": "PRODUCT GROUP CODE","length": 2, "char_start": 26, "char_end":27
    },
    8: {
        "name": "EXCHANGE CODE","length": 4, "char_start": 28, "char_end":31
    },
    9: {
        "name": "SYMBOL","length": 6, "char_start": 32, "char_end":37
    },
    11: {
        "name": "EXPIRY DATE","length": 8, "char_start": 38, "char_end":42
    },
    13: {
        "name": "CURRENCY CODE","length": 3, "char_start": 46, "char_end":48
    },
    14: {
        "name": "MOVEMENT CODE","length": 2, "char_start": 49, "char_end":50
    },
    16: {
        "name": "QTY LONG","length": 10, "char_start": 53, "char_end":62
    },
    17: {
        "name": "QTY SHORT","length": 10, "char_start": 64, "char_end":73
    },
    20: {
        "name": "TRANSACTION PRICE","length": 15, "char_start": 148, "char_end":162
    },
    37: {
        "name": "TICKET NUMBER","length": 37, "char_start": 136, "char_end":141
    }
}

import sys

fpath = sys.argv[1]

class Record:
    def __init__(self, fread):
        file = fread

    def get_client_info(self):
        c_name = self.file[MAPPING[2]["char_start":"char_end"]]
