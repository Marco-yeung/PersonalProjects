import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv("adult.data.csv")

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = len(df['race'].unique())

    # What is the average age of men?
    df_male = df[df['sex'] == 'Male']
    average_age_men = round(df_male['age'].mean(), 0)

    # What is the percentage of people who have a Bachelor's degree?
    no_bachelor = len(df[df['education'] == 'Bachelors'])
    percentage_bachelors = no_bachelor/len(df) * 100
    percentage_bachelors = round(percentage_bachelors, 2) 

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    df_high_edu = df.loc[df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
    df_without_high_edu = df.loc[~df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
    higher_education = df.loc[df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
    lower_education = df.loc[~df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]

    # percentage with salary >50K
    no_high_edu = len(df_high_edu[df_high_edu['salary'] == '>50K'])
    no_without_high_edu = len(df_without_high_edu[df_without_high_edu['salary'] == '>50K'])
    higher_education_rich = no_high_edu/len(df) * 100
    lower_education_rich = no_without_high_edu/len(df) * 100

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    df_50k_up= df[df['salary'] == '>50K']
    num_min_workers = len(df_50k_up['hours-per-week'] == 1)

    rich_percentage = round(num_min_workers/len(df) *100, 2)

    # What country has the highest percentage of people that earn >50K?
    highest_earning_country_count = df_50k_up.groupby('native-country').size().reset_index(name = "count")
    max_count = highest_earning_country_count['count'].max()
    highest_earning_country = highest_earning_country_count.loc[highest_earning_country_count['count'].idxmax(), 'native-country']
    highest_earning_country_percentage = round(max_count/len(df_50k_up) *100, 2)

    # Identify the most popular occupation for those who earn >50K in India.
    df_50k_up_india = df_50k_up[df_50k_up['native-country'] == 'India']
    df_50k_up_india_count = df_50k_up_india.groupby('occupation').size().reset_index(name= "count") 
    top_IN_occupation = df_50k_up_india_count.loc[df_50k_up_india_count['count'].idxmax(), 'occupation']

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }

calculate_demographic_data(print_data=False)