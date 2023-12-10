'''
    Plotando Grafico de contagem
    
'''
import seaborn as sns
import matplotlib.pyplot as plt

# Trazendo dados
gorjeta = sns.load_dataset('tips')
print(gorjeta)

#Grafico apenas de contagem
sns.countplot(data=gorjeta, x= 'sex')
plt.show()
