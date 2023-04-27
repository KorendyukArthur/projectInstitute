A = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' * 2  # алфавит

def f(text, k, op):
    k *= len(text) // len(k) + 1
    text = text.upper()
    return ''.join([A[A.index(j) + int(k[i]) * op] for i, j in enumerate(text)])

def encrypt(message, key):
    return f(message, key, 1)

def decrypt(ciphertext, key):
    return f(ciphertext, key, -1)

print("были взяты фамилия имя отчетсво: Ivanov Igor Urevich")

print('Шифрование и расшифровка фамилии с использованием системы Гронсфельда:')
print(encrypt('Ivanov', '31415'))  # шифрование
print(decrypt('LWEOTY', '31415'))  # расшифровывание

print('Шифрование и расшифровка имени с использованием системы Гронсфельда:')
print(encrypt('Igor', '31415'))  # шифрование
print(decrypt('LHSS', '31415'))  # расшифровывание

print('Шифрование и расшифровка отчества с использованием системы Гронсфельда:')
print(encrypt('Urevich', '31415'))  # шифрование
print(decrypt('XSIWNFI', '31415'))  # расшифровывание
