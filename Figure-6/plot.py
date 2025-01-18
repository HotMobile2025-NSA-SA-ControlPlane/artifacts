import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

def get_iqr_values(df_in, col_name):
    median = df_in[col_name].median()
    q1 = df_in[col_name].quantile(0.25)  # 25th percentile / 1st quartile
    q3 = df_in[col_name].quantile(0.75)  # 7th percentile / 3rd quartile
    iqr = q3 - q1  # Interquartile range
    minimum = q1 - 1.5 * iqr  # The minimum value or the |- marker in the box plot
    maximum = q3 + 1.5 * iqr  # The maximum value or the -| marker in the box plot
    return median, q1, q3, iqr, minimum, maximum

def remove_outliers(df_in, col_name):
    _, _, _, _, minimum, maximum = get_iqr_values(df_in, col_name)
    df_out = df_in.loc[(df_in[col_name] > minimum) & (df_in[col_name] < maximum)]
    return df_out

# Load the data
NSADF = pd.read_csv("../Processed-Data/RRC_Procedure/Delay_NSA_RRC_Procedure.txt", sep="\t")
SADF = pd.read_csv("../Processed-Data/RRC_Procedure/Delay_SA_RRC_Procedure.txt", sep="\t")
DataColumn = 'Time (secs)'
Identifier = 'T2'

NSADF = NSADF[NSADF["Time Deltas"] == Identifier]
SADF = SADF[SADF["Time Deltas"] == Identifier]

NSADF = remove_outliers(NSADF,DataColumn)
SADF = remove_outliers(SADF,DataColumn)

# Plot PDF
fig = plt.figure(figsize=(3, 2))
gs1 = gridspec.GridSpec(1, 1, wspace=0.35, hspace=0.4, top=.96, bottom=0.25, left=0.21, right=0.96,
                        figure=fig)
ax0 = plt.subplot(gs1[0])

sns.kdeplot(data=SADF[DataColumn], cumulative=False, ax=ax0, alpha=0.8, label='SA')
sns.kdeplot(data=NSADF[DataColumn], cumulative=False, ax=ax0, alpha=0.8, label='NSA')

plt.xlabel(DataColumn)
plt.ylabel('PDF')

plt.legend()
plt.show()