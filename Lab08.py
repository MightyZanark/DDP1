# Topic: Recursion

def get_rel_dict() -> dict:
    """Gets the relationship data from the user and returns it as a dict"""

    relationship_dict = {}
    user_input = input("Masukkan data hubungan:\n")
    while user_input != "SELESAI":
        name, acquaintance, closeness = user_input.split()
        relationship_dict[name] = [acquaintance, float(closeness)]
        user_input = input()
    print()
    return relationship_dict


def closeness(name: str, acquaintance: str, relationship_dict: dict) -> float:
    """Calculates the closeness between 'name' and 'acquaintance' recursively
    Returns the closeness level as a float value
    """
    
    cur_closeness = 0
    if name in relationship_dict:

        # If the person 'name' knows is the said 'acquaintance', returns their
        # closeness value and exits
        if relationship_dict[name][0] == acquaintance:
            return relationship_dict[name][1]
        
        # Recursive check if the person 'name' knows is in the dict keys
        # If the person is not in the dict keys, that means 'name' does not know
        # 'acquaintance'
        # If the person is in the dict keys, theres a chance said person knows
        # 'acquaintance' which means a chance 'name' might know 'acquaintance'
        # from this person.
        recurse = closeness(relationship_dict[name][0], acquaintance, relationship_dict)
        if recurse:
            cur_closeness += relationship_dict[name][1] + recurse
        else:
            cur_closeness = 0
        
        return cur_closeness

    else:
        return 0
    

def print_exp(closeness_lvl: int, name: str, acquaintance: str) -> None:
    """Prints the closeness expression depending on the closeness_lvl"""

    if closeness_lvl > 1000:
        return print(f'{name} dan {acquaintance} tidak saling kenal.')
    if 100 < closeness_lvl <= 1000:
        return print(f'{name} dan {acquaintance} mungkin saling kenal.')
    return print(f'{name} dan {acquaintance} kenal dekat.')

if __name__ == '__main__':
    relationship_dict = get_rel_dict()
    name = input("Masukkan nama awal: ")
    acq = input("Masukkan nama tujuan: ")
    closeness_lvl = closeness(name, acq, relationship_dict) * 10
    if closeness_lvl > 0:
        print(f'Jarak total: {closeness_lvl}')
        print_exp(closeness_lvl, name, acq)
    
    else:
        print(f'Tidak ada hubungan antara {name} dan {acq}.')
