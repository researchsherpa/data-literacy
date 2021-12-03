from collections import namedtuple

NCGroup = namedtuple("NCGroup", "color_code nc_list")

empowerla_groups = {
    1: NCGroup("#00BFFF",
               [4, 114, 99, 113, 118, 120, 124, 111]),
    2: NCGroup("#FFFF00",
               [5, 101, 7, 9, 10, 8, 6, 112, 100]),
    3: NCGroup("#EE82EE",
               [11, 13, 14, 15, 19, 16, 17, 18]),
    4: NCGroup("#32CD32",
               [20, 21, 22, 23, 24, 25, 26, 27, 28]),
    5: NCGroup("#DC143C",
               [64, 127, 63, 66, 62, 61, 115, 67, 68, 70, 71]),
    6: NCGroup("#CD853F",
               [29, 30, 32, 33, 34, 58, 119, 60]),
    7: NCGroup("#87CEEB",
               [36, 37, 38, 53, 44, 43]),
    8: NCGroup("#FF8C00",
               [39, 40, 41, 42, 102, 47, 48, 50]),
    9: NCGroup("#FF00FF",
               [104, 55, 76, 52, 121, 128, 54, 97]),
    10: NCGroup("#800080",
                [73, 75, 79, 80, 81, 77, 74]),
    11: NCGroup("#7FFFD4",
                [78, 109, 125, 110, 86, 84, 87, 88]),
    12: NCGroup("#DB7093",
                [90, 91, 92, 93, 94, 95, 96])
}

nc_map = []
