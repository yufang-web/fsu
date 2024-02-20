import os
import glob
import matplotlib.pyplot as plt
import numpy as np

file_list = glob.glob('*.txt')
percentage_data = {}  # 

for file in file_list:
    filename = file.split('_')[0]  # 
    read_file = open(file, 'r')
    lines = read_file.readlines()
    
    for line in lines:
        if line.startswith('C methylated in CpG context'):
            line_list = line.split()
            percentage_CG = float(line_list[5].rstrip('%')) / 100
            if filename in percentage_data:
                percentage_data[filename]['CpG'] = percentage_CG
            else:
                percentage_data[filename] = {'CpG': percentage_CG}

        if line.startswith('C methylated in CHG context'):
            line_list = line.split()
            percentage_CHG = float(line_list[5].rstrip('%')) / 100
            if filename in percentage_data:
                percentage_data[filename]['CHG'] = percentage_CHG
            else:
                percentage_data[filename] = {'CHG': percentage_CHG}

        if line.startswith('C methylated in CHH context'):
            line_list = line.split()
            percentage_CHH = float(line_list[5].rstrip('%')) / 100
            if filename in percentage_data:
                percentage_data[filename]['CHH'] = percentage_CHH
            else:
                percentage_data[filename] = {'CHH': percentage_CHH}



categories = list(percentage_data.keys())
cg_values = [data.get('CpG', 0) for data in percentage_data.values()]
chg_values = [data.get('CHG', 0) for data in percentage_data.values()]
chh_values = [data.get('CHH', 0) for data in percentage_data.values()]


num_samples = len(categories)
bar_width = 0.2


x = np.arange(num_samples)


plt.bar(x - bar_width, cg_values, bar_width, label='CpG')
plt.bar(x, chg_values, bar_width, label='CHG')
plt.bar(x + bar_width, chh_values, bar_width, label='CHH')


plt.xticks(x, categories, rotation=45)


plt.legend()


plt.title('Methylation Percentage in Different Contexts')
plt.xlabel('Samples')
plt.ylabel('Percentage')


plt.ylim(0, 1)


plt.tight_layout()
plt.show()