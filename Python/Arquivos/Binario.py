# Abrindo dois arquivos ao mesmo tempo com with
with open("foto.png", "rb") as origem, \
    open("cópia.png", "wb") as destino:
    tamanho_bloco = 4096 # 4 KB por vez
    while True:
        bloco = origem. read(tamanho_bloco)
        if not bloco:
            break # Fim do arquivo
        destino.write(bloco)