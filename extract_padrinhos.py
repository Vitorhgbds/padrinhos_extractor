import pandas as pd
import io
import sys
df = pd.read_csv(str(sys.argv[1]))
df = df.drop(columns=['Timestamp'])

curso_indexes = {}

for i,curso in enumerate(df['Qual o seu curso?']):
    if(curso not in curso_indexes):
        curso_indexes[curso] = []
    curso_indexes[curso].append(i)

mensagens = []
for curso in curso_indexes.keys():
    padrinhos = curso + " \n \n "
    for pessoas_indexes in curso_indexes[curso]:
        padrinhos = padrinhos + 'Nome -> ' + df['Identifique seu nome'].get(pessoas_indexes) + ' \n '
        padrinhos = padrinhos + 'Bicho favorito -> ' + df['Qual seu bicho favorito?'].get(pessoas_indexes) + ' \n '
        padrinhos = padrinhos + 'Area de interesse -> ' + df['Qual sua area de interesse?'].get(pessoas_indexes) + ' \n '
        padrinhos = padrinhos + 'Cor favorita -> ' + df['Cor favorita'].get(pessoas_indexes) + ' \n '
        padrinhos = padrinhos + 'Hobbie -> ' + df['Um Hobbie'].get(pessoas_indexes) + ' \n '
        padrinhos = padrinhos + 'Musica -> ' + df['Musica, banda ou genero musical favorito'].get(pessoas_indexes) + ' \n '
        padrinhos = padrinhos + 'preferencia de contato -> ' + df['Como prefere ser contatado?'].get(pessoas_indexes) + ' \n '
        padrinhos = padrinhos + 'telefone -> ' + str(df['Numero de telefone (opcional)'].get(pessoas_indexes)) + ' \n '
        padrinhos = padrinhos + 'nick do disc -> ' + str(df['Nick do discord (opcional)'].get(pessoas_indexes)) + ' \n \n '
    mensagens.append(padrinhos)

f = io.open("padrinhos.txt", "w", encoding='utf8')
for mensagem in mensagens:    
    f.write(mensagem)
f.close()