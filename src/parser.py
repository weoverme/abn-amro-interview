import logging
import time

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
    "QTY LONG": {
        "ref": 16,"length": 10, "char_start": 53, "char_end":62
    },
    "QTY SHORT": {
        "ref": 17,"length": 10, "char_start": 64, "char_end":73
    }
}

logging.basicConfig(filename="../log/parser.log", format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.WARNING)


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

        self.qty_long = self.get_qty_long()
        self.qty_short = self.get_qty_short()
        logging.info(f"Created new Transaction.")

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

    def get_qty_long(self):
        qty_long = MAPPING["QTY LONG"]
        return self.line[qty_long["char_start"]-1:qty_long["char_end"]]

    def get_qty_short(self):
        qty_short = MAPPING["QTY SHORT"]
        return self.line[qty_short["char_start"]-1:qty_short["char_end"]]

    def get_unique_client_information(self):
        return f"{self.client_type}_{self.client_number}_{self.client_acc}_{self.client_subacc}"

    def get_unique_product_information(self):
        return f"{self.exch_code}_{self.product_group}_{self.symbol}_{self.exp_date}"

    def calculate_net_total(self):
        net_total = int(self.get_qty_long()) - int(self.get_qty_short())
        return net_total


class Parser:

    def __init__(self, file_path):
        try:
            with open(file_path, "r") as file:
                self.f_transactions = file.readlines()
                logging.info(f"Opened '{file_path}'. There are {len(self.f_transactions)-1} transactions to be parsed.")

            self.client_transactions = {}
        except FileNotFoundError:
            logging.warning("Provided path is not a path.\n Try in format: \t\tparser.py path delimiter")

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
                logging.info(f"New client added to client transactions - {unique_client}")

            # Separate transaction by product
            product = t.get_unique_product_information()

            if not self.is_product_present(t):
                # If new, set product value = 0, as this should hold the net total
                self.client_transactions[unique_client][product] = 0
                logging.info(f"New product added to client transactions - {product}")

            self.client_transactions[unique_client][product] += t.calculate_net_total()

    def parse(self, outpath, delimiter):
        logging.info(f"Delimiter set to {delimiter}")
        self.calculate_total_transaction_amount()

        # Output to file
        with open(outpath, "w+") as f_output:
            f_output.write("CLIENT_INFORMATION%sPRODUCT_INFORMATION%sTOTAL_TRANSACTION_AMOUNT\n" % (delimiter, delimiter))
            for client in self.client_transactions.keys():
                for product in self.client_transactions[client].keys():
                    product_total_transaction_amount = self.client_transactions[client][product]
                    f_output.write(f"{client}{delimiter}{product}{delimiter}{product_total_transaction_amount}\n")
        logging.info(f"Completed writing to output - {outpath}. Please check output.")

if __name__ == "__main__":
    import sys

    try:
        fpath = sys.argv[1]
        outpath = sys.argv[2]
        delimiter = sys.argv[3]

        pr = Parser(fpath)

        pr.parse(outpath, delimiter)
    except IndexError:
        print("Parser.py was expecting three args. \nFormat: python parser.py path_input path_output delimiter\nEx. python parser.py ../res/Input.txt ../res/Output.csv ,")