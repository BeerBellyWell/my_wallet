import src.constants as constants


def is_valid_category(category: str) -> bool:
    """
    Проверяет, входит ли категория в список допустимых категорий.
    
    Параметры:
        category (str): Категория для проверки.
    
    Возвращает:
        bool: Возвращает True, если категория в списке допустимых категорий, иначе False.
    """
    return category.lower() in constants.CATEGORIES


def is_valid_amount(amount: str) -> bool:
    """
    Проверяет, является ли строка допустимой суммой денег. Сумма должна быть положительным числом
    и может содержать максимум два знака после заяптой.
    
    Параметры:
        amount (str): Сумма в виде строки для проверки.
    
    Возвращает:
        bool: Возвращает True, если строка является допустимой суммой, иначе False.
    """
    try:
        amount = float(amount)
        return amount >= 0 and amount == round(amount, 2)
    except ValueError:
        return False
