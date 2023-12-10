'''
    Plotando Grafico de Dispersao
    
'''
import seaborn as sns
import matplotlib.pyplot as plt

# Trazendo dados
gorjeta = sns.load_dataset('tips')
print(gorjeta)

# Criando o grafico de dontagem e disperção

sns.jointplot(x = 'total_bill', y= 'tip', data=gorjeta)
sns.jointplot(x = 'total_bill', y= 'tip', data=gorjeta, kind='reg')
sns.jointplot(x = 'total_bill', y= 'tip', data=gorjeta, kind='hex')

plt.show()