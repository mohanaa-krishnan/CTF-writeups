# CTF Learning Progress

## Overview

This repository documents my journey in learning Capture The Flag (CTF).
The goal is to build strong fundamentals in cryptography, problem-solving, and security concepts through consistent practice and hands-on challenges.

---

## Platform Used

* PicoCTF (practice challenges)

---

## Progress Log

### Initial Steps

* Created account on PicoCTF
* Started exploring beginner-level challenges

---

### Password Cracking (pw crack 1-5)

* Used **Base64 decoding**
* Used **CrackStation** for hash lookup
* Wrote simple Python scripts for decoding and automation

---

### Hashing Challenge (hashcrack)

* Initially tried Base64 (incorrect approach)
* Learned difference between encoding and hashing
* Used **CrackStation** to successfully solve

---

### Caesar & Rotation Cipher

* Used Cryptii tool to convert ciphertext to plaintext
* Understood basic shift/rotation techniques

---

### Substitution Cipher (Level 0-2)

* Applied **frequency analysis**
* Used online frequency analysis tools
* Successfully decoded substitution-based ciphertext

---

### Recent Cryptography Practice

* Solved 3 RSA-based challenges using large 30-40 digit numbers
* Learned the core RSA flow conceptually: public key, private key, modulus, exponent, encryption, and decryption
* Used online RSA tooling for the heavy arithmetic while focusing on the challenge logic
* Practiced Caesar cipher solving with shift/rotation tools
* Practiced Base64 decoding and recognized when a challenge was encoding instead of encryption
* Modified challenge-provided Python code to reverse a custom Base16 plus Caesar cipher scheme
* Converted the custom solver into a reusable mini tool: [B16 Caesar Brute Forcer](tools/b16-caesar-bruteforcer/)

---

## Concepts Learned

* Encoding vs Encryption vs Hashing
* Base64 encoding
* MD5 hashing
* Dictionary attacks
* Wordlist-based attacks
* Basic cryptography problem-solving approach
* RSA fundamentals
* Caesar cipher brute force
* Custom Base16 decoding
* Reading and modifying challenge source code

---

## Tools Used

* CrackStation
* dCode RSA Cipher
* Cryptii Caesar Cipher
* Base64 Decode
* Frequency analysis tools
* ChatGPT for debugging help and concept clarification
* Python (basic scripts)

---

## Tools Built

* [Hash Cracker (Basic)](tools/hash-cracker/)
* [B16 Caesar Brute Forcer](tools/b16-caesar-bruteforcer/)
