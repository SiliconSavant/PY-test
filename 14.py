import matplotlib.pyplot as plt
Subject=['Physics','Chemistry','Hindi','Biology','ComputerSc']
Percentage=[85,78,65,90,100]
plt.bar(Subject,Percentage,align='center',color='green')
plt.xlabel('SUBJECTS NAME')
plt.ylabel('PASS PERCENTAGE')
plt.title('Bar Graph For Result Analysis')
plt.show()