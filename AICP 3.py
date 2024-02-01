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

def calculate_weight_difference(initial_weights, final_weights):
    return [final - initial for initial, final in zip(initial_weights, final_weights)]

def identify_sign(weight_difference):
    return "rise" if weight_difference > 0 else "fall"

def main():
    num_pupils = 30
    weight_threshold = 2.5

    names = []
    initial_weights = []
    final_weights = []

    # Input initial weights
    print("Input initial weights:")
    for i in range(num_pupils):
        name = input("Enter the name of pupil {}: ".format(i + 1))
        weight = get_valid_weight()

        names.append(name)
        initial_weights.append(weight)

    # Input final weights
    print("\nInput final weights:")
    for i in range(num_pupils):
        weight = get_valid_weight()
        final_weights.append(weight)

    # Calculate and store the difference in weight
    weight_differences = calculate_weight_difference(initial_weights, final_weights)

    # Output the names, initial weights, final weights, and weight differences
    print("\nResults:")
    for i in range(num_pupils):
        print("Name: {}, Initial Weight: {} kg, Final Weight: {} kg, Weight Difference: {} kg"
              .format(names[i], initial_weights[i], final_weights[i], weight_differences[i]))

    # Identify and output pupils with a weight difference of more than 2.5 kilograms
    print("\nPupils with a weight difference of more than {} kilograms:".format(weight_threshold))
    for i in range(num_pupils):
        if abs(weight_differences[i]) > weight_threshold:
            sign = identify_sign(weight_differences[i])
            print("Name: {}, Weight Difference: {} kg {}"
                  .format(names[i], abs(weight_differences[i]), sign, "rise" if sign == "rise" else "fall"))

if __name__ == "__main__":
    main()
