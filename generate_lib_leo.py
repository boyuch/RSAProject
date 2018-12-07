"""
Generate RSA Public and Private Keys library
Contains functions that will allow for
generation of public key, private key pair
and then save those to file
"""
import random

def pick_two_random_primes():
    """
    Pick 2 random primes and then return them
    Currently, the random primes are of size
    ~10,000,000
    """
    # TODO: Leo
    pass
    with open ('big_primes.txt') as infile:
        my_list = infile.read().splitlines()
        p = random.choice(my_list)
        q = random.choice(my_list)
    return (p,q)

def generate_public_key(enc_exponent, modulus):
    """
    Use the encryption exponent and the modulus to
    create a 2-tuple that contains those two.
    """
    # TODO: Leo
    # temp value.  TODO change this to correct
    n = 12
    E = 65537
    public_key = (E,n)
    
    return public_key


def extended_euclidean_algorithm(e, phi):
    """
    Using the Extended Euclidean Algorithm to invert
    invert the form   e * d = 1 (mod phi)
    ref: https://en.wikipedia.org/wiki/Extended_Euclidean_algorithm#Pseudocode
    """
    # TODO: Leo
    # TODO look up the extended euclidean algorithm and use that pseudo code here

    # temp value for d.  TODO replace this with real value
    d = 17

    return d
