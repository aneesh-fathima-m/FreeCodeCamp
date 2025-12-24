import pandas as pd

def calculate_demographic_data(df):
    # 1. Number of people of each race
    race_count = df['race'].value_counts()

    # 2. Average age of men
    average_age_men = round(df[df['sex'] == 'Male']['age'].mean(), 1)

    # 3. Percentage of people with a Bachelor's degree
    total_people = df.shape[0]
    bachelors_count = df[df['education'] == 'Bachelors'].shape[0]
    percentage_bachelors = round(bachelors_count / total_people * 100, 1)

    # 4. Percentage with advanced education (>50K)
    advanced_education = ['Bachelors', 'Masters', 'Doctorate']
    higher_edu = df[df['education'].isin(advanced_education)]
    lower_edu = df[~df['education'].isin(advanced_education)]

    higher_edu_rich = higher_edu[higher_edu['salary'] == '>50K']
    lower_edu_rich = lower_edu[lower_edu['salary'] == '>50K']

    higher_education_rich = round(len(higher_edu_rich) / len(higher_edu) * 100, 1)
    lower_education_rich = round(len(lower_edu_rich) / len(lower_edu) * 100, 1)

    # 5. Minimum number of hours worked per week
    min_work_hours = df['hours-per-week'].min()

    # 6. Percentage of rich among those who work minimum hours
    min_workers = df[df['hours-per-week'] == min_work_hours]
    rich_min_workers = min_workers[min_workers['salary'] == '>50K']
    rich_percentage_min_workers = round(len(rich_min_workers) / len(min_workers) * 100, 1)

    # 7. Country with highest percentage of rich people
    country_counts = df['native-country'].value_counts()
    country_rich_counts = df[df['salary'] == '>50K']['native-country'].value_counts()
    rich_country_percentages = (country_rich_counts / country_counts * 100).fillna(0)
    highest_earning_country = rich_country_percentages.idxmax()
    highest_earning_country_percentage = round(rich_country_percentages.max(), 1)

    # 8. Most popular occupation for those who earn >50K in India
    india_rich = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]
    top_IN_occupation = india_rich['occupation'].mode()[0] if not india_rich.empty else None

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage_min_workers': rich_percentage_min_workers,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage': highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
