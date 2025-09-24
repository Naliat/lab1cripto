import base64

def encriptar(texto_claro: str, chave: str) -> str:

    if not chave:
        raise ValueError("Chave não pode ser vazia.")
    pt_bytes = texto_claro.encode("latin-1")
    key_bytes = chave.encode("latin-1")
    out = bytearray()
    for i, b in enumerate(pt_bytes):
        k = key_bytes[i % len(key_bytes)]
        out.append((b + k) % 256)
    return base64.b64encode(bytes(out)).decode("ascii")  


def decriptar(texto_encriptado: str, chave: str) -> str:
    if not chave:
        raise ValueError("Chave não pode ser vazia.")
    try:
        cipher_bytes = base64.b64decode(texto_encriptado)
    except Exception:
        raise ValueError("Texto encriptado inválido: espere uma string base64.")
    key_bytes = chave.encode("latin-1")
    out = bytearray()
    for i, c in enumerate(cipher_bytes):
        k = key_bytes[i % len(key_bytes)]
        out.append((c - k + 256) % 256)
    return bytes(out).decode("latin-1")


def executar_testes_manualmente():
    try:
        n = int(input("Quantos casos de teste deseja executar? "))
    except ValueError:
        print("Número inválido.")
        return

    for i in range(n):
        print(f"\n--- Caso {i+1} ---")
        texto = input("Digite o texto claro: ")
        chave = input("Digite a chave: ")
        try:
            cifrado = encriptar(texto, chave)
            decifrado = decriptar(cifrado, chave)
        except Exception as e:
            print("Erro:", e)
            continue

        print("Cifrado (base64):", cifrado)
        print("Decifrado:", decifrado)
        print("Resultado:", "OK — decifrou corretamente" if decifrado == texto else "FALHOU")


if __name__ == "__main__":
    menu = (
        "Escolha uma opção:\n"
        "1 - Cifrar (encriptar)\n"
        "2 - Decifrar (decriptar)\n"
        "3 - Executar testes manuais\n"
        "0 - Sair\n"
    )
    while True:
        print()
        opcao = input(menu + "Digite sua escolha: ").strip()
        if opcao == "1":
            texto = input("Digite o texto claro: ")
            chave = input("Digite a chave: ")
            try:
                cif = encriptar(texto, chave)
                print("Texto cifrado (base64):", cif)
            except Exception as e:
                print("Erro:", e)

        elif opcao == "2":
            texto_cifrado = input("Digite o texto cifrado (base64): ")
            chave = input("Digite a chave: ")
            try:
                dec = decriptar(texto_cifrado, chave)
                print("Texto decifrado:", dec)
            except Exception as e:
                print("Erro:", e)

        elif opcao == "3":
            executar_testes_manualmente()

        elif opcao == "0":
            break

        else:
            print("Opção inválida. Tente novamente.")
