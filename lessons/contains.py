"""Example of a function that processes a list."""


def main() -> None:
    names: list[str] = ["Alayna", "Lorenzana"]
    print(contains("Alayna", names))


def contains(needle: str, haystack: list[str]) -> bool:
    """Return True if needle is found in haystack, False otherwise."""
    i: int = 0
    while i < len(haystack):
        if haystack[i] == needle:
            return True
        i += 1
    return False


if __name__ == "__main__":
    main()