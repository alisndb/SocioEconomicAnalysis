import matplotlib.pyplot as plt
from IPython.display import display, HTML


class DataViewer:
    FOOTER = 'Рассчитано по данным Федеральной службы государственной статистики (Росстат).'

    def __init__(self):
        pass

    @staticmethod
    def plot_data(data, mode, header):
        assert mode in ('region', 'all'), 'Incorrect mode!'

        fig, ax1 = plt.subplots(figsize=(10, 6))

        styles = ['k--', 'k-']
        regions = data['Регион']

        if mode == 'all':
            ax1.plot(data.columns[1:], data.iloc[0, 1:].values, styles[0], label=regions[0])
            ax1.set_ylabel('Значения для ' + regions[0], color='k')

        ax1.tick_params(axis='y', labelcolor='k')
        ax1.set_xlabel('Годы')
        ax1.grid()

        ax2 = ax1.twinx()
        ax2.plot(data.columns[1:], data.iloc[1, 1:].values, styles[1], label=regions[1])
        ax2.set_ylabel('Значения для ' + regions[1], color='k')
        ax2.tick_params(axis='y', labelcolor='k')

        plt.suptitle(f'Рис. {header}', y=-0.01, fontsize='medium')

        lines, labels = ax1.get_legend_handles_labels()
        lines2, labels2 = ax2.get_legend_handles_labels()
        ax2.legend(lines + lines2, labels + labels2, loc='upper center', bbox_to_anchor=(0.5, -0.15), ncol=2)

        plt.tight_layout()
        plt.show()

    def display_data(self, header, data):
        display(HTML(f'Таблица. {header}'))
        display(data)
        display(HTML(self.FOOTER))
