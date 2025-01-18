import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec


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

fig = plt.figure(figsize=(5, 2))
gs1 = gridspec.GridSpec(1, 1, wspace=0.35, hspace=0.4, top=.96, bottom=0.25, left=0.15, right=0.96,
                        figure=fig)
ax0 = plt.subplot(gs1[0])

ax0.plot(SADF1[SA1Column], alpha=0.8, label='SA')
ax0.plot(NSADFSub[NSAColumn], alpha=0.8, label='NSA')

# Add labels and legend
plt.ylabel("delay(sec)")
plt.xlabel('Data Points')
plt.legend()
plt.show()