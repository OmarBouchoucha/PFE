from matplotlib import pyplot as plt

def plot(list1,list2,xlabel,title,label):
    plt.figure()
    plt.plot(list2, list1)
    plt.ylabel(xlabel)
    plt.yticks(rotation='vertical')
    plt.xlabel('Time')
    plt.title(title)
    plt.legend()
    plt.tight_layout()
    plt.savefig(f'C:\\Users\BOUCHOUCHA\Desktop\PFE\web app - original\web_server_with_flask\static\images\plotof{label}.png')