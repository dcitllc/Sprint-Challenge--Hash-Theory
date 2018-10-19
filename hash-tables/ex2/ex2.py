def reconstruct_trip(tickets):
    tickets_dict = {}
    route = [''] * (len(tickets) - 1)

    for ticket in tickets:
        tickets_dict[ticket[0]] = ticket[1]
        if ticket[0] is None:
            route[0] = ticket[1]

    for i in range(1, len(route)):
        if route[i - 1] in tickets_dict:
            route[i] = tickets_dict[route[i - 1]]
        else:
            return []

    return route


if __name__ == '__main__':
    # You can write code here to test your implementation using the Python repl
    pass
