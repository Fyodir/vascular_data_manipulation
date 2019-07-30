# Vascular Placement - Andrew Smith

## SBI102 Information and Communications Technology in the Clinical Environment

## Competencies

Analyse data and report on the use of specific measurements (particularly in terms of accuracy, reproducibility, bias, specificity and sensitivity) in the context of bioinformatics.

## Knowledge and skills you might demonstrate

- Sources of appropriate literature relating to the technical, scientific and clinical basis of clinical measurements.
- Common artefacts in equipment calibration and performance.
- Statistical tests applied to clinical measuring data to measure accuracy, precision, resolution and bias.
- Range of statistical tests and the appropriate choice for each situation.
- Use of commonly available databases, spreadsheets and statistics packages.
- Concept of Patient Identifiable Data and the process of de-identification for both teaching and research purposes.
- Governance and ethical issues surrounding such secondary use of data.

### Author

Andrew Smith (July 2019)

---

## Importance of Reproducibility

Within the clinical environment and the concurrent testing theat follows, the imporance of high levels of reproducibility of sufficiently accurate, precise and reliable results is of the utomost importance. Beforereapeatability patients are even considered, from an economical standpoint Freedman et al (2015) links low reproducibility of research with increased delays and cost of development. The advancement of medical research is also reliant on the fact that knowledge gained from research can be reproduced in a robust and reliable manner. If this is not the case, such research will not provide a firm enough base for which further advances can be developed upon (Begley et al 2015, McNutt 2014).

This perspective on reproducibility gathered from research tranfers smoothly over to the  aspect of clinical care. If a given test procedure is not reproducibile between individuals it can not then be considered reliable. Unreproducibility of results will  not allow for these measurements to be compared against a "normal" value. As such, clinical measurements taken from an unreprodubilbe test will not be substantial to make informed decisions on treatment.

## Carotid Ultrasound

### What is Carotid Ultrasound?

A safe and painless procedure, Carotid Artery (CA) ultrasound is the utilisation of ultrasonic high frequency sound waves to detect variations in  in structure below the surface of the skin. In the case of CA ultrasound this largeley focuses upon the area surrounding the neckfousing upon three arteries in particular:

- Common Carotid Artery (CCA)
  - Inferior to the ICA and CCA
- Internal Carotid Artery (ICA)
  - Provides blood flow to the brain
  - Does not branch (until reaching the brain)
  - Minimal resistance - Brain requires constant blood flow and suply of oxygen
- External Carotid Artery (ECA)
  - Supplies blood flow to the face
  - Consists of many brancheses leading towards various parts of the face
  - Greater resistance than ICA - facial regions do not require constant supply of oxygen, intermittent flow is substantial

High-frequency sound waves travel from the probe through gel into the region of interest. The probe collects the sound waves that bounce back . THese soundwaves are processed by a computer to create an image. Unlike other imageing modalities such as Omputed Tomography (CT) and Positron Emission Tomography (PET), ultrasound exams do not use radiation. Images are also captured in real-time,  can show the structure and movement of the body's internal organs, and,in the case of vascular studies can also show blood flowing through blood vessels.

### Common Artefacts in Ultrasound performance

Often occur due to various occurences, such includes:

- Operator Error
- Physical Principles
- Equipment Malfunction/Design

The wave transmitted travels in a direct line from the probe(transducer) to an obect, then is reflected back to the probe(transducer). A signal is created depending upon the distance in which the wave was required to travel to and from the point of reflection. An increase in wavelength of the transmitted wave will result in greater penetrance of the signal, but will adverseley affect resolution.

#### Catagories of Artefacts

- Image detail resolution related
- Locational artifacts
- Attenuation artifacts
- Doppler artifacts

### Identifiable Data

Data gathered foor this exercises was obtained by undertaking ultrasound scans from the Common and Internal Carotid Arteries. The data gathered from the scans has been anonymised to protect confidentiality of the individual whom they were taken from.

### Methodology

Ultrasound scans were taken of the "Right Common Carotid Artery" (RCCA) and "Right Internal Carotid Artery" (RICA). To ensure optimum reproducibility of results, the following factors were kept idencital throughout the process:

- Same Operator
- Same Ultrasound Scanner/Probe
- Results were one after another over a space of 15 minutes
- Same method of data retrieval was undertaken for each measurement
- Same location throughout the procedure
- Same Environmental Conditions
- Same state of the subject (Resting State).

The RCCA and RICA were scanned 5 times each, and post systolic (psv) and end diastolic psv) velocities were measured at each scan. This created a dataset for use in statistical analysis containing:

- RCCA psv - 5 measurements
- RCCA edv - 5 measurements
- RICA psv - 5 measurements
- RCCA edv - 5 measurements
  
This data was used in statistical analysis to assess reproducibility (carried out in `data_manipulation.py`). Numerous visual aids were created regarding mean average, standard deviation concerning the measurements and corresponding ratios **ICApsv:CCApsv** and **ICApsv:CCAedv**.

### Results

#### Average Velocities and Standard Deviation

Firstly mean average of each of the 4 varying types of measurements obtained was calculated, along with corresponding margin for error.

![alt text](plots/bar_plot_mean_systollic&#32;velocities.png)

For visual representation these awere also plotted onto serperate scatter graphs, one for the CCA and another for the CCA. These two scatter graphs show each easurement in turn, mean average (dash line), and ±1 standard deviation (dotted lines).

![alt text](plots/scatter_plot_CCA_velocities.png)

![alt text](plots/scatter_plot_ICA_velociteis.png)

#### Ratio's

The next port of call was the calculation and assessment of reproducibility of velocity ratio's.

**Table 1.1** - Catagorisation of CA Velocities and Ratios

|  	                | ICApsv 	    | Ratio - ICApsv:CCApsv 	        | Ratio - ICApsv:CCAedv 	|
|-----------------|-----------------|-----------------------------------|---------------------------|
| Normal 	      | <124 cm/s 	    | <2 	                            | <8 	                    |
| Mild Atheroma   | <124 cm/s 	    | <2 	                            | <8 	                    |
| <50% stenosis   | <124 cm/s 	    | <2 	                            | <8 	                    |
| 50-69% stenosis | 125 to 229 cm/s | 2-4 	                            | 8-13 	                    |
| 70-89% stenosis | 230 to 399 cm/s | >4 	                            | 14-35                     |
| >90% stenosis   | >400 cm/s 	    | >5 	                            | >35 	                    |
| Trickle flow    |  	            | Threadlike flow visible, either   |                           |
|                 |                 | >> 400 cm/s or severely           |                           |
|                 |                 | damped low velocity flow          |                           |
| Occluded 	      |  	            | No Flow 	                        |     	                    |

The two plots below display calculated Ratios with margins for error

![alt text](plots/ICApsv:CCApsv_Ratio.png)

![alt text](plots/ICApsv:CCAedv_Ratio.png)

These can be further visualised in the following plot (with accompanying threshold for a normal value)

![alt text](plots/comparison_ICApsv:CCApsv_and_&#32;ICApsv_CCAedv_Ratios.png)

Average ICApsv:CCApsv and ICApsv:CCAedv ratios along with  margins of error can also be seen below

![alt text](plots/bar_plot_average_ratios.png)

### Discussion

#### Velocities

The results obtained from this project were gathered to determine the accuracy and reproducibility of results gathered by a single individual whislt taking ultrasound scans of the Carotid Artery. As many factors as possible were kept identical during the results gathering process, as mentioned in methodology to minimise the effect of unknown factors on the end results.

One key factor that must be made aware  was that results obtained were not gathered directly by a trained professional, but instead by an operator being guided by such. As such it is likely that the results were more prone to variation and error as a result of unfamiliarity. Results were also tkaen from an individual not currently known to have any medical conditions that may effect them, so only healthy "normal" values were expected (as described in Table 1.1).

Firstly, the average velocies visualised in figures 1.1 - 1.3 correspond with that of a  healthy individual. The average velocites displayed in figure 1.1 even presenting with a room for error no greater than 10cm/s in the RICA (which presented with the largest margin of error) show the results of a healthy individual. Figures 1.2 and 1.3 show more in depth information regarding the precision of these results. As can be seen in these two figures, a considerable portion of the results obtained lie within 1 standard deviation from the mean. This shows a high level of precision. However, those that lie outside of this should be discarded as are liekly due to sources of error with the measurement. These mayhave arisen due to inexperience of the operator, or artefacts with that accumulated with the gathering of the reuslts. It is likely that these may be accounted for if the sample size used for statistical anlysis was extended further, or results gathering was repeated with a more experienced user.

#### Ratios

To further assess the results, ratios used typically used in patient diagnosis (Table 1.1) during routine testing were calso calculated from the dataset.  Each possible ratio was calculated from the dataset and these can be seen in Figures 2.1-2.4.

Figures 2.1 and 2.2, in a similar fashion to that used in 1.2 and 1.3 show how each data value lies in accordance with the mean value and corresponding standard deviations. There is a considerable variation from the mean and values that lie outside of 1 standard deviaiton, which is quite prevalent in figure 2.1. This is likely due to the fact they were calculated from the same dataset used to plot velocites. This as mentioned, already possessed a number of outlying data values, and will have been emphasized during ratio calculations. Figure 2.2 which displays ratios of ICA,psv:CCAedv presents with much greater precision with less values lieing outside of 1 standard deviation, however, this ratio does possess a much larger margin for error in comparison, with a margin of 0.5, compared to 0.07 in figure 2.1 (ICApsv:CCApsv).

Figure 2.3 plots the calulated ratios in figure 2.1 and 2.2 in relation to the maximum threshold for normal "healthy" values. Despite The high level of error in calcualted ratios none show variations in diagnosis, with each displaying ratios that lie within the normal range.

Averages of ratios are plotted in figure 2.4 and show the variation exhibited in both.

### Conclusion

The results obtained from this project emphasize the variation that can occur during the results gathering process, even when many factors remain the same. The dataset shows condiderable variation in results with a number of possibly anomalous values. Accuracy and precision is diplayed in some areas, and the possibility of reprodciple results can be considered with.  However, it is not  possible to comfortably say that these results are likely to be consistantly reproducible without further work.

It is likely that the anomalous values are a result of the inexpereince of the ultrasound operator and may be reduced if repeated by another with more expereince. It must also be considered that the dataset used in analysis only contained 5 sets of values for each region of interest where arterial velocity was measured.

If this study was repeated, it is highly recommended that the same measurements are carried out by multiple operators to allow for comparison, and that the dataset be enlarged proportionally to account for the presence of anomalous results.

### References

Freedman et al (2015) <https://journals.plos.org/plosbiology/article?id=10.1371/journal.pbio.1002165>

Begley et al (2015) <https://www.ahajournals.org/doi/full/10.1161/CIRCRESAHA.114.303819>

McNutt (2014) <https://science.sciencemag.org/content/343/6168/229>
