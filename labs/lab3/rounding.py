def roundFloat(float_point):
    int_float = int(float_point)
    difference = float_point - int_float
    if difference > 0:
        return int((float_point + 0.5))
    else:
        return (int(float_point - 0.5))
def main():
    float_point = float(input("Enter a floating-point value: "))
    print("the rounded integer is", roundFloat(float_point))
if __name__ == '__main__':
    main()
