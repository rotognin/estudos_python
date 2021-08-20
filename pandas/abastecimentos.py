# Estudo importando uma planilha de abastecimentos em Excel para leitura das informações

import pandas as pd

# Importar o arquivo Excel
fExcel = pd.read_excel('arquivos\\abastecimentos.xlsx', sheet_name = 'Principal')
print(type(fExcel))

# Colunas do arquivo:
# Data, KM, Combustível, Valor/Litro, Valor Abastecido, Litros, KM Rodado, 
# Rodado/Litro, Dias, KM/Dia, Valor Acumulado, No Mês, KM no Mês, Custo/Km

# Selecionar algumas colunas, criando um DF específico
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
print('--- Abastecimentos agrupados por combustível ---')
print(dfComb.groupby(['Combustível']).sum())

# Somar uma coluna inteira, no caso o total de abastecimentos
print('--- Total de Abastecimentos em R$ ---')
print(pd.DataFrame(fExcel, columns = ['Valor Abastecido']).sum())

