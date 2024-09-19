"""Practice with conditionals"""


def get_ticket_price() -> int:
    age: int = int(input("What is your age?"))
    if (age <= 12) or (age > 60):
        price: int = 5
    else:
        price: int = 10
    return price


def less_than_10(num: int) -> None:
    """tell me if nm is < 10."""
    if num < 10:
        print("small number!")
    else:
        print("big number!")
    print("Have a nice day!")


def should_i_eat(hungry: bool) -> None:
    """Tells me whether or not to eat based on hunger."""
    if hungry:
        print("eat some food")
    else:
        print("stay in dorm and dont eat")  # elseblock
    print("proud of you!")


def check_first_letter(word: str, letter: str) -> str:
    """matching first letter or word to word"""
    if word[0] == letter:  # use==to use assigning in the body
        return "match"
    else:
        return "no match!"


print(check_first_letter(word="happy", letter="h"))
