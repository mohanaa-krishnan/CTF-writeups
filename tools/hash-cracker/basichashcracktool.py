import hashlib

def hash_pw(pw, algo):
    if algo == "md5":
        return hashlib.md5(pw.encode()).hexdigest()
    elif algo == "sha1":
        return hashlib.sha1(pw.encode()).hexdigest()
    elif algo == "sha256":
        return hashlib.sha256(pw.encode()).hexdigest()


def detect_algo(hash_str):
    if len(hash_str) == 32:
        return "md5"
    elif len(hash_str) == 40:
        return "sha1"
    elif len(hash_str) == 64:
        return "sha256"
    return None


def crack_hash(target_hash, dict_file):
    algo = detect_algo(target_hash)

    if algo is None:
        print("[-] Unknown hash type")
        return

    print(f"[+] Detected algorithm: {algo}")

    passwords = open(dict_file).read().splitlines()

    for pw in passwords:
        if hash_pw(pw, algo) == target_hash:
            print(f"[+] Password found: {pw}")
            return

    print("[-] Not found")


# Run
target = input("Enter password: ")
algorithm=imput("enter algorithm:")
target=hash_pw(target,algorithm)
crack_hash(target, "dictionary.txt")
