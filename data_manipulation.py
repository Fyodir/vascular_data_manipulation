#%%
# Import Modules

import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['figure.figsize'] = (10.0, 10.0)
#%% [markdown]

### Mean and Standard Deviaiton

#%%
# Inputting of data from CA ultrasounds

rcca_psv = [71.7, 68.8, 71.7, 68.8, 72.1]
rcca_edv = [15.0, 20.8, 19.3, 19.3, 21.2]

rica_psv = [61.5, 60.0, 70.2, 55.7, 59.0]
rica_edv = [23.7, 29.5, 28.1, 22.2, 29.9]

#%%
# Calculation of mean averages for ultrasound scans

mean_rcca_psv = round(np.mean(rcca_psv),2)
mean_rcca_edv = round(np.mean(rcca_edv),2)
mean_rica_psv = round(np.mean(rica_psv),2)
mean_rica_edv = round(np.mean(rica_edv),2)

print("Mean Averages")
print("RCCA PSV: " + str(mean_rcca_psv))
print("RCCA EDV: " + str(mean_rcca_edv))
print("RICA PSV: " + str(mean_rica_psv))
print("RICA EDV: " + str(mean_rica_edv))

#%%
# Standard Deviations

stdev_rcca_psv = round(np.std(rcca_psv), 2)
stdev_rcca_edv = round(np.std(rcca_edv), 2)
stdev_rica_psv = round(np.std(rica_psv), 2)
stdev_rica_edv = round(np.std(rica_edv), 2)

print("Standard Deviations")
print("RCCA PSV: " + str(stdev_rcca_psv))
print("RCCA ESV: " + str(stdev_rcca_edv))
print("RICA PSV: " + str(stdev_rica_psv))
print("RICA EDV: " + str(stdev_rcca_edv))

#%%
# Creation of lists for use in plots

scans = ['RCCApsv', 'RCCAedv', 'RICApsv', 'RICAedv']
x_pos = np.arange(len(scans))
CTEs = [mean_rcca_psv, mean_rcca_edv, mean_rica_psv, mean_rica_edv]
error = [stdev_rcca_psv, stdev_rcca_edv, stdev_rica_psv, stdev_rica_edv]

#%%
#Building Bar plot - Average Velocities

fig, ax = plt.subplots()
ax.bar(x_pos, CTEs, yerr=error, align='center', alpha=0.5, color="green", ecolor='red', capsize=10)
ax.set_ylabel('Velocity (cm/s)')
ax.set_xticks(x_pos)
ax.set_xticklabels(scans)
ax.set_title('Figure 1.1 - Peak Systolic (psv) and End Systolic (esv) Velocity')
ax.yaxis.grid(True)

# Save the figure and show
plt.tight_layout()
plt.savefig('plots/bar_plot_mean_systollic_velocities.png')
plt.show()

#%%
# Scatter Plot - Right Common Carotid Artery Velocities
# w/mean average and std deviation

x_pos = np.arange(len(rcca_psv))

fig, ax = plt.subplots()

ax.scatter(x_pos, rcca_psv, c="steelblue", label="RCCA psv")
ax.hlines(mean_rcca_psv, -0.2, len(x_pos) -0.8, colors="steelblue", linestyles="dashed")
ax.hlines(mean_rcca_psv + stdev_rcca_psv, -0.2, len(x_pos) -0.8, colors="steelblue", linestyles="dotted")
ax.hlines(mean_rcca_psv - stdev_rcca_psv, -0.2, len(x_pos) -0.8, colors="steelblue", linestyles="dotted")

ax.scatter(x_pos, rcca_edv, c="y", label="RCCA edv")
ax.hlines(mean_rcca_edv, -0.2, len(x_pos) -0.8, colors="y", linestyles="dashed")
ax.hlines(mean_rcca_edv + stdev_rcca_edv, -0.2, len(x_pos) -0.8, colors="y", linestyles="dotted")
ax.hlines(mean_rcca_edv - stdev_rcca_edv, -0.2, len(x_pos) -0.8, colors="y", linestyles="dotted")

ax.set_ylim(ymin=0, ymax=80)
ax.set_ylabel('Velocity (cm/s)')
ax.set_xticks(x_pos)
ax.set_xlabel('Measurement Attempt')
ax.set_title('Figure 1.2 - Right Common Carotid Artery (CCA) Velocities w/ mean and 1 standard deviation')
# ax.yaxis.grid(True)

plt.legend(loc='best')
plt.savefig('plots/scatter_plot_CCA_velocities.png')
plt.show()

#%%
# Scatter Plot Right Internal Carotid Artery Velocities
# w/mean average and std deviation

fig, ax = plt.subplots()

ax.scatter(x_pos, rica_psv, c="m", label="RICA psv")
ax.hlines(mean_rica_psv, -0.2, len(x_pos) -0.8, colors="m", linestyles="dashed")
ax.hlines(mean_rica_psv + stdev_rica_psv, -0.2, len(x_pos) -0.8, colors="m", linestyles="dotted")
ax.hlines(mean_rica_psv - stdev_rica_psv, -0.2, len(x_pos) -0.8, colors="m", linestyles="dotted")

ax.scatter(x_pos, rica_edv, c="mediumseagreen", label="RICA edv")
ax.hlines(mean_rica_edv, -0.2, len(x_pos) -0.8, colors="mediumseagreen", linestyles="dashed")
ax.hlines(mean_rica_edv + stdev_rica_edv, -0.2, len(x_pos) -0.8, colors="mediumseagreen", linestyles="dotted")
ax.hlines(mean_rica_edv - stdev_rica_edv, -0.2, len(x_pos) -0.8, colors="mediumseagreen", linestyles="dotted")

ax.set_ylim(ymin=0, ymax=100)
ax.set_ylabel('Velocity (cm/s)')
ax.set_xticks(x_pos)
ax.set_xlabel('Measurement Attempt')
ax.set_title('Figure 1.3 - Right Internal Carotid Artery (ICA) Velocities w/ mean and 1 standard deviation')
# ax.yaxis.grid(True)


plt.legend(loc='best')
plt.savefig('plots/scatter_plot_ICA_velociteis.png')
plt.show()

#%% [markdown]
### Ratios

#%% [markdown]

# |  	            | ICApsv 	        | Ratio - ICApsv:CCApsv 	| Ratio - ICApsv:CCAedv 	|
# |-----------------|-----------------	|--------------------------	|---------------------------|
# | Normal 	        | <124 cm/s 	    | <2 	                            | <8 	|
# | Mild Atheroma 	| <124 cm/s 	    | <2 	                            | <8 	|
# | <50% stenosis 	| <124 cm/s 	    | <2 	                            | <8 	|
# | 50-69% stenosis | 125 to 229 cm/s 	| 2-4 	                            | 8-13 	|
# | 70-89% stenosis | 230 to 399 cm/s 	| >4 	                            | 14-35 |
# | >90% stenosis 	| >400 cm/s 	    | >5 	                            | >35 	|
# | Trickle flow 	|  	                | Threadlike flow visible, either   |       |
# |                 |                   | >> 400 cm/s or severely           |       |
# |                 |                   | damped low velocity flow          |       |
# | Occluded 	    |  	                | No Flow 	                        |     	|

#%%

# ICApsv:CCApsv Ratios
ICApsv_CCApsv_ratios = []


for i in rica_psv:
    ICApsv_CCApsv_ratios.append(round(rica_psv[list.index(rica_psv, i)]/rcca_psv[0], 2)),
    ICApsv_CCApsv_ratios.append(round(rica_psv[list.index(rica_psv, i)]/rcca_psv[1], 2)),
    ICApsv_CCApsv_ratios.append(round(rica_psv[list.index(rica_psv, i)]/rcca_psv[2], 2)),
    ICApsv_CCApsv_ratios.append(round(rica_psv[list.index(rica_psv, i)]/rcca_psv[4], 2))
    ICApsv_CCApsv_ratios.append(round(rica_psv[list.index(rica_psv, i)]/rcca_psv[3], 2)),


print("ICApsv:CCApsv Ratios: " + str(ICApsv_CCApsv_ratios))

#%%
# ICApsv:CCAedv Ratios

ICApsv_CCAedv_ratios = []

for i in rica_psv:
    ICApsv_CCAedv_ratios.append(round(rica_psv[list.index(rica_psv, i)]/rcca_edv[0], 2)),
    ICApsv_CCAedv_ratios.append(round(rica_psv[list.index(rica_psv, i)]/rcca_edv[1], 2)),
    ICApsv_CCAedv_ratios.append(round(rica_psv[list.index(rica_psv, i)]/rcca_edv[2], 2)),
    ICApsv_CCAedv_ratios.append(round(rica_psv[list.index(rica_psv, i)]/rcca_edv[4], 2))
    ICApsv_CCAedv_ratios.append(round(rica_psv[list.index(rica_psv, i)]/rcca_edv[3], 2)),

print("ICApsv:CCAedv Ratios: " + str(ICApsv_CCAedv_ratios))

#%%
# Calculate mean and std deviation for ratios

mean_ICApsv_CCApsv_ratio = np.mean(ICApsv_CCApsv_ratios)
mean_ICApsv_CCAedv_ratio = np.mean(ICApsv_CCAedv_ratios)

stdev_ICApsv_CCApsv_ratio = np.std(ICApsv_CCApsv_ratios)
stdev_ICApsv_CCAedv_ratio = np.std(ICApsv_CCAedv_ratios)

#%%
# Scatter Plot - ICApsv_CCApsv_ratios

x_pos = np.arange(len(ICApsv_CCApsv_ratios))

fig, ax = plt.subplots()
ax.scatter(x_pos, ICApsv_CCApsv_ratios, c="r", label="ICApsv:CCApsv Ratio")
ax.hlines(mean_ICApsv_CCApsv_ratio, -0.2, len(x_pos) -0.8, colors="r", linestyles="dashed")
ax.hlines(mean_ICApsv_CCApsv_ratio + stdev_ICApsv_CCApsv_ratio, -0.2, len(x_pos) -0.8, colors="r", linestyles="dotted")
ax.hlines(mean_ICApsv_CCApsv_ratio - stdev_ICApsv_CCApsv_ratio, -0.2, len(x_pos) -0.8, colors="r", linestyles="dotted")
ax.set_ylim(ymin=0.4, ymax=1.2)
ax.set_ylabel('Ratio')
ax.set_xticks(x_pos)
ax.set_xlabel('Ratio Calculation')
ax.set_title('Figure 2.1 - ICApsv:CCApsv Ratios')
ax.yaxis.grid(True)

plt.savefig('plots/ICApsv:CCApsv_Ratio.png')
plt.show()

#%%
# Scatter Plot - ICApsv_CCAedv_ratios

x_pos = np.arange(len(ICApsv_CCAedv_ratios))

fig, ax = plt.subplots()
ax.scatter(x_pos, ICApsv_CCAedv_ratios, c="deepskyblue", label="ICApsv:CCAedv Ratio")
ax.hlines(mean_ICApsv_CCAedv_ratio, -0.2, len(x_pos) -0.8, colors="deepskyblue", linestyles="dashed")
ax.hlines(mean_ICApsv_CCAedv_ratio + stdev_ICApsv_CCAedv_ratio, -0.2, len(x_pos) -0.8, colors="deepskyblue", linestyles="dotted")
ax.hlines(mean_ICApsv_CCAedv_ratio - stdev_ICApsv_CCAedv_ratio, -0.2, len(x_pos) -0.8, colors="deepskyblue", linestyles="dotted")
ax.set_ylim(ymin=0, ymax=5)
ax.set_ylabel('Ratio')
ax.set_xticks(x_pos)
ax.set_xlabel('Ratio Calculation')
ax.set_title('Figure 2.2 - ICApsv:CCAedv Ratios')
ax.yaxis.grid(True)

plt.savefig('plots/ICApsv:CCAedv_Ratio.png')
plt.show()

#%%
# Scatter Plot - Comparison ICApsv_CCApsv_ratios Vs ICApsv_CCAedv_ratios

x_pos = np.arange(len(ICApsv_CCApsv_ratios))

fig, ax = plt.subplots()
ax.scatter(x_pos, ICApsv_CCApsv_ratios, c="r", label="ICApsv:CCApsv Ratio")
ax.scatter(x_pos, ICApsv_CCAedv_ratios, c="deepskyblue", label="ICApsv:CCAedv Ratio")
ax.set_ylim(ymin=0.4, ymax=10)
ax.set_ylabel('Ratio')
ax.hlines(2, 0, len(ICApsv_CCApsv_ratios), color="r", linestyles="dashed")
ax.text(0, 2.1, "Normal Maximum Threshold - ICApsv:CCApsv")
ax.hlines(8, 0, len(ICApsv_CCAedv_ratios), color="deepskyblue", linestyles="dashed")
ax.text(0, 8.1, "Normal Maximum Threshold - ICApsv:CCAedv")
ax.set_xticks(x_pos)
ax.set_xlabel('Ratio Calculation')
ax.set_title('Figure 2.3 - ICApsv:CCApsv Ratio Vs ICApsv:CCAedv Ratio w/ corresponding "normal" thresholds')
# ax.yaxis.grid(True)

plt.legend(loc='best')
plt.savefig('plots/comparison_ICApsv:CCApsv_and_ICApsv_CCAedv_Ratios.png')
plt.show()

#%%
# Bar plot - Mean ratios w/ std deviation

ratio = ['ICApsv:CCApsv', 'ICApsv:CCAedv']
x_pos = np.arange(len(ratio))
CTEs = [mean_ICApsv_CCApsv_ratio, mean_ICApsv_CCAedv_ratio]
error = [stdev_ICApsv_CCApsv_ratio, stdev_ICApsv_CCAedv_ratio]

#Building the Bar plot

fig, ax = plt.subplots()
ax.bar(x_pos, CTEs, yerr=error, align='center', alpha=0.7, color="dodgerblue", ecolor='orangered', capsize=10)
ax.set_ylabel('Ratio')
ax.set_xticks(x_pos)
ax.set_xticklabels(ratio)
ax.set_title('Figure 2.4 - Average Carotid Artery Velocity Ratios')
ax.yaxis.grid(True)

# Save the figure and show
plt.tight_layout()
plt.savefig('plots/bar_plot_average_ratios.png')
plt.show()

#%%

print(stdev_ICApsv_CCAedv_ratio)
print(stdev_ICApsv_CCApsv_ratio)

#%%
