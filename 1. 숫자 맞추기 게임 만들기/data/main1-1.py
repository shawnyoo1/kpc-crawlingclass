import random
class RandomNumber:
    def get_random_numbers__(self):
        random_number = random.randint(a:1, b:100)
        return random_number

    def __init__(self):
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    r = RandomNumber()
    random_number = r.get_random_numbers__()
    print(random_number)