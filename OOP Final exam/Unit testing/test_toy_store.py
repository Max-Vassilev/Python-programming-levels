from final_exam.ex_3.toy_store import ToyStore
from unittest import TestCase, main


class ToyStoreTests(TestCase):
    def setUp(self):
        self.store = ToyStore()

    def test_initialization(self):

        shelf = {"A": None, "B": None, "C": None, "D": None, "E": None, "F": None, "G": None}

        self.assertEqual(shelf, self.store.toy_shelf)

    def test_add_toy_with_not_existing_shelf(self):
        with self.assertRaises(Exception) as ex:
            self.store.add_toy("H", "doll")

        self.assertEqual("Shelf doesn't exist!", str(ex.exception))

    def test_add_toy_where_toy_already_on_the_shelf(self):
        self.store.toy_shelf["A"] = "doll"

        with self.assertRaises(Exception) as ex:
            self.store.add_toy("A", "doll")

        self.assertEqual("Toy is already in shelf!", str(ex.exception))

    def test_add_toy_if_shelf_is_taken_by_some_other_toy(self):
        self.store.toy_shelf["A"] = "truck"

        with self.assertRaises(Exception) as ex:
            self.store.add_toy("A", "doll")

        self.assertEqual("Shelf is already taken!", str(ex.exception))

    def test_add_toy_expect_success(self):
        result = self.store.add_toy("A", "doll")

        self.assertEqual(result, "Toy:doll placed successfully!")

        shelf = {"A": "doll", "B": None, "C": None, "D": None, "E": None, "F": None, "G": None}
        self.assertEqual(shelf, self.store.toy_shelf)

    def test_remove_toy_if_the_shelf_does_not_exist(self):
        with self.assertRaises(Exception) as ex:
            self.store.remove_toy("H", "whatever")

        self.assertEqual("Shelf doesn't exist!", str(ex.exception))

    def test_remove_toy_if_the_toy_is_not_there(self):
        with self.assertRaises(Exception) as ex:
            self.store.remove_toy("A", "truck")

        self.assertEqual("Toy in that shelf doesn't exists!", str(ex.exception))

    def test_remove_toy_expect_success(self):
        self.store.toy_shelf["A"] = "doll"
        result = self.store.remove_toy("A", "doll")

        self.assertEqual(result, "Remove toy:doll successfully!")

        shelf = {"A": None, "B": None, "C": None, "D": None, "E": None, "F": None, "G": None}
        self.assertEqual(shelf, self.store.toy_shelf)


if __name__ == "__main__":
    main()
