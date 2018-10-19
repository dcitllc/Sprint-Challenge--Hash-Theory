def get_indices_of_item_weights(weights, limit):
    weights_dict = {}

    for i in range(len(weights)):
        weight = weights[i]
        if (limit - weight) in weights_dict:
            return (i, weights_dict[limit - weight])
        else:
            weights_dict[weight] = i

    return ()


if __name__ == '__main__':
    # You can write code here to test your implementation using the Python repl
    pass
