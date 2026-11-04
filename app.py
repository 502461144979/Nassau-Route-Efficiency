
import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(
    page_title="Nassau Candy Route Efficiency",
    page_icon="🚚",
    layout="wide"
)


# ==============================
# CUSTOM DASHBOARD CSS
# ==============================

st.markdown("""
<style>


/* Professional dashboard header */
.dashboard-header {
    display: flex;
    align-items: center;
    gap: 22px;
    padding: 28px 32px;
    margin-bottom: 25px;
    background: linear-gradient(120deg, #142D4E, #126E82);
    border-radius: 18px;
    box-shadow: 0 5px 18px rgba(20, 45, 78, 0.15);
}

.dashboard-header .header-icon {
    font-size: 48px;
}

.dashboard-header h1 {
    color: #FFFFFF !important;
    font-size: 30px;
    margin: 0;
    font-weight: 800;
}

.dashboard-header p {
    color: #D5F3F2;
    font-size: 13px;
    font-weight: 700;
    letter-spacing: 1.5px;
    margin: 8px 0;
}

.dashboard-header span {
    color: #FFFFFF;
    font-size: 14px;
}

/* Main dashboard background */
.stApp {
    background-color: #F4F7FB;
    color: #1E293B;
}

/* Main content area */
.block-container {
    padding-top: 2rem;
    padding-bottom: 3rem;
}

/* Dashboard title */
h1 {
    color: #142D4E;
    font-weight: 800;
    letter-spacing: -0.5px;
}


/* Professional section headings */
h2, h3 {
    color: #173B5E;
    font-weight: 750;
    letter-spacing: -0.4px;
    padding-bottom: 10px;
    border-bottom: 3px solid #D5E9EA;
    margin-top: 30px;
    margin-bottom: 18px;
}


/* KPI metric cards */
[data-testid="stMetric"] {
    background: linear-gradient(135deg, #FFFFFF, #EAF2FB);
    border: 1px solid #D7E3F0;
    padding: 20px;
    border-radius: 14px;
    box-shadow: 0 3px 12px rgba(20, 45, 78, 0.07);
}

/* Metric labels */
[data-testid="stMetricLabel"] {
    color: #52677F;
    font-weight: 600;
}

/* Metric values */
[data-testid="stMetricValue"] {
    color: #126E82;
    font-weight: 800;
}

/* Sidebar */


/* Professional sidebar filter styling */
[data-testid="stSidebar"] label {
    font-weight: 700;
    color: #173B5E;
    font-size: 15px;
}


/* Sidebar Professional Styling */
[data-testid="stSidebar"] h2 {
    color: #173B5E;
    font-size: 23px;
    font-weight: 800;
    padding-bottom: 12px;
    border-bottom: 3px solid #1595A3;
    margin-bottom: 22px;
}

/* Filter labels */
[data-testid="stSidebar"] label {
    font-weight: 700;
    color: #173B5E;
    font-size: 15px;
    margin-bottom: 7px;
}

/* Space between filter widgets */
[data-testid="stSidebar"] [data-testid="stSelectbox"] {
    margin-bottom: 16px;
}

/* Sidebar divider */
[data-testid="stSidebar"] hr {
    border-color: #C9D9E8;
    margin-top: 20px;
    margin-bottom: 18px;
}


[data-testid="stSidebar"] [data-baseweb="select"] > div {
    border-radius: 10px;
    border: 1px solid #C9D9E8;
    background-color: #FFFFFF;
    min-height: 46px;
}

[data-testid="stSidebar"] [data-baseweb="select"] > div:hover {
    border-color: #126E82;
}

[data-testid="stSidebar"] [data-baseweb="select"] > div:focus-within {
    border-color: #126E82;
    box-shadow: 0 0 0 2px rgba(18, 110, 130, 0.15);
}


[data-testid="stSidebar"] {
    background-color: #E8F0F8;
    border-right: 1px solid #D4E0ED;
}

/* Sidebar text */
[data-testid="stSidebar"] * {
    color: #193653;
}

/* Buttons */
.stButton > button {
    background-color: #126E82;
    color: white;
    border: none;
    border-radius: 9px;
    padding: 8px 18px;
    font-weight: 600;
}

.stButton > button:hover {
    background-color: #0D5365;
    color: white;
    border: none;
}

/* Dataframes and tables */
[data-testid="stDataFrame"] {
    border: 1px solid #D7E3F0;
    border-radius: 10px;
    overflow: hidden;
}

/* Dividers */
hr {
    border-color: #D7E3F0;
}

/* Captions */
.stCaption {
    color: #64748B;
}

/* Download button */
[data-testid="stDownloadButton"] button {
    background-color: #1E456D;
    color: white;
    border-radius: 9px;
    border: none;
}

/* Chart containers */
[data-testid="stPlotlyChart"] {
    background-color: white;
    padding: 10px;
    border: 1px solid #E1EAF3;
    border-radius: 12px;
}


/* Reset Filters Button */
[data-testid="stSidebar"] button {
    background: linear-gradient(135deg, #126E82, #1595A3);
    color: white !important;
    border: none;
    border-radius: 10px;
    font-weight: 700;
    min-height: 45px;
    transition: all 0.2s ease;
}

[data-testid="stSidebar"] button:hover {
    background: linear-gradient(135deg, #0E596B, #126E82);
    color: white !important;
    border: none;
    box-shadow: 0 4px 12px rgba(18, 110, 130, 0.25);
}


/* Project Information Card */
.project-info {
    background: linear-gradient(145deg, #EAF4F8, #FFFFFF);
    border: 1px solid #C9DDE8;
    border-left: 4px solid #126E82;
    border-radius: 12px;
    padding: 16px;
    margin-top: 18px;
    box-shadow: 0 3px 10px rgba(23, 59, 94, 0.08);
}

.project-info h3 {
    color: #173B5E;
    font-size: 17px;
    margin-top: 0;
    margin-bottom: 15px;
}

.project-info p {
    color: #334155;
    font-size: 13px;
    line-height: 1.5;
    margin-bottom: 12px;
}

.project-info strong {
    color: #126E82;
}

.project-footer {
    border-top: 1px solid #C9DDE8;
    padding-top: 10px;
    margin-top: 12px;
    color: #126E82;
    font-size: 11px;
    font-weight: 800;
    letter-spacing: 1px;
}


</style>
""", unsafe_allow_html=True)



# Professional Dashboard Header
st.markdown("""
<div class="dashboard-header">
    <div class="header-icon">🚚</div>
    <div>
        <h1>Factory-to-Customer Route Efficiency</h1>
        <p>NASSAU CANDY DISTRIBUTOR | INTERNSHIP PROJECT</p>
        <span>Route Analytics • Factory Performance • Customer Distribution</span>
    </div>
</div>
""", unsafe_allow_html=True)


st.warning(
    "Data-quality notice: the recorded order and ship dates produce "
    "lead times of 904–1,642 days. Shipping-time KPIs are withheld "
    "until the date issue is verified."
)

@st.cache_data
def load_data():
    data = pd.read_csv("Nassau Candy Distributor.csv")

    factory_map = {
        "Wonka Bar - Nutty Crunch Surprise": "Lot's O' Nuts",
        "Wonka Bar - Fudge Mallows": "Lot's O' Nuts",
        "Wonka Bar -Scrumdiddlyumptious": "Lot's O' Nuts",
        "Wonka Bar - Milk Chocolate": "Wicked Choccy's",
        "Wonka Bar - Triple Dazzle Caramel": "Wicked Choccy's",
        "Laffy Taffy": "Sugar Shack",
        "SweeTARTS": "Sugar Shack",
        "Nerds": "Sugar Shack",
        "Fun Dip": "Sugar Shack",
        "Fizzy Lifting Drinks": "Sugar Shack",
        "Everlasting Gobstopper": "Secret Factory",
        "Hair Toffee": "The Other Factory",
        "Lickable Wallpaper": "Secret Factory",
        "Wonka Gum": "Secret Factory",
        "Kazookles": "The Other Factory",
    }

    data["Factory"] = data["Product Name"].map(factory_map)
    data["State/Province"] = (
        data["State/Province"].astype(str).str.strip()
    )
    data["Region"] = data["Region"].astype(str).str.strip()
    return data

df = load_data()



st.sidebar.header("Filters")

factories = ["All"] + sorted(df["Factory"].dropna().unique().tolist())
regions = ["All"] + sorted(df["Region"].dropna().unique().tolist())
ship_modes = ["All"] + sorted(df["Ship Mode"].dropna().unique().tolist())

def reset_filters():
    st.session_state["factory_filter"] = "All"
    st.session_state["region_filter"] = "All"
    st.session_state["ship_mode_filter"] = "All"

selected_factory = st.sidebar.selectbox(
    "Factory", factories, key="factory_filter"
)

selected_region = st.sidebar.selectbox(
    "Region", regions, key="region_filter"
)

selected_ship_mode = st.sidebar.selectbox(
    "Ship mode", ship_modes, key="ship_mode_filter"
)

# Reset button at the bottom
st.sidebar.markdown("---")

st.sidebar.button(
    "↻ Reset All Filters",
    on_click=reset_filters,
    use_container_width=True
)

filtered = df.copy()


# Project Information at the bottom of sidebar
st.sidebar.markdown("""
<div class="project-info">
    <h3>📊 Project Information</h3>
    <p><strong>Project:</strong><br>Nassau Candy Distributor</p>
    <p><strong>Analysis:</strong><br>Shipping Route Efficiency</p>
    <p><strong>Technology:</strong><br>Python • Streamlit • Plotly</p>
    <div class="project-footer">INTERNSHIP PROJECT</div>
</div>
""", unsafe_allow_html=True)



if selected_factory != "All":
    filtered = filtered[filtered["Factory"] == selected_factory]

if selected_region != "All":
    filtered = filtered[filtered["Region"] == selected_region]

if selected_ship_mode != "All":
    filtered = filtered[filtered["Ship Mode"] == selected_ship_mode]


# Top-level KPIs
col1, col2, col3, col4 = st.columns(4)

total_sales = filtered["Sales"].sum()

if abs(total_sales) >= 1000:
    sales_display = f"${total_sales / 1000:,.1f}K"
else:
    sales_display = f"${total_sales:,.2f}"

col1.metric(
    "Dataset Rows",
    f"{len(filtered):,}"
)

col2.metric(
    "Unique Orders",
    f"{filtered['Order ID'].nunique():,}"
)

col3.metric(
    "Customer Locations",
    f"{filtered['State/Province'].nunique():,}"
)

col4.metric(
    "Total Sales",
    sales_display,
    help=f"Exact total sales: ${total_sales:,.2f}"
)

st.divider()

# Route volume analysis
st.subheader("Factory-to-Customer Route Volume")

route_summary = (
    filtered.groupby(["Factory", "State/Province"])
    .agg(
        Row_Count=("Row ID", "count"),
        Unique_Orders=("Order ID", "nunique"),
        Total_Sales=("Sales", "sum"),
        Total_Units=("Units", "sum")
    )
    .reset_index()
    .sort_values("Row_Count", ascending=False)
)

if not route_summary.empty:
    top_routes = route_summary.head(15)

    fig_routes = px.bar(
        top_routes.sort_values("Row_Count"),
        x="Row_Count",
        y="State/Province",
        color="Factory",
        orientation="h",
        title="Top 15 Factory-to-State Routes by Dataset Row Count",
        hover_data=["Unique_Orders", "Total_Sales", "Total_Units"]
    )

    
    st.plotly_chart(fig_routes, use_container_width=True)

    st.dataframe(route_summary, use_container_width=True)
else:
    st.info("No routes match the selected filters.")

st.divider()




# Factory Insights Summary
st.subheader("📌 Factory Insights Summary")

factory_insights = (
    filtered.groupby("Factory")
    .agg(
        Dataset_Rows=("Row ID", "count"),
        Unique_Orders=("Order ID", "nunique"),
        Customer_States=("State/Province", "nunique"),
        Total_Sales=("Sales", "sum")
    )
    .reset_index()
)

if not factory_insights.empty:
    highest_volume = factory_insights.loc[
        factory_insights["Dataset_Rows"].idxmax()
    ]

    highest_orders = factory_insights.loc[
        factory_insights["Unique_Orders"].idxmax()
    ]

    widest_coverage = factory_insights.loc[
        factory_insights["Customer_States"].idxmax()
    ]

    total_routes = filtered.groupby(
        ["Factory", "State/Province"]
    ).ngroups

    col1, col2 = st.columns(2)

    col1.metric(
        "Highest Dataset Volume",
        highest_volume["Factory"],
        f"{int(highest_volume['Dataset_Rows']):,} rows"
    )

    col2.metric(
        "Highest Unique Orders",
        highest_orders["Factory"],
        f"{int(highest_orders['Unique_Orders']):,} orders"
    )

    col3, col4 = st.columns(2)

    col3.metric(
        "Widest State Coverage",
        widest_coverage["Factory"],
        f"{int(widest_coverage['Customer_States'])} states/provinces"
    )

    col4.metric(
        "Factory-to-State Connections",
        f"{total_routes:,}"
    )

    st.dataframe(
        factory_insights,
        use_container_width=True,
        hide_index=True
    )
else:
    st.info("No factory data available for the selected filters.")


# Factory Performance Comparison
st.subheader("🏭 Factory Performance Comparison")

factory_performance = (
    filtered.groupby("Factory")
    .agg(
        Dataset_Rows=("Row ID", "count"),
        Unique_Orders=("Order ID", "nunique"),
        Total_Sales=("Sales", "sum"),
        Total_Units=("Units", "sum")
    )
    .reset_index()
    .sort_values("Dataset_Rows", ascending=False)
)

factory_chart = px.bar(
    factory_performance,
    x="Factory",
    y="Dataset_Rows",
    color="Factory",
    hover_data=["Unique_Orders", "Total_Sales", "Total_Units"],
    title="Dataset Volume by Factory"
)

st.plotly_chart(factory_chart, use_container_width=True)

st.dataframe(
    factory_performance,
    use_container_width=True,
    hide_index=True
)

st.caption(
    "Dataset rows and unique order IDs are used as volume indicators. "
    "They do not directly measure factory productivity or delivery efficiency."
)

# Geographic customer destination map (United States)
st.subheader("🗺️ US Customer Destination Map")

us_data = filtered[
    filtered["Country/Region"].str.strip().eq("United States")
].copy()

state_sales = (
    us_data.groupby("State/Province")
    .agg(
        Dataset_Rows=("Row ID", "count"),
        Total_Sales=("Sales", "sum"),
        Unique_Orders=("Order ID", "nunique")
    )
    .reset_index()
)

# State abbreviations required by Plotly's US map
state_codes = {
    "Alabama": "AL", "Arizona": "AZ", "Arkansas": "AR",
    "California": "CA", "Colorado": "CO", "Connecticut": "CT",
    "Delaware": "DE", "District of Columbia": "DC", "Florida": "FL",
    "Georgia": "GA", "Idaho": "ID", "Illinois": "IL",
    "Indiana": "IN", "Iowa": "IA", "Kansas": "KS",
    "Kentucky": "KY", "Louisiana": "LA", "Maine": "ME",
    "Maryland": "MD", "Massachusetts": "MA", "Michigan": "MI",
    "Minnesota": "MN", "Mississippi": "MS", "Missouri": "MO",
    "Montana": "MT", "Nebraska": "NE", "Nevada": "NV",
    "New Hampshire": "NH", "New Jersey": "NJ", "New Mexico": "NM",
    "New York": "NY", "North Carolina": "NC", "North Dakota": "ND",
    "Ohio": "OH", "Oklahoma": "OK", "Oregon": "OR",
    "Pennsylvania": "PA", "Rhode Island": "RI",
    "South Carolina": "SC", "South Dakota": "SD",
    "Tennessee": "TN", "Texas": "TX", "Utah": "UT",
    "Vermont": "VT", "Virginia": "VA", "Washington": "WA",
    "West Virginia": "WV", "Wisconsin": "WI", "Wyoming": "WY"
}

state_sales["State Code"] = state_sales["State/Province"].map(state_codes)
map_data = state_sales.dropna(subset=["State Code"])

if not map_data.empty:
    fig_map = px.choropleth(
        map_data,
        locations="State Code",
        locationmode="USA-states",
        color="Dataset_Rows",
        scope="usa",
        hover_name="State/Province",
        hover_data=["Dataset_Rows", "Unique_Orders", "Total_Sales"],
        title="Customer Distribution by US State"
    )
    st.plotly_chart(fig_map, use_container_width=True)
else:
    st.info("No US states match the selected filters.")

st.caption(
    "Map values represent dataset rows, not confirmed delivery counts. "
    "Canadian provinces are excluded from this US-only map."
)


# Factory-to-Customer Route Flow Map
st.subheader("🚚 Factory-to-Customer Route Flow Map")

factory_coordinates = {
    "Lot's O' Nuts": (32.881893, -111.768036),
    "Wicked Choccy's": (32.076176, -81.088371),
    "Sugar Shack": (48.11914, -96.18115),
    "Secret Factory": (41.446333, -90.565487),
    "The Other Factory": (35.1175, -89.971107)
}

state_coordinates = {
    "California": (36.7783, -119.4179),
    "New York": (40.7128, -74.0060),
    "Texas": (31.9686, -99.9018),
    "Pennsylvania": (41.2033, -77.1945),
    "Washington": (47.7511, -120.7401),
    "Illinois": (40.6331, -89.3985),
    "Ohio": (40.4173, -82.9071),
    "Florida": (27.6648, -81.5158),
    "Michigan": (44.3148, -85.6024),
    "North Carolina": (35.7596, -79.0193)
}

route_flow = (
    filtered.groupby(["Factory", "State/Province"])
    .agg(Dataset_Rows=("Row ID", "count"))
    .reset_index()
)

route_flow = route_flow[
    route_flow["State/Province"].isin(state_coordinates)
].copy()

route_flow = route_flow.sort_values(
    "Dataset_Rows", ascending=False
).head(30)

fig_flow = px.scatter_geo(
    route_flow,
    lat=route_flow["State/Province"].map(
        lambda state: state_coordinates[state][0]
    ),
    lon=route_flow["State/Province"].map(
        lambda state: state_coordinates[state][1]
    ),
    color="Factory",
    size="Dataset_Rows",
    hover_name="State/Province",
    hover_data=["Factory", "Dataset_Rows"],
    scope="usa",
    title="Top 30 Factory-to-Customer State Connections"
)


for factory, (latitude, longitude) in factory_coordinates.items():
    fig_flow.add_scattergeo(
        lat=[latitude],
        lon=[longitude],
        mode="markers+text",
        marker=dict(size=12, symbol="star"),
        text=[factory],
        textposition="top center",
        name=factory,
        showlegend=False
    )


st.plotly_chart(fig_flow, use_container_width=True)

st.caption(
    "Factory stars show factory locations. Customer markers show "
    "selected destination states. Marker sizes represent dataset rows. "
    "This is a geographic relationship map, not actual road routes."
)



# Bottom 10 Factory-to-State Routes
st.subheader("📉 Bottom 10 Factory-to-State Routes")

bottom_routes = (
    filtered.groupby(["Factory", "State/Province"])
    .agg(
        Dataset_Rows=("Row ID", "count"),
        Unique_Orders=("Order ID", "nunique"),
        Total_Sales=("Sales", "sum"),
        Total_Units=("Units", "sum")
    )
    .reset_index()
    .sort_values("Dataset_Rows", ascending=True)
    .head(10)
)

st.dataframe(
    bottom_routes,
    use_container_width=True,
    hide_index=True
)

bottom_chart = px.bar(
    bottom_routes,
    x="Dataset_Rows",
    y="State/Province",
    color="Factory",
    orientation="h",
    hover_data=["Unique_Orders", "Total_Sales", "Total_Units"],
    title="10 Lowest-Volume Factory-to-State Routes"
)

st.plotly_chart(bottom_chart, use_container_width=True)


st.caption(
    "These are the 10 routes with the lowest dataset-row counts "
    "after applying the selected filters. Low volume does not necessarily "
    "mean poor shipping efficiency."
)


# Ship mode comparison
st.subheader("Shipping Mode Comparison")

mode_summary = (
    filtered.groupby("Ship Mode")
    .agg(
        Dataset_Rows=("Row ID", "count"),
        Unique_Orders=("Order ID", "nunique"),
        Total_Sales=("Sales", "sum")
    )
    .reset_index()
)

col1, col2 = st.columns(2)

with col1:
    fig_modes = px.bar(
        mode_summary,
        x="Ship Mode",
        y="Dataset_Rows",
        title="Dataset Rows by Ship Mode",
        hover_data=["Unique_Orders", "Total_Sales"]
    )
    st.plotly_chart(fig_modes, use_container_width=True)

with col2:
    fig_sales = px.pie(
        mode_summary,
        names="Ship Mode",
        values="Dataset_Rows",
        title="Share of Dataset Rows by Ship Mode"
    )
    st.plotly_chart(fig_sales, use_container_width=True)

st.divider()

st.subheader("Data Quality")
st.write(f"Missing values in filtered data: {int(filtered.isna().sum().sum())}")
st.write(
    "Shipping lead-time and delay KPIs are not displayed because "
    "the recorded dates require verification."
)

st.download_button(
    "Download filtered route summary",
    data=route_summary.to_csv(index=False).encode("utf-8"),
    file_name="filtered_route_summary.csv",
    mime="text/csv"
)

st.caption(
    "Note: route volume is based on dataset rows. "
    "Unique orders are counted separately because an order can contain "
    "multiple product rows."
)
