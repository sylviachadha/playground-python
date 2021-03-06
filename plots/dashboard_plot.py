from helpers import get_db_connection
import random


def all_plots_dashboard_dict(query_components):
    conn = get_db_connection()
    cursor = conn.cursor(as_dict=True)

    age_group = age_group_plot_data(cursor, query_components)
    gauge = random.randint(80, 90)

    conn.close()
    python_dict = {"age_group": age_group, "gauge": gauge}
    return python_dict


def age_group_plot_data(cursor, query_components):  # Extract Data from Microsoft SQL Server

    start_date = query_components["start_date"]
    end_date = query_components["end_date"]
    radio_value = query_components["radio"]

    # Initialize dictionary which will be returned at end
    return_dict = {"longTerm": [], "recent": []}

    long_term_db_query = f"SELECT Age_Group,COUNT(*) AS Count FROM HIV_Sample_tables WHERE RecencyTest_Date >= '{start_date}' and RecencyTest_Date <= '{end_date}' GROUP BY Age_Group, New_HIV_Diagnosis_and_Recency_Test_taken HAVING New_HIV_Diagnosis_and_Recency_Test_taken = 'Long-term' ORDER BY Age_Group;"
    recent_db_query = f"SELECT Age_Group,COUNT(*) AS Count FROM HIV_Sample_tables WHERE RecencyTest_Date >= '{start_date}' and RecencyTest_Date <= '{end_date}' GROUP BY Age_Group, New_HIV_Diagnosis_and_Recency_Test_taken HAVING New_HIV_Diagnosis_and_Recency_Test_taken = 'Recent' ORDER BY Age_Group;"

    if radio_value == 'all' or radio_value == 'longTerm':
        cursor.execute(long_term_db_query)
        # row return as per query will have age group and count but we only take count for plot in javascript
        for row in cursor:
            return_dict['longTerm'].append(row["Count"])

    if radio_value == 'all' or radio_value == 'recent':
        cursor.execute(recent_db_query)
        for row in cursor:
            return_dict['recent'].append(row["Count"])

    return return_dict
