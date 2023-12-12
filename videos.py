#ANOTAÇÕES SOBRE OS VÍDEOS

#Testes dos códigos primeiro vídeo

#def soma[T](x:T, y; T) -> T:
    #return x+y
####

"""def simulacaodejuros(
        valor: float, taxa: float, parcelas: int)-> str:
        template= "juros em {}x parcelas: {}. Valor final: {}."

        juros=valor*taxa*parcelas
        valor_final=valor+juros

        return template.format(parcelas, juros, valor_final)"""
###

"""verbos = ['comer', 'amar', 'saber']

sorted(verbos)
["resultado em uma ordem sorteada"]

sorted(verbos, key=lambda x: x[-2:])
['saber', 'amar', 'comer']"""
###

"""path_1=extract_audio( 'video_1.mp4', 'result 1.wav', eq=False)
path_2=extract_audio('video 2.mp4', 'result 2.wav', eq=False)
path_3=extract_audio('video 3.mp4', 'result 3.wav', eq=False)
path_4, path_eq_4=extract_audio('video_4.mp4', 'result_4.wav', eq=True)"""

###
"""def extract_audio(video_file, output_file, eq=True):
    path_1=extract_audio( 'video_1.mp4', 'result 1.wav', eq=False)"""
###

"""def soma(x,y):
    return x+y"""

###
"""lista=[]
def aumentar_lista(val):
    lista.append(val)

aumentar_lista(1)
[1]
aumentar_lista(2)
[1,2]"""

###

"""def somas(x,/,y,*,z):
    return x+y+z"""
###
"""def somas(x,y,z):
    return x+y+z"""
###

"""def transformaemstring(numero):
    return str(numero)"""
###

"""(lambda x: x+1)(1)
("vai retornar 2")

soma=lambda x: x+1
soma(10)
"vai retornar 11"
"""
###

"""def soma(x):
    return x+1
resultado=soma(10)"""
"vai retornar 11"
###

"""def cadastro(nome, telefone, *kwargs):
    print(f'{nome=}, {telefone=}, {kwargs}')"""
###

"""def somatorio(*args):
    acumulador=3
    for val in args:
        acumulador +=val
    return acumulador"""
###

#para se criar variantes evitar usar maiusculas e NAO USAR espaços nem começar com numeros ou caracteres especiais

###
#def enviar_email(remetente, destinatario, assunto, corpo):
 #   mensgaem = f"""
  #  subject: {assunto}
   # {corpo}"""

#    with smtplib.SMTP_SSL(servidor, porta, contexto) as servidor:
#        server.login(remetente, senha)
#         server.sendemail(remetente, destinatario, mensagem)

###

#funções sao subprogramas, o contribuidor zeca é um queriiiidooo
#começa com o cabeçalho, o que ta dentro dele é o corpo
"""existem dois tipos de subprogramas, lambda são programas e o corpo contem apenas uma expressão, procedimento não retorna mas função sim.
"""
"""anonimo= lambda: x+1
anonimo(1)
"vai retornar 2"

anonimo=lambda x:10 if x<10 else x"""

"se for mnr que 10 retorna 10 se não retorna o numero"

"""da pra concatenar lambda uma dentro da outra e NÃO TEM RETURN
def cabe vaaaaarias linhas 
#em teoria, se tem return é função, se não tem é procedimento, mas as vezes não já que tem os void (não tem retorno), em python sem return é void
#em python tudo é sempre função, todo subprograma tem retorno, mesmo que seja vazio (ai retorna none)
#no return vai dizer que a d=função nunca volta (notação maneira)
#é possivel usar os lambda para provar a logica booleana
#se chamar a função de fora vai receber a função de dentro
#colocar os numeros juntos se as variaveis tão juntas
#existem varivaies locais, livres, globais, etc...
#python tem polimorfismo (usa decoradores) e despacho pra quem tava falando mal
#livre é uma variavel que faz parte da closure
#inner e closure (rever)
#rever as corrotinas
#tem corrotinas classicas e assincronas
o yeld deixa o controle simetrico
na corrotina faz uma pausa pro controle simetrico
existem também os gerados que em python são corrotinas, mas tem quem discorde
controle simetrico é a troca daquelas respostas ping pong
geradores são criadores de dados
da para juntar os geradores com o yeld e devolver valores
computação simatrica da medo
map é objeto gerador
Da para usar o yield como expressao e como retorno
yield from transforma subprograma em subgerador
async=corrotina assincrona
await delega a fun;'ao de uma corrotina para outra corrotina
"""

"""iteravel é todo objeto que pode ser percorrido, como no for em uma lista
usa a função next para isso
essa é a base para o for
lazy evaluation atrasa o calculo até que o uso seja necessário (quando for solicitado)

range não é iterador
uma forma de criar a lazy é com os geradores
da pra usar o lazy para criar um sequencia infitia
(conexão entre os videos envolve os geradores)
usa o lazy para grandes volumes de dados
funções embutidas é [estranho] de usar

zip é um exemplo de função embutida que serve para combinar listas alternando
map também é função
filter filtra [obvio]
é confuso mas ainda que melhor que tentar criar essas coisas do zero
assistir videos sobre decoradores
o itertools fornece funções para criar iteradores para tarefas em loop (é escrito em C puro então é rápido)

oferece o zip_longest(para zipar sequencias de tmanhos diferentes)
startmap(desempacota)
filterfalse(filter ao contrario)
islice(add a função do slice aos iteradores)

para usar o ziplongest, usa o fillvalue e define para seu usado
para fazer a média vocÊ pode usar o filter para tirar o none 
nan provavelmente é melhor

para o filterfalse ele te da o contrario do que pediu

starmap faz seu trabalho através do desmontamento da sequência
vai poupar linha e permiter usando map junto de zip sem problemas
muito util em caso que os valores sejam tuplas

usando o islice é possivel tornar o gerador lazy e permitir "andar" nos numeros gerados
não é possível usar o step nem numeros negativos
PERA DA SIM PARA IR DD 2 EM 2 SÓ COLCOAR OS VALORES COMO NONE (ESTA NO MOMOENTO 1:05:20)

TAMBÉM TEM O COUNT QUE CONTA
c=count(0,pi)

também existe o cycle (1:14:05)
da para fazer um semafaro
ou um sistema que informa quem irá te atender ou mesmo para animações e música

repeat te manda de voltar o mesmo valor o numero de vezes que você mandar
mas tem como deixar infinito
melhor que o while true
muito util para videogames
tabém evita breaks desnecessários

existem também os combinadores

product (1:28:00)
produz possiveis combinações, como quando é preciso citar as combinações de cores com tamanhos de camisetas
(evita colocar for dentro de for)
muito bom quando tem vários fatores para combinar
ele concatena as coisas em uma tupla

permutation (1:34:30)
todas as combiações de determinados valores usando determinado numero de valores por combinação
p=permutations('abcd',2)
permutação -> AB != BA

combinations
na permutação tem repetição (a com b e b com a), já na combinação não

coombinations_with_replacement
PESQUISA DEPOIS

existem funções que não podem ser infinitas

acummulate cria uma progressão aritmetica
da para usar para ver o balaço da conta bancária

takewhile (1:51:50)
filtro que itera
dropwhile serve para ignorar

existe também a diminuição de containers

chain: junta iteraveis em um unico iteravel (2:00:55)
para quando crises iterar 2 geradores para criar uma coisa única

compress (02:03:00)
te permite agregar false e true á valores para decidir se eles devem ser levados em consideração ou não

groupby
ordena por grupos tal qual no sql
é possível usar um itemgetter a depender da situação

tee repete os dados para que possam ser utilizados novamente

pairwise cria combinações mas só usa de 2 valores

existem outras bibliotecas como o moreitertools e o toolz
"""
