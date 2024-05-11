import csv
import datetime as dt
from typing import List

import src.constants as constants
from src.validators import is_valid_category, is_valid_amount


class Record:
    """Класс представляет запись о финансах."""

    def __init__(self, category: str, amount: str, desc: str) -> None:
        self.date = dt.datetime.now().strftime('%Y-%m-%d')
        self.category = category.lower()
        self.amount = amount
        self.desc = desc.lower()

    def to_csv(self) -> List[str]:
        return [self.date, self.category, self.amount, self.desc]


class WalletManager:
    """Управляет записями о финансах, хранящимися в файле CSV."""

    def __init__(self, filename: str = 'my_wallet.csv') -> None:
        self.filename = filename

    def add_record(self, category: str, amount: str, desc: str) -> None:
        """
        Добавляет новую запись о финансах в файл CSV.
        Параметры:
            category (str): Категория транзакции (доход или расход).
            amount (str): Сумма транзакции.
            desc (str): Описание транзакции.
        """
        if not is_valid_category(category):
            print(constants.CATEGORY_ERROR.format(
                category=category, 
                categories=constants.CATEGORIES))
            return
        if not is_valid_amount(amount):
            print(constants.AMOUNT_ERROR)
            return

        record = Record(category, amount, desc)
        with open(self.filename, 'a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(record.to_csv())
        print(constants.ADD_SUCCESS)

    def balance(self) -> None:
        """
        Выводит общий баланс, сумму доходов и расходов из файла.
        """
        total_income = 0
        total_expense = 0

        try:
            with open(self.filename, 'r', newline='', encoding='utf-8') as file:
                reader = csv.reader(file)
                for row in reader:
                    if row[1] == 'доход':
                        total_income += float(row[2])
                    elif row[1] == 'расход':
                        total_expense += float(row[2])
                balance = total_income - total_expense
                print(f'Баланс: {balance}')
                if balance < 0:
                    print(constants.BALANCE_WARNING)
                print(f'Доходы: {total_income}')
                print(f'Расходы: {total_expense}')
        except FileNotFoundError:
            print(constants.FILE_NOT_FOUND)

    def edit(self, date: str, category: str) -> None:
        """
        Редактирует запись в файле по указанной дате и категории.
        Параметры:
            date (str): Дата записи для поиска.
            category (str): Категория записи для поиска.
        """
        records = []
        with open(self.filename, 'r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            records = list(reader)

        updated_records = []
        edited = False
        for row in records:
            if row[0] == date and row[1] == category:
                print(f'Найдена запись: {row}')
                new_amount = input('Введите новую сумму (оставьте пустым, чтобы оставить прежнее значение): ')
                new_desc = input('Введите новое описание (оставьте пустым, чтобы оставить прежнее значение): ')

                if new_amount and not is_valid_amount(new_amount):
                    print(constants.AMOUNT_ERROR)
                    continue
                if new_amount:
                    row[2] = new_amount
                if new_desc:
                    row[3] = new_desc

                edited = True
            updated_records.append(row)

        if edited:
            with open(self.filename, 'w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerows(updated_records)
            print(constants.RECORD_EDITED)
        else:
            print(constants.RECORD_NOT_FOUND)

    def search(self, item: str) -> None:
        """
        Поиск и вывод записей, содержащих заданное значение в любом из полей.
        Параметр:
            item (str): Строка поиска.
        """
        with open(self.filename, 'r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            for row in reader:
                if item.lower() in row[0].lower() or \
                   item.lower() in row[1].lower() or \
                   item.lower() in row[2].lower() or \
                   item.lower() in row[3].lower():
                    print(row)
