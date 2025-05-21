import pandas as pd
def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('adult.data.csv')

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df['race'].value_counts()

    # What is the average age of men?
    average_age_men = round(df[df['sex'] == 'Male']['age'].mean(), 1)

    # What is the percentage of people who have a Bachelor's degree?
    total = len(df)
    num_bachelors = df[df['education'] == 'Bachelors'].shape[0]
    percentage_bachelors = round(num_bachelors / total * 100, 1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    adv_quals = ['Bachelors','Masters','Doctorate']
    adv = df[df['education'].isin(adv_quals)]
    higher_education = df[df['education'].isin(adv_quals)]
    num_adv_rich = higher_education[higher_education['salary'] == '>50K'].shape[0]
    lower_education = df[~df['education'].isin(adv_quals)]
    num_non_adv_rich = lower_education[lower_education['salary'] == '>50K'].shape[0]
    # What percentage of people without advanced education make more than 50K?
    # with and without `Bachelors`, `Masters`, or `Doctorate`
    higher_education = df[df['education'].isin(adv_quals)]
    lower_education = df[~df['education'].isin(adv_quals)]

    # percentage with salary >50K
    higher_education_rich = round(num_adv_rich / higher_education.shape[0] * 100, 1)
    lower_education_rich = round(num_non_adv_rich / lower_education.shape[0] * 100, 1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-pear-week'].min()
    ft_min_workers = df[df['hours-per-week'] == min_work_hours]
    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    min_workers = df[df['hours-pear-week'] == min_work_hours]
    num_min_workers = len(min_workers)
    num_min_workers_rich = len(min_workers[min_workers['salary'] == '>50K'])
    rich_percentage = round(num_min_workers_rich / num_min_workers * 100, 1)

    # What country has the highest percentage of people that earn >50K?
    country_counts = df['native-country'].value_counts()
    country_rich_counts = df[df['salary'] == '>50K']['native-country'].value_counts()
    rich_percentage_by_country = (country_rich_counts / country_counts * 100).fillna(0)
    highest_earning_country = rich_percentage_by_country.idxmax()
    highest_earning_country_percentage = round(rich_percentage_by_country.max(), 1)

    # Identify the most popular occupation for those who earn >50K in India.
    indian_rich = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]
    top_IN_occupation = indian_rich['occupation'].value_counts().idxmax()

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