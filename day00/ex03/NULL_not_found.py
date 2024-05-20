def NULL_not_found(object: any) -> int:

    if object is None:
        print("\033[0;33mNothing\033[0m:", object, type(object))

    elif isinstance(object, bool) and object is False:
        print("\033[0;33mFake\033[0m:", object, type(object))

    elif isinstance(object, float) and object != object:
        print("\033[0;33mCheese\033[0m:", object, type(object))

    elif isinstance(object, int) and object == 0:
        print("\033[0;33mZero\033[0m:", object, type(object))

    elif isinstance(object, str) and len(object) == 0:
        print("\033[0;33mEmpty\033[0m:", type(object))

    else:
        print("\033[0;31mType not found\033[0m")
        return (1)
    return (0)
