import unittest
from my_program import make_it_uppercase, get_first_word, return_a_list


class TestMyProgram(unittest.TestCase):

    def test_hello_world(self):
        result = make_it_uppercase("hello world")
        self.assertEqual(result, "HELLO WORLD")


    def test_first_word_in_sentence(self):
        sentence = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley"
        result = get_first_word(sentence)
        self.assertEqual(result, "Lorem")

    def test_first_word_in_sentence_with_on_word(self):
        sentence = "Lorem"
        result = get_first_word(sentence)
        self.assertEqual(result, "Lorem")

    def test_return_a_list(self):
        result = return_a_list()
        self.assertListEqual(
            result,
            ['Cats', 'Dogs', 'Birds'], "The LIST was wrong!")


if __name__ == "__main__":
    unittest.main()
