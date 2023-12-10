'''
    Plotando Grafico de Enxame
    
'''
import seaborn as sns
import matplotlib.pyplot as plt

# Trazendo dados
gorjeta = sns.load_dataset('tips')
print(gorjeta)

# Grafico de exame
sns.swarmplot(x='day', y='total_bill', data=gorjeta)
plt.show()