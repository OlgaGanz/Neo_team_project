# goitneo-python-final-project-group14

Проєкт "Assistant bot" створений для зберігання, редагування пощук контактної інформації та нотаток.

1. Модуль: Fields.py
Клас: Field
Конструктор: приймає значення для поля.

def __init__(self, value):
    self.value = value
Метод для перетворення об'єкта на рядок:

def __str__(self):
    return str(self.value)

2. Модуль: help_command.py
Клас: HelpCommand
Конструктор: приймає опис та команду.

def __init__(self, desc, cmd):
    self.desc = desc
    self.cmd = cmd

3. Модуль: Name.py
Клас: Name
Наслідується від класу Field.
Конструктор: перевіряє допустимість імені перед його зберіганням.

def __init__(self, name: str):
    Name.validate(name)
    super().__init__(name)

Статичний метод для валідації імені:
@staticmethod
def validate(name: str):
    if not name:
        raise IncorrectNameException("missing required name")

4. Модуль: Phone.py
Клас: Phone
Наслідується від класу Field.
Конструктор: перевіряє формат телефонного номера перед його зберіганням.

def __init__(self, value):
    if len(value) == 10 and value.isdigit():
        self.value = value
    else:
        raise IncorrectPhoneFormatException("Phone number must be 10 digits")

5. Модуль: Record.py
Цей клас представляє собою контактну інформацію людини.

Імпорти:
from Name import Name
from Phone import Phone
from Email import Email
from Birthday import Birthday
from Address import Address
Атрибути:
name: Об'єкт класу Name, що представляє ім'я контакту.
phones: Список телефонних номерів контакту.
email: Електронна адреса контакту.
birthday: День народження контакту.
address: Адреса контакту.
Методи:
Конструктор:
Ініціалізує об'єкт з іменем.

def __init__(self, name: Name):
    self.name = Name(name)
    self.phones: list[Phone] = []
    self.email: Email = None
    self.birthday: Birthday = None
    self.address: Address = None

Додавання телефону:
Додає новий телефонний номер до контакту.

def add_phone(self, phone):
    self.phones.append(Phone(phone))

Редагування телефону:
Змінює існуючий телефонний номер у контакті.

def edit_phone(self, old_phone, new_phone):
    for index, phone in enumerate(self.phones):
        if phone.value == old_phone:
            self.phones[index] = Phone(new_phone)
Видалення телефону:
Видаляє вказаний телефонний номер з контакту.

def remove_phone(self, phone_to_remove):
    self.phones = [phone for phone in self.phones if phone.value != phone_to_remove]

Встановлення дня народження:
Встановлює дату народження для контакту.

def set_birthday(self, year, month, day):
    self.birthday = Birthday(year, month, day)

Встановлення адреси:
Встановлює адресу для контакту.

def set_address(self, address: Address):
    self.address = address

Встановлення електронної пошти:
Встановлює електронну адресу для контакту.

def set_email(self, email: Email):
    self.email = email

Отримання списку телефонних номерів:
Повертає всі телефонні номери контакту у формі рядка.

def get_phones_list(self):
    return ";".join(p.value for p in self.phones)

Перетворення об'єкта на рядок:
Виводить детальну інформацію про контакт.

def __str__(self):
    details = [f"Name: {self.name}"]
    if self.phones:
        details.append(f"Phones: {', '.join([str(phone) for phone in self.phones])}")
    if self.email:
        details.append(f"Email: {self.email}")
    if self.birthday:
        details.append(f"Birthday: {self.birthday}")
    if self.address:
        details.append(f"Address: {self.address}")
    return "\n".join(details)

6. Модуль: Email.py
Клас: Email
Методи:

Конструктор:

def __init__(self, value: str):
    self.value = value

Перетворення об'єкта на рядок:

def __str__(self):
    return self.value

7. Модуль: Birthday.py
Клас: Birthday

Метод:
Конструктор:

def __init__(self, year: int, month: int, day: int):
    self.value = date(year, month, day)

8. Модуль: Address.py
Клас: Address
Методи:

Конструктор:

def __init__(self, value: str):
    self.value = value
Перетворення об'єкта на рядок:

def __str__(self):
    return self.value

9. Модуль: Book.py
Клас: AddressBook
Методи:

Конструктор:

def __init__(self):
    self.records = []

Додавання запису:

def add_record(self, record: Record):
    self.records.append(record)

Видалення запису:

def remove_record(self, name: Name):
    self.records = [record for record in self.records if record.name != name]

10. Модуль: Notes.py (в реалізації)


11. Avaliable commands:
┌────────────────────────────────────────────────────┬─────────────────────────────────────────────────────────────────────────────┐
│ Description                                        │ Command                                                                     │
╞════════════════════════════════════════════════════╪═════════════════════════════════════════════════════════════════════════════╡
│ Exit                                               │ 'close' or 'exit'                                                           │
├────────────────────────────────────────────────────┼─────────────────────────────────────────────────────────────────────────────┤
│ Start work                                         │ 'hello'                                                                     │
├────────────────────────────────────────────────────┼─────────────────────────────────────────────────────────────────────────────┤
│ Get help. List of available commands               │ 'help'                                                                      │
├────────────────────────────────────────────────────┼─────────────────────────────────────────────────────────────────────────────┤
│ Get help. Search commands by text                  │ 'help' {value to search}                                                    │
├────────────────────────────────────────────────────┼─────────────────────────────────────────────────────────────────────────────┤
│ Add new contact                                    │ 'add' {contact's name without spaces} {phone}                               │
├────────────────────────────────────────────────────┼─────────────────────────────────────────────────────────────────────────────┤
│ Remove existing contact                            │ 'remove {contact's name without spaces}                                     │
├────────────────────────────────────────────────────┼─────────────────────────────────────────────────────────────────────────────┤
│ Find contacts by value                             │ 'find' {value containing in any field}                                      │
├────────────────────────────────────────────────────┼─────────────────────────────────────────────────────────────────────────────┤
│ Add new phone to existing contact                  │ 'add-phone' {contact's name without spaces} {phone}                         │
├────────────────────────────────────────────────────┼─────────────────────────────────────────────────────────────────────────────┤
│ Remove all phones from existing contact            │ 'remove-phone' {contact's name without spaces}                              │
├────────────────────────────────────────────────────┼─────────────────────────────────────────────────────────────────────────────┤
│ Edit phone of existing contact                     │ 'edit' {contact's name without spaces} phone {new phone}                    │
├────────────────────────────────────────────────────┼─────────────────────────────────────────────────────────────────────────────┤
│ Add/edit email of existing contact                 │ 'edit' {contact's name without spaces} email {new email}                    │
├────────────────────────────────────────────────────┼─────────────────────────────────────────────────────────────────────────────┤
│ Remove email of existing contact                   │ 'get-phone' {contact's name without spaces}                                 │
├────────────────────────────────────────────────────┼─────────────────────────────────────────────────────────────────────────────┤
│ Add/edit birthday of existing contact              │ 'edit' {contact's name without spaces} birthday {date in format DD.MM.YYYY} │
├────────────────────────────────────────────────────┼─────────────────────────────────────────────────────────────────────────────┤
│ Get birthday of existing contact                   │ 'show-birthday' {contact's name without spaces}                             │
├────────────────────────────────────────────────────┼─────────────────────────────────────────────────────────────────────────────┤
│ Edit name of existing contact                      │ 'edit' {contact's name without spaces} name {new name}                      │
├────────────────────────────────────────────────────┼─────────────────────────────────────────────────────────────────────────────┤
│ Add address to existing contact                    │ 'add-address' {contact's name without spaces} {new address}                 │
├────────────────────────────────────────────────────┼─────────────────────────────────────────────────────────────────────────────┤
│ Edit address of existing contact                   │ 'edit' {contact's name without spaces} address {new address}                │
├────────────────────────────────────────────────────┼─────────────────────────────────────────────────────────────────────────────┤
│ Get list of contacts to be congratulated next week │ 'birthdays'                                                                 │
├────────────────────────────────────────────────────┼─────────────────────────────────────────────────────────────────────────────┤
│ Remove existing contact                            │ 'remove' {contact's name without spaces}                                    │
├────────────────────────────────────────────────────┼─────────────────────────────────────────────────────────────────────────────┤
│ Print all contacts                                 │ 'all'                                                                       │
└────────────────────────────────────────────────────┴─────────────────────────────────────────────────────────────────────────────┘
