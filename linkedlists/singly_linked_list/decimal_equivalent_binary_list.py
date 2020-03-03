from singly_linked_list import LinkedList

class DecimalEquivalent(LinkedList):

    def decimal_equivalent(self):
        """
        Function to get the decimal equivalent of a binary number represented by a linked list
        It fetches the number from linked list to a array and applies the decimal to binary conversion on the list.
        :return: Int
        """
        if not self.head:
            return 0
        numbers = []
        temp = self.head
        while temp:
            numbers.append(temp.data)
            temp = temp.next
        n = len(numbers) - 1
        decimal = 0
        for index, number in enumerate(numbers):
            if number == 1:
                decimal += 2**(n-index)
        return decimal


if __name__ == "__main__":
    ll1 = DecimalEquivalent()
    ll1.insert(0)
    ll1.insert(0)
    ll1.insert(1)
    ll1.print_linked_list()
    x = ll1.decimal_equivalent()
    print("Decimal equivalent of above list is {}".format(x))
    ll2 = DecimalEquivalent()
    ll2.insert(0)
    ll2.insert(1)
    ll2.insert(1)
    ll2.insert(1)
    ll2.print_linked_list()
    x = ll2.decimal_equivalent()
    print("Decimal equivalent of above list is {}".format(x))
