import numpy as np
from scipy import integrate
import matplotlib.pyplot as plt
import math


def omegaf(f,theta_max,t):
    return np.array([theta_max*(-2*pi*f)*math.sin(2*pi*f*ti) for ti in t])


def alphaf(f,theta_max,t):
    return np.array([theta_max*(-4*pi**2*f**2)*math.cos(2*pi*f*ti) for ti in t])


def calc_interia(dev_ftr):
    h,w,m,l = dev_ftr[0], dev_ftr[1], dev_ftr[2], dev_ftr[3]
    return 1.0/12*m*(h**2)+m*(l+h/2)**2


def calc_air(dev_ftr, omega):
    h,w,m,l = dev_ftr[0], dev_ftr[1], dev_ftr[2], dev_ftr[3]
    c = 1.2 #抗力係数
    lo = 1.2 #空気密度
    Moment_u = integrate.quad(lambda u, omega: w*u**2*omega**2*c*lo/2, l, l+h, args=omega)[0]
    return Moment_u


def plot_list(f,theta_max,dev_ftr_list):
    t = np.arange(0,0.5/f,0.5/f/100)
    alpha = alphaf(f,theta_max,t)
    omega = omegaf(f,theta_max,t)
    fig_line = len(dev_ftr_list)
    fig = plt.figure(figsize=(6,8))
    fig_row_max = 3
    for l in range(fig_line):
        fig_row = len(dev_ftr_list[l])
        for i in range(fig_row):
            moment_from_interia = calc_interia(dev_ftr_list[l][i])*alpha
            vec_calc_air = np.vectorize(calc_air)
            vec_calc_air.excluded.add(0)
            moment_from_air = vec_calc_air(dev_ftr_list[l][i], omega)
            ax = fig.add_subplot(fig_line,fig_row_max,l*fig_row_max+i+1)
            ax.plot(t,abs(moment_from_interia),'o',label='inertia',markersize=2)
            ax.plot(t,abs(moment_from_air),'o',label='air',markersize=2)
            ax.set_title(titles[l][i])
            plt.xlabel('time[sec]')
            plt.ylabel('moment(abs)[Nm]')
    plt.tight_layout()
    plt.savefig('res/f{}th{:.0f}.jpg'.format(f,theta_max/pi*180))
    plt.show()

def plot(f,theta_max,dev_ftr):
    t = np.arange(0,0.5/f,0.5/f/100)
    alpha = alphaf(f,theta_max,t)
    omega = omegaf(f,theta_max,t)
    fig = plt.figure(figsize=(3,3))
    moment_from_interia = calc_interia(dev_ftr)*alpha
    vec_calc_air = np.vectorize(calc_air)
    vec_calc_air.excluded.add(0)
    moment_from_air = vec_calc_air(dev_ftr, omega)
    plt.plot(t,abs(moment_from_interia),'o',label='inertia',markersize=2)
    plt.plot(t,abs(moment_from_air),'o',label='air',markersize=2)
    plt.title(title)
    plt.xlabel('time[sec]')
    plt.ylabel('moment(abs)[Nm]')
    plt.tight_layout()
    plt.legend()
    plt.xlim(0,)
    plt.ylim(0,)
    plt.savefig('res/f{}th{:.0f}.jpg'.format(f,theta_max/pi*180),dpi=300)
    plt.show()


if __name__ == '__main__':

    '''
    デバイスの特徴量をdev_ftr = [縦h(m), 幅w(m), 質量m(kg), 底辺の原点との距離l(m)]で表す
    例えば、全面は[0.27, 0.16, 0.1, 0.015]
    角速度はomega(rad/s)角加速度はalpha(rad/s^2)とすると、振動数f(HZ)と定数alpha_max(rad/s^2)を用いて
    omega = alpha_max/(2*pi*f)*sin(2*pi*f*t)
    alpha = alpha_max*cos(2*pi*f*t)
    ->alpha_maxのかわりにtheta_max(rad)を使うと
    theta = theta_max*cos(2*pi*f*t)
    omega = theta_max*(-2*pi*f)*sin(2*pi*f*t)
    alpha = theta_max*(-4*pi**2*f**2)*cos(2*pi*f*t)
    '''
    pi = math.pi
    f = 2
    alpha_max = 200
    theta_max = 1.0/3*pi
    
    dev_ftr_list = [[[0.09, 0.32, 0.15, 0.015], [0.09, 0.32, 0.15, 0.105], [0.09, 0.32, 0.15, 0.195]],
                    [[0.135, 0.32, 0.15, 0.015], [0.135, 0.32, 0.15, 0.15], [0.135, 0.32, 0.15, 0.2175]],
                    [[0.18, 0.32, 0.15, 0.015], [0.18, 0.32, 0.15, 0.105], [0.18, 0.32, 0.15, 0.195]],
                    [[0.27, 0.32, 0.15, 0.015]]]
    titles = [['A1', 'A2', 'A3'],
              ['B1', 'B2', 'B3'],
              ['C1', 'C2', 'C3'],
              ['D1']]
    
    #dev_ftr = [0.27, 0.32, 0.15, 0.05]
    dev_ftr = [0.30, 0.30, 0.1, 0.05]
    title = 'Moment on hand per time'
    plot(f,theta_max,dev_ftr)