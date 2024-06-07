def callLimit(limit: int):
    """this function count the number of time she is call"""
    callLimit.count = 0

    def callLimiter(function):
        """this fonction call the limiter"""

        def limit_function(*args: any, **kwds: any):
            """this fonction check how many she has been
 calling and block it if needed"""
            if callLimit.count > limit:
                print("Error:", function, "call too may times")
                return
            function()
            callLimit.count += 1
        return limit_function
    return callLimiter


def main():
    return


if __name__ == "__main__":
    main()
