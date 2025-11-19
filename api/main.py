# api/main.py
from scraping.olx import buscar_olx
from fipe.fipe_api import get_fipe
from utils.db import init_db, inserir_ou_atualizar
from utils.filtros import aplicar_filtros
from utils.notificacao import notificar
from datetime import datetime

def run_once():
    init_db()
    anuncios = []
    anuncios += buscar_olx()
    # anúncios += buscar_webmotors() etc.

    for a in anuncios:
        # extrair brand/model/ano de 'modelo' (parsing)
        fipe = get_fipe("brand", "model", a['ano'])
        a['fipe'] = fipe
        a['diferenca'] = fipe - a['preco']
        a['data_hora'] = datetime.utcnow().isoformat()
        if aplicar_filtros(a, fipe):
            inserir_ou_atualizar(a)
            notificar(a)
