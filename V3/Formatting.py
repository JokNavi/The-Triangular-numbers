def find_longest(tokens):
    longest_length = 0
    for x in tokens:
        current_token_length = len(str(x))
        if current_token_length > longest_length:
            longest_length = current_token_length
    return longest_length


def format_row_spacing(rows):
    spacing_collector = list()
    for item in zip(*rows):
        spacing_collector.append(find_longest(item))
    formatted_rows = list()
    for row in rows:
        formatted_row = list()
        for item, space in zip(row,spacing_collector):
            formatted_row.append("{0:>{1}}".format(item, space))
        formatted_rows.append(formatted_row)
    return formatted_rows

def print_nicely(rows):
    LENGTH_PER_LINE = 160
    formatted_rows = format_row_spacing(rows)
    for i in range(0, sum([len(x) for x in formatted_rows[0]]), LENGTH_PER_LINE):
        for row in formatted_rows:
            print(", ".join(row)[i:i+LENGTH_PER_LINE])
        print()

def get_seperator(rows):
    seperators = []
    for values in zip(*rows):
        seperators.append("-"*find_longest(values))
    return seperators
      

if __name__ == "__main__":
    rows = [[10]*100, [100]*100]
    print_nicely(rows)

