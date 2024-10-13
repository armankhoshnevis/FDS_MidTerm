import streamlit as st
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils.race_schedule_vis import (
    f1_circuit_world_map,
    races_by_continent,
    races_by_circuit,
    races_by_country
    )

from utils.constructor_standing_vis import (
    plot_constructor_ranking_vs_year,
    plot_constructor_wins_vs_year,
    plot_constructor_points_vs_year,
    plot_constructor_points_distribution_per_year,
    plot_overall_win_percentage,
    plot_yearly_win_percentage
    )

st.set_page_config(
    page_title="FDS Project - F1",
    page_icon="f1logo.png",
    layout="wide"
)

# Sidebar for EDA section
st.sidebar.title("F1 Data Analysis")

# EDA Sections
eda_section = st.sidebar.selectbox("Select Section", ["Introduction", "Race Circuits", "Constructor Standing", "Driver Standing", "Race Results", "Pit Stops"])

# Race Circuits Subsection
if eda_section == "Introduction":
    image_path = os.path.join(os.path.dirname(__file__), "DALLE_2024_10_10.webp")
    st.image(image_path, caption="AI-Generated Picture, DALL·E, 2024-10-10", use_column_width=True)
    st.markdown("""
                ### Hello F1
                
                Formula One, or F1, stands as the world's most elite motorsport league. It is not only about the
                drivers battling for the championship but also about the constructors, supported by a vast team of
                designers, manufacturers, engineers, data scientists, AI specialists, and more, all competing for
                the constructors' championship. In many ways, this is truly a "league of nerds" as well!

                Each F1 season, which spans roughly nine months, features 24 races known as Grands Prix, where 20
                drivers from 10 teams compete against each other. During each race, lap, sector, and corner, an
                enormous amount of data is collected by car sensors and transmitted to various engineering teams.
                This data enables the teams to fine-tune car settings, introduce updates throughout the season, 
                and prepare the best possible car for the following year.

                In today's world of data and AI, F1 is no exception. As James Vowles, Team Principal of Williams
                Racing, aptly put it, “Data, for me, is the foundation of F1. There's no human judgment involved.
                You've got to get your foundation right in data.” In this analysis, powered by the renowned Ergast
                API, we delve into different aspects of F1 to gain a clearer, more profound understanding of 
                driver and constructor performance, along with the many factors influencing them.
                
                In this project, we are primarily focused on the "Hybrid Era" of Formula 1, which began in 2014 with the
                introduction of 1.6-liter V6 turbocharged hybrid power units. Emphasis is placed on data from 2017
                onwards, to account for the learning curve teams faced while adapting to hybrid engines and to
                observe the impact of the regulation changes in 2022, along with the dominance and team battles in
                recent years.
                
                Explore the data through interactive visualization tools on this website and uncover the dynamics
                of F1. Enjoy your journey into the world of data-driven motorsport!
                
                Prepared by Arman Khoshnevis (khoshne1@msu.edu), Fall 2024
                """)

elif eda_section == "Race Circuits":
    visualization = st.sidebar.selectbox(
        "Select Visualization",
        ["World Map (F1 Circuits)", "Races by Continent", "Races by Circuit/Country"]
    )
    if visualization == "World Map (F1 Circuits)":
        year = st.sidebar.selectbox("Select Year", options=[2024, 2023, 2022, 2021, 2020, 2019, 2018, 2017])
        fig = f1_circuit_world_map(year)
        st.plotly_chart(fig, use_container_width=True)
        st.markdown("""
                    Here, you can see the global distribution of Formula 1 circuits for a selected year.
                    Each marker highlights a race location, with details on the circuit and country.
                    The map emphasizes the diverse environmental conditions, that teams must adapt to for optimal
                    performance. These variations influence car setup and driver preparation, 
                    underscoring the logistical challenges teams face in navigating the season's unique demands.
                    """
        )
    
    elif visualization == "Races by Continent":
        fig = races_by_continent()
        st.plotly_chart(fig, use_container_width=True)
        st.markdown("""
                    This visualization illustrates the distribution of Formula 1 races by continent over the past
                    several seasons. Europe holds the largest share of the calendar each year, emphasizing its
                    historical and ongoing importance in F1. Asia and the Middle East follow closely, reflecting 
                    the sport's expansion into new regions. North and South America account for fewer races,
                    yet play a critical role in rounding out the global F1 season. Each continent’s race count is
                    shown in terms of absolute numbers and percentages, highlighting their relative contributions.
                    """
        )
    
    elif visualization == "Races by Circuit/Country":
        start_year, end_year = st.sidebar.select_slider(
            "Select Year Range",
            options=list(range(2017, 2025)),
            value=(2017, 2024)
        )
        y_axis_choice = st.sidebar.selectbox(
            "Select Y-Axis",
            options=["Circuit", "Country"]
        )
        if y_axis_choice == "Circuit":
            fig = races_by_circuit(start_year=start_year, end_year=end_year)
        elif y_axis_choice == "Country":
            fig = races_by_country(start_year=start_year, end_year=end_year)
        st.plotly_chart(fig, use_container_width=True)
        st.markdown("""
                    This bar chart showcases the number of Formula 1 races held in each country/circuit over the
                    selected time frame. The visualization highlights the USA’s growing influence on the F1 
                    calendar, partially due to the attractive documentary named Drive to Survive by Netflix,
                    currently hosting three races each season in Austin, Miami, and Las Vegas. It also reflects
                    the enduring presence of classic circuits in countries such as Monaco, the UK, Hungary, and
                    Austria, which have consistently retained their places in the F1 schedule. Additionally, this
                    chart reveals countries that were once hosts but have since departed from the calendar,
                    underscoring F1's dynamic global footprint.
                    """)

elif eda_section == "Constructor Standing":
    st.subheader("Constructor Standing Visualizations")
    
    constructor_vis_option = st.sidebar.selectbox(
        "Select Visualization",
        ["Yearly Trends", "Dominance"]
    )
    
    if constructor_vis_option == "Yearly Trends":
        start_year, end_year = st.sidebar.select_slider(
            "Select Year Range",
            options=list(range(2017, 2025)),
            value=(2017, 2024)
        )
        
        show_ranking = st.sidebar.checkbox("Show Ranking vs Year", value=True)
        show_wins = st.sidebar.checkbox("Show Wins vs Year", value=True)
        show_points = st.sidebar.checkbox("Show Points vs Year", value=True)

        if show_ranking:
            st.write("### Ranking vs Year")
            fig_ranking = plot_constructor_ranking_vs_year(start_year=start_year, end_year=end_year)
            st.plotly_chart(fig_ranking, use_container_width=True)

        if show_wins:
            st.write("### Wins vs Year")
            fig_wins = plot_constructor_wins_vs_year(start_year=start_year, end_year=end_year)
            st.plotly_chart(fig_wins, use_container_width=True)

        if show_points:
            st.write("### Points vs Year")
            fig_points = plot_constructor_points_vs_year(start_year=start_year, end_year=end_year)
            st.plotly_chart(fig_points, use_container_width=True)
        
        st.markdown("""
                    These visualizations track constructor performance trends in rankings, wins, and points across
                    recent seasons. Mercedes' dominance is evident from 2017 to 2021, followed by the rise of
                    Red Bull, starting in 2021 and solidifying through 2023. By 2024, a closer championship battle
                    emerges between Red Bull, McLaren, Ferrari, and Mercedes, reflecting the impact of the 2022
                    regulation changes aimed at enhancing competition.

                    In the mid-to-lower rankings, Aston Martin has solidified a middle-ground position, with Haas
                    showing marked improvement. In contrast, Alpine has experienced a notable decline, continuing
                    from its rebranding of Renault in 2020-2021. Additionally, Alfa Romeo’s transition to Sauber
                    in 2023 further reshapes the grid's landscape, highlighting the evolving dynamics within the
                    constructor standings.
                    """)

    elif constructor_vis_option == "Dominance":
        st.write("### Points Distribution per Year")
        fig_points_dist = plot_constructor_points_distribution_per_year()
        st.plotly_chart(fig_points_dist, use_container_width=True)

        st.write("### Overall Win Percentage per Constructor")
        fig_overall_win_percentage = plot_overall_win_percentage()
        st.plotly_chart(fig_overall_win_percentage, use_container_width=True)

        st.write("### Year-by-Year Win Percentage per Constructor")
        fig_yearly_win_percentage = plot_yearly_win_percentage()
        st.plotly_chart(fig_yearly_win_percentage, use_container_width=True)
        
        st.markdown("""
                    The points distribution visualization provides a higher-level look into constructor dominance
                    each season. Notably, 2021 and 2023 show a wide range of high points, reflecting dominant
                    performances. In contrast, the 2024 season displays a much narrower distribution, indicating
                    a more competitive field.
                    
                    The overall and yearly win percentage charts further emphasize the shifts in constructor
                    dominance, highlighting how leading teams' win shares have evolved. Together, these
                    visualizations underscore the competitive dynamics and changes in the F1 landscape over recent
                    years.
                    """)