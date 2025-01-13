
## A Peek into 5G NSA vs. SA Control Plane:A Peek into 5G NSA vs. SA Control Plane Performance

In this repository, we release the dataset and artifacts of the conference paper 
[A Peek into 5G NSA vs. SA Control Plane:A Peek into 5G NSA vs. SA Control Plane Performance](https://raw.githubusercontent.com/SIGCOMM24-5GinMidBands/artifacts/refs/heads/main/HERE.pdf) published at [HotMobile 2025](https://hotmobile.org/2025/). 

This is a measurement paper with various types of data processed for different purposes having different methodologies. In out GitHub,
we group the artifacts by Section number and name. There are README files with each Section folder with more specific
instructions to validate our experimental results. Lastly, here are some generic principles we followed for releasing the artifacts:

---

### Abstract  
> 5G Stand-Alone (SA) deployment mode promises many gains over 5G Non-Stand-Alone (NSA) mode, such as improved throughput, lower latency, and more architectural flexibility, to better support emerging future applications such as AR/VR, IoT, and teleoperated driving.
> These promised improvements also extend to the control plane operations of SA, such as attachment/registration procedures to mobile networks, mobility, and security management to provide better user quality-of-experience (QoE).
> The majority of the existing works explore the data plane and end-to-end performance of 5G. 
> In this paper, we investigate and quantify the control plane performance differences of SA compared to NSA. Our results indicate SA mostly has a worse (i.e. slower) control performance (by 16.6% for attachment/registration, PDU session establishment, and 64.3% RRC procedure), unlike expectations, which raises questions about current (virtualized) SA deployment and core functionality placement. 

---

### Dataset Sizes/Data Analysis
- We included the curated dataset file in this repository.
- If the dataset files are huge, we use a small sample of the dataset in the repository to demonstrate the functionality/correctness.
- If data analysis is involved, our instructions will contain information on how to process the data.
- No matter what the dataset size is, we provide the fully generated results and/or plots. If you decide to run the analysis
and/or plotting scripts, the outcome of processing will create
the raw results files in the repository. Artifacts and Info

### NOTE: We ONLY include the curated dataset in this repo. If you are interested in the raw data, please contact us. 

---


### Paper Structure to Folder Structure
 
|                Content in Paper                |                                                    Folder in Repo.                                                     | Section Description                                                                          |
|:----------------------------------------------:|:----------------------------------------------------------------------------------------------------------------------:|----------------------------------------------------------------------------------------------|
|          Section 4 (Figures 5 - 8)             | [RRC RACH and Others](https://github.umn.edu/fezeu001/5G-Mid-Band/blob/main/Sec4-Mid-Band-PhyPerformance/README.md)    | PHY DL Throughput Performance.                                                               |
|	   Section 5 (Figures 11)		 | [PDU PDN]()															  |												 |
---

### Instructions on how to validate these artifacts
1. Clone this repo: ``git clone``
2. Run ``chmod +x setup-venv.sh``
3. Run ``./setup-venv.sh``
4. Run ``source /venv/bin/activate``
5. Run ``pip install -r requirements.txt``
6. Navigate to each Section folder and follow the README file

NOTE: \
If ``SHOW_PLOT_FLAG = True``, the figure will be display\
If ``SHOW_PLOT_FLAG = False``, the figure will be saved in ``Finals_Plots`` folder in the parent directory.

---

As always, if there are any questions, feel free to reach out to us [Rostand A. K. Fezeu](mailto:fezeu001@umn.edu?cc=claudio.fiandrino@imdea.org&cc=eman@cs.umn.edu&bcc=zhang089@umn.edu&subject=[NSA-SA-Control-Plane]%HOTMOBILE'25%Paper).

