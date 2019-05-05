import argparse

# from luigi import build

from tasks.Author_add import import SQLATask


parser = argparse.ArgumentParser(description='Command description.')


def main(args=None):
    args = parser.parse_args(args=args)
    print(args.names)

    luigi.build([
        SQLATask(
        )], local_scheduler=True)
