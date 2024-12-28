from typing import Callable


def add_child(func: Callable):
    def wrapper(self, *args, **kwargs):
        result = func(self, *args, **kwargs)
        self.children.append(result)

        return result
    return wrapper


class Doctype:

    def __str__(self) -> str:
        return f"<!DOCTYPE html>"


class Html:

    def __init__(self, child: str) -> None:
        self.children = [child]

    def __str__(self) -> str:
        return f"<html>{self.children[0]}</html>"


class Head:

    def __str__(self) -> str:
        return "<head></head>"


class Body:

    def __init__(self, *args) -> None:
        self.children = list(args)

    def __str__(self) -> str:
        return f"<body>{''.join(map(lambda x: x.__str__(), self.children))}</body>"


class Meta:
    ...


class Title:

    def __init__(self, title="Dhtml") -> None:
        self.title = title

    def __str__(self) -> str:
        return f"<title>{self.title}</title>"


class H1:

    def __init__(self, text="") -> None:
        self.text = text

    def __str__(self) -> str:
        return f"<h1>{self.text}</h1>"


class H2:
    ...


html = Html(Body(H1("Hello World!"), H1("Hello Wanda Maximoff")))
print(html)
