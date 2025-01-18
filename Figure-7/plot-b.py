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

NSADF = pd.read_csv("../Processed-Data/Attachment_Registration/Delay_NSA_Attachment.txt", sep="\t")
SADF1 = pd.read_csv("../Processed-Data/PDU_Session/Delay_SA_PDU_Session.txt", sep="\t")
SADF2 = pd.read_csv("../Processed-Data/Attachment_Registration/Delay_SA_Registration.txt", sep="\t")

SA1Column = "Auth Time"
SA2Column = "5G-NR NAS Registration Procedure Registration Time(ReqToComp) [sec]"
NSAColumn = "NAS Attach Procedure Attach Time(ReqToComp) [sec]"

SADF2 = SADF2.dropna(subset=[SA2Column], ignore_index=True)
SADF1[SA1Column] = SADF1[SA1Column] + SADF2[SA2Column]

# Filter out outliers
SADF1 = SADF1[SADF1[SA1Column] <= 1.40]
NSADF = NSADF.dropna(subset=[NSAColumn], ignore_index=True)
NSADF = NSADF[NSADF[NSAColumn] <= 1.0]
# Trim out data
SADF1 = SADF1.head(550)
NSADFSub = NSADF.head(550)

NSADF = remove_outliers(NSADF,NSAColumn)
SADF = remove_outliers(SADF1,SA1Column)

# Plot PDF
fig = plt.figure(figsize=(3, 2))
gs1 = gridspec.GridSpec(1, 1, wspace=0.35, hspace=0.4, top=.96, bottom=0.25, left=0.21, right=0.96,
                        figure=fig)
ax0 = plt.subplot(gs1[0])

sns.kdeplot(data=SADF[SA1Column], cumulative=False, ax=ax0, alpha=0.8, label='SA')
sns.kdeplot(data=NSADF[NSAColumn], cumulative=False, ax=ax0, alpha=0.8, label='NSA')

plt.xlabel("delay(sec)")
plt.ylabel('PDF')

plt.legend()
plt.show()