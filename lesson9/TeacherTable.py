from sqlalchemy import create_engine


class TeacherTable:

    # Добавляем для теста свои скрипты SQL

    __scripts = {
        "select": "select * from teacher",
        "add_new": "insert into teacher(teacher_id, email, group_id) values ('12133', 'teacher_inna@mail.com', '345')",
        "update": "update teacher set email = 'new-email@mail.com' where teacher_id = 12133",
        "delete by id": "delete from teacher where teacher_id = 12133",
    }

    def __init__(self, connection_string):
        self.__db = create_engine(connection_string)

    def get_teacher(self):
        return self.__db.execute(self.__scripts["select"]).fetchall()

    def add_teacher(self):
        return self.__db.execute(self.__scripts["add_new"])

    def update_teacher(self):
        return self.__db.execute(self.__scripts["update"])

    def delete(self):
        self.__db.execute(self.__scripts["delete by id"])
