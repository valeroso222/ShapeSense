import numpy as np
import matplotlib.pyplot as plt

def conv_to_RGB(data):
    list = [[]for i in range(data.shape[0])]
    for i in range(data.shape[0]):
        for j in range(data.shape[1]):
            color = 1.0 - data[i][j]
            list[i].append([color, color, color])
    return list[::-1]

def Overlay_one_C(plot_datas):
    num = len(plot_datas)
    #print(len(plot_datas[0][0]))
    c_plot_data = []
    for i in range(len(plot_datas[0])):
        c_plot_data.append([])
        for j in range(len(plot_datas[0][0])):
            color = sum([plot_datas[l][i][j] for l in range(num)])/num
            c_plot_data[i].append(color)
    #plt.imshow(conv_to_RGB(np.array(c_plot_data)))
    #plt.show()
    return c_plot_data

def plot_all_c(cis):
    num = len(cis)
    row = int(num/2)
    print(num,row)
    fig = plt.figure()
    for j in range(2):
        for i in range(row):
            ax = fig.add_subplot(2,num/2,i+j*row+1)
            ax.imshow(conv_to_RGB(np.array(cis[j+i*2])))
            ax.axis('off')
    plt.show()
    

def main_CShape(all_plot_datas):
    c_start = 13
    c_end = 18
    one_set = 19
    cis = []
    for i in range(c_start,c_end+1):
        ci = []
        cis.append(all_plot_datas[0][i])
        for j in range(10):
            ci.append(all_plot_datas[j+1][i])
            ci.append(all_plot_datas[j+1][i+one_set])
        cis.append(Overlay_one_C(ci))
    plot_all_c(cis)