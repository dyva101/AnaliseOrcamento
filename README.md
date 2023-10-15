<div align=center>
  
# Public Education Budget Analysis

### _Repository for Public Expenditure Data Analysis and Visualization (2014-2023)_

</div>

---

<div align=center>
  
  [Detailed Description](README.md#detailed-description)
  ·
  [Configs/Requirements](README.md#configs/requirements)
  ·
  [Docs](README.md#docs)
  ·
  [About Us](README.md#about-us)
  
</div>

---

### Detailed Description

  1. **Our Assumptions**
     1. We're checking if federal public spending levels increase during federal election years.
        
     2. Since we're only looking at education expenses and ignoring the economic landscape, we're
     not trying to find solid facts. We're just spotting trends and important pointers, a fundamental
     premise!

     4. Our last assumption is that our work should be scalable, meaning our functions and modules
     will be handy for future and more complex analyses.
  
  2. **Developed Modules**
     1. [datacleaning.py](datacleaning.py)
          - Responsible for cleaning data from CSV tables, especially those that are super extensive.
            You can use it to drop columns and keep only the data you desire.

     2. [graficos.py](graficos.py)
          - Takes care of plotting the main graphs for this analysis, which often need some special handling.
            Useful for graphs that need grouping or preprocessing of columns.

     3. [boxplot.py](graficos.py)
          - Handles the plotting of necessary box plots for exploratory analysis and deals with any outliers
            found in these box plots if needed.
---

### Configs/Requirements:

  - **Cloning the Repository and Running Main.py**:
    Just for demonstration, here's the code snippet that allows you to access and execute the code in the
    repository (including the installation of required packages):

    ```
    git clone https://github.com/dyva101/AnaliseOrcamento #(log in to Github)

    cd AnaliseOrcamento #unless you have a different path configured for the cloned repository

    pip install -r requirements.txt #successful installation

    python3 main.py #running main.py
    ```
  
  - For a complete view of the work (and for future use of the modules and functions developed here), _you'll
    need an environment with access to the 'pandas' library_, which is a crucial part of this project. This is
    listed in the requirements.txt file, used for package installation in the code snippet above.

    You'll also need _access to the 'matplotlib' and 'seaborn' libraries, along with a compatible version of the 
    Python interpreter_.

  > [!WARNING]
  > The tables loaded in this project add up to more than 100 MB of memory, which could lead to issues during execution.
  > Make sure your machine has enough memory!

---

### Docs

  - The documentation for the repository can be found at (insert link when ready), complementing the instructions in this
    document. It also includes the individual analyses performed by each team member, which make up the overall scope of
    the proposed Budget Analysis.

---

### About Us

  Our working team, informally known as the "Push & Pull" group, was formed for the first evaluation of the Programming 
  Languages course and currently works together on other projects as well. Curious about us? So check out our individual 
  profiles linked below:

  * <a href="https://github.com/isabelli31">Isabelli Cristhini da Silva 'Isa'</a>

    ![Picture, with CONSENT, of a team member](img/isa.jpg)
  
  * <a href="https://github.com/nataliabrandao">Natália Brandão de Souza 'Nati'</a>

    ![Picture, with CONSENT, of a team member](img/nati.jpg)
   
  * <a href="https://github.com/joao998-brt">João Otávio Siqueira de Brito 'Joãum'</a>

    ![Picture, with CONSENT, of a team member](img/joaum.jpg)
 
  * <a href="https://github.com/dyva101">Davy Albert Dutra de Andrade 'Dyva'</a>

    ![Picture, with CONSENT, of a team member](img/dyva.jpg)