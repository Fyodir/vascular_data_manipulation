# Competencies

Analyse data and report on the use of specific measurements (particularly in terms of accuracy, reproducibility, bias, specificity and sensitivity) in the context of bioinformatics.

## Knowledge and skills you might demonstrate

- Sources of appropriate literature relating to the technical, scientific and clinical basis of clinical measurements.
- Common artefacts in equipment calibration and performance.
- Statistical tests applied to clinical measuring data to measure accuracy, precision, resolution and bias.
- Range of statistical tests and the appropriate choice for each situation.
- Use of commonly available databases, spreadsheets and statistics packages.
- Concept of Patient Identifiable Data and the process of de-identification for both teaching and research purposes.
- Governance and ethical issues surrounding such secondary use of data.

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
  - Does not branch
  - Minimal resistance - Brain requires constant blood flow and suply of oxygen
- External Carotid Artery (ECA)
  - supplies blood flow to the face
  - consists of many brancheses to various parts of the face
  - Greater resistance than ICA - facial regions do not require constant supply of oxygen, intermittent flow is substantial

High-frequency sound waves travel from the probe through gel into the region of interest. The probe collects the sound waves that bounce back . THese soundwaves are processed by a computer to create an image. Unlike other imageing modalities such as Omputed Tomography (CT) and Positron Emission Tomography (PET), ultrasound exams do not use radiation. Images are also captured in real-time,  can show the structure and movement of the body's internal organs, and,in the case of vascular studies can also show blood flowing through blood vessels.

### Identifiable Data

Data gathered foor this exercises was obtained by undertaking ultrasound scans from the Common and Internal Carotid Arteries. The data gathered from the scans has been anonymised to protect confidentiality of the individual whom they were taken from.

#### Methodology

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

### References

Freedman et al (2015) <https://journals.plos.org/plosbiology/article?id=10.1371/journal.pbio.1002165>

Begley et al 2015 <https://www.ahajournals.org/doi/full/10.1161/CIRCRESAHA.114.303819>

McNutt 2014 <https://science.sciencemag.org/content/343/6168/229>
