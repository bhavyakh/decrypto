from decrypto.cipher import (
    Atbash, Rot, RailFence, Basen, AsciiShift, Binary, T9Text, DTMF, Periodic, Prime, A1Z26, Vigenere, VigenereBreaker)

cipherList = {
    "alpha_nonkeyed": {
        "AtBash": Atbash.decrypt,
        "Rot - n": Rot.decrypt,
        "Railfence": RailFence.decrypt
    },
    "alphanumeric-nonkeyed": {
        "Base - n": Basen.decrypt,
        "Ascii shift": AsciiShift.decrypt
    },
    "numeric-nonkeyed": {
        "T9Numbers": T9Text.decrypt,
        "DTMF": DTMF.decrypt,
        "Binary": Binary.decrypt,
        "Periodic Elements to text": Periodic.decrypt,
        "Prime indexing": Prime.decrypt,
        "A1Z26": A1Z26.decrypt
    },
    "alpha_keyed": {
        "Viginere": Vigenere.decrypt
    },
    "alpha_keyed_unknown": {
        "Viginere Breaker": VigenereBreaker.decrypt
    }
}
