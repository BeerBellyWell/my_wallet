from src.wallet_manager import WalletManager


def main():
    try:
        manager = WalletManager()
        manager.add_record('доход', '1200', 'Зарплата')
        manager.add_record('расход', '400', 'Магазин')
        manager.balance()
        manager.edit('2024-05-12', 'расход')
        manager.search('зарплата')
    except Exception as e:
        print(f"Произошла ошибка: {e}")

if __name__ == '__main__':
    main()
