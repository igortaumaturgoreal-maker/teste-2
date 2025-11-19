# api/utils/filtros.py
def aplicar_filtros(anuncio, fipe):
    # Critérios
    if not anuncio.get('anunciante') or 'loj' in (anuncio.get('anunciante') or '').lower():
        return False
    ano = anuncio.get('ano')
    if ano is None or not (2013 <= int(ano) <= 2024):
        return False
    km = anuncio.get('km') or 999999
    if int(km) > 150000:
        return False
    preco = anuncio.get('preco') or 0
    diferenca = fipe - preco
    if diferenca < 15000:
        return False
    # ignore sinistrados / peças — procurar palavras-chave no texto
    texto = (anuncio.get('descricao') or "").lower()
    for bad in ['sinistro','batido','leilão','somente para peças','peças']:
        if bad in texto:
            return False
    return True
