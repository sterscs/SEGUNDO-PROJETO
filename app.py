"""
 de Consumo Eletrico Inteligente
Autor: Seu NomCalculadorae
Data: 2026
Descricao: Programa que calcula o consumo mensal de energia eletrica de aparelhos
"""

import os
import time

def limpar_tela():
    """Limpa a tela do terminal"""
    os.system('cls' if os.name == 'nt' else 'clear')

def calcular_consumo(potencia, horas_dia):
    """
    Calcula o consumo mensal em kWh
    
    Args:
        potencia (float): Potencia do aparelho em watts
        horas_dia (float): Horas de uso por dia
    
    Returns:
        float: Consumo mensal em kWh
    """
    return (potencia * horas_dia * 30) / 1000

def calcular_custo(consumo_mensal, preco_kwh=0.75):
    """
    Calcula o custo estimado
    
    Args:
        consumo_mensal (float): Consumo em kWh
        preco_kwh (float): Preco por kWh em reais
    
    Returns:
        float: Custo estimado em reais
    """
    return consumo_mensal * preco_kwh

def exibir_cabecalho():
    """Exibe o cabecalho do programa"""
    print("=" * 60)
    print("⚡ CALCULADORA DE CONSUMO ELETRICO INTELIGENTE ⚡")
    print("=" * 60)
    print("📊 Estime o consumo de energia dos seus aparelhos")
    print("💡 Economize energia e dinheiro!")
    print("-" * 60)

def obter_dados_usuario():
    """
    Obtem os dados do usuario com validacao
    
    Returns:
        tuple: (nome_aparelho, potencia, horas_dia)
    """
    while True:
        nome_aparelho = input("🔌 Nome do aparelho: ").strip().capitalize()
        if nome_aparelho:
            break
        print("❌ Nome invalido. Digite um nome valido.")
    
    while True:
        try:
            potencia = float(input("⚡ Potencia (W): "))
            if potencia > 0:
                break
            print("❌ A potencia deve ser maior que zero.")
        except ValueError:
            print("❌ Digite um numero valido.")
    
    while True:
        try:
            horas_dia = float(input("⏰ Horas de uso por dia: "))
            if 0 <= horas_dia <= 24:
                break
            print("❌ As horas devem estar entre 0 e 24.")
        except ValueError:
            print("❌ Digite um numero valido.")
    
    return nome_aparelho, potencia, horas_dia

def exibir_resultados(nome_aparelho, consumo_mensal, custo_estimado):
    """
    Exibe os resultados formatados
    
    Args:
        nome_aparelho (str): Nome do aparelho
        consumo_mensal (float): Consumo mensal em kWh
        custo_estimado (float): Custo estimado em reais
    """
    print("-" * 60)
    print("📋 RESULTADO DO CALCULO")
    print("-" * 60)
    print(f"🔌 Aparelho: {nome_aparelho}")
    print(f"⚡ Consumo estimado: {consumo_mensal:.1f} kWh/mes")
    print(f"💰 Custo estimado: R$ {custo_estimado:.2f}/mes")
    print("-" * 60)
    
    # Classificação de consumo
    if consumo_mensal <= 50:
        print("🟢 Consumo BAIXO - Economico!")
    elif consumo_mensal <= 150:
        print("🟡 Consumo MEDIO - Atencao!")
    else:
        print("🔴 Consumo ALTO - Considere reduzir o uso!")
    print("=" * 60)

def exibir_dicas():
    """Exibe dicas para economia de energia"""
    print("\n💡 DICAS PARA ECONOMIZAR ENERGIA:")
    print("• 💡 Troque lampadas por LED")
    print("• 🔌 Desligue aparelhos da tomada quando nao estiver usando")
    print("• 📱 Use o modo de economia de energia em dispositivos")
    print("=" * 60)

def main():
    """Funcao principal do programa"""
    try:
        while True:
            limpar_tela()
            exibir_cabecalho()
            
            # Obter dados do usuario
            nome_aparelho, potencia, horas_dia = obter_dados_usuario()
            
            # Calcular consumo e custo
            consumo_mensal = calcular_consumo(potencia, horas_dia)
            custo_estimado = calcular_custo(consumo_mensal)
            
            # Exibir resultados
            exibir_resultados(nome_aparelho, consumo_mensal, custo_estimado)
            exibir_dicas()
            
            # Perguntar se deseja continuar
            continuar = input("\n🔄 Deseja calcular outro aparelho? (s/n): ").lower()
            if continuar != 's':
                print("\n👋 Obrigado por usar a Calculadora de Consumo Eletrico!")
                print("🌱 Economize energia e preserve o meio ambiente!")
                break
                
    except KeyboardInterrupt:
        print("\n\n👋 Programa encerrado pelo usuario. Volte sempre!")
    except Exception as e:
        print(f"\n❌ Ocorreu um erro inesperado: {e}")

if __name__ == "__main__":
    main()