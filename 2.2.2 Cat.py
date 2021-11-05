class Cat:
    count_cats = 0

    def __init__(self, _age, _name="Kitty"):
        self._name = _name
        self._age = _age
        Cat.count_cats += 1

    def birthday(self):
        self._age += 1

    def get_age(self):
        if self._age == 1:
            print(f"{self._name} is {self._age} year old")
        else:
            print(f"{self._name} is {self._age} years old")

    def set_name(self, _newname):
        print(f"{self._name} now has a new name:")
        self._name = _newname
        print(self._name)


def main():
    tuli = Cat(0, "Tuli")
    lainey = Cat(10)

    print(tuli._age)

    tuli.birthday()
    tuli.get_age()
    lainey.get_age()
    lainey.set_name("Lainey")

    print(f"There are {Cat.count_cats} cats in the hood")


if __name__ == '__main__':
    main()
