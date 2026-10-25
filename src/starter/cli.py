import argparse

from starter.core import greet


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="starter", description="Print a greeting.")
    parser.add_argument("name", nargs="?", default="World")
    args = parser.parse_args(argv)
    print(greet(args.name))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
