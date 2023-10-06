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

    @staticmethod
    def plot_pie_charts(data, header):
        years = data['Год'].unique()
        regions = ['Российская Федерация', 'г. Москва']

        for year in years:
            fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

            for region in regions:
                filtered_data = data[(data['Год'] == year) & (data['Регион'] == region)]
                labels = filtered_data.columns[2:]
                sizes = filtered_data.iloc[0, 2:]

                if region == 'Российская Федерация':
                    ax = ax1
                else:
                    ax = ax2

                ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
                ax.axis('equal')
                ax.set_title(region)

            plt.suptitle(f'Рис. {header} - {year}', y=-0.01, fontsize='medium')

            plt.tight_layout()
            plt.show()

    @staticmethod
    def plot_ratios(data, header):
        fig, ax = plt.subplots(figsize=(10, 6))

        for column in data.columns[1:]:
            if column != 'Год':
                ax.plot(data['Год'], data[column], label=column)

        ax.set_xlabel('Годы')
        ax.set_ylabel('Отношение Москва/Россия')
        ax.grid()
        ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.15), ncol=2)
        plt.suptitle(f'Рис. {header}', y=-0.01, fontsize='medium')

        plt.tight_layout()
        plt.show()

    def display_data(self, header, data):
        display(HTML(f'Таблица. {header}'))
        display(data)
        display(HTML(self.FOOTER))
