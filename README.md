# nlp-traininglabs

# Environment Setup Guides
There are four important steps in setting up your environment:

## Step 1: Install Anaconda

1. Go to [Anaconda Official Website](https://www.anaconda.com/products/individual) and download the latest **Anaconda Individual Edition** installer with **Python 3.x**.

2. Open the installer and follow all the setup instruction.

3. For more setup information, please refer to [Anaconda Setup For Windows](https://www.datacamp.com/community/tutorials/installing-anaconda-windows).

<br>

## Step 2: Install NLP-Labs Dependencies

1. Open Anaconda Prompt.

2. Navigate to your NLP-Labs root folder, e.g: 

    > `cd C:\Users\{enter your path here}\Certifai\nlp-labs`

3. Run the following command to create new conda environment: 

    > `conda env create -f environment.yml`

4. Press y to confirm installation.

5. Your installation should be completed.

6. Activate `nlp-labs` environment:

    > `conda activate nlp-labs`

<br>

## Step 3: Install Python Packages

1. Open Anaconda Prompt and activate nlp-labs environment.

2. Navigate to NLP-Labs root folder:

3. Run the following command to install required modules for this training lab:

    > `pip install -r requirement.txt`

4. Wait for the download and installation to complete.

<br>

## Step 4: Install Spacy Language Models

Throughout this training labs, we will mainly using these language models:

- en_core_web_sm

- de_core_news_sm

- en_core_web_lg

- fr_core_news_lg


To install these modules, run the following commands:

    > python -m spacy download en_core_web_sm

    > python -m spacy download de_core_news_sm

    > python -m spacy download en_core_web_lg

    > python -m spacy download fr_core_news_lg