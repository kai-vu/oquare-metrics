import matplotlib.pyplot as plt
import matplotx

class oquareGraphs:

    def plot_oquare_values(self, data: dict, outputPath: str):
        names = list(data.keys())
        values = list(data.values())
        xpos = range(len(values))

        with plt.style.context(matplotx.styles.ayu["light"]):
            plt.rc('font', size=10)
            plt.ylim([0, 5])
            plt.bar(xpos, values)
            plt.xticks(xpos, names, fontsize=8, rotation=90)
            plt.gca().grid(True, which='major', axis='y', color='#888888', linestyle='--')
            plt.title('OQuaRE model values')
            plt.savefig(outputPath + '/temp_results/OQuaRE_model_values.png', format="png", bbox_inches='tight')
    
    def plot_oquare_categories(self, data: dict, fileName: str, basePath: str):

        names = list(data.keys())
        values = list(data.values())
        xpos = range(len(values))

        with plt.style.context(matplotx.styles.ayu["light"]):
            plt.ylim([0, 5])
            plt.bar(xpos, values)
            plt.xticks(xpos, names, fontsize=10, rotation=45)
            matplotx.show_bar_values("{:.2f}")
            plt.title('OQuaRE category values')
            plt.savefig(basePath + fileName + '/' + fileName + "category_values.png", format="png", bbox_inches='tight')

    def plot_historic(self, data: dict, date: str, outputPath: str):

        line_labels = list(data.keys())
        values = list(data.values())
        
        with plt.style.context(matplotx.styles.ayu["light"]):
            plt.rc('font', size=10)

            for label in line_labels:
                values = data.get(label).values()
                dates = data.get(label).keys()
                plt.plot(dates, values, label=label)

            plt.ylim([0, 5])
            plt.xticks(fontsize=8, rotation=90)
            plt.yticks(fontsize=10)
            plt.title("OQuaRE historic values")
            matplotx.line_labels()
            plt.savefig(outputPath + '/results/' + date + '/OQuaRE_historic_model_value.png', format="png", bbox_inches='tight')