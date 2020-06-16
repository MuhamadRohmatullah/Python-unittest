
import unittest

inputan = int(input("Masukan input:"))

 if inputan >= 21 :
     print("DEWASA")
 elif inputan >= 13 :
     print("REMAJA")
 elif inputan >= 9 :
    print("BIMBINGAN ORANG TUA")
 elif inputan < 9 :
     print("SEMUA USIA")
     
class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == '__main__':
    unittest.main()

