import sqlite3

class DataBase:
    def __init__(self, debug = False):
        if debug:
            self.con = sqlite3.connect('database.db')
        else:
            self.con = sqlite3.connect('database/database.db')

    def close(self):
        self.con.close()

    def select(self, name_table: str, fields: list, condition: str = ''):
        cursor = self.con.cursor()
        for field in fields:
            field = f'`{field}`'
        if len(condition) > 0: condition = 'WHERE ' + condition
        cmd = f'SELECT {",".join(fields)} FROM {name_table} {condition}'
        cursor.execute(cmd)
        result = cursor.fetchall()
        self.con.commit()
        return result

    def insert(self, name_table: str, data: dict) -> int:
        cursor = self.con.cursor()
        fields = []
        values = []
        for key, value in data.items():
            fields.append(f'`{key}`')
            if type(value) is int:
                values.append(f'{value}')
            else:
                values.append(f'"{value}"')
        cmd = f'INSERT INTO `{name_table}` ({",".join(fields)}) VALUES ({",".join(values)})'
        try:
            cursor.execute(cmd)
            self.con.commit()
            return 0
        except Exception as ex:
            template = "An exception of type {0} occurred. Arguments:\n{1!r}"
            message = template.format(type(ex).__name__, ex.args)
            return 1

    def is_except(self, name_table: str, condition: str) -> bool:
        cursor = self.con.cursor()
        cmd = f'SELECT 1 FROM {name_table} WHERE {condition}'
        cursor.execute(cmd)
        result = cursor.fetchall()
        self.con.commit()
        return False if len(result) == 0 else True

    def update(self):
        pass

    def delete(self):
        pass
