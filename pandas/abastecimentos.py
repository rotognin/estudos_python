# Estudo importando uma planilha de abastecimentos em Excel para leitura das informações

import pandas as pd

# Importar o arquivo Excel
fExcel = pd.read_excel('arquivos\\abastecimentos.xlsx', sheet_name = 'Principal')
print(type(fExcel))

# Colunas do arquivo:
# Data, KM, Combustível, Valor/Litro, Valor Abastecido, Litros, KM Rodado, 
# Rodado/Litro, Dias, KM/Dia, Valor Acumulado, No Mês, KM no Mês, Custo/Km

# Selecionar algumas colunas, criando um DataFrame específico
#dFrame = pd.DataFrame(fExcel, columns = ['Data', 'KM', 'Combustível'])
#print(dFrame)

dfValor = pd.DataFrame(fExcel, columns = ['Valor Abastecido'])
print('---- Valores de abastecimento ---')
print(dfValor)
print('---------------------------------')

dfCompleto = pd.DataFrame(fExcel)
print(dfCompleto['Data'].max()) # Data do último abastecimento

# Agrupar os dados do Excel por Combustível, exibindo o valor total para cada combustível
dfComb = pd.DataFrame(fExcel, columns = ['Combustível', 'Valor Abastecido'])

# Adicionar uma nova coluna no dataframe para contar quantas vezes o carro foi abastecido com os
# combustíveis agrupados
dfComb.insert(len(dfComb.columns), 'Contagem', 1)
print(dfComb)

print('--- Abastecimentos agrupados por combustível ---')
print(dfComb.groupby(['Combustível']).sum())

# Somar uma coluna inteira, no caso o total de abastecimentos
print('--- Total de Abastecimentos em R$ ---')
print(pd.DataFrame(fExcel, columns = ['Valor Abastecido']).sum())

# Média de KM rodado entre os abastecimentos
print('--- Média de KM rodado ---')
dfRodado = pd.DataFrame(fExcel, columns = ['KM Rodado'])
print(dfRodado.median())
print('---------------------------------')

# O menor e o maior preço de cada combustível abastecido
dfPrecos = pd.DataFrame(fExcel, columns = ['Data', 'Combustível', 'Valor/Litro'])
print('--- O valor mínimo de cada combustível abastecido ---')
print(dfPrecos.groupby(['Combustível']).min())
print('--- O valor máximo de cada combustível abastecido ---')
print(dfPrecos.groupby(['Combustível']).max())

# Quanto foi o maior Km rodado?
dfRodado = pd.DataFrame(fExcel, columns = ['Data', 'KM Rodado'])
print('--- Maior KM Rodado ---')
print(dfRodado.loc[dfRodado['KM Rodado'].idxmax()])