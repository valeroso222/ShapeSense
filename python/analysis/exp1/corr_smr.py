# python correation.py data/area.csv 'Area'
# python correation.py data/max_width.csv 'Mwidth'
# python correation.py data/max_height.csv 'Mheight'
# python correation.py data/cog.csv 'cog'
 
import sys
import pandas as pd
 
import numpy as np
import matplotlib.pyplot as plt

import smr_test
 
A_label = ['A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8']
B_label = ['B1', 'A3']
C_label = ['C1', 'C2', 'C3']
D_label = ['D1', 'D2', 'D3']
DA_label= ['A6', 'A5', 'A3']
A5678_label = [ 'A5', 'A6', 'A7', 'A8']
All_label = ['A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8', 'B1', 'C1', 'C2', 'C3', 'D1', 'D2', 'D3']
 
 
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

    return output_ave, input
 
 
def save_graph(inp, out, feature_name, axlabel1, axlabel2, show_graph=False):
    #print(out)
    #print(inp)
    sum, sum_grad = 0, 0
    plt.figure(figsize=(3,3))
    #plt.clf()
    smr_list = smr(out)
    smr_inp, smr_out = [], []
    for i in range(len(out)):
        tmp_inp, tmp_out = list(inp), list(out[i])
        for smr_lst in smr_list[i][::-1]:
            tmp_inp.pop(smr_lst)
            tmp_out.pop(smr_lst)
        smr_inp.extend(tmp_inp)
        smr_out.extend(tmp_out)
        cor = np.corrcoef(inp, out[i])[0,1]
        sum+=cor
        grad = np.polyfit(inp, out[i],1)[0]
        sum_grad+=grad
        if i!=len(out)-1:
            plt.plot(inp, out[i], "o", label='p'+str(i+1)+':  '+'{: .2f}'.format(round(cor,2))+', '+'{: .2f}'.format(round(grad,2)))
        else:
            plt.plot(inp, out[i], "o", label='p'+str(i+1)+':'+'{: .2f}'.format(round(cor,2))+', '+'{: .2f}'.format(round(grad,2)))
    corre = np.corrcoef(smr_inp, smr_out)[0,1]
    grad = np.polyfit(smr_inp, smr_out, 1)[0]
    sum=sum/len((out))
    sum_grad=sum_grad/len((out))

    plt.xlabel(axlabel1 + ' of actual shape ' + axlabel2)
    plt.ylabel(axlabel1 + ' of virtual shape ' + axlabel2)
    xmin, xmax = plt.xlim()
    ymin, ymax = plt.ylim()
    ax_max = max(xmax, ymax)
    plt.xlim(0, ax_max)
    plt.ylim(0, ax_max)
    plt.legend(loc='upper left', bbox_to_anchor=(1.05,1), borderaxespad=0.,)
 
    plt.title(feature_name + ' corre:{:.2f} grad:{:.2f}'.format(corre, grad))
    plt.savefig('smr/' + feature_name + '.jpg', bbox_inches='tight',dpi=300)
    if show_graph:
        plt.show()
    #plt.clf()
    plt.close()

def smr(data):
    data = np.array(data).T
    res = [[] for i in range(data.shape[1])]
    for i in range(data.shape[0]):
        x,o,xi,oi = smr_test.smirnov_grubbs(data[i],0.01)
        for oii in sorted(oi):
            res[oii].append(i)
        #print(x,o,xi,oi)
    #print(res)
    return res


def main_each(path, feature_name, axlabel1, axlabel2):
    csv = read_csv(path)
    #print(csv)

    labels = [A_label, B_label, C_label, D_label, All_label, A5678_label]
    label_names = ['A', 'B', 'C', 'D', 'All', 'A\'']
    #labels = [A5678_label]
    #label_names = ['A\'']

    for i in range(len(labels)):
        output_ave, input = get_out_in(csv, labels[i])
        title = feature_name + label_names[i]
        save_graph(input, output_ave, title, axlabel1, axlabel2)
    
    

if __name__ == '__main__':
    
    main_each('data/Area.csv','Area', "Area", "$\mathrm{[cm^{2}]}$" )
    
    main_each('data/cog.csv','cog', "CoG", "$\mathrm{[cm]}$" )
    main_each('data/Mheight.csv','Mheight', "Height", "$\mathrm{[cm]}$" )
    main_each('data/Mwidth.csv','Mwidth', "Width", "$\mathrm{[cm]}$" )
    main_each('data/Moment_u.csv','Moment_u', "$\mathrm{I_{u}}$", "$\mathrm{[cm^{4}]}$" )
    
    main_each('data/Moment_v.csv','Moment_v', "$\mathrm{I_{v}}$", "$\mathrm{[cm^{2}]}$" )
    