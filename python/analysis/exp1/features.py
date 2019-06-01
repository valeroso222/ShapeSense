import sys
import pandas as pd
 
import numpy as np
from scipy import integrate
import matplotlib.pyplot as plt
import csv
import show_shape
import cshape


def read_csv(path, units=3, isPlot=False):
    csv = np.round(pd.read_csv(path).values * 100)
    plot_datas = []
    Area = []
    cog = []
    Mheight = []
    Mwidth = []
    Moment_u = []
    Moment_v = []
    for i in range(csv.shape[0]):
        plot_data = np.zeros([50,50])
        for j in range(csv.shape[1]):
            #print(i,j)
            #nan to 0
            if(csv[i][j]!=csv[i][j]):
                csv[i][j]=0
            for l in range(units):
                for n in range(int(round((50-csv[i][j])/2)),int(round((50+csv[i][j])/2))):
                    #print(l,n)
                    plot_data[units*j+l][n] = 1
        plot_datas.append(plot_data)
        tmp_area, tmp_cog, tmp_Mheight, tmp_Mwidth, tmp_moment_u, tmp_moment_v = calc_features(csv[i],plot_data,units)
        Area.append(tmp_area)
        cog.append(tmp_cog)
        Mheight.append(tmp_Mheight)
        Mwidth.append(tmp_Mwidth)
        Moment_u.append(tmp_moment_u)
        Moment_v.append(tmp_moment_v)
    all_plot_datas.append(plot_datas)
    if isPlot:
        show_shape.plot_shape_one_person(plot_datas, all_plot_datas)
    return [Area, cog, Mheight, Mwidth, Moment_u, Moment_v]
    
def calc_features(csv,plot_data,units):
    offset = 6.5
    Area = np.sum(csv)*units
    cog = 0
    Mheight = offset
    Mwidth = np.amax(csv)
    Moment_u = 0
    Moment_v = 0
    for i in range(csv.shape[0]):
        cog += csv[i]*units*(i*units+units/2.0)
        if(csv[i]>1):
            Mheight = units*(i+1)+offset
        Moment_u += integrate.quad(lambda x: csv[i]*(i*units+x+offset)**2, 0, units)[0]
        Moment_v += integrate.quad(lambda x: units*x**2*2, 0, csv[i]/2)[0]
    cog = cog/Area + offset
    return [Area, cog, Mheight, Mwidth, Moment_u, Moment_v]

def write_csv(path, file_name, p_name):
    #読み込みcsv_lsit=[Area,cog,Mheight,Mwidth,Moment_u,Moment_v]
    if p_name=='input':
        csv_list = read_csv(path,isPlot=False)
    else:
        csv_list = read_csv(path,isPlot=False)
    #書き込み
    
    for i in range(len(file_name)):
        with open('data/'+file_name[i]+'.csv', 'a') as f:
            csvWriter = csv.writer(f, lineterminator='\n')
            csvWriter.writerow([p_name]+csv_list[i][:15])
            if (p_name!='input'):
                csvWriter.writerow([p_name]+csv_list[i][15:])
    


if __name__ == '__main__':
    param_name = ['Area','cog','Mheight','Mwidth','Moment_u','Moment_v']
    all_plot_datas = []
    #1行目の書き込み
    
    for i in range(len(param_name)):
        with open('data/'+param_name[i]+'.csv', 'w') as f:
            csvWriter = csv.writer(f, lineterminator='\n')
            csvWriter.writerow(['Device-ID','A1','A2','A3','A4','A5','A6','A7','A8','B1', 'C1','C2','C3','D1','D2','D3'])
    
    write_csv('raw_data/answer.csv', param_name, 'input')
    write_csv('raw_data/ichimura.csv', param_name, 'p1')
    write_csv('raw_data/kobatake.csv', param_name, 'p2')
    write_csv('raw_data/morita.csv', param_name, 'p3')
    write_csv('raw_data/nakagawa.csv', param_name, 'p4')
    write_csv('raw_data/sato.csv', param_name, 'p5')
    write_csv('raw_data/shimoyama.csv', param_name, 'p6')
    write_csv('raw_data/sugimoto.csv', param_name, 'p7')
    write_csv('raw_data/takahashi.csv', param_name, 'p8')
    write_csv('raw_data/yamamoto.csv', param_name, 'p9')
    write_csv('raw_data/yokoo.csv', param_name, 'p10')
    
    show_shape.plot_shape_all_person(all_plot_datas)
    #cshape.main_CShape(all_plot_datas)