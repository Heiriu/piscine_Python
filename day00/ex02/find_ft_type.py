def all_thing_is_obj(object: any) -> int:

    if isinstance(object, str):
        print(object, "is in the kitchen\033[0m :", type(object))

    elif isinstance(object, list):
        print("\033[0;33mList\033[0m :", type(object))

    elif isinstance(object, tuple):
        print("\033[0;33mTuple\033[0m :", type(object))

    elif isinstance(object, set):
        print("\033[0;33mSet\033[0m :", type(object))

    elif isinstance(object, dict):
        print("\033[0;33mDict\033[0m :", type(object))

    else:
        print("\033[0;31mType not found\033[0m")

    return (42)
