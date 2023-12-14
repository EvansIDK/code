#ANOTAÇÕES SOBRE OS VÍDEOS

#Testes dos códigos primeiro vídeo

"""def soma[T](x:T, y; T) -> T:
    return x+y"""
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

#Para se criar variantes deve-se evitar usar maiusculas e NÃO USAR espaços nem começar com numeros ou caracteres especiais;

###
#def enviar_email(remetente, destinatario, assunto, corpo):
 #   mensgaem = f"""
  #  subject: {assunto}
   # {corpo}"""

#    with smtplib.SMTP_SSL(servidor, porta, contexto) as servidor:
#        server.login(remetente, senha)
#         server.sendemail(remetente, destinatario, mensagem)

###

"""Funções são chamadas diversas vezes de subprogramas;
Começam com o cabeçalho, o que se encontra dentro dele é chamado de corpo;
Existem dois tipos de subprogramas, as lambdas, que são programas  cujo corpo contem apenas uma expressão, e as demais que contém instruções maiores;
Procedimentos não apresentam retorno, mas funções sim. """

###

"""anonimo= lambda: x+1
anonimo(1)
"vai retornar 2"
"""
###

"""anonimo=lambda x:10 if x<10 else x
"se for mnr que 10 retorna 10 se não retorna o numero"
"""

###
"""
É possível concatenar uma lambda dentro de outra sem apresentar return;
Def é a categoria de função que apresenta várias linhas;
Em teoria, se tem return é função, se não tem é procedimento, mas as vezes isso não se aplica a realidade em razão dos voids;
Voids não apresentam retorno, assim, em python 'no return' é void;
Em python,tudo é sempre função, todo subprograma tem retorno, mesmo que seja vazio (none);
É possivel usar os lambda para provar a logica booleana;
Se chamada uma função de 'fora', irá ser devolvida uma função de 'dentro';
Em situações que as variáveis estão juntas, deve-se colocar os numeros juntos;
Existem varivaies locais, livres, globais, etc...
Python tem polimorfismo (usa decoradores) e despacho;
Livre é uma variavel que faz parte da closure;
Existem corrotinas classicas e assincronas;
O yeld deixa o controle simetrico;
Na corrotina é feita uma pausa para o controle simetrico;
Existem também os gerados que em python são corrotinas, mas tem quem discorde;
Controle simetrico é a troca de respostas ("ping pong");
Geradores são criadores de dados;
É possível juntar os geradores com o yeld e devolver valores;
Map é objeto gerador;
É possível usar o yield como expressao e como retorno;
"yield from" transforma subprograma em subgerador;
async=corrotina assincrona;
await delega a função de uma corrotina para outra corrotina.
"""

"""
Iteravel é todo objeto que pode ser percorrido, como no "for" em uma lista;
Usa a função next para isso;
Essa é a base para a construção do for;
Lazy evaluation atrasa o calculo até que o uso seja necessário (quando for solicitado).

Range não é iterador;
Uma forma de criar a lazy é com os geradores;
Pode-se usar o lazy para criar um sequencia infinita;
(conexão entre os videos envolve os geradores)
Usa-se o lazy para grandes volumes de dados.

"zip" é um exemplo de função embutida que serve para combinar listas alternando;
"map" também é função;
"filter" filtra;
o itertools fornece funções para criar iteradores para tarefas em loop (é escrito em C puro então é rápido).

oferece o "zip_longest"(para zipar sequencias de tamanhos diferentes);
"startmap"(desempacota);
"filterfalse"(filter ao contrario);
"islice"(add a função do slice aos iteradores).

Para usar o "ziplongest", usa o fillvalue e define o que será usado;
Para fazer a média você pode usar o filter para tirar o "none";
"nan" provavelmente é melhor.

Para o filterfalse ele te fornece o contrario do que foi descrito.

"starma" faz seu trabalho através do desmontamento da sequência;
Poupa linhas e permite usar map junto de zip sem problemas;
Muito util em caso que os valores sejam tuplas.

Usando o ""islice é possivel tornar o gerador lazy e permitir "andar" nos numeros gerados;
Não é possível usar numeros negativos;
(1:05:20).

A função "count" conta;
c=count(0,pi).

Existe o cycle (1:14:05);
Pode ser utilizado para fazer um semafaro;
Ou um sistema que informa quem irá te atender ou mesmo para animações e música;
Ele divide em ciclos.

"repeat" te retorna o mesmo valor o numero de vezes que você solicitar;
É possível deixar infinito;
(melhor que o while true)
Muito util para videogames;
Evita breaks desnecessários.


Existem também os combinadores:

"product" (1:28:00)
Produz possiveis combinações, como quando é preciso citar as combinações de cores com tamanhos de camisetas;
(evita colocar for dentro de for);
Muito bom quando tem vários fatores para combinar;
Ele concatena as coisas em uma tupla.

"permutation" (1:34:30)
Todas as combiações de determinados valores;
Usando determinado numero de valores que devem aparecer por combinação;
exemplo: p=permutations('abcd',2);
permutação -> AB != BA.

"combinations"
Na permutação tem repetição (a com b e b com a), já na combinação não.


Existem funções que não podem ser infinitas.

"acummulate" cria uma progressão aritmetica;
Pode ser utilizada para ver o balaço da conta bancária.

"takewhile" (1:51:50);
Filtro que itera.

"dropwhile" serve para ignorar o que for definido.

"Chain": junta iteraveis em um unico iteravel (2:00:55);
Para quando precisar iterar 2 geradores para criar um unico item.

"compress" (02:03:00);
Permite agregar false e true á valores para decidir se eles devem ser levados em consideração ou não;

"groupby";
Ordena por grupos tal qual no sql;
É possível usar um itemgetter a depender da situação.

"tee" repete os dados para que possam ser utilizados novamente.

"pairwise" cria combinações; mas só usa de 2 valores.

Existem outras bibliotecas como o moreitertools e o toolz.
"""
