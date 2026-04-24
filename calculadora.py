import math
from collections import Counter

# ====================== FUNÇÕES ÚTEIS ======================
def media(dados):
    return sum(dados) / len(dados) if dados else 0

def mediana(dados):
    ordenados = sorted(dados)
    n = len(ordenados)
    if n % 2 == 0:
        return (ordenados[n//2 - 1] + ordenados[n//2]) / 2
    return ordenados[n//2]

def moda(dados):
    if not dados:
        return None
    contagem = Counter(dados)
    max_cont = max(contagem.values())
    return [k for k, v in contagem.items() if v == max_cont][0]

def desvio_medio(dados):
    m = media(dados)
    return sum(abs(x - m) for x in dados) / len(dados)

def desvio_padrao_amostral(dados):
    if len(dados) < 2:
        return 0
    m = media(dados)
    n = len(dados)
    variancia = sum((x - m)**2 for x in dados) / (n - 1)
    return math.sqrt(variancia)

def amplitude(dados):
    return max(dados) - min(dados)

def sturges(n):
    return round(1 + 3.322 * math.log10(n))

def binomial_pmf(n, p, k):
    if k < 0 or k > n:
        return 0.0
    comb = math.factorial(n) // (math.factorial(k) * math.factorial(n - k))
    return comb * (p ** k) * ((1 - p) ** (n - k))

def binomial_ge(n, p, min_k=2):
    total = 0.0
    for k in range(min_k, n + 1):
        total += binomial_pmf(n, p, k)
    return total

def poisson_p0(lam):
    return math.exp(-lam)

def prob_sem_defeito(boas, defeito_menor, defeito_grave):
    total = boas + defeito_menor + defeito_grave
    return boas / total if total > 0 else 0

def bayes_maquina_c():
    # Valores fixos do problema clássico
    p_def_total = 0.4*0.04 + 0.3*0.03 + 0.2*0.05 + 0.1*0.02
    p_def_c = 0.2 * 0.05
    return p_def_c / p_def_total

def prob_condicional(p_joint, p_b):
    return p_joint / p_b if p_b > 0 else 0

def coef_correlacao(x, y):
    if len(x) != len(y) or len(x) < 2:
        return 0.0
    n = len(x)
    mx = sum(x) / n
    my = sum(y) / n
    num = sum((xi - mx) * (yi - my) for xi, yi in zip(x, y))
    denx = math.sqrt(sum((xi - mx)**2 for xi in x))
    deny = math.sqrt(sum((yi - my)**2 for yi in y))
    return num / (denx * deny) if denx != 0 and deny != 0 else 0.0

def graus_anova(num_grupos, total_obs):
    entre = num_grupos - 1
    dentro = total_obs - num_grupos
    return entre, dentro

def z_score(mu, sigma, x):
    """Calcula o escore Z"""
    return (x - mu) / sigma

def area_tabela_normal(z):
    """Retorna a área da tabela normal de 0 até |z| (exatamente o que as provas pedem)"""
    return 0.5 * math.erf(abs(z) / math.sqrt(2))

def poisson_ge1(lam):
    """Probabilidade de pelo menos 1 defeito (P(X ≥ 1))"""
    return 1 - poisson_p0(lam)

# ====================== MENU ======================
def ajuda():
    print("=" * 60)
    print("   CALCULADORA COMPLEXA - ESTATÍSTICA E PROBABILIDADE")
    print("   (roda no Programiz - só Python padrão)")
    print("=" * 60)
    print("0  → Desvio Médio")
    print("1  → Desvio Padrão Amostral")
    print("2  → Amplitude Amostral")
    print("3  → Média / Mediana / Moda / Min / Max")
    print("4  → Sturges (número de classes)")
    print("5  → Binomial - P(X >= k) em caixa")
    print("6  → Poisson - P(nenhum evento)")
    print("7  → Lote de peças - Probabilidade sem defeito")
    print("8  → Máquinas (Bayes) - Prob máquina C")
    print("9  → Probabilidade Condicional ('dado que')")
    print("A  → Coeficiente de Correlação")
    print("B  → Graus de Liberdade ANOVA")
    print("C  → Lambda Poisson + P(0)")
    print("D  → Probabilidade simples (ex: dado)")
    print("E  → Desvios Médio + Padrão juntos")
    print("F  → Tudo da lista de 20 pesos (padrão)")
    print("G  → Distribuição Normal (Ex: Dias X com desvio de Y)")
    print("I  → Poisson - P(pelo menos 1 defeito)")
    print("Q  → Sair")
    print("H  → Ajuda")
    print("=" * 60)

lista_padrao = [89, 99, 96, 89, 101, 75, 87, 90, 120, 85, 115, 80, 110, 116, 102, 105, 109, 100, 82, 110]
alturas_padrao = [170, 160, 165, 178, 190, 189, 179, 167, 180, 192]
pesos_padrao = [95, 100, 102, 110, 120, 117, 100, 98, 118, 120]

ajuda()
while True:
    op = input("\n> ").strip().upper()
    if op == "Q":
        print("Até a prova! Boa sorte amanhã!")
        break
    
    # H - Ajuda
    elif op == "H":
        ajuda()

    # 0 - Desvio Médio
    elif op == "0":
        print("Insira os números separados por espaço:")
        dados = list(map(float, input().split()))
        print(f"[+] Desvio Médio = {desvio_medio(dados):.1f}")

    # 1 - Desvio Padrão Amostral
    elif op == "1":
        print("Insira os números separados por espaço:")
        dados = list(map(float, input().split()))
        print(f"[+] Desvio Padrão Amostral = {desvio_padrao_amostral(dados):.2f}")

    # 2 - Amplitude
    elif op == "2":
        print("Insira os números separados por espaço:")
        dados = list(map(float, input().split()))
        print(f"[+] Amplitude Amostral = {amplitude(dados):.0f}")

    # 3 - Média + Mediana + Moda + Min + Max
    elif op == "3":
        print("Insira os números separados por espaço (ou Enter para usar lista de 20 pesos):")
        entrada = input().strip()
        if entrada:
            dados = list(map(float, entrada.split()))
        else:
            dados = lista_padrao[:]
        print(f"[+] Média     = {media(dados):.1f}")
        print(f"[+] Mediana   = {mediana(dados):.1f}")
        print(f"[+] Moda      = {moda(dados)}")
        print(f"[+] Mínimo    = {min(dados):.0f}")
        print(f"[+] Máximo    = {max(dados):.0f}")

    # 4 - Sturges
    elif op == "4":
        n = int(input("[?] Quantos elementos (N)? "))
        print(f"[+] Classes Sturges = {sturges(n)}")

    # 5 - Binomial
    elif op == "5":
        n = int(input("[?] Peças na caixa (n): "))
        p = float(input("[?] Chance de defeito (ex: 0.1): "))
        k = int(input("[?] A partir de quantas defeituosas? (geralmente 2): "))
        print(f"[+] P(X >= {k}) = {binomial_ge(n, p, k):.4f}")

    # 6 - Poisson P(0)
    elif op == "6":
        lam = float(input("[?] Lambda: "))
        print(f"[+] P(0) = {poisson_p0(lam):.4f}")

    # 7 - Lote de peças
    elif op == "7":
        boas = int(input("[?] Peças boas: "))
        menor = int(input("[?] Defeitos menores: "))
        grave = int(input("[?] Defeitos graves: "))
        print(f"[+] Prob sem defeito = {prob_sem_defeito(boas, menor, grave):.2f}")

    # 8 - Bayes máquinas
    elif op == "8":
        print(f"[+] Prob máquina C | defeituosa = {bayes_maquina_c():.2f} (0.25)")

    # 9 - Prob condicional
    elif op == "9":
        joint = float(input("[?] P(X e Y): "))
        b = float(input("[?] P(Y): "))
        print(f"[+] P(X | Y) = {prob_condicional(joint, b):.2f}")

    # A - Correlação
    elif op == "A":
        print("Insira alturas (x) separadas por espaço (Enter = padrão):")
        x_str = input().strip()
        x = list(map(float, x_str.split())) if x_str else alturas_padrao
        print("Insira pesos (y) separadas por espaço (Enter = padrão):")
        y_str = input().strip()
        y = list(map(float, y_str.split())) if y_str else pesos_padrao
        r = coef_correlacao(x, y)
        print(f"[+] Coeficiente de Correlação = {r:.2f} (≈0.85)")

    # B - ANOVA
    elif op == "B":
        g = int(input("[?] Número de grupos/máquinas: "))
        t = int(input("[?] Total de observações: "))
        entre, dentro = graus_anova(g, t)
        print(f"[+] Graus de liberdade: {entre} e {dentro}")

    # C - Lambda Poisson
    elif op == "C":
        total_ev = float(input("[?] Total de eventos (ex: 5): "))
        total_unid = float(input("[?] Total de unidades (ex: 20 km): "))
        lam = total_ev / total_unid
        print(f"[+] Lambda = {lam}")
        print(f"[+] P(0) = {poisson_p0(lam):.4f}")

    # D - Prob simples
    elif op == "D":
        bons = int(input("[?] Resultados bons: "))
        tot = int(input("[?] Total possível: "))
        print(f"[+] Probabilidade = {bons / tot:.2f}")

    # E - Desvios juntos
    elif op == "E":
        print("Insira os números separados por espaço:")
        dados = list(map(float, input().split()))
        print(f"[+] Desvio Médio     = {desvio_medio(dados):.1f}")
        print(f"[+] Desvio Padrão    = {desvio_padrao_amostral(dados):.2f}")

    # F - Lista completa de 20 pesos
    elif op == "F":
        dados = lista_padrao[:]
        print("[+] Lista de 20 pesos carregada")
        print(f"[+] Média          = {media(dados):.1f}")
        print(f"[+] Mediana        = {mediana(dados):.1f}")
        print(f"[+] Moda           = {moda(dados)}")
        print(f"[+] Amplitude      = {amplitude(dados):.0f}")
        print(f"[+] Desvio Médio   = {desvio_medio(dados):.1f}")
        print(f"[+] Desvio Padrão  = {desvio_padrao_amostral(dados):.2f}")
    
    # G - Distribuição Normal
    elif op == "G":
        print("\n=== DISTRIBUIÇÃO NORMAL (Z-score) ===")
        mu = float(input("[?] Média (μ): (Ex: 850)\n> "))
        sigma = float(input("[?] Desvio padrão (σ): (Ex: 40)\n> "))
        x = float(input("[?] Valor de x: (Ex: 750, etc.)\n> "))
        
        z = z_score(mu, sigma, x)
        area = area_tabela_normal(z)
        
        print(f"[+] Z-score                          = {z:.2f}")
        print(f"[+] |Z|                              =  {abs(z):.2f}")
        print(f"[+] Probabilidade exata P(X ≤ {x}) ≈  {0.5 * (1 + math.erf(z / math.sqrt(2))):.4f}")
        print(f"[+] Área 0 a |Z|                     =  {area:.4f}  ← VALOR DA TABELA")
        
    # I - Poisson Pelo menos 1 defeito
    elif op == "I":
        print("\n=== POISSON - PELO MENOS 1 DEFEITO ===")
        print("Exemplo: 5 defeitos em cada 1000 artigos, amostra de 8000")
        defeitos_por_1000 = float(input("[?] Média de defeitos em cada 1000 artigos:\n> "))
        n = float(input("[?] Tamanho da amostra (número de artigos):\n> "))
        
        lam = (defeitos_por_1000 / 1000) * n
        p = poisson_ge1(lam)
        
        print(f"[+] λ (lambda)   = {lam:.4f}")
        print(f"[+] P(X ≥ 1)     = {p:.4f}   ← RESPOSTA DA PROVA")
    
    else:
        print("Opção inválida. Digite 0-F ou Q.")
