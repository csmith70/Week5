## Find, through brute force, the five-letter passwords corresponding with the following SHA-256 hashes:
import multiprocessing
from hashlib import sha256
import time
import sys

print("""Usage: python hashcrack.py [ncores])
    [ncores] - the number of workers to run in parallel,
    if omitted it will be set to the number of processors in the system
""")
## Number of cores to use
if len(sys.argv) > 1:
    cores = int(sys.argv[1])
else:
    # Creates number of cores with automatically detected number
    cores = multiprocessing.cpu_count()

print('Using {} cores.'.format(cores)) 
start_time = time.time()
 
def HashFromSerial(serial):
    divisor = 456976
    letters = []
    for i in range(5):
        letter, serial = divmod(serial, divisor)
        letters.append( 97 + int(letter) )
        divisor /= 26
    return (letters, sha256(bytes(letters)).digest())
 
 
def main():
    h1 = bytes().fromhex("1115dd800feaacefdf481f1f9070374a2a81e27880f187396db67958b207cbad")
    h2 = bytes().fromhex("3a7bd3e2360a3d29eea436fcfb7e44c735d117c42d1c1835420b6b9942dd4f1b")
    h3 = bytes().fromhex("74e1bb62f8dabb8125a58852b63bdf6eaef667cb56ac7f7cdba6d7305c50a22f")
    numpasswords = int(26 ** 5)
#    chunksize = int(numpasswords / multiprocessing.cpu_count())
    chunksize = int(numpasswords / cores)
    with multiprocessing.Pool(cores) as p:
        for (letters, digest) in p.imap_unordered(HashFromSerial, range(numpasswords), chunksize):
            if digest == h1 or digest == h2 or digest == h3:
                password = "".join(chr(x) for x in letters)
                print(password + " => " + digest.hex())
 
 
if __name__ == "__main__":
    main()

print("Time elapsed: ", time.time() - start_time, "s")
