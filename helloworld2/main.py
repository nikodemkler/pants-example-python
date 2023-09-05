# Copyright 2020 Pants project contributors.
# Licensed under the Apache License, Version 2.0 (see LICENSE).

from colors import green

from helloworld2.foo.greeting import Greeter


def say_hello_2() -> None:
    greeting = Greeter().greet("Pantsbuild")
    print(green(greeting))


if __name__ == "__main__":
    say_hello_2()
