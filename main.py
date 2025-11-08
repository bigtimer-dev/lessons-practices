import functools


def main(doc_so_far, sentence):
    return functools.reduce(
        lambda doc_so_far, sentence: f"{doc_so_far}. " + f"{sentence}", sentence
    )


if __name__ == "__main__":
    print(main("hello", "my name is alvin"))
