# PUT YOUR NAME HERE
# PUT YOUR SBU ID NUMBER HERE
# PUT YOUR NETID (BLACKBOARD USERNAME) HERE
#
# CSE 337 (Fall 2019)
# Unit Homework 1

from count_failed_addresses import count_failed_addresses

def consolidate_sources(logname):
    # ADD YOUR CODE HERE
    failed_addresses_cnt = count_failed_addresses(logname)
    octet_failed_addresses = {}
    for failed_address, failed_address_cnt in failed_addresses_cnt.items():
        octet_val = failed_address[:failed_address.rfind(".")]
        octet_failed_addresses.setdefault(octet_val, 0)
        octet_failed_addresses[octet_val] += failed_address_cnt

    return octet_failed_addresses  


# DO NOT DELETE THE FOLLOWING LINES OF CODE! YOU MAY
# CHANGE THE FUNCTION CALLS TO TEST YOUR WORK WITH
# DIFFERENT INPUT VALUES.
if __name__ == "__main__":
    # print("test-log-1.txt produced the consolidated dictionary:")
    # print(consolidate_sources("test-log-1.txt"))
    # print()

    # print("test-log-2.txt produced the consolidated dictionary:")
    # print(consolidate_sources("test-log-2.txt"))
    # print()

    # print("test-log-3.txt produced the consolidated dictionary:")
    # print(consolidate_sources("test-log-3.txt"))
    # print()

    # print("test-log-4.txt produced the consolidated dictionary:")
    # print(consolidate_sources("test-log-4.txt"))
    # print()
    
    print("test.txt produced the consolidated dictionary:")
    print(consolidate_sources("test.txt"))
    print()

