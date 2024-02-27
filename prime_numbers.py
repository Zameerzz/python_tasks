lower_num = int(input("lower number: "))
upper_num = int(input("upper number: "))


def find_primenumbers(lower_num, upper_num):
    """we are taking in between numbers by setting range so we need two arguements and can use range method"""
    for num in range(lower_num, upper_num + 1):  # third arguement for increment
        """we are taking the lower number and passing condiation which says
        prime number must be greater than 1. if the conditon is true then the number goes loop and 
        I am searching diviable factors of that number"""
        if num > 1:
            for i in range(2, num):
                if num % i == 0:
                    break
                """ we are making sure that if the number has divisable factors then exit the loop and num takes other value starts
                looking for the divisable factors for that num (primarity)"""
            else:
                print(f"here all prime numbers can be printed: {num}")


find_primenumbers(lower_num, upper_num)
