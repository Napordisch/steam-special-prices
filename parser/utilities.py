import re


def to_kebab_case(string:str) -> str:
    return '-'.join(
        map(lambda word: word.lower(),
            re.findall("(\\w+)", string
                       .replace("'", "")
                       .replace("+", "plus")))
    )



if __name__ == "__main__":
    print(to_kebab_case("No Man's sky"))