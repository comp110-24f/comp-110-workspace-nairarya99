"""Tea Party Planning"""

__author__ = "730745919"


def main_planner(guests: int) -> None:
    """total planning based on number of guests"""
    print(
        "A Cozy Tea Party for " + str(guests) + " People!"
    )  # prints first lines title statement and all must be str
    print(
        "Tea Bags: " + str(tea_bags(people=guests))
    )  # set people = to guests so that it can read the variable of people in tea_bag function
    print("Treats: " + str(treats(people=guests)))  # same as line 9
    print(
        "Cost: $"
        + str(
            cost(tea_count=tea_bags(people=guests), treat_count=treats(people=guests))
        )
    )  # when you are setting a function = to another you have to assign parameters to the original function


def tea_bags(people: int) -> int:
    """number of teabags for people attending"""
    return int(people * 2)  # this calls the teabags per person


def treats(people: int) -> int:
    """number of treats based on teabags"""
    return int(tea_bags(people=people) * 1.5)  # this calls treats per teabags


def cost(tea_count: int, treat_count: int) -> float:
    """cost of teabags and treats combined"""
    return float(tea_count * 0.5) + (
        treat_count * 0.75
    )  # teabags and treats times the indivual cost to find total


if __name__ == "__main__":
    main_planner(
        guests=int(input("How many guests are attending your tea party?"))
    )  # input shows what you want ur statment to ask, and guests=int shows what you are "plugging in" so you can get a value
