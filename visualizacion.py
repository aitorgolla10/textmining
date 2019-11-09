import matplotlib.pyplot as plt

class Visualizacion():

    def visualizarClusters(self, clustersTodos):

        plt.plot([0.1, 0.2, 0.3, 0.4], [1, 2, 3, 4], label='first plot')
        plt.plot([0.1, 0.2, 0.3, 0.4], [1, 4, 9, 16], label='second plot')
        plt.legend()

    if __name__ == '__main__':
        visualizarClusters()