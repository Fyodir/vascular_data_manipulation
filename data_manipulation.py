#%% [markdown]

### Competencies

# Analyse data and report on the use of specific measurements (particularly in terms of accuracy, 
# reproducibility, bias, specificity and sensitivity) in the context of bioinformatics.

### Knowledge and skills you might demonstrate
# - Sources of appropriate literature relating to the technical, scientific and clinical basis of clinical measurements.
# - Common artefacts in equipment calibration and performance.
# - Statistical tests applied to clinical measuring data to measure accuracy, precision, resolution and bias.
# - Range of statistical tests and the appropriate choice for each situation.
# - Use of commonly available databases, spreadsheets and statistics packages.
# - Concept of Patient Identifiable Data and the process of de-identification for both teaching and research purposes.
# - Governance and ethical issues surrounding such secondary use of data.

#%% [markdown]

### Importance of Reproducibility

# Within the clinical environment and the concurrent testing theat follows, the imporance of high levels of reproducibility of 
# sufficiently accurate, precise and reliable results is of the utomost importance. Before patients are even considered, from 
# an economical standpoint Freedman et al (2015) links low reproducibility of research with increased delays and cost of development.
# The advancement of medical research is also reliant on the fact that knowledge gained from research can be reproduced in a robust 
# and reliable manner. If this is not the case, such research will not provide a firm enough base for which further advances can be 
# developed upon (Begley et al 2015, McNutt 2014).
#
# This perspective on reproducibility gathered from research tranfers smoothly over to the  aspect of clinical care. 
# If a given test procedure is not reproducibile between individuals it can not then be considered reliable. Unreproducibility of results
# will  not allow for these measurements to be compared against a "normal" value. As such, clinical measurements taken from an unreprodubilbe test
# wiill not be substantial to make informed decisions on treatment.


### Identifiable Data

# Data gathered foor this exercisesed was obtained by undertaking ultrasound scans from the Common and Internal Carotid Arteries
# The data gathered from the scans has been anonymised to protect confidentiality of the individual whom they were taken from.
#
# To ensure reproducibility of the results, the following factors were kept idencital throughout the process
# - Same Operator
# - Same Ultrasound Scanner/Probe
# - Results were one after another over a space of 15 minutes
# - Same method of data retrieval was undertaken for each measurement
# - Same location throughout the procedure
# - Same Environmental Conditions
# - Same state of the subject (Resting State)

### Common Artefacts in Ultrasound performance

# Often occur due to various occurences, such includes:
# - Operator Error
# - Physical Principles
# - Equipment Malfunction/Design
#
#
# The wave transmitted travels in a direct line from the probe(transducer) to an obect, then is reflected back to the probe(transducer).
# A signal is created depending upon the distance in which the wave was required to travel to and from the point of reflection.
# An increase in wavelength of the transmitted wave will result in greater penetrance of the signal, but will adverseley affect resolution.

#### Catagories of Artefacts

# - Image detail resolution related
# - Locational artifacts
# - Attenuation artifacts
# - Doppler artifacts 
#

### References
# Freedman et al (2015) <https://journals.plos.org/plosbiology/article?id=10.1371/journal.pbio.1002165>
#
# Begley et al 2015 <https://www.ahajournals.org/doi/full/10.1161/CIRCRESAHA.114.303819>
#
# McNutt 2014 <https://science.sciencemag.org/content/343/6168/229>


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
# Creation of lists for the plot

scans = ['RCCApsv', 'RCCAedv', 'RICApsv', 'RICAedv']
x_pos = np.arange(len(scans))
CTEs = [mean_rcca_psv, mean_rcca_edv, mean_rica_psv, mean_rica_edv]
error = [stdev_rcca_psv, stdev_rcca_edv, stdev_rica_psv, stdev_rica_edv]

#%%
#Building the Bar plot

fig, ax = plt.subplots()
ax.bar(x_pos, CTEs, yerr=error, align='center', alpha=0.5, ecolor='red', capsize=10)
ax.set_ylabel('Velocity (cm/s)')
ax.set_xticks(x_pos)
ax.set_xticklabels(scans)
ax.set_title('Peak Systolic (psv) and End Systolic (esv) Velocity')
ax.yaxis.grid(True)

# Save the figure and show
plt.tight_layout()
plt.savefig('plots/bar_plot_with_error_bars.png')
plt.show()

#%%
# Scatter Plot - Right Common Carotid Artery Velocities
# w/mean average and std deviation

x_pos = np.arange(len(rcca_psv))

fig, ax = plt.subplots()

ax.scatter(x_pos, rcca_psv, c="cyan", label="RCCA psv")
ax.hlines(mean_rcca_psv, -0.2, len(x_pos) -0.8, colors="cyan", linestyles="dashed")
ax.hlines(mean_rcca_psv + stdev_rcca_psv, -0.2, len(x_pos) -0.8, colors="cyan", linestyles="dotted")
ax.hlines(mean_rcca_psv - stdev_rcca_psv, -0.2, len(x_pos) -0.8, colors="cyan", linestyles="dotted")

ax.scatter(x_pos, rcca_edv, c="y", label="RCCA edv")
ax.hlines(mean_rcca_edv, -0.2, len(x_pos) -0.8, colors="y", linestyles="dashed")
ax.hlines(mean_rcca_edv + stdev_rcca_edv, -0.2, len(x_pos) -0.8, colors="y", linestyles="dotted")
ax.hlines(mean_rcca_edv - stdev_rcca_edv, -0.2, len(x_pos) -0.8, colors="y", linestyles="dotted")

ax.set_ylim(ymin=0, ymax=80)
ax.set_ylabel('Velocity (cm/s)')
ax.set_xticks(x_pos)
ax.set_xlabel('Measurement Attempt')
ax.set_title('Right Common Carotid Artery (CCA) Velocities w/ mean and 1 standard deviation')
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

ax.scatter(x_pos, rica_edv, c="g", label="RICA edv")
ax.hlines(mean_rica_edv, -0.2, len(x_pos) -0.8, colors="g", linestyles="dashed")
ax.hlines(mean_rica_edv + stdev_rica_edv, -0.2, len(x_pos) -0.8, colors="g", linestyles="dotted")
ax.hlines(mean_rica_edv - stdev_rica_edv, -0.2, len(x_pos) -0.8, colors="g", linestyles="dotted")

ax.set_ylim(ymin=0, ymax=100)
ax.set_ylabel('Velocity (cm/s)')
ax.set_xticks(x_pos)
ax.set_xlabel('Measurement Attempt')
ax.set_title('Right Internal Carotid Artery (ICA) Velocities w/ mean and 1 standard deviation')
# ax.yaxis.grid(True)


plt.legend(loc='best')
plt.savefig('plots/scatter_plot_ICA_velociteis.png')
plt.show()

#%% [markdown]
### Ratios

#%%
# ICApsv:CCApsv Ratios
ICApsv_CCApsv_ratios = []

for i in rica_psv:
    ICApsv_CCApsv_ratios.append(round(rica_psv[list.index(rica_psv, i)]/rcca_psv[list.index(rica_psv, i)], 2))

print("ICApsv:CCApsv Ratios: " + str(ICApsv_CCApsv_ratios))

#%%
# Scatter Plot - ICApsv_CCApsv_ratios

x_pos = np.arange(len(ICApsv_CCApsv_ratios))

fig, ax = plt.subplots()
ax.scatter(x_pos, ICApsv_CCApsv_ratios, c="r", label="ICApsv:CCApsv Ratio")
ax.set_ylim(ymin=0.4, ymax=1.2)
ax.set_ylabel('Ratio')
ax.set_xticks(x_pos)
ax.set_xlabel('Measurement Attempt')
ax.set_title('ICApsv:CCApsv Ratios')
ax.yaxis.grid(True)

plt.savefig('plots/ICApsv:CCApsv_Ratio.png')
plt.show()

#%%
# ICApsv:CCAedv Ratios

ICApsv_CCAedv_ratios = []

for i in rica_psv:
    ICApsv_CCAedv_ratios.append(round(rica_psv[list.index(rica_psv, i)]/rcca_edv[list.index(rica_psv, i)], 2))

print("ICApsv:CCAedv Ratios: " + str(ICApsv_CCAedv_ratios))


#%%
# Scatter Plot - ICApsv_CCAedv_ratios

x_pos = np.arange(len(ICApsv_CCAedv_ratios))

fig, ax = plt.subplots()
ax.scatter(x_pos, ICApsv_CCAedv_ratios, c="b", label="ICApsv:CCAedv Ratio")
ax.set_ylim(ymin=0, ymax=5)
ax.set_ylabel('Ratio')
ax.set_xticks(x_pos)
ax.set_xlabel('Measurement Attempt')
ax.set_title('ICApsv:CCAedv Ratios')
ax.yaxis.grid(True)

plt.savefig('plots/ICApsv:CCAedv_Ratio.png')
plt.show()

#%%
# Scatter Plot - Comparison ICApsv_CCApsv_ratios Vs ICApsv_CCAedv_ratios

x_pos = np.arange(len(ICApsv_CCApsv_ratios))

fig, ax = plt.subplots()
ax.scatter(x_pos, ICApsv_CCApsv_ratios, c="r", label="ICApsv:CCApsv Ratio")
ax.scatter(x_pos, ICApsv_CCAedv_ratios, c="b", label="ICApsv:CCAedv Ratio")
ax.set_ylim(ymin=0.4, ymax=10)
ax.set_ylabel('Ratio')
ax.hlines(2, 0, 4, color="r", linestyles="dashed")
ax.text(0, 2.1, "Normal Maximum Threshold")
ax.hlines(8, 0, 4, color="b", linestyles="dashed")
ax.text(0, 8.1, "Normal Maximum Threshold")
ax.set_xticks(x_pos)
ax.set_xlabel('Measurement Attempt')
ax.set_title('ICApsv:CCApsv Ratio Vs ICApsv:CCAedv Ratio w/ corresponding "normal" thresholds')
# ax.yaxis.grid(True)

plt.legend(loc='best')
plt.savefig('plots/comparison_ICApsv:CCApsv_and_ ICApsv_CCAedv_Ratios.png')
plt.show()

#%%
