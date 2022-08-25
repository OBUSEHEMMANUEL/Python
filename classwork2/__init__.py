def counter(iterable: list | str | tuple) -> dict:
    item_dict = {}

    for item in iterable:
        #  if item in item_dict:
        #     item_dict[item] += 1
        # else:
        #    item_dict[item] = 1

        # item_dict[item] = item_dict.get(item, 0) + 1

        item_dict[item] = iterable.count(item)

    return item_dict


print(counter("hello"))


def counter(iterable: list | str | tuple) -> dict:
    from collections import Counter

    # dict can be removed to print the largest first.
    return dict(Counter(iterable))


print(counter(input("ENTER WORD: ")))
