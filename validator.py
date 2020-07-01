# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 18:57:27 2020

@author: 91976
"""
import argparse,sys,textwrap,logging
import re
class Passwd:
    def __init__(self,password):
        self.password=password
    def length_check(self):
        if len(self.password) < 8:
            logging.error("Password should contain atleast 8 Characters")
            return False
        else:
            return True
    def isUpper(self):
        if any([i for i in self.password if i.isupper()]):
            return True
        else:
            logging.error("Password should contain atleast 1 upper case letter")
            return False
    def isLower(self):
        if any([i for i in self.password if i.islower()]):
            return True
        else:
            logging.error("Password should contain atleast 1 lower case letter")
            return False
    def isAlnum(self):
            if any([i for i in self.password if i.isalnum()]):
                return True
            else:
                logging.error("Password should contain atleast alphanumeric characters")
            return False
                
    def isSpace(self):
        match=re.search('\s+',self.password)
        if match:
            logging.error('Password should not contain any whitespace character')
            return False
        else:
            return True
    def isSpecial(self):
        match=re.search('[~!@#$%^&*]+',self.password)
        if not match:
            logging.error('Password should  contain atleast 1 special character [~!@#$%^&*]')
            return False
        else:
            return True
if __name__=='__main__':
#argparse module
    parser=argparse.ArgumentParser(prog='validator',formatter_class=argparse.RawDescriptionHelpFormatter,
                                   description = textwrap.dedent('''\
        Password Validator Tool
        Following Rules to be followed:
        1. Length of password should be of at-least 8 characters
        2. At-least one uppercase character
        3. At-least one alpha-numeric character
        4. No whitespace character is allowed
        '''))
    requiredNamed=parser.add_argument_group('Required Named Argument')
    requiredNamed.add_argument('-p','--p',dest='password',
                               help='Please enter the password',required=True)
    args=parser.parse_args()
#logger
    logger=logging.getLogger()
    formatter = logging.Formatter('%(asctime)s - %(message)s', datefmt = '%d-%b-%y %H:%M:%S')
    filehandler=logging.FileHandler(filename='app1.log')
    filehandler.setFormatter(formatter)
    logger.setLevel(level=logging.INFO)
    
    streamhandler=logging.StreamHandler()
    streamhandler.setFormatter(formatter)
    logger.addHandler(filehandler)
    logger.addHandler(streamhandler)
    logger.info("Password entered by user :{}".format(args.password))
    
    logger.debug('Creating password validator object')
    pObj=Passwd(args.password)
    
    logger.debug('Checking whitespace character')
    if not pObj.isSpace():
        sys.exit(1)
    logger.debug('Checking password Length')
    if  not pObj.length_check():
        sys.exit(1)
    logger.debug("Checking for alpha-numeric character")
    if not pObj.isAlnum():
        sys.exit(1)
    logger.debug("Checking for uppercase character")
    if not pObj.isUpper():
        sys.exit(1)

    logger.debug("Checking for Special character")
    if not pObj.isSpecial():
        sys.exit(1)

    logger.info("Valid Password, All checks done!!")
    