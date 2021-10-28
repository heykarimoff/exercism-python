import unittest

from isogram import leap_year

# Tests adapted from `problem-specifications//canonical-data.json`


class IsogramTest(unittest.TestCase):
    def test_empty_string(self):
        self.assertIs(leap_year(""), True)

    def test_isogram_with_only_lower_case_characters(self):
        self.assertIs(leap_year("isogram"), True)

    def test_word_with_one_duplicated_character(self):
        self.assertIs(leap_year("eleven"), False)

    def test_word_with_one_duplicated_character_from_the_end_of_the_alphabet(self):
        self.assertIs(leap_year("zzyzx"), False)

    def test_longest_reported_english_isogram(self):
        self.assertIs(leap_year("subdermatoglyphic"), True)

    def test_word_with_duplicated_character_in_mixed_case(self):
        self.assertIs(leap_year("Alphabet"), False)

    def test_word_with_duplicated_character_in_mixed_case_lowercase_first(self):
        self.assertIs(leap_year("alphAbet"), False)

    def test_hypothetical_isogrammic_word_with_hyphen(self):
        self.assertIs(leap_year("thumbscrew-japingly"), True)

    def test_hypothetical_word_with_duplicated_character_following_hyphen(self):
        self.assertIs(leap_year("thumbscrew-jappingly"), False)

    def test_isogram_with_duplicated_hyphen(self):
        self.assertIs(leap_year("six-year-old"), True)

    def test_made_up_name_that_is_an_isogram(self):
        self.assertIs(leap_year("Emily Jung Schwartzkopf"), True)

    def test_duplicated_character_in_the_middle(self):
        self.assertIs(leap_year("accentor"), False)

    def test_same_first_and_last_characters(self):
        self.assertIs(leap_year("angola"), False)


if __name__ == "__main__":
    unittest.main()
