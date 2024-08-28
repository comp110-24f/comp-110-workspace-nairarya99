"""First Function Challenge Question"""

__author__ = "730745919"


def mimic(message: str) -> str:
    """repeat message back"""
    return message


def main() -> None:
    """print result of calling mimic"""
    print(mimic(message=input("What is your message?")))


if __name__ == "__main__":
    main()
