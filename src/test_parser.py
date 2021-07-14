from unittest import TestCase
from src.parser import Record


class TestRecord(TestCase):
    def setUp(self):
        self.test_line = "315CL  432100020001SGXDC FUSGX NK    20100910JPY01B 0000000001 0000000000000000000060DUSD000000000030DUSD000000000000DJPY201008200012380     688032000092500000000             O"
        self.record = Record(self.test_line)

    def test_init(self):
        self.assertIsNotNone(self.record)

class TestClientInformation(TestRecord):

    def test_get_client_type(self):
        self.assertTrue("315", self.record.get_client_type())

    def test_get_client_number(self):
        self.assertTrue("4321", self.record.get_client_number())

    def test_get_client_acc(self):
        self.assertTrue("0002", self.record.get_client_acc())

    def test_get_client_subacc(self):
        self.assertTrue("0001", self.record.get_client_subacc())

class TestProductInformation(TestRecord):

    def test_get_product_group(self):
        self.assertTrue("FU", self.record.get_product_group())

    def test_get_exch_code(self):
        self.assertTrue("SGX", self.record.get_exch_code())

    def test_get_symbol(self):
        self.assertTrue("NK", self.record.get_symbol())

    def test_get_expiry_date(self):
        self.assertTrue("20100910", self.record.get_expiry_date())

    def test_get_ccy_code(self):
        self.assertTrue("JPY", self.record.get_ccy_code())

    def test_get_movement_code(self):
        self.assertTrue("01", self.record.get_movement_code())

    def test_get_buysell_code(self):
        self.assertTrue("B", self.record.get_buysell_code())

    def test_get_qty_long(self):
        self.assertTrue("0000000001", self.record.get_qty_long())

    def test_get_qty_short(self):
        self.assertTrue("000000000", self.record.get_qty_short())

    def test_get_transaction_price(self):
        self.assertEqual("9250.0000000", self.record.get_transaction_price())

    def test_get_transaction_date(self):
        self.assertTrue("20100820", self.record.get_transaction_date())

    def test_get_ticket_num(self):
        self.assertTrue("0", self.record.get_ticket_num())
