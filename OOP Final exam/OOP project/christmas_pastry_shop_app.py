from final_exam.ex_1_and_2.project.delicacies.gingerbread import Gingerbread
from final_exam.ex_1_and_2.project.delicacies.stolen import Stolen

from final_exam.ex_1_and_2.project.booths.open_booth import OpenBooth
from final_exam.ex_1_and_2.project.booths.private_booth import PrivateBooth


class ChristmasPastryShopApp:

    def __init__(self):
        self.booths = []
        self.delicacies = []
        self.income = 0

    def add_delicacy(self, type_delicacy: str, name: str, price: float):
        for delicacy in self.delicacies:
            if delicacy.name == name:
                raise Exception(f"{delicacy.name} already exists!")

        if type_delicacy != "Gingerbread" and type_delicacy != "Stolen":
            raise Exception(f"{type_delicacy} is not on our delicacy menu!")

        if type_delicacy == "Gingerbread":
            delicacy = Gingerbread(name, price)

        else:
            delicacy = Stolen(name, price)

        self.delicacies.append(delicacy)
        return f"Added delicacy {delicacy.name} - {type_delicacy} to the pastry shop."

    def add_booth(self, type_booth: str, booth_number: int, capacity: int):

        for booth in self.booths:
            if booth.booth_number == booth_number:
                raise Exception(f"Booth number {booth_number} already exists!")

        if type_booth != "Open Booth" and type_booth != "Private Booth":
            raise Exception(f"{type_booth} is not a valid booth!")

        if type_booth == "Open Booth":
            booth = OpenBooth(booth_number, capacity)
        else:
            booth = PrivateBooth(booth_number, capacity)

        self.booths.append(booth)
        return f"Added booth number {booth_number} in the pastry shop."

    def reserve_booth(self, number_of_people: int):

        current_booth = None

        for booth in self.booths:
            if booth.capacity >= number_of_people and not booth.is_reserved:
                current_booth = booth

                break

        if current_booth is None:
            raise Exception(f"No available booth for {number_of_people} people!")

        else:
            current_booth.is_reserved = True
            current_booth.reserve(number_of_people)
            return f"Booth {current_booth.booth_number} has been reserved for {number_of_people} people."

    def order_delicacy(self, booth_number: int, delicacy_name: str):

        try:
            booth = next(filter(lambda b: b.booth_number == booth_number, self.booths))

        except StopIteration:
            raise Exception(f"Could not find booth {booth_number}!")

        try:
            delicacy = next(filter(lambda d: d.name == delicacy_name, self.delicacies))

        except StopIteration:
            raise Exception(f"No {delicacy_name} in the pastry shop!")

        booth.delicacy_orders.append(delicacy)
        return f"Booth {booth.booth_number} ordered {delicacy.name}."

    def leave_booth(self, booth_number: int):

        booth = next(filter(lambda b: b.booth_number == booth_number, self.booths))

        bill = booth.price_for_reservation

        for delicacy in booth.delicacy_orders:
            print(delicacy.price)
            print(delicacy.portion)
            bill += delicacy.price

        self.income += bill

        booth.delicacy_orders = []
        booth.price_for_reservation = 0
        booth.is_reserved = False

        return f"Booth {booth.booth_number}:\n"\
               f"Bill: {bill:.2f}lv."

    def get_income(self):
        return f"Income: {self.income:.2f}lv."
