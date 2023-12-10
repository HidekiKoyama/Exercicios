'''
    Plotando Grafico de Histograma
    
'''
import seaborn as sns
import matplotlib.pyplot as plt

# Trazendo dados
gorjeta = sns.load_dataset('tips')
print(gorjeta)

# Trazendo todas as colunas e fazendo seus graficos por gorjeta

sns.histplot(x='tip',data=gorjeta, kde=True)

plt.show()
