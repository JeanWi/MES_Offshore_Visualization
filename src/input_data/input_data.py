import streamlit as st
from .installed_capacities import *
from .node_definition import *
from .profiles import *
from .annual_figures import *

def show_page_input_data(sub_page):

    st.header(sub_page)

    categories = {'Installed Capacities':
                  ['Compare installed capacities per country from sources',
                   'Installed Capacities per node'],
                  'Renewable generation profiles and demand':
                  ['Aggregated (total)', 'Aggregated (per country)', 'Per node']}

    # Installed Capacities
    if sub_page == 'Installed Capacities':
        st.write('This page gives two options: You can show installed capacities per country and compare the assumptions made in '
                 'this work to TYNDP, ERAA and PyPsa. Or you can show installed capacities allocated to each node of this work. The allocation '
                 'method is described in the SI of the paper. Select an option and technologies below.')
        category = st.selectbox("Select an option:", categories[sub_page])
        if category == 'Compare installed capacities per country from sources':
            compare_national_capacities()
        elif category == 'Installed Capacities per node':
            show_nodal_capacities()

    # Node definitions (map)
    elif sub_page == 'Node definition':
        st.write('This page shows the node definition used in this work, as well as NUTS2 regions used and wind farms included. '
                 'Select a respective layer below.')
        show_node_definition()
        # pass

    # Renewable Profiles and Demand
    elif sub_page == 'Renewable generation profiles and demand':
        st.write('This page shows the generation profiles of non-dispatchable generation technologies, inflows to hydro storage technologies'
                 'as well as electricity demand on three levels (without curtailment). Aggregated (total) depicts total generation and '
                 'demand summed over all nodes, this data is not to be used in the optimizations. Aggregated (per country) depicts total generation'
                 'and demand for each country, summed over the nodes for each country, also this data is not to be used in the optimizations. '
                 'Per node depicts demand and generation per node, as to be used in the optimizations. Select a respective time series below. You can also '
                 'shorten the shown time horizon on the side bar.')
        category = st.selectbox("Select an option:", categories[sub_page])
        show_profiles(category)

    elif sub_page == 'Annual renewable generation and demand':
        st.write('This page shows the aggregation of non-dispatchable generation technologies over a full year as well as average capacity'
                 'factor over a full year.')
        show_annual_figures()





