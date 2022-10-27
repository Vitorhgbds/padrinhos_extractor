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

padrinhos_registrados = pd.read_csv('files/padrinhos_registrados.csv')

mensagens = []
for curso in curso_indexes.keys():
    padrinhos = curso + " \n \n "
    for pessoas_indexes in curso_indexes[curso]:
        nome = df['Identifique seu nome'].get(pessoas_indexes).lower()
        if (nome not in padrinhos_registrados['nome'].to_list()):
            padrinhos_registrados.loc[len(padrinhos_registrados.index)] = [nome,curso]
            padrinhos = padrinhos + 'Nome -> ' + nome + ' \n '
            padrinhos = padrinhos + 'preferencia de contato -> ' + df['Como prefere ser contatado?'].get(pessoas_indexes) + ' \n '
            padrinhos = padrinhos + 'telefone -> ' + str(df['Numero de telefone (opcional)'].get(pessoas_indexes)) + ' \n '
            padrinhos = padrinhos + 'nick do disc -> @' + str(df['Nick do discord (opcional)'].get(pessoas_indexes)) + ' \n \n '
            padrinhos = padrinhos + '```\n'
            padrinhos = padrinhos + 'Bicho favorito -> ' + df['Qual seu bicho favorito?'].get(pessoas_indexes) + ' \n '
            padrinhos = padrinhos + 'Area de interesse -> ' + df['Qual sua area de interesse?'].get(pessoas_indexes) + ' \n '
            padrinhos = padrinhos + 'Cor favorita -> ' + df['Cor favorita'].get(pessoas_indexes) + ' \n '
            padrinhos = padrinhos + 'Hobbie -> ' + df['Um Hobbie'].get(pessoas_indexes) + ' \n '
            padrinhos = padrinhos + 'Musica -> ' + df['Musica, banda ou genero musical favorito'].get(pessoas_indexes) + ' \n '
            padrinhos = padrinhos + '```\n'
            padrinhos = padrinhos + '__________\n'
    mensagens.append(padrinhos)


#f = io.open("alreadyRegistered.txt", "w", encoding='utf8')
#for nome_padrinho in alreadyRegistered:    
#    f.write(nome_padrinho)
#f.close()
padrinhos_registrados.to_csv('files/padrinhos_registrados.csv')

f = io.open("files/padrinhos_para_registrar.txt", "w", encoding='utf8')
for mensagem in mensagens:    
    f.write(mensagem)
f.close()