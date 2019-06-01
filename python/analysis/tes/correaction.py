
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
 
 
def get_out_in(data, label):
    output = data[1:][label].values
    output_all = []
    #print(output)
    output_ave = []
    for i in range(0,len(output),2):
        output_ave.append([int((x+y)/2) for (x,y) in zip(output[i],output[i+1])])
        output_all.append(np.hstack((output[i],output[i+1])))
    #print(output_ave)
 
    input = data[0:1][label].values[0]
    #print(input)

    return output_all, output_ave, input
 
 
def save_graph(inp, out, corre_str, graph_title, file_name, correaction_List, show_graph=True):
    #print(out)
    #print(inp)
    sum=0
    plt.figure(figsize=(3,3))
    #plt.clf()
    for i in range(len(out)):
        cor = np.corrcoef(out[i],inp)[0,1]
        sum+=cor
        plt.plot(inp, out[i], "o", label='p'+str(i+1)+'; '+str(round(cor,2)))
        if(cor==cor):
            correaction_List[i].append(cor)
    sum=sum/len((out))
    if(sum==sum):
        correaction_List[len(out)].append(sum)

    plt.xlabel('input')
    plt.ylabel('output')
    xmin, xmax = plt.xlim()
    ymin, ymax = plt.ylim()
    ax_max = max(xmax, ymax)
    plt.xlim(0, ax_max)
    plt.ylim(0, ax_max)
    #plt.axes().set_aspect('equal', 'datalim')
    plt.legend(loc='upper left', bbox_to_anchor=(1.05,1), borderaxespad=0.,)
 
    # plt.text(50, 220, corre_str, fontsize=10)
 
    plt.title(str(corre_str)+' ave: '+ str(round(sum,2)))
    plt.savefig(file_name, bbox_inches='tight')
    if show_graph:
        plt.show()
    #plt.clf()
 

def main_each(path, feature_name):
    #mean = np.array([0, 0])
 
    csv = read_csv(path)
    #print(csv)
 
    # A
    print('A---------------------------------------------------')
    output_all, output_ave, input = get_out_in(csv, A_label)

    corre_str = 'Correation_ave(A): %.3f' % np.corrcoef(output_ave, input)[0, 1]
    save_graph(input, output_ave, corre_str, feature_name, 'fig/' + feature_name + '_ave_A.jpg', correaction_List_ave)
    #corre_str = 'Correation_all(A): %.3f' % np.corrcoef(output_all, np.hstack((input,input)))[0, 1]
    #save_graph(np.hstack((input,input)), output_all, corre_str, feature_name, 'fig/' + feature_name + '_all_A.jpg', correaction_List_all)
    
    # B
    print('B---------------------------------------------------')
    output_all, output_ave, input = get_out_in(csv, B_label)
 
    corre_str = 'Correation_ave(B): %.3f' % np.corrcoef(output_ave, input)[0, 1]
    save_graph(input, output_ave, corre_str, feature_name, 'fig/' + feature_name + '_ave_B.jpg', correaction_List_ave)
    #corre_str = 'Correation_all(B): %.3f' % np.corrcoef(output_all, np.hstack((input,input)))[0, 1]
    #save_graph(np.hstack((input,input)), output_all, corre_str, feature_name, 'fig/' + feature_name + '_all_B.jpg', correaction_List_all)
 
    # C
    print('C---------------------------------------------------')
    output_all, output_ave, input = get_out_in(csv, C_label)
 
    corre_str = 'Correation_ave(C): %.3f' % np.corrcoef(output_ave, input)[0, 1]
    save_graph(input, output_ave, corre_str, feature_name, 'fig/' + feature_name + '_ave_C.jpg', correaction_List_ave)
    #corre_str = 'Correation_all(C): %.3f' % np.corrcoef(output_all, np.hstack((input,input)))[0, 1]
    #save_graph(np.hstack((input,input)), output_all, corre_str, feature_name, 'fig/' + feature_name + '_all_C.jpg', correaction_List_all)
    
    
if __name__ == '__main__':
    N = 10
    correaction_List_ave = [[] for i in range(N+1)]
    correaction_List_all = [[] for i in range(N+1)]

    main_each('data/Area.csv', 'Area')
    
    main_each('data/cog.csv', 'cog')
    main_each('data/Mheight.csv', 'Mheight')
    main_each('data/Mwidth.csv', 'Mwidth')
    main_each('data/Moment_u.csv', 'Moment_u')
    main_each('data/Moment_v.csv', 'Moment_v')
    
    
    print(correaction_List_ave)
    #print(correaction_List_all)
