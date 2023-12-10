'''
    Plotando Grafico de Violino
    
'''
import seaborn as sns
import matplotlib.pyplot as plt

# Trazendo dados
gorjeta = sns.load_dataset('tips')
print(gorjeta)

# Diagrama de violino
sns.violinplot(x='day', y='total_bill', data=gorjeta)
plt.show()


# O parêmetro hue neste caso nos possibilita adicionar mais um parâmetro a nossa análise

# Já o split ele junta os dois parâmetros lado a lado, podemos comparar ambos parâmetros agora
sns.violinplot(x='day', y='total_bill', data=gorjeta, hue='sex', split=True)
plt.show()