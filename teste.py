
def execute(solution_fn, entries=None):
    try:
        if entries is not None:
            entradas =  str(entries).strip().split("\n")
        else:
            entradas = []
            while True:
                try:
                    linha = input()
                    entradas.append(linha)
                except EOFError:
                    break
        result = solution_fn(entries)

        if isinstance(result, list):
           for linha in result:
                print(linha)


    except Exception as e:
        print(f"Erro ao executar o exercício: {e}")

def solution(num1):      
    import math as m
    num1, num2 = list(map(int, input().split()))
    angulo = m.radians(num2)
    pontos = [list(map(int, input().split())) for _ in range(num1)]
    
    for p in pontos:
        x = (p[0] * m.cos(angulo)) - (p[1] * m.sin(angulo))
        y = (p[0] * m.sin(angulo)) - (p[1] * m.cos(angulo))
        print(f"{x:.2f} {y:.2f}")
execute(solution, int(input()))

