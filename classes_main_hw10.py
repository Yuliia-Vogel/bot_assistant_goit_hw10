from collections import UserDict


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)
    

class Name(Field):
    pass
    

class Phone(Field):
    def __init__(self, value): # phone number validation
        self.value = value
        if len(value) != 10:
            print('Incorrect lenght of number')
            raise ValueError
        elif value.isdigit() == False:
            print('Number should be digits only')
            raise ValueError
        else:
            return None


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

    def add_phone(self, phone):
        self.phone = Phone(phone)
        self.phones.append(self.phone)
        for i in self.phones:
            print(i)

    def edit_phone(self, old_phone, new_phone):
        for index, number in enumerate(self.phones):
            if number.value == old_phone:
                self.phones[index] = Phone(new_phone)
                print(f'old number {old_phone} changed to new one {new_phone}')
                return 
        print("phone to edit not exist")
        raise ValueError
        

    def find_phone(self, phone):
        for number in self.phones:
            if number.value == phone:
                print(f'I found necessary number {number.value}')
                return number
            else: 
                pass
        print('phone not found')
        raise ValueError

    def remove_phone(self, phone):
        for number in self.phones:
            if number.value == phone:
                self.phones.remove(number)
                print(f'{number} removed')


class AddressBook(UserDict):
    def add_record(self, record: Record):
        self.data[record] = record

    def find(self, name_to_find):
        for record in self.data:
            if record.name.value != name_to_find:
                pass
            elif record.name.value == name_to_find:
                print(f'{record} found')
                return record
        return None

    def delete(self, name):
        try: 
            name_to_delete = self.find(name)
            self.data.pop(name_to_delete)
            print(self.data)
        except ValueError:
            print('such phone to delete not found')