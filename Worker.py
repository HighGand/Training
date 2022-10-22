class Worker:
    workers = {}

    def __init__(self, nas, job, tw, eotc):
        self.nas = nas
        self.job = job
        self.tw = tw
        self.eotc = eotc

    def app(self):
        self.workers[self.nas] = [self.job, self.tw, self.eotc]

    def display(self):
        return self.workers

    def display_worker(self):
        k = input('Podaj imię i nazwisko pracownika, którego chcesz sprawdzić: ')
        if k in self.workers.keys():
            return f'Imię i nazwisko: {k}, Dział: {self.workers[k][0]}, Godziny pracy: {self.workers[k][1]}, Data ' \
                   f'końca umowy: {self.workers[k][2]} '

    # Napisać kod, ktróy robi następujące czynności:
    def change(self):
        for w in self.workers.keys():
            print(w)
        input('Wprowadź imię i nazwisko pracownika, któremu chcesz zmienić informacje: ')
        choice = input('Jakie informacje uległy zmianie: nazwisko, dział, godziny pracy, data końca umowy?')

        if choice == 'dział':
            self.workers[self.nas][0] = input('Do jakiego działu przenieść pracownika: ')
        elif choice == 'data końca umowy':
            self.workers[self.nas][2] = input('Podaj nową datę końca umowy: ')


w1 = Worker('Tymoty Budz', 'programer', 8, '2025-3-12')
w2 = Worker('Anna Kolas', 'HR', 8, '2024-3-12')
w3 = Worker('Jan Kowalski', 'programer architect', 8, 'no limit')

w1.app()
w2.app()
w3.app()


def main():
    while True:
        print('''Jaką z dostępnych opcji chcesz użyć:
                   1 - Wyświetl informację o wszystkich pracownikach
                   2 - Wyświetl informacje o wybranym pracowniku
                   3 - Zmień informację na temat pracownika
                   4 - Zakończ działanie programu''')

        choice = input('Podaj wartość: ')
        print()
        if choice == '1':
            print(w1.display())
            print()
        elif choice == '2':
            print(w1.display_worker())
            print()
        elif choice == '3':
            w1.change()
        elif choice == '4':
            print('Program zakończył swoje zadanie. Miłego dnia ;)')
            quit()


main()
