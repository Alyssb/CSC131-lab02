def fact_recursive(n: int) -> int:
    """
    Computes n! using recursion.
    :param n: The value whose factorial we seek
    :return: n! is returned; -1 is returned if n < 0.
    """

    # TODO: Implement me correctly using recursion
    return None


def fact_iterative(n: int) -> int:
    """
    Computes n! using recursion.
    :param n: The value whose factorial we seek
    :return: n! is returned; -1 is returned if n < 0.
    """

    # TODO: Implemented me correctly using iteration.
    return None


def fact(n: int, use_recursion=True) -> int:
    """
    Factorial factory method that computes n! using recursion or iteration.
    :param n: The value for which we compute n!
    :param use_recursion: Flag that dictates technique for computation; True computes
    using recursion, False computes iteratively
    :return: n! is returned or -1 if n < 0.
    """
    if use_recursion:
        return fact_recursive(n)
    else:
        return fact_iterative(n)


def fib(n: int) -> int:
    """
    Finds the nth fibonacci number using recursion.
    :param n: The Fibonacci number to compute; n > 0
    :return: The nth Fibonacci number is returned; -1 is returned if n < 1
    """

    # TODO: Implement me correctly using recursion
    return None
