import json

with open("config.json", "r") as f:
    CONFIG = json.load(f)


def custo_filamento(preco_kg, peso_g):
    return (preco_kg / 1000) * peso_g


def custo_energia(potencia_w, tempo_h, valor_kwh):
    return (potencia_w / 1000) * tempo_h * valor_kwh


def depreciacao(valor_maquina, tempo_h):
    if valor_maquina == 0:
        return 0
    return (valor_maquina / CONFIG["vida_util_horas"]) * tempo_h


def custo_indireto(tempo_h, petg, multipartes, acabamento):
    base = 0
    for faixa in CONFIG["custos_indiretos_faixa"]:
        if tempo_h <= faixa["max_horas"]:
            base = faixa["valor"]
            break

    adicional = 0
    if petg:
        adicional += CONFIG["adicionais"]["petg"]
    if multipartes:
        adicional += CONFIG["adicionais"]["multipartes"]
    if acabamento == "lixa":
        adicional += CONFIG["adicionais"]["lixa"]
    elif acabamento == "pintura":
        adicional += CONFIG["adicionais"]["pintura"]

    return base + adicional


def calcular_preco(dados):
    filamento = custo_filamento(dados["preco_kg"], dados["peso_g"])
    energia = custo_energia(dados["potencia_w"], dados["tempo_h"], dados["kwh"])
    dep = depreciacao(dados["valor_maquina"], dados["tempo_h"])
    mao_obra = CONFIG["valor_hora_trabalho"] * dados["horas_trabalho"]

    indiretos = custo_indireto(
        dados["tempo_h"],
        dados["petg"],
        dados["multipartes"],
        dados["acabamento"]
    )

    custo_total = filamento + energia + dep + mao_obra + indiretos
    preco_venda = custo_total * dados["markup"]

    return {
        "custo_total": round(custo_total, 2),
        "preco_venda": round(preco_venda, 2),
        "lucro": round(preco_venda - custo_total, 2)
    }

import json

with open("config.json", "r") as f:
    CONFIG = json.load(f)


def custo_filamento(preco_kg, peso_g):
    return (preco_kg / 1000) * peso_g


def custo_energia(potencia_w, tempo_h, valor_kwh):
    return (potencia_w / 1000) * tempo_h * valor_kwh


def depreciacao(valor_maquina, tempo_h):
    if valor_maquina == 0:
        return 0
    return (valor_maquina / CONFIG["vida_util_horas"]) * tempo_h


def custo_indireto(tempo_h, petg, multipartes, acabamento):
    base = 0
    for faixa in CONFIG["custos_indiretos_faixa"]:
        if tempo_h <= faixa["max_horas"]:
            base = faixa["valor"]
            break

    adicional = 0
    if petg:
        adicional += CONFIG["adicionais"]["petg"]
    if multipartes:
        adicional += CONFIG["adicionais"]["multipartes"]
    if acabamento == "lixa":
        adicional += CONFIG["adicionais"]["lixa"]
    elif acabamento == "pintura":
        adicional += CONFIG["adicionais"]["pintura"]

    return base + adicional


def calcular_preco(dados):
    filamento = custo_filamento(dados["preco_kg"], dados["peso_g"])
    energia = custo_energia(dados["potencia_w"], dados["tempo_h"], dados["kwh"])
    dep = depreciacao(dados["valor_maquina"], dados["tempo_h"])
    mao_obra = CONFIG["valor_hora_trabalho"] * dados["horas_trabalho"]

    indiretos = custo_indireto(
        dados["tempo_h"],
        dados["petg"],
        dados["multipartes"],
        dados["acabamento"]
    )

    custo_total = filamento + energia + dep + mao_obra + indiretos
    preco_venda = custo_total * dados["markup"]

    return {
        "custo_total": round(custo_total, 2),
        "preco_venda": round(preco_venda, 2),
        "lucro": round(preco_venda - custo_total, 2)
    }