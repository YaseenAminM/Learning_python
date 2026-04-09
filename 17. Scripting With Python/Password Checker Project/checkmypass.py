import sys

import requests
import hashlib


def request_api_data(query_char):
    url = 'https://api.pwnedpasswords.com/range/' + query_char
    res = requests.get(url)
    # print(res)

    if res.status_code != 200:
        raise RuntimeError(
            f"Error fetching :{res.status_code} check the api and try again")
    return res


def get_password_leaks_count(hashes, hash_to_check):
    hashes = (line.split(":") for line in hashes.text.splitlines())
    print(hashes)

    for h, count in hashes:
        if h == hash_to_check:
            return count
    return 0


def read_response(response):
    print(response.text)


def pwned_api_check(password):
    sha1password = hashlib.sha1(
        password.encode("utf-8")).hexdigest().upper()
    first5_char, tail = sha1password[:5], sha1password[5:]

    response = request_api_data(first5_char)
    print(
        f"Full Password : {sha1password}\nfirst_5_char : {first5_char}\nTail: {tail}")
    # print(f"Count : {get_password_leaks_count(response, tail)}")
    return get_password_leaks_count(response, tail)


# print(pwned_api_check("123456789"))


def main(args):
    for passwords in args:
        count = pwned_api_check(passwords)
        if count:
            print(
                f"{passwords} was found times...({count}) you should probably change your password")
        else:
            print(f"{passwords} was NOT found. Carry on!.")
        print("-----------------------------------------------------------------")
    return "done!"


main(sys.argv[1::])

# print(sys.argv[1::])
