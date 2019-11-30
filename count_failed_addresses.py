# PUT YOUR NAME HERE
# PUT YOUR SBU ID NUMBER HERE
# PUT YOUR NETID (BLACKBOARD USERNAME) HERE
#
# CSE 337 (Fall 2019)
# Unit Homework 1

import re

def count_failed_addresses(logname):
    # ADD YOUR CODE HERE
    failed_addresses = {}
    with open(logname, "r") as f:
        lines = f.readlines()
        pattern = re.compile("Disconnected from (\d*\.\d*\d*\.\d*\.\d*)")
        for line in lines:
            result = pattern.search(line)
            if result:
                IP_address = result.group(1)
                failed_addresses.setdefault(IP_address, 0)
                failed_addresses[IP_address] += 1

    return failed_addresses  # CHANGE OR REMOVE THIS LINE


# DO NOT DELETE THE FOLLOWING LINES OF CODE! YOU MAY
# CHANGE THE FUNCTION CALLS TO TEST YOUR WORK WITH
# DIFFERENT INPUT VALUES.
if __name__ == "__main__":
    # print("test-log-1.txt produced the dictionary:")
    # print(count_failed_addresses("test-log-1.txt"))
    # print()

    # print("test-log-2.txt produced the dictionary:")
    # print(count_failed_addresses("test-log-2.txt"))
    # print()

    # print("test-log-3.txt produced the dictionary:")
    # print(count_failed_addresses("test-log-3.txt"))
    # print()

    # print("test-log-4.txt produced the dictionary:")
    # print(count_failed_addresses("test-log-4.txt"))
    # print()

    print("test.txt produced the dictionary:")
    print(count_failed_addresses("test.txt"))
    print()


