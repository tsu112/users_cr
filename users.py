from unittest import result
from winreg import QueryInfoKey
from mysqlconnection import connectToMySQL  # connects my database


class User:
    def __init__(self, data):
        self.id = data['id']
        self.f_name = data['f_name']
        self.l_name = data['l_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls):
        query = "select * from users"
        results = connectToMySQL('users').query_db(query)
        users = []
        for row in results:
            users.append(cls(row))
        return users
        #

    @classmethod
    def create(cls, data):
        query = "INSERT INTO users (f_name, l_name, email) VALUES ( %(f_name)s, %(l_name)s, %(email)s);"
        result = connectToMySQL('users').query_db(query, data)
        return result
        # This is the function that will allow to add the new user to the table

    @classmethod
    def update(cls, data):
        query = "UPDATE users SET f_name = %(f_name)s, l_name = %(l_name)s, email = %(email)s WHERE id = %(id)s"
        results = connectToMySQL('users').query_db(query, data)
        return results
