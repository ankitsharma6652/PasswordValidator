import unittest
from validator import Passwd
class PasswordValidatorTest(unittest.TestCase):
    def test_valid_password_length(self):
        passObj=Passwd("Wel@1234")
        self.assertTrue(passObj.length_check())
    def test_invalid_password_length(self):
        passObj=Passwd("Wel234")
        self.assertFalse(passObj.length_check())
    def test_atleast_one_uppercase_character(self):
        passObj=Passwd("Wel@1234")
        self.assertTrue(passObj.isUpper())
    def test_no_uppercase_character(self):
        passObj=Passwd("abcdef123")
        self.assertFalse(passObj.isUpper())
    def test_atleast_one_alphanumeric_character(self):
        passObj=Passwd('Wel@1234')
        self.assertTrue(passObj.isAlnum())
    def test_no_alphanumeric_character(self):
        passObj=Passwd('!@#$%^&*!')
        self.assertFalse(passObj.isAlnum())
    def test_atleast_one_special_character(self):
        passObj=Passwd('Welco@1234')
        self.assertTrue(passObj.isSpecial())
    def test_no_special_character(self):
        passObj=Passwd('Welcome12')
        self.assertFalse(passObj.isSpecial())
    def test_no_whitespace_character(self):
        passObj=Passwd('Wel@1234')
        self.assertTrue(passObj.isSpace())
    def test_atleast_one_whitespace_character(self):
        passObj=Passwd('Wel 1234')
        self.assertFalse(passObj.isSpace())        