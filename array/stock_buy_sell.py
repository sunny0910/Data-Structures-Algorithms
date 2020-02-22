def stock_buy_sell(a, n):
    """
    Function to determine buying and selling of stocks to maximize profits.
    It finds local minima first and then local maxima from the next index and repeats the process of index has not
    reached to the end of array.
    Local Minima: the element which is lower than the next element
    Local Maxima: the element which is higher than the next element and previous element
    :param a: List
    :param n: Int
    :return: None
    """
    if n == 1:
        return
    i = 0
    while i < n-1:

        while i < n-1 and a[i+1] <= a[i]:
            i += 1
        if i == n-1:
            break
        buy = i
        i += 1

        while i < n and a[i-1] <= a[i]:
            i += 1
        sell = i-1

        print("Buy on day {0}, sell on day {1}".format(buy, sell))


price = [100, 180, 260, 310, 40, 535, 695]
days = len(price)
stock_buy_sell(price, days)
