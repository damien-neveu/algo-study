from tries.autocomplete import autocomplete
import unittest


class TestAutocomplete(unittest.TestCase):
    words = ["desole", "desolee", "dernier", "desolees", "desolation", "meunier", "dent"]

    def test_autocomplete_empty_string(self):
        self.assertEqual([], autocomplete("", TestAutocomplete.words))

    def test_autocomplete(self):
        self.assertEqual(["desole", "desolee", "desolees", "desolation"], autocomplete("des", TestAutocomplete.words))


if __name__ == "__main__":
    unittest.main()
