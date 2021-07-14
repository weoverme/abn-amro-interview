MAPPING = {
    "CLIENT TYPE": {
        "ref":2, "length": 4, "char_start": 4, "char_end": 7
    },
    "CLIENT NUMBER": {
        "ref":3,"length": 4, "char_start": 8, "char_end":11
    },
    "ACCOUNT NUMBER": {
        "ref": 4,"length": 4, "char_start": 12, "char_end":15
    },
    "SUBACCOUNT NUMBER": {
        "ref": 5,"length": 4, "char_start": 16, "char_end":19
    },
    "PRODUCT GROUP CODE": {
        "ref": 7,"length": 2, "char_start": 26, "char_end":27
    },
    "EXCHANGE CODE": {
        "ref": 8,"length": 4, "char_start": 28, "char_end":31
    },
    "SYMBOL": {
        "ref": 9,"length": 6, "char_start": 32, "char_end":37
    },
    "EXPIRY DATE": {
        "ref": 11,"length": 8, "char_start": 38, "char_end":45
    },
    "CURRENCY CODE": {
        "ref": 13,"length": 3, "char_start": 46, "char_end":48
    },
    "BUY SELL CODE": {
        "ref": 15,"length": 1, "char_start": 51, "char_end":51
    },
    "MOVEMENT CODE": {
        "ref": 14,"length": 2, "char_start": 49, "char_end":50
    },
    "QTY LONG": {
        "ref": 16,"length": 10, "char_start": 53, "char_end":62
    },
    "QTY SHORT": {
        "ref": 17,"length": 10, "char_start": 64, "char_end":73
    },
    "TRANSACTION PRICE": {
        "ref": 20,"length": 15, "char_start": 148, "char_end":162
    },
    "TRANSACTION DATE": {
        "ref": 34,"length": 8, "char_start": 122, "char_end":129
    },
    "TICKET NUMBER": {
        "ref": 37,"length": 37, "char_start": 136, "char_end":141
    }
}

import sys

# fpath = sys.argv[1]

class Transaction:
    """
    A transaction that must be cleared and reconciled for trade settlement.
    :param f_line:
    """
    def __init__(self, f_line):
        self.line = f_line
        self.client_type = self.get_client_type()
        self.client_number = self.get_client_number()
        self.client_acc = self.get_client_acc()
        self.client_subacc = self.get_client_subacc()

        self.product_group = self.get_product_group()
        self.exch_code = self.get_exch_code()
        self.exp_date = self.get_expiry_date()
        self.symbol = self.get_symbol()
        self.ccy_code = self.get_ccy_code()

        self.buysell_code = self.get_buysell_code()
        self.movement_code = self.get_movement_code()
        self.qty_long = self.get_qty_long()
        self.qty_short = self.get_qty_short()

        self.transaction_price = self.get_transaction_price()
        self.transaction_date = self.get_transaction_date()

    def get_client_type(self):
        c_type = MAPPING["CLIENT TYPE"]
        return self.line[c_type["char_start"]-1:c_type["char_end"]].strip(" ")

    def get_client_number(self):
        c_number = MAPPING["CLIENT NUMBER"]
        return self.line[c_number["char_start"]-1:c_number["char_end"]].strip(" ")

    def get_client_acc(self):
        c_acc = MAPPING["ACCOUNT NUMBER"]
        return self.line[c_acc["char_start"]-1:c_acc["char_end"]].strip(" ")

    def get_client_subacc(self):
        c_subacc = MAPPING["SUBACCOUNT NUMBER"]
        return self.line[c_subacc["char_start"]-1:c_subacc["char_end"]].strip(" ")

    def get_product_group(self):
        product_group = MAPPING["PRODUCT GROUP CODE"]
        return self.line[product_group["char_start"]-1:product_group["char_end"]].strip(" ")

    def get_exch_code(self):
        exch_code = MAPPING["EXCHANGE CODE"]
        return self.line[exch_code["char_start"]-1:exch_code["char_end"]].strip(" ")

    def get_symbol(self):
        symbol = MAPPING["SYMBOL"]
        return self.line[symbol["char_start"]-1:symbol["char_end"]].strip(" ")

    def get_expiry_date(self):
        c_expiry = MAPPING["EXPIRY DATE"]
        return self.line[c_expiry["char_start"]-1:c_expiry["char_end"]].strip(" ")

    def get_ccy_code(self):
        t_ccy = MAPPING["CURRENCY CODE"]
        return self.line[t_ccy["char_start"]-1:t_ccy["char_end"]].strip(" ")

    def get_buysell_code(self):
        buysell = MAPPING["BUY SELL CODE"]
        return self.line[buysell["char_start"]-1].strip(" ")

    def get_movement_code(self):
        movement = MAPPING["MOVEMENT CODE"]
        return self.line[movement["char_start"]-1:movement["char_end"]].strip(" ")

    def get_qty_long(self):
        qty_long = MAPPING["QTY LONG"]
        return self.line[qty_long["char_start"]-1:qty_long["char_end"]]

    def get_qty_short(self):
        qty_short = MAPPING["QTY SHORT"]
        return self.line[qty_short["char_start"]-1:qty_short["char_end"]]

    def get_transaction_date(self):
        t_date = MAPPING["TRANSACTION DATE"]
        return self.line[t_date["char_start"]-1:t_date["char_end"]].strip(" ")

    def get_transaction_price(self):
        t_price = MAPPING["TRANSACTION PRICE"]
        return "{:.7f}".format(int(self.line[t_price["char_start"]-1:t_price["char_end"]])/10000000)

    def get_ticket_num(self):
        ticket_num = MAPPING["TICKET NUMBER"]
        return self.line[ticket_num["char_start"]-1:ticket_num["char_end"]].strip(" ")

    def get_unique_client_information(self):
        return "%s_%s_%s_%s" % (self.client_type, self.client_number, self.client_acc, self.client_subacc)

    def get_unique_product_information(self):
        return "%s_%s_%s_%s" % (self.exch_code, self.product_group, self.symbol, self.exp_date)

    def calculate_net_total(self):
        net_total = int(self.get_qty_long()) - int(self.get_qty_short())
        return net_total


class Parser:

    def __init__(self, file_path):
        self.f_transactions = open(file_path, "r").readlines()
        self.client_transactions = {} # transactions grouped by unique combination of client type, number, acc, subacc

    def is_client_present(self, t):
        unique_client = t.get_unique_client_information()

        if unique_client in self.client_transactions.keys():
            return True
        return False

    def is_product_present(self, t):
        unique_client = t.get_unique_client_information()
        product = t.get_unique_product_information()

        if product in self.client_transactions[unique_client].keys():
            return True
        return False

    def is_transaction_date_present(self, t):
        unique_client = t.get_unique_client_information()
        product = t.get_unique_product_information()

        if t.transaction_date in self.client_transactions[unique_client][product].keys():
            return False
        return True

    def calculate_total_transaction_amount(self):
        # Separate transaction by client
        for line in self.f_transactions:
            t = Transaction(line)
            unique_client = t.get_unique_client_information()

            if not self.is_client_present(t):
                # If new, set unique_client dict up
                self.client_transactions[unique_client] = {}

            # Separate transaction by product
            product = t.get_unique_product_information()

            if not self.is_product_present(t):
                # If new, set product value = 0, as this should hold the net total
                self.client_transactions[unique_client][product] = 0

            self.client_transactions[unique_client][product] += t.calculate_net_total()

    def parse(self, delimiter):
        self.calculate_total_transaction_amount()

        # Gather output data
        output_header = "CLIENT_INFORMATION%sPRODUCT_INFORMATION%sTOTAL_TRANSACTION_AMOUNT\n" %(delimiter, delimiter)
        output = ""
        for client in self.client_transactions.keys():
            for product in self.client_transactions[client].keys():
                product_total_transaction_amount = self.client_transactions[client][product]
                output += "%s%s%s%s%s\n" %(client, delimiter, product, delimiter, product_total_transaction_amount)

        # Output to file
#        f_output = open("../res/Output.txt", "w+")
        print(output)

if __name__ == "__main__":
    path = "../res/Input.txt"
    pr = Parser(path)
    #pr.calculate_total_transaction_amount()

    for k in pr.client_transactions.keys():
        total = 0
        for v in pr.client_transactions[k]:
            attrs = vars(v)
            print(', '.join("%s: %s" % item for item in attrs.items()))

        break
            #
            # print(v.client_type, v.client_number, v.acc)
            # total += v.calculate_net_total()
            # print("%s - %s" %(v.buysell_code, v.calculate_net_total()))
        # print("Key: %s, Values: %s" %(k, total))

    pr.parse(",")
