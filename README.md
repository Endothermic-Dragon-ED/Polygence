# Polygence Project
This GitHub respository contains everything related to my Polygence project.

The result of my project are a set of articles about machine learning, and a research paper.

The article series is titled "In-Depth Machine Learning for Teens", and the individual articles can be accessed below.
- [In-Depth Machine Learning for Teens: Introduction](https://medium.com/@endothermic-dragon/in-depth-machine-learning-for-teens-introduction-559e07fe6c78)
- [In-Depth Machine Learning for Teens: Gradient Descent](https://medium.com/@endothermic-dragon/in-depth-machine-learning-for-teens-gradient-descent-ce2d0370303c)
- [In-Depth Machine Learning for Teens: Linear Regression](https://medium.com/@endothermic-dragon/in-depth-machine-learning-for-teens-linear-regression-d66db85c8f3a)
- [In-Depth Machine Learning for Teens: Training Faster And Better](https://medium.com/@endothermic-dragon/in-depth-machine-learning-for-teens-training-faster-and-better-93f35bb263e3)
- [In-Depth Machine Learning for Teens: Logistic Regression](https://medium.com/@endothermic-dragon/in-depth-machine-learning-for-teens-logistic-regression-3e9b86102482)
- [In-Depth Machine Learning for Teens: Neural Networks](https://medium.com/@endothermic-dragon/in-depth-machine-learning-for-teens-neural-networks-ded1af6a84de)

The research paper is titled "Machine Learning Simplified:
A New Resource to Introduce Advanced Concepts
in a High School Approachable Format".

## License
All code in this respository is licensed under the "MIT License" license. All media is licensed under the "Creative Commons Attribution 4.0 International" license.

## Survey Data
A survey was conducted to determine the efficacy of this article series. The raw data can be viewed on Google Spreadsheets.
- [Link to published version](https://docs.google.com/spreadsheets/d/e/2PACX-1vQ4FkiR-W5BWaTlzzs4rtWSXPva6P8srhmtekCcg7pXdHynkoLrSi_AwWxOcSc1OkCRKB63UyjFu94s/pubhtml)
- [Link to copyable and downloadable version](https://docs.google.com/spreadsheets/d/1cv4CYCXmYwg2qu2BBy-XX7fPDgA6nNRk-ZihCLghCgY/edit?usp=sharing)

## Folders
Each folder in this GitHub holds certain assets used during the writing of the article series.
- HTML Files - holds tables which are used within the articles. A screenshot is provided in the article, and a direct link is provided so the reader can view the table on GitHub Pages.
- Jupyter Notebooks - used for storing datasets (to be used in labs) and the labs themselves
- LaTeX - used for image generation in articles, specifically to format math and export as an image
  - Custom built
    - Can specify directory (faster compilation since then you're only converting a subset)
    - With some slight modifications, can have fine control over output image size
  - How it works:
    1. Uses MathJax from Node.js to convert `.tex` files in `src` into `.svg` files in `build`
    2. Maps each `.svg` into a new `.svg` file
      - Other apps seem to view it as "corrupt" or just can't parse it
    3. Uses Inkscape to convert each `.svg` vector image into a `.png` bitmap image
       - `.png` file replaces the `.svg` file in `build`
- Manim - used for image generation in articles
  - Uses `manim` to generate images
- Plots - used for image generation in articles
  - Uses `pyplot` from `matplotlib` to generate images