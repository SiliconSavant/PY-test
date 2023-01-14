import matplotlib.pyplot as plt 
import numpy as np
s=['1st','2nd','3rd']
per_sc=[95,89,77]
per_com=[90,93,75]
per_hum=[97,92,77]
x=np.arange(len(s))
plt.bar(x,per_sc,label='Science',width=0.25,color='green')
plt.bar(x+.25,per_com,label='Commerce',width=0.25,color='red')
plt.bar(x+.50,per_hum,label='Humanities',width=0.25,color='gold')
plt.xticks(x,s)
plt.xlabel('Position')
plt.ylabel('Percentage')
plt.title('Bar Graph For Result Analysis')
plt.legend()
plt.show()