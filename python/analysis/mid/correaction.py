
# python correation.py data/area.csv 'Area'
# python correation.py data/max_width.csv 'Mwidth'
# python correation.py data/max_height.csv 'Mheight'
# python correation.py data/cog.csv 'cog'
 
import sys
import pandas as pd
 
import numpy as np
import matplotlib.pyplot as plt
 
A_label = ['A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8', 'A9', 'A10']
B_label = ['B1', 'B2', 'B3', 'A4']
C_label = ['C1', 'C2', 'C3', 'C4', 'C5', 'C6']
 
 
def read_csv(path):
    csv = pd.read_csv(path, index_col=0)
    # print(csv)
    return csv
 
 
def get_xy_with_label(data, label):
    subdata = data[1:22][label]  # p1-p10
    #print(subdata)
 
    input = data[0:1][label].values[0]
    x = []  # input  (Stimuli)
    y = []  # output (Participants answers)
    #print(input)
 
    # print(len(subdata))
    # print(len(subdata.columns))
    # Calc average of two measured values from each participant
    for i in range(0, len(subdata), 2):
        for j in range(0, len(subdata.columns)):
            # print(subdata.values[i][j])
            # print(subdata.values[i + 1][j])
            p_avg = (subdata.values[i][j] + subdata.values[i + 1][j]) * 0.5
            y.append(p_avg)
            x.append(input[j])
 
    return x, y
 
 
def save_graph(x, y, num, corre_str, graph_title, file_name, show_graph=False):
    sort_order = np.argsort(np.array(x[:num]))
    i=0
    sum=0
    for i in range(10):
        x_i = np.array(x[i*num:(i+1)*num])[sort_order]
        y_i = np.array(y[i*num:(i+1)*num])[sort_order]
        #print(x_i,y_i)
        #print('p'+str(i+1)+': '+str(np.corrcoef(x_i,y_i)[0,1]))
        cor = np.corrcoef(x_i,y_i)[0,1]
        sum+=cor
        plt.plot(x_i, y_i, "o", label='p'+str(i+1)+'; '+str(round(cor,2)))
        if(cor==cor):
            correaction_List[i].append(cor)
    sum=sum/10
    if(sum==sum):
        correaction_List[10].append(sum)

    plt.xlabel('input')
    plt.ylabel('output')
    plt.legend(loc='upper left', bbox_to_anchor=(1.05,1), borderaxespad=0.,)
 
    # plt.text(50, 220, corre_str, fontsize=10)
 
    plt.title(str(corre_str)+' ave: '+ str(round(sum,2)))
    plt.savefig(file_name, bbox_inches='tight')
    if show_graph:
        plt.show()
    plt.clf()
 
 

def main_each(path, name):
    #mean = np.array([0, 0])
 
    csv = read_csv(path)
    #print(csv)
 
    # A
    print('---------------------------------------------------')
    x, y = get_xy_with_label(csv, A_label)
    print('---------------------------------------------------')
 
    corre_str = 'Correation(A): %.3f' % np.corrcoef(x, y)[0, 1]
    print(corre_str)
    # print(np.corrcoef(x, y))
    save_graph(x, y, 10, corre_str, name, 'fig/' + name + '_A.jpg')
 
    # B
    print('---------------------------------------------------')
    x, y = get_xy_with_label(csv, B_label)
    print('---------------------------------------------------')
 
    corre_str = 'Correation(B): %.3f' % np.corrcoef(x, y)[0, 1]
    print(corre_str)
    save_graph(x, y, 4, corre_str, name, 'fig/' + name + '_B.jpg')
 
    # C
    print('---------------------------------------------------')
    x, y = get_xy_with_label(csv, C_label)
    print('---------------------------------------------------')
 
    corre_str = 'Correation(C): %.3f' % np.corrcoef(x, y)[0, 1]
    print(corre_str)
    save_graph(x, y, 6, corre_str, name, 'fig/' + name + '_C.jpg')
    
if __name__ == '__main__':
    correaction_List = [[] for i in range(11)]

    main_each('data/Area.csv', 'Area')
    main_each('data/cog.csv', 'cog')
    main_each('data/Mheight.csv', 'Mheight')
    main_each('data/Mwidth.csv', 'Mwidth')
    main_each('data/Moment_u.csv', 'Moment_u')
    main_each('data/Moment_v.csv', 'Moment_v')

    print(correaction_List)
