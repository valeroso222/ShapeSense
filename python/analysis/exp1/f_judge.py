import numpy as np
import pandas as pd
import scipy as sp
from scipy import stats
from statistics import mean, median,variance,stdev
import math



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

    return output_ave

def f_judge(data):
    data = pd.DataFrame({
        "x": data[0][1::],
        "y": data[1][1::]
    })
    #1標本の場合
    #res = stats.ttest_asamp(data.x,0)
    #対応のある場合
    #res = stats.ttest_rel(data.x,data.y)
    #対応がなく分散が等しい場合
    res = stats.ttest_ind(data.x, data.y, equal_var=True)[1]
    #対応がなく分散が異なる場合
    #res = stats.ttest_ind(data.x, data.y, equal_var=False)
    #print(data)
    x_mean=mean(data.x)
    y_mean=mean(data.y)
    print(x_mean,y_mean)
    vx=data.var()[0]
    vy=data.var()[1]
    print(vx,vy)
    d=abs(x_mean-y_mean)/math.sqrt((vx+vy)/2)
    
    
    return res, d

def effect_size(data):
    x=data[0]
    y=data[1]
    print(x)
    print(y)
    x_mean=mean(x)
    y_mean=mean(y)
    print(x_mean,y_mean)
    vx=variance(x)
    vy=variance(y)
    d=abs(x_mean-y_mean)/math.sqrt((vx+vy)/2)
    return d

if __name__ == "__main__":
    featuer_names = ['Area','Mheight','Mwidth','cog','Moment_u','Moment_v']
    
    #A6D1_label = ['A6', 'D1']
    #A5D2_label = ['A5', 'D2']
    #A3D3_label = ['A3', 'D3']
    #labels = [A6D1_label, A5D2_label, A3D3_label]
    #labels = [A3D3_label]
    
    A3B1_label = ['A3', 'B1']
    labels = [A3B1_label]
    

    result_list = []
    p_list = []
    d_list = []
    
    for j in range(len(featuer_names)):
        result_list.append([])
        p_list.append([])
        d_list.append([])
        csv = read_csv('data/'+featuer_names[j]+'.csv')
        for i in range(len(labels)):
            data = get_out_in(csv, labels[i])
            data = np.array(data).T
            p,d = f_judge(data)
            p_list[j].append(int(round(p*50)))
            d_list[j].append(d*100)
            if p < 0.1:
                result_list[j].append('diff')
                #print(data)
            else:
                result_list[j].append('same')
                #print(data)
    """
    csv = read_csv('data/'+featuer_names[3]+'.csv')
    data = get_out_in(csv, labels[0])
    data = np.array(data).T
    print(f_judge(data))
    """
    print(result_list)
    print(p_list)
    print(d_list)
    
