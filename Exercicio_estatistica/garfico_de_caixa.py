'''
    Plotando Grafico de Caixa
    
'''
import seaborn as sns
import matplotlib.pyplot as plt

# Trazendo dados
gorjeta = sns.load_dataset('tips')
print(gorjeta)

# Fazendo a análide de total da conta por dia da semana, para verificar se há uma relação entre essas variáveis

sns.boxplot(x='day', y='total_bill', data=gorjeta)
plt.show()
sns.boxplot(x='day', y='total_bill', data=gorjeta, hue='smoker')
plt.show()