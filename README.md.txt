# GSOC 2026 Submission - ML4SCI DeepLense

This repository contains the code, models, and documentation for my GSOC 2026 submission for the **Machine Learning for Science (ML4SCI) - DeepLense** project. It includes two deep learning pipelines designed for astronomical lens classification and substructure detection.

## Project Overview
The goal of this project is to build robust machine learning models capable of analyzing simulated dark matter lenses and large-scale astronomical data (like LSST). The repository is structured for easy review and reproducibility, with all artifacts, training histories, and evaluation outputs included.

## Repository Structure

| Path / Folder | Description |
| :--- | :--- |
| `README.md` | Project overview and setup instructions (this file). |
| `Common_Test_I/` | Contains the pipeline for **Multi-Class Classification** of dark matter substructures (`no_sub`, `subhalo`, `vortex`). |
| `Specific_Test_V/` | Contains the **Data Pipeline** for highly imbalanced binary classification of LSST data (Lenses vs. Non-Lenses). |

*Note: Due to GitHub's file size limits, the trained `.pth` model weights are securely backed up on Google Drive. Links or loading instructions are provided within the notebooks.*

##  Setup & Usage
1. **Requirements:** Python 3.8+, PyTorch, Torchvision, NumPy, Matplotlib, scikit-learn.
2. **Execution:** It is highly recommended to run the `.ipynb` notebooks in **Google Colab** with a GPU runtime (T4/P100) for optimal training speed.
3. **Data:** The datasets used are provided by ML4SCI. Please refer to the specific test folders for data links and extraction logic.

---
*For detailed information on strategies, models, and results, please navigate to the respective test directories.*