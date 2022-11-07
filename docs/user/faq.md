# Frequently Asked Questions

## Which OS Config types have Parsers?

The documentation is provided in the [development docs](../../dev/dev_config/#current-included-parsers).

For creating new Parsers, see the [new parsers](../../dev/dev_config/#new-parsers) docs.

## Can you provide an example of how to use the functions?

The documentation is always provided in the function for [code docs](../../dev/code_reference/) for each function. There is additional documentation in [Use Cases](../lib_use_cases/) and subsequent sections.

## Optional Dependencies
One of the requirements of this library is to avoid having dependencies; however, including a few optional dependencies in an opt in fashion allows `netutils` to remain lean while offering some powerful addons.

Installing the optional dependencies is only needed when the user needs access to the functions using the dependencies. If the dependency is not installed the function simply raises an exception and warns the user that the library is not installed.
