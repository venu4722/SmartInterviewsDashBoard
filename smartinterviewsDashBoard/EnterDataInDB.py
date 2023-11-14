import json


def enter_details(record):
    record = record.lower()
    d  = json.load(open('database.json'))
    #print(d,record,record in d)
    if record in d:
        raise "User name already exists. Try different user name"
    else:
        leetcode     = input('Enter leetcode username')
        #if 'leetcode.com/' not in leetcode:
        #    raise "Enter a valid leetcode link. You can see sample links https://leetcode.com/"
        gfg          = input('Enter gfg username')
        #if 'auth.geeksforgeeks.org/user/.com/' not in gfg:
        #    raise "Enter a valid gfg link"
        codecheff    = input('Enter codecheff username')
        codeforces   = input('Enter codeforces username')
        InterviewBit = input('Enter interviewbit username')
        d[record] = {'leetcode':leetcode,'gfg':gfg,'codecheff':codecheff,
                        'codeforces':codeforces,'interviewbit':InterviewBit}
    with open("database.json", 'w') as json_file:
        json.dump(d, json_file,indent=4)


if __name__ == "__main__":
    enter_details(input('Enter Username'))