# 🔭 GSOC 2026 Submission - ML4SCI DeepLense

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![PyTorch](https://img.shields.io/badge/PyTorch-Latest-orange)
![Status](https://img.shields.io/badge/Status-Completed-success)

This repository contains the code, models, and documentation for my GSOC 2026 submission for the **Machine Learning for Science (ML4SCI) - DeepLense** project. It includes two deep learning pipelines specifically designed for astronomical lens classification and dark matter substructure detection.

##  Project Overview
The primary goal of this project is to build robust, scalable machine learning models capable of analyzing simulated dark matter lenses and large-scale astronomical data (such as LSST mocks). 

To achieve this, the pipelines leverage advanced computer vision architectures (ResNet18 and EfficientNet-B0) and address critical domain challenges, including:
* **Severe Class Imbalance:** Handled effectively via PyTorch's `WeightedRandomSampler`.
* **Data Dimensionality:** Dynamically adapting 1-channel or `(3, 64, 64)` filter arrays for standard pre-trained models.
* **Feature Robustness:** Implementing extensive on-the-fly geometric data augmentation to ensure spatial invariance.

##  Repository Structure

| Path / Folder | Description |
| :--- | :--- |
| `README.md` | Project overview, key highlights, and setup instructions (this file). |
|  `Common_Test_I/` | Contains the pipeline for **Multi-Class Classification** of dark matter substructures (`no_sub`, `subhalo`, `vortex`). Evaluated using Macro-Average OvR ROC AUC. |
| `Specific_Test_V/` | Contains the **Data Pipeline** for highly imbalanced binary classification of LSST data (Lenses vs. Non-Lenses). |

*(Note: Due to GitHub's file size limits, the trained `.pth` model weights are securely backed up on Google Drive. Scripts and instructions to load them are provided within the notebooks.)*

##  Key Results (Summary)
* **Specific Test V (Binary - LSST):** Successfully trained models to distinguish lenses from non-lenses despite extreme class imbalance, achieving exceptional AUC scores.
* **Common Test I (Multi-Class):** Implemented a comprehensive pipeline for 3-class classification, evaluating models using One-vs-Rest (OvR) Macro-Average ROC curves, demonstrating high substructure detection capabilities.

##  Setup & Usage

### 1. Requirements
* Python 3.8+
* `torch`, `torchvision`
* `numpy`, `scikit-learn`, `matplotlib`

### 2. Execution (Recommended: Google Colab)
It is highly recommended to run the `.ipynb` notebooks in **Google Colab** with a GPU runtime (T4/P100) for optimal training speed.
1. Upload the notebooks to Colab.
2. Follow the data-download and mounting instructions in the first cell of each notebook.
3. Run all cells sequentially.

### 3. Local Execution
If you wish to run the pipelines locally, clone the repository:
```bash
git clone [https://github.com/Mayar-hany-2005/DeepLense-GSoC-2026.git](https://github.com/Mayar-hany-2005/DeepLense-GSoC-2026.git)
cd DeepLense-GSoC-2026

jupyter notebook
📬 Contact & Author
Mayar Hany * GitHub: @Mayar-hany-2005

Email: [اmayarhany1999@gmail.com]
