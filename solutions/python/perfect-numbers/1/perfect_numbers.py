def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    if number < 1:
        raise ValueError("Classification is only possible for positive integers.")
    ali_sum = 0

    for factor in range(1, number):
        if number % factor == 0:
            ali_sum += factor

    if ali_sum == number:
        return 'perfect'
    if ali_sum > number:
        return 'abundant'
    return 'deficient'