NAMES = ['arnold schwarzenegger', 'alec baldwin', 'bob belderbos',
         'julian sequeira', 'sandra bullock', 'keanu reeves',
         'julbob pybites', 'bob belderbos', 'julian sequeira',
         'al pacino', 'brad pitt', 'matt damon', 'brad pitt']


def dedup_and_title_case_names(names):
    """Should return a list of title cased names,
       each name appears only once"""
    new_names = []
    for name in names:
        name = name.title()
        if name not in new_names:
            new_names.append(name)
    return new_names

def sort_by_surname_desc(names):
    """Returns names list sorted desc by surname"""
    names = dedup_and_title_case_names(names)
    names.sort(key=lambda s: s.split()[1], reverse=True)
    return names


def shortest_first_name(names):
    """Returns the shortest first name (str).
       You can assume there is only one shortest name.
    """
    names = dedup_and_title_case_names(names)
    firsts = [x.split()[0] for x in names]
    return min(firsts)


if __name__ == '__main__':
    # print(dedup_and_title_case_names(NAMES))
    # print(sort_by_surname_desc(NAMES))
    print(shortest_first_name(NAMES))