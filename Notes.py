import json
import os
from datetime import datetime

# Программа: Заметки
class Note:

    def __init__(self, title, noteBody, datetime):
        self.title = title
        self.noteBody = noteBody
        self.datetime = datetime

    def printNote(self):
        print(f"Заголовок:  {self.title}   Заметка: {self.noteBody}    Время изменения:  {self.datetime}")

class ManagerNote:

    def __init__(self, file_path):
        self.file_path = file_path
        self.notes = []
        self.notesDatajson = dict(title=[], noteBody=[], datetime=[])

    def load_notes(self):
        with open(self.file_path, 'r') as file:
            f = os.stat(self.file_path)
            if f.st_size != 0:
                self.notesDatajson = json.load(file)
                for i in range(len(self.notesDatajson.get("title"))):
                    note = Note(self.notesDatajson["title"][i], self.notesDatajson["noteBody"][i], self.notesDatajson["datetime"][i])
                    self.notes.append(note)
    def safe_notes(self):
        with open(self.file_path, 'w') as file:
            self.notesDatajson = dict(title=[], noteBody=[], datetime=[])
            for i in range(len(self.notes)):
                self.notesDatajson["title"].append(self.notes[i].title)
                self.notesDatajson["noteBody"].append(self.notes[i].noteBody)
                self.notesDatajson["datetime"].append(str(self.notes[i].datetime))

            json.dump(self.notesDatajson, file)

    def add_note(self, note):
        self.notes.append(note)

    def delete_note(self, indexnote):
        self.notes.pop(indexnote)

    def edit_note(self, indexnote, new_title, new_noteBody):
        self.notes[indexnote].title = new_title
        self.notes[indexnote].noteBody = new_noteBody
        self.notes[indexnote].datetime = datetime.now()

manager = ManagerNote('Notes.json')
manager.load_notes()
a = str(manager.notes[0].datetime)
print(a.split())
print(a.split()[0].split("-"))
true = 1
while true == 1:
    print("Введите команду:")
    print("   Вывести на экран все заметки: print")
    print("   Добавить заметку: add")
    print("   Удалить заметку : del")
    print("   Редактировать заметку : edit")
    print("   Выбрать заметки по дате : select_date")

    inp = input()
    if (inp == "print"):
        true = -1
        for i in range(len(manager.notes)):
            manager.notes[i].printNote()
    elif (inp == "add"):
        true = -1
        title = input("Введите Заголовок: ")
        for el in manager.notes:
            if el.title == title:
                true = 0
        if  true == 0:
            true = -1
            print("Такой заголовок уже существует")
        else:
            true = -1
            noteBody = input("Введите текст Заметки: ")
            note = Note(title, noteBody, datetime.now())
            manager.add_note(note)
    elif (inp == "del"):
        true = -1
        title = input("Введите Заголовок удаляемой Заметки: ")
        for el in manager.notes:
            if el.title == title:
                manager.delete_note(manager.notes.index(el))
    elif (inp == "edit"):
        true = -1
        title = input("Введите существующий Заголовок: ")
        newtitle = input("Введите новый Заголовок: ")
        for el in manager.notes:
            if el.title == newtitle:
                true = 0
        if  true == 0:
            true = -1
            print("Такой заголовок уже существует")
        else:
            true = -1
            newnoteBody = input("Введите новый текст Заметки: ")
            for el in manager.notes:
                if el.title == title:
                    manager.edit_note(manager.notes.index(el),newtitle, newnoteBody)
    elif (inp == "select_date"):
        true = -1
        data = input("Введите дату последнего изменения Заметки в формате ДД.ММ.ГГГГ: ")
        datainput = data.split(".")
        for el in manager.notes:
            dat = str(el.datetime).split()[0].split("-")
            if dat[0] == datainput[2] and dat[1] == datainput[1] and dat[2] == datainput[0]:
                el.printNote()

    else:
        print("Неправильно введена команда")

manager.safe_notes()



