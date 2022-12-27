import re


if __name__ == '__main__':
    # # 1.
    # my_word: str = input("Enter a word: ")
    # check_cap = re.match("^([A-Z][a-z])", my_word)
    # if check_cap is None:
    #     print(f"The word \'{my_word}\' is not capitalized.")
    # else:
    #     print(f"The word \'{my_word}\' is capitalized.")

    # # 2. 3.
    # DNA1: str = "ACGACGTTTACACGGATATAAGGGTTACGCGCTGTATAATGTTTGATCAGCTGATTCGAA"
    # DNA2: str = "ACGACGTTTACACGGAAATAAGGGTTACGCGCTGTATAATGTGATCAGCTGATTCGAA"
    # check_TATA_box1 = re.findall("TATAA[ACGT]{3}TT", DNA1)
    # check_TATA_box2 = re.findall("TATAA[ACGT]{3}TT", DNA2)
    # print(check_TATA_box1)
    # print(check_TATA_box2)

    # # 4.
    # my_word: str = input("Enter a string: ")
    # check_match = re.match("[0-9]{2}.[^0-9]{2}", my_word)
    # print(check_match)

    # 5.
    DNA1: str = "ACGACGTTTACACGGATAATAGGGTTACGCGCTGTATAATGTTTCAGCTGATTCGAATATAATTTTT"
    check_2pTATA_box1 = re.match(r"(.*?TATAA[ACGT]{3}TT){2,}", DNA1)
    print(check_2pTATA_box1)

    # 6.
    DNA2: str = "ACGACGTTTACACGGAATATAAGGGTTACGCGCTGTATAATGATTGATCAGCTGATTCGATATAAGCTTTA"
    check_2pTATA_box2 = re.match("(?!(.*?TATAA[ACGT]{3}TT){3,})", DNA2)
    print(check_2pTATA_box2)

    # # 7.
    # my_str: str = input("Enter a string: ")
    # print(re.search("(\s*[0-9]\s*){3}", my_str))

    # # 8.
    # text: str = input("Enter a string: ")
    # print(re.findall(r"05\d-\d{7}", text))
