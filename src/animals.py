def show_all_animals(animals: list) -> None:
        delimiter = "-" * 28
        template = "|{:<5}|{:<20}|"
        print(delimiter)
        for i, animal in enumerate(animals, start=1):
            print(template.format(i, animal))
        else:
            print(delimiter)

        print("\nНатисніть 'enter' для продовження\n")


def add_animal(animals: list) -> list:
        animal = input("\nВведіть нову тварину для додавання до списку: ")

        if animal in animals:
            print("\nТака тварина вже додана до цього списку")
        else:
            animals.append(animal)
            print("\nНова тварина була додана до списку")

            return animals


def add_animals(animals: list) -> list:
        anims = input("\nВведіть список тварин для вилікування через пробіл: \n").split()
        animals.extend(anims)
        print("\n Список тварин розширено")

        return animals


def exit():
    print("Дякую за вашу роботу. До наступної зустрічі")
    quit()


def del_anim_by_name(animals: list) -> list:
        animal = input("Введіть назву товару для видалення: ")

        if animal in animals:
            animals.remove(animal)
            print(f"\nТваринку '{animal}' видалено зі списку")
        else:
            print(f"\nТваринка '{animal}' відсутній у списку")

            return animals


def del_anim_by_numb(animals: list) -> list:
        number = input("Введіть номер товару для видалення: ")

        if number.isdigit() and 0 < int(number) <= len(animals):
            animal = animals.pop(int(number) - 1)
            print(f"\nТваринка '{animal}' видалена зі списку")
        else:
            print("\nВвели невірний номер")

            return animals


def sort_animals_by_name(animals: list) -> None:
        anims = sorted(animals)

        for i, anim in enumerate(anims, start=1):
            print(f"{i}: {anim}")

            print("\nСписок тваринок відсортовано")


def change_name_of_animal(animals: list) -> list:
        animal = input("Ввести ім'я тваринки зі списку: ")
        new_name = input("Ввсти ім'я тваринки: ")

        if animal in animals:
            index = animals.index(animal)
            animals[index] = new_name
            print(f"Ім'я тваринки '{animal}' буде змінено на '{new_name}'.\n")
        else:
            print(f"Такої тваринки '{animal}' в списку нема.\n")

        return animals


def find_numb_anim_by_name(animals: list) -> None:
        animal = input("Введіть назву тваринки: ")

        if animal in animals:
            index = animals.index(animal)
            print(f"Тваринка '{animal}' знаходиться під номером '{index +1 }'")
        else:
            print(f"Тваринка '{animal}' відсутній у списку")


def find_palindrome(animals: list) -> None:
        palin_prod = []
        for animal in animals:
            if animal.lower() == animal.lower()[::-1]:
                palin_prod.append(animal)

        print(f"Слова паліндроми:\n{palin_prod}\n.")

def show_animals_cured(animals_cured: list) -> None:
    print("\nСписок вилікуваних тваринок\n")
    for i, animal in enumerate(animals_cured, start=1):
        print(f"{i}: {animal}")


def history_cured_animals(animals_cured: list) -> None:
    anims_cured = animals_cured[::-1]

    if not anims_cured:
        print("\nСписок вилікуваних тваринок пустий\n")

    print("\nІсторія вилікуваних тваринок\n")
    for animal in anims_cured:
        print(animal)