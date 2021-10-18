# Folders:

1. Documentation - contains documents (including this one)
2. Command Files - executable jupyter notebooks loading, cleaning and saving new data and creating charts.
3. Original - untouched data
4. Analysis Data - new data generated from executables and generated charts

# Command Files

##load\_and_operate.ipynb <br />
- loads data from original folder <br />
- cleans data using dropna method from DataFrame <br />
- creates a python dict mapping column names to new names <br />
- using DataFrame.rename and question map renames columns <br />
- creates new table only with age, gender and answer to one question <br />
- saves table with renamed columns to questions_renamed.csv in Analysis data <br />
- saves new table with 3 columns to age\_gender\_worried_table.csv in Analysis data <br />




## create\_charts.ipynb <br />
- loads renamed\_question_table.csv <br />
- maps it to dict <br />
- displays bar chart for each column (question) and its answers count
- saves bar charts to png in Analysis Data



