
# python correation.py data/area.csv 'Area'
# python correation.py data/max_width.csv 'Mwidth'
# python correation.py data/max_height.csv 'Mheight'
# python correation.py data/cog.csv 'cog'
 
import sys
import pandas as pd
 
import numpy as np
import matplotlib.pyplot as plt
 
A_label = ['A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8']
B_label = ['B1', 'A3']
C_label = ['C1', 'C2', 'C3']
D_label = ['D1', 'D2', 'D3']
DA_label= ['A6', 'A5', 'A3']
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

    return output_all, output_ave, input
 
 
def save_graph(inp, out, corre_str, graph_title, file_name, Correlation_List=[], show_graph=False):
    #print(out)
    #print(inp)
    sum=0
    sum_grad=0
    plt.figure(figsize=(3,3))
    #plt.clf()
    for i in range(len(out)):
        cor = np.corrcoef(inp,out[i])[0,1]
        sum+=cor
        grad = np.polyfit(inp, out[i],1)[0]
        sum_grad+=grad
        if i!=len(out)-1:
            plt.plot(inp, out[i], "o", label='p'+str(i+1)+':  '+'{: .2f}'.format(round(cor,2))+', '+'{: .2f}'.format(round(grad,2)))
        else:
            plt.plot(inp, out[i], "o", label='p'+str(i+1)+':'+'{: .2f}'.format(round(cor,2))+', '+'{: .2f}'.format(round(grad,2)))
        if(cor==cor):
            Correlation_List[i].append(cor)
    sum=sum/len((out))
    sum_grad=sum_grad/len((out))
    if(sum==sum):
        Correlation_List[len(out)].append(sum)

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
 
    plt.title(str(corre_str)+' ave:{:.2f} {:.2f}'.format(sum,sum_grad))
    plt.savefig(file_name, bbox_inches='tight')
    if show_graph:
        plt.show()
    #plt.clf()
    plt.close()

def Compare(csv,in_label,out_label,file_name,graph_title):
    a,input,b = get_out_in(csv, in_label)
    a,output,b = get_out_in(csv, out_label)
    input=np.array(input).flatten()
    output=np.array(output).flatten()
    corre = np.corrcoef(input,output)[0,1]
    grad = np.polyfit(input,output,1)[0]
    corre_str = graph_title +'{:.2f} {:.2f}'.format(corre,grad)
    plt.figure(figsize=(3,3))
    plt.plot(input,output,'o')
    xmin, xmax = plt.xlim()
    ymin, ymax = plt.ylim()
    ax_max = max(xmax, ymax)
    plt.xlim(0, ax_max)
    plt.ylim(0, ax_max)
    plt.title(str(corre_str))
    plt.savefig(file_name, bbox_inches='tight')
    plt.show()
 

def main_each(path, feature_name):
    #mean = np.array([0, 0])
 
    csv = read_csv(path)
    #print(csv)
    '''
    # A
    #print('A---------------------------------------------------')
    output_all, output_ave, input = get_out_in(csv, A_label)

    corre = np.corrcoef(np.reshape(np.array([input for i in range(len(output_ave))]),(1,-1)),np.array(output_ave).flatten())[0,1]
    grad = np.polyfit(np.reshape(np.array([input for i in range(len(output_ave))]),(1,-1)).flatten(),np.array(output_ave).flatten(),1)[0]
    corre_str = 'Correlation_ave(A): '+'{:.2f} {:.2f}'.format(corre,grad)
    save_graph(input, output_ave, corre_str, feature_name, 'fig_ave/' + feature_name + '_ave_A.jpg', Correlation_List_ave)
    input = np.hstack((input,input))
    corre = np.corrcoef(np.reshape(np.array([input for i in range(len(output_all))]),(1,-1)),np.array(output_all).flatten())[0,1]
    grad = np.polyfit(np.reshape(np.array([input for i in range(len(output_all))]),(1,-1)).flatten(),np.array(output_all).flatten(),1)[0]
    corre_str = 'Correlation_all(A): '+'{:.2f} {:.2f}'.format(corre,grad)
    save_graph(input, output_all, corre_str, feature_name, 'fig/' + feature_name + '_all_A.jpg', Correlation_List_all)
    
    # B
    #print('B---------------------------------------------------')
    output_all, output_ave, input = get_out_in(csv, B_label)

    corre = np.corrcoef(np.reshape(np.array([input for i in range(len(output_ave))]),(1,-1)),np.array(output_ave).flatten())[0,1]
    grad = np.polyfit(np.reshape(np.array([input for i in range(len(output_ave))]),(1,-1)).flatten(),np.array(output_ave).flatten(),1)[0]
    corre_str = 'Correlation_ave(B): '+'{:.2f} {:.2f}'.format(corre,grad)
    save_graph(input, output_ave, corre_str, feature_name, 'fig_ave/' + feature_name + '_ave_B.jpg', Correlation_List_ave)
    input = np.hstack((input,input))
    corre = np.corrcoef(np.reshape(np.array([input for i in range(len(output_all))]),(1,-1)),np.array(output_all).flatten())[0,1]
    grad = np.polyfit(np.reshape(np.array([input for i in range(len(output_all))]),(1,-1)).flatten(),np.array(output_all).flatten(),1)[0]
    corre_str = 'Correlation_all(B): '+'{:.2f} {:.2f}'.format(corre,grad)
    save_graph(input, output_all, corre_str, feature_name, 'fig/' + feature_name + '_all_B.jpg', Correlation_List_all)
    
    # C
    #print('C---------------------------------------------------')
    output_all, output_ave, input = get_out_in(csv, C_label)
 
    corre = np.corrcoef(np.reshape(np.array([input for i in range(len(output_ave))]),(1,-1)),np.array(output_ave).flatten())[0,1]
    grad = np.polyfit(np.reshape(np.array([input for i in range(len(output_ave))]),(1,-1)).flatten(),np.array(output_ave).flatten(),1)[0]
    corre_str = 'Correlation_ave(C): '+'{:.2f} {:.2f}'.format(corre,grad)
    save_graph(input, output_ave, corre_str, feature_name, 'fig_ave/' + feature_name + '_ave_C.jpg', Correlation_List_ave)
    input = np.hstack((input,input))
    corre = np.corrcoef(np.reshape(np.array([input for i in range(len(output_all))]),(1,-1)),np.array(output_all).flatten())[0,1]
    grad = np.polyfit(np.reshape(np.array([input for i in range(len(output_all))]),(1,-1)).flatten(),np.array(output_all).flatten(),1)[0]
    corre_str = 'Correlation_all(C): '+'{:.2f} {:.2f}'.format(corre,grad)
    save_graph(input, output_all, corre_str, feature_name, 'fig/' + feature_name + '_all_C.jpg', Correlation_List_all)
    
    # D
    #print('D---------------------------------------------------')
    output_all, output_ave, input = get_out_in(csv, D_label)
    
    corre = np.corrcoef(np.reshape(np.array([input for i in range(len(output_ave))]),(1,-1)),np.array(output_ave).flatten())[0,1]
    grad = np.polyfit(np.reshape(np.array([input for i in range(len(output_ave))]),(1,-1)).flatten(),np.array(output_ave).flatten(),1)[0]
    corre_str = 'Correlation_ave(D): '+'{:.2f} {:.2f}'.format(corre,grad)
    save_graph(input, output_ave, corre_str, feature_name, 'fig_ave/' + feature_name + '_ave_D.jpg', Correlation_List_ave)
    '''
    '''
    input = np.hstack((input,input))
    corre = np.corrcoef(np.reshape(np.array([input for i in range(len(output_all))]),(1,-1)),np.array(output_all).flatten())[0,1]
    grad = np.polyfit(np.reshape(np.array([input for i in range(len(output_all))]),(1,-1)).flatten(),np.array(output_all).flatten(),1)[0]
    corre_str = 'Correlation_all(D): '+'{:.2f} {:.2f}'.format(corre,grad)
    save_graph(input, output_all, corre_str, feature_name, 'fig/' + feature_name + '_all_D.jpg', Correlation_List_all)

    # All
    #print('All---------------------------------------------------')
    output_all, output_ave, input = get_out_in(csv, All_label)
 
    corre = np.corrcoef(np.reshape(np.array([input for i in range(len(output_ave))]),(1,-1)),np.array(output_ave).flatten())[0,1]
    grad = np.polyfit(np.reshape(np.array([input for i in range(len(output_ave))]),(1,-1)).flatten(),np.array(output_ave).flatten(),1)[0]
    corre_str = 'Correlation_ave(All): '+'{:.2f} {:.2f}'.format(corre,grad)
    save_graph(input, output_ave, corre_str, feature_name, 'fig_ave/' + feature_name + '_ave_All.jpg', Correlation_List_ave)
    input = np.hstack((input,input))
    corre = np.corrcoef(np.reshape(np.array([input for i in range(len(output_all))]),(1,-1)),np.array(output_all).flatten())[0,1]
    grad = np.polyfit(np.reshape(np.array([input for i in range(len(output_all))]),(1,-1)).flatten(),np.array(output_all).flatten(),1)[0]
    corre_str = 'Correlation_all(All): '+'{:.2f} {:.2f}'.format(corre,grad)
    save_graph(input, output_all, corre_str, feature_name, 'fig/' + feature_name + '_all_All.jpg', Correlation_List_all)
    '''

    Compare(csv,['A6', 'A5', 'A3'],D_label,'fig_DA/'+feature_name+'_ave_DA.jpg','Correlation(DA): ')
    
if __name__ == '__main__':
    N = 10
    Correlation_List_ave = [[] for i in range(N+1)]
    Correlation_List_all = [[] for i in range(N+1)]

    main_each('data/Area.csv', 'Area')
    
    main_each('data/cog.csv', 'cog')
    main_each('data/Mheight.csv', 'Mheight')
    main_each('data/Mwidth.csv', 'Mwidth')
    main_each('data/Moment_u.csv', 'Moment_u')
    main_each('data/Moment_v.csv', 'Moment_v')
    
    
    #print(Correlation_List_ave)
    #print(Correlation_List_all)
