def greet(name: str) -> str:
    return f"Hello, {name}! 👋"


def calculate_sum(a: int, b: int) -> int:
    return a + b


def main():
    name = "World"
    result = calculate_sum(3, 5)

    print(greet(name))
    print(f"3 + 5 = {result}")
    print("This Python file ran successfully.")


if __name__ == "__main__":
    main()
