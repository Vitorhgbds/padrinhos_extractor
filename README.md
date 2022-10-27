# padrinhos_extractor

1. Criar uma pasta com o nome de `files`
2. Criar um arquivo na pasta `files` `padrinhos_registrados.csv` com a primeira linha no seguinte formato:
`nome,curso`
3. baixar o arquivo csv do forms de padrinhos e colocar na pasta `files`

após baixar o arquivo csv do forms e colocar na pasta files do projeto basta executar o seguinte comando:
```console
pip install -r requirements.txt

```
Então, passe como argumento o nome do arquivo na hora de rodar o programa, utilizando a seguinte sintaxe:
```console
python extract_padrinhos.py <path_to_archive.csv>
```
