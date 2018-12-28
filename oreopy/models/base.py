import sqlite3

class Model:

    """ This is Base Model for all ORM Models """

    def __init__(self, **kwargs):

        try:
            conn = sqlite3.connect('sqlite.db')
            self.cursor = conn.cursor()
            create_table = 'CREATE TABLE {} ('.format(self.__get_class_name())

            for attr in self.__get_props():
                create_table += attr + ' ' + str(self.__class__.__dict__[attr]) + ', '
            
            create_table = create_table[:-2] + ')'

            self.cursor.execute(create_table)
            self.allow_kwargs = self.__get_props()


    def __get_class_name(self):
        return self.__class__.__name__


    def __get_props(self):
        return [i for i in self.__class__.__dict__.keys() if i[:1] != '_']


    def save(self):
        pass
