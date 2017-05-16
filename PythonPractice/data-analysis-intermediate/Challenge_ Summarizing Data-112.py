## 3. Introduction to the Data ##

# Unique values in Major_category column.
majors = (all_ages['Major_category'].unique())

aa_cat_counts = {}
rg_cat_counts = {}

def calculate_major_cat_totals(df):
    majors= df['Major_category'].unique()
    counts_dictionary = {}
    
    for major in majors:
        major_df = df['Major_category'] == major
        major_true_df = df[major_df]
        major_total = major_true_df['Total'].sum()
        counts_dictionary[major] = major_total
    return counts_dictionary

aa_cat_counts = calculate_major_cat_totals(all_ages)
rg_cat_counts = calculate_major_cat_totals(recent_grads)

## 4. Summarizing Major Categories ##

# Unique values in Major_category column.
majors = (all_ages['Major_category'].unique())

aa_cat_counts = {}
rg_cat_counts = {}

def calculate_major_cat_totals(df):
    majors= df['Major_category'].unique()
    counts_dictionary = {}
    
    for major in majors:
        major_df = df['Major_category'] == major
        major_true_df = df[major_df]
        major_total = major_true_df['Total'].sum()
        counts_dictionary[major] = major_total
    return counts_dictionary

aa_cat_counts = calculate_major_cat_totals(all_ages)
rg_cat_counts = calculate_major_cat_totals(recent_grads)

## 5. Low-Wage Job Rates ##

low_wage_percent = 0.0

low_wage_total = recent_grads['Low_wage_jobs'].sum()
total = recent_grads['Total'].sum()

low_wage_percent = low_wage_total/total

## 6. Comparing Data Sets ##

# All majors, common to both DataFrames
majors = recent_grads['Major'].unique()
rg_lower_count = 0

for major in majors:
    recent_grads_major = recent_grads['Major'] == major
    rg_major_true = recent_grads[recent_grads_major]
    all_ages_major = all_ages['Major'] == major
    aa_major_true = all_ages[all_ages_major]
    if rg_major_true.iloc[0]['Unemployment_rate'] < aa_major_true.iloc[0]['Unemployment_rate']:
        rg_lower_count += 1
    