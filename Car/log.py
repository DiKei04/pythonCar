import os
from datetime import datetime


class Log:
    def print_error(self, e, fn_desc):
        '''

        :param e:
        :param fn_desc:
        :return:
        '''
        now = datetime.now()
        os.chdir('C:\\Users\\karin\\PycharmProjects\\pythonProject\\Car')
        f = open('log.txt', 'a')
        f.writelines(f'\nError: {e}\nDescription:{fn_desc}\nDate:{now}')
        f.flush()
        f.close()

    def print_log(self, fn_desc):
        '''

        :param fn_desc:
        :return:
        '''
        now = datetime.now()
        f = open('log.txt', 'a')
        f.writelines(f'\nSuccess: {fn_desc}\nDate:{now}\n')
        f.flush()
        f.close()

    def print_in_txt(self, text):
        '''

        :param text:
        :return:
        '''
        now = datetime.now()
        os.chdir('C:\\Users\\karin\\PycharmProjects\\pythonProject\\Car')
        f = open('logTest.txt', 'a')
        f.writelines(f'\n Description: {text}  Date:{now}\n')
        f.flush()
        f.close()

