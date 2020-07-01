Problem Statement:-

Write a Python Program to generate a logic for Password Validator.

Using Classes and Objects
Log all the Events
Write Positive and Negative Unit TestCases.
Steps:-

We have to take the input from user using ArgParse Module
Create Logging Configuration object for saving the Events.
Create PasswordValidator Class
Define all the methods - check_length(), check_uppercase(), check_alphanumeric(), check_special_character, check_whitespace_character()
Call all the methods for checking for Valid Password String.
Write all the Positive and Negative Test Cases for each of the methods defined.
Help File:-

(base) C:\Users\admin\PycharmProjects\PasswordValidator>python validator.py -h usage: validator [-h] -p PASSWORD

Password Validator Tool Following Rules to be followed:

Length of password should be of at-least 8 characters
At-least one uppercase character
At-least one alpha-numeric character
No whitespace character is allowed
optional arguments: -h, --help show this help message and exit

Required Named Argument.: -p PASSWORD, --p PASSWORD Please enter the Password

Execution:-

D:\Python_CodingNest\ProjectSol\PasswordValidator>python validator.py -p Hello@12
01-Jul-20 20:58:02 - Password entered by user :Hello@12
01-Jul-20 20:58:02 - Valid Password, All checks done!!

Test Case Execution:-

D:\Python_CodingNest\ProjectSol\PasswordValidator>python -m unittest test_validator.py -v
test_atleast_one_alphanumeric_character (test_validator.PasswordValidatorTest) ... ok
test_atleast_one_special_character (test_validator.PasswordValidatorTest) ... ok
test_atleast_one_uppercase_character (test_validator.PasswordValidatorTest) ... ok
test_atleast_one_whitespace_character (test_validator.PasswordValidatorTest) ... ERROR:root:Password should not contain any whitespace character
ok
test_invalid_password_length (test_validator.PasswordValidatorTest) ... ERROR:root:Password should contain atleast 8 Characters
ok
test_no_alphanumeric_character (test_validator.PasswordValidatorTest) ... ERROR:root:Password should contain atleast alphanumeric characters
ok
test_no_special_character (test_validator.PasswordValidatorTest) ... ERROR:root:Password should  contain atleast 1 special character [~!@#$%^&*]
ok
test_no_uppercase_character (test_validator.PasswordValidatorTest) ... ERROR:root:Password should contain atleast 1 upper case letter
ok
test_no_whitespace_character (test_validator.PasswordValidatorTest) ... ok
test_valid_password_length (test_validator.PasswordValidatorTest) ... ok

----------------------------------------------------------------------
Ran 10 tests in 0.010s

OK
