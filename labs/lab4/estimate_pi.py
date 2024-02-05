import random

def estimate_pi(sample_size):
    count = 0
    for i in range(sample_size):
        x = random.uniform(-1.0, 1.0)
        y = random.uniform(-1.0, 1.0)

        if (x ** 2) + (y ** 2) <= 1:
            count += 1

    return (count / sample_size) * 4

def main():
    while True:
        sample_size = int(input("choose a sample size: "))
                        
        print(estimate_pi(sample_size))

        goAgain = input("do you want to continue (y/n)? ")
        if goAgain == 'n':
                break
if __name__ == '__main__':
    main()
