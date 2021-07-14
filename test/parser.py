import unittest
from src.parser import Record


class MyTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDown(cls):
        pass

    def setUp(self):
        self.test_value = "315CL  432100020001SGXDC FUSGX NK    20100910JPY01B 0000000001 0000000000000000000060DUSD000000000030DUSD000000000000DJPY201008200013350     689458000092150000000             O"

    def tearDown(self):
        pass



if __name__ == '__main__':
    unittest.main()
