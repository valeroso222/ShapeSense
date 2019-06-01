import matplotlib.pyplot as plt

def conv_to_RGB(data):
    list = [[]for i in range(data.shape[0])]
    for i in range(data.shape[0]):
        for j in range(data.shape[1]):
            if data[i][j] == 1:
                list[i].append([0.0,0.0,0.0])
            else:
                list[i].append([1.0,1.0,1.0])
    return list[::-1]

def plot_shape_one_person(plot_datas, all_plot_datas):
    fig = plt.figure()
    for i in range(15):
        ax = fig.add_subplot(15,3,i*3+1)
        ax.imshow(conv_to_RGB(all_plot_datas[0][i]))
        ax.axis('off')
        for j in range(2):
            ax = fig.add_subplot(15,3,i*3+2+j)
            ax.imshow(conv_to_RGB(plot_datas[15*j+i]))
            ax.axis('off')
    plt.show()

def plot_shape_all_person(all_plot_datas):
    fig = plt.figure()
    fig_row = len(all_plot_datas)*2 - 1
    for i in range(15):
        ax = fig.add_subplot(15,fig_row,i*fig_row+1)
        ax.imshow(conv_to_RGB(all_plot_datas[0][i]))
        ax.axis('off')
        for p in range(len(all_plot_datas)-1):
            for j in range(2):
                ax = fig.add_subplot(15,fig_row,i*fig_row+1+p*2+j+1)
                ax.imshow(conv_to_RGB(all_plot_datas[p+1][15*j+i]))
                ax.axis('off')
    plt.show()