def encriptar(texto_claro, chave):
    texto_encriptado = []
    for i, c in enumerate(texto_claro):
        p = ord(c)
        k = ord(chave[i % len(chave)])
        cifra = (p + k) % 256
        texto_encriptado.append(cifra)
    return texto_encriptado 


def decriptar(lista_cifrada, chave):
    texto_claro = []
    for i, c in enumerate(lista_cifrada):
        k = ord(chave[i % len(chave)])
        dec = (c - k + 256) % 256
        texto_claro.append(chr(dec))
    return "".join(texto_claro)


def hex_para_lista(hex_string):
    return [int(x, 16) for x in hex_string.split()]


def lista_para_hex(lista):
    return " ".join(f"{x:02X}" for x in lista)


if __name__ == "__main__":
    print("Escolha uma opção:")
    print("1 - Cifrar (encriptar)")
    print("2 - Decifrar (decriptar)")
    opcao = input("Digite sua escolha: ")

    if opcao == "1":
        texto = input("Digite o texto claro: ")
        chave = input("Digite a chave de criptografia: ")
        cifrado = encriptar(texto, chave)
        print("Texto cifrado em HEX (copie este para decifrar):", lista_para_hex(cifrado))

    elif opcao == "2":
        hex_texto = input("Digite o texto cifrado em HEX (ex: 88 98 94): ")
        chave = input("Digite a chave de criptografia: ")
        lista_cifrada = hex_para_lista(hex_texto)
        decifrado = decriptar(lista_cifrada, chave)
        print("Texto decifrado:", decifrado)

    else:
        print("Opção inválida!")
