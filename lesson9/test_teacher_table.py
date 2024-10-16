from TeacherTable import TeacherTable

db = TeacherTable("postgresql://postgres:1234@localhost:5432/postgres")


def test_add_new_teacher():
    db.add_teacher()
    result = db.get_teacher()
    db.delete()
    assert result[-1] == (12133, 'teacher_inna@mail.com', 345)


def test_up_teacher():
    db.add_teacher()
    db.update_teacher()
    result = db.get_teacher()
    db.delete()
    assert result[-1] == (12133, 'new-email@mail.com', 345)


def test_delete_teacher():
    list_bef = db.get_teacher()
    db.add_teacher()
    list_af = db.get_teacher()
    db.delete()
    assert len(list_af) - len(list_bef) == 1
