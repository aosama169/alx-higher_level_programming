#!/usr/bin/python3
def to_subtract(listNumber):
    subNo = 0
    max_list = max(listNumber)
    for n in listNumber:
        if max_list > n:
            subNo += n
    return (max_list - subNo)


def roman_to_int(roman_string):
    if not roman_string:
        return 0
    if not isinstance(roman_string, str):
        return 0
    rom_n = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    list_keys = list(rom_n.keys())
    num = 0
    last_rom = 0
    listNumber = [0]
    for ch in roman_string:
        for r_num in list_keys:
            if r_num == ch:
                if rom_n.get(ch) <= last_rom:
                    num += to_subtract(listNumber)
                    listNumber = [rom_n.get(ch)]
                else:
                    listNumber.append(rom_n.get(ch))
                last_rom = rom_n.get(ch)
    num += to_subtract(listNumber)
    return (num)
