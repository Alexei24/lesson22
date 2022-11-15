from model.human import Human
from model.analyst import Analyst
from Util.convertor import Convertor
from Util.creator import HumanCreator




def main():
    ls = HumanCreator.create(5)
    print(Convertor.convert_to_string(ls))

    count_adults = Analyst.count_adults(ls)
    count_alive = Analyst.count_alive_people(ls)

    print(f"Count of adults: {count_adults}")
    print(f"Count of alive: {count_alive}")






if __name__ == "__main__":
    main()