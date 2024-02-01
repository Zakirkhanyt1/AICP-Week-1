
def get_valid_weight():
    while True:
        try:
            weight = float(input("Enter the weight (in kilograms): "))
            if weight > 0:
                return weight
            else:
                print("Invalid weight. Please enter a positive number.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def main():
    num_pupils = 30

    names = []
    weights = []

    for i in range(num_pupils):
        name = input("Enter the name of pupil {}: ".format(i + 1))
        weight = get_valid_weight()

        names.append(name)
        weights.append(weight)

    print("\nNames and Weights:")
    for i in range(num_pupils):
        print("Name: {}, Weight: {} kg".format(names[i], weights[i]))

if __name__ == "__main__":
    main()
