
from pathlib import Path

import pandas as pd
import streamlit as st
import plotly.express as px


# =========================================================
# 1. PAGE CONFIGURATION
# =========================================================
st.set_page_config(
    page_title="Air Quality Explorer | Beijing",
    page_icon="🌫️",
    layout="wide",
    initial_sidebar_state="expanded",
)


# =========================================================
# 2. CUSTOM STYLING
# =========================================================

st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }

    .stApp {
        background-color: #0B1120;
        color: #E5EDF7;
    }

    [data-testid="stHeader"] {
        background-color: rgba(11, 17, 32, 0.95);
    }

    /* ===== SIDEBAR BASE ===== */
    [data-testid="stSidebar"] {
        background-color: #111B2E;
        border-right: 1px solid #263852;
    }

    [data-testid="stSidebar"] > div:first-child {
        padding-top: 1.2rem;
    }

    [data-testid="stSidebar"] h1,
    [data-testid="stSidebar"] h2,
    [data-testid="stSidebar"] h3,
    [data-testid="stSidebar"] label {
        color: #E5EDF7;
    }

    /* Sidebar header */
    .sidebar-brand {
        display: flex;
        align-items: center;
        gap: 11px;
        padding: 5px 0 20px;
    }

    .sidebar-brand-icon {
        display: flex;
        align-items: center;
        justify-content: center;
        flex-shrink: 0;
        width: 48px;
        height: 48px;
        border-radius: 14px;
        background: #15374B;
        color: #67E8F9;
        font-size: 30px;
        font-weight: 700;
    }

    .sidebar-brand-text {
        flex: 1;
        min-width: 0;
    }

    .sidebar-brand-title {
        color: #F8FAFC;
        font-size: 17px;
        font-weight: 750;
        line-height: 1.35;
    }

    .sidebar-brand-subtitle {
        margin-top: 4px;
        color: #94A3B8;
        font-size: 9px;
        line-height: 1.5;
        letter-spacing: 0.5px;
    }

    .sidebar-year {
        align-self: flex-start;
        padding: 4px 7px;
        border-radius: 20px;
        background: #15374B;
        color: #67E8F9;
        font-size: 10px;
        white-space: nowrap;
    }

    .sidebar-divider {
        height: 1px;
        margin-bottom: 20px;
        background: #334155;
    }

    .sidebar-heading {
        margin-bottom: 6px;
        color: #F1F5F9;
        font-size: 18px;
        font-weight: 700;
    }

    .sidebar-description {
        margin-bottom: 20px;
        color: #94A3B8;
        font-size: 13px;
        line-height: 1.6;
    }

    .sidebar-field-label {
        margin: 12px 0 8px;
        color: #DCE7F5;
        font-size: 14px;
        font-weight: 600;
    }

    /* Station selector */
    [data-testid="stSidebar"] [data-baseweb="select"] > div {
        background-color: #0B1424;
        border-color: #334155;
        border-radius: 11px;
    }

    [data-testid="stSidebar"] [data-baseweb="tag"] {
        background-color: #15374B !important;
        border: 1px solid #28566A !important;
        border-radius: 8px !important;
    }

    [data-testid="stSidebar"] [data-baseweb="tag"] span {
        color: #A5F3FC !important;
    }

    [data-testid="stSidebar"] [data-baseweb="tag"] svg {
        color: #A5F3FC !important;
        fill: #A5F3FC !important;
    }

    /* Date input */
    [data-testid="stSidebar"] [data-baseweb="input"] > div {
        background-color: #0B1424;
        border: 1px solid #334155;
        border-radius: 11px;
    }

    [data-testid="stSidebar"] input {
        color: #F1F5F9;
    }

    [data-testid="stSidebar"] [data-baseweb="select"]:focus-within,
    [data-testid="stSidebar"] [data-baseweb="input"]:focus-within {
        border-color: #22D3EE;
        box-shadow: 0 0 0 1px #22D3EE;
    }

    /* Sidebar information cards */
    .sidebar-info-grid {
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 9px;
        margin-top: 15px;
    }

    .sidebar-info-card {
        min-width: 0;
        padding: 12px;
        border: 1px solid #203B53;
        border-radius: 13px;
        background: #153044;
    }

    .sidebar-info-icon {
        margin-bottom: 7px;
        color: #67E8F9;
        font-size: 22px;
    }

    .sidebar-info-label {
        margin-bottom: 4px;
        color: #94A3B8;
        font-size: 12px;
    }

    .sidebar-info-value {
        color: #F1F5F9;
        font-size: 14px;
        font-weight: 650;
        overflow-wrap: anywhere;
    }

    .sidebar-period-note {
        display: flex;
        flex-direction: column;
        gap: 5px;
        margin-top: 17px;
        padding-top: 14px;
        border-top: 1px solid #334155;
    }

    .sidebar-period-note span {
        margin-top: 5px;
        color: #94A3B8;
        font-size: 11px;
    }

    .sidebar-period-note strong {
        color: #CBD5E1;
        font-size: 12px;
        font-weight: 500;
        overflow-wrap: anywhere;
    }

    /* ===== MAIN DASHBOARD ===== */
    .hero {
        background: linear-gradient(120deg, #14243B, #103D4A);
        padding: 30px 32px;
        border: 1px solid #28566A;
        border-radius: 18px;
        margin-bottom: 22px;
    }

    .hero-tag, .section-label {
        color: #67E8F9;
        font-size: 11px;
        font-weight: 700;
        letter-spacing: 1.5px;
        text-transform: uppercase;
    }

    .hero h1 {
        color: #F8FAFC;
        font-size: 34px;
        font-weight: 800;
        margin: 10px 0;
    }

    .hero p {
        color: #C1D3E5;
        font-size: 14px;
        line-height: 1.7;
        margin-bottom: 0;
    }

    .section-description {
        color: #94A3B8;
        font-size: 13px;
        margin-bottom: 12px;
    }

    [data-testid="stMetric"] {
        background: linear-gradient(145deg, #152238, #111B2E);
        border: 1px solid #263852;
        padding: 18px;
        border-radius: 14px;
    }

    [data-testid="stMetricLabel"] {
        color: #A9BBD0;
    }

    [data-testid="stMetricValue"] {
        color: #F1F5F9;
        font-weight: 700;
    }

    [data-testid="stPlotlyChart"] {
        background-color: #111B2E;
        border: 1px solid #263852;
        border-radius: 14px;
        padding: 7px;
    }

    div[data-testid="stExpander"] {
        background-color: #111B2E;
        border: 1px solid #263852;
        border-radius: 12px;
    }

    .insight-card {
        background: #111B2E;
        border: 1px solid #263852;
        border-radius: 14px;
        padding: 17px 18px;
        min-height: 175px;
        height: 100%;
        box-sizing: border-box;
    }

    .insight-kicker {
        color: #67E8F9;
        font-size: 11px;
        font-weight: 700;
        letter-spacing: 1px;
        text-transform: uppercase;
    }

    .insight-title {
        color: #F8FAFC;
        font-size: 17px;
        font-weight: 700;
        margin: 8px 0;
    }

    .insight-body {
        color: #B8C7D9;
        font-size: 13px;
        line-height: 1.65;
    }

    .footer {
        color: #8193A9;
        font-size: 12px;
        line-height: 1.8;
        padding: 10px 0 20px;
    }

    hr {
        border-color: #263852;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# =========================================================
# 3. LOAD DATA
# =========================================================
DATA_PATH = Path(__file__).parent / "main_data.csv"


@st.cache_data
def load_data(path):
    data = pd.read_csv(path)

    if "datetime" not in data.columns:
        raise ValueError("Kolom 'datetime' tidak ditemukan.")

    data["datetime"] = pd.to_datetime(
        data["datetime"], errors="coerce"
    )

    data = data.dropna(subset=["datetime"]).copy()

    if "station" not in data.columns:
        raise ValueError("Kolom 'station' tidak ditemukan.")

    data["station"] = data["station"].astype(str)

    return data


# Header ditampilkan sebelum pemuatan dataset
st.markdown(
    """
    <div class="hero">
        <div class="hero-tag">Environmental Data Analytics</div>
        <h1>🌫️ Air Quality Explorer</h1>
        <p>
            Memahami pola polusi udara di Beijing melalui data dari
            stasiun pemantauan selama Maret 2013–Februari 2017.
            Jelajahi perubahan konsentrasi, bandingkan stasiun,
            dan temukan hubungan antarpolutan.
        </p>
    </div>
    """,
    unsafe_allow_html=True,
)

try:
    df = load_data(str(DATA_PATH))
except FileNotFoundError:
    st.error(
        "File main_data.csv tidak ditemukan. "
        "Letakkan file tersebut di folder yang sama dengan dashboard.py."
    )
    st.stop()
except Exception as error:
    st.error(f"Dataset gagal dibaca: {error}")
    st.stop()


required_columns = [
    "datetime", "station", "PM2.5", "PM10",
    "SO2", "NO2", "CO", "O3", "TEMP", "DEWP", "WSPM"
]

missing_columns = [
    column for column in required_columns
    if column not in df.columns
]

if missing_columns:
    st.error(
        "Kolom dataset berikut belum tersedia: "
        + ", ".join(missing_columns)
    )
    st.stop()


# Pastikan kolom polutan bertipe numerik
pollutants = [
    "PM2.5", "PM10", "SO2", "NO2", "CO",
    "O3", "TEMP", "DEWP", "WSPM"
]

for column in pollutants:
    df[column] = pd.to_numeric(df[column], errors="coerce")


# Tambahkan musim jika belum tersedia
if "season" not in df.columns:
    month_to_season = {
        12: "Winter", 1: "Winter", 2: "Winter",
        3: "Spring", 4: "Spring", 5: "Spring",
        6: "Summer", 7: "Summer", 8: "Summer",
        9: "Autumn", 10: "Autumn", 11: "Autumn"
    }

    df["season"] = df["datetime"].dt.month.map(month_to_season)



# =========================================================
# 4. SIDEBAR FILTERS — REDESIGNED LAYOUT
# =========================================================

# Header sidebar
st.sidebar.markdown(
    """
    <div class="sidebar-brand">
        <div class="sidebar-brand-icon">≋</div>
        <div class="sidebar-brand-text">
            <div class="sidebar-brand-title">Air Quality Explorer</div>
            <div class="sidebar-brand-subtitle">
                BEIJING · ENVIRONMENTAL DATA ANALYTICS
            </div>
        </div>
        <div class="sidebar-year">2013–2017</div>
    </div>
    <div class="sidebar-divider"></div>
    <div class="sidebar-heading">Pengaturan analisis</div>
    <div class="sidebar-description">
        Pilih stasiun dan periode untuk mengeksplorasi kualitas udara.
    </div>
    """,
    unsafe_allow_html=True,
)

# Pilihan stasiun
stations = sorted(df["station"].dropna().unique().tolist())

st.sidebar.markdown(
    '<div class="sidebar-field-label">Stasiun pemantauan</div>',
    unsafe_allow_html=True,
)

selected_stations = st.sidebar.multiselect(
    "Pilih stasiun",
    options=stations,
    default=stations,
    label_visibility="collapsed",
    key="station_filter",
)

# Rentang tanggal
date_min = df["datetime"].min().date()
date_max = df["datetime"].max().date()

st.sidebar.markdown(
    '<div class="sidebar-field-label">Rentang tanggal</div>',
    unsafe_allow_html=True,
)

date_range = st.sidebar.date_input(
    "Pilih periode",
    value=(date_min, date_max),
    min_value=date_min,
    max_value=date_max,
    label_visibility="collapsed",
    key="date_filter",
)

# Tentukan periode yang dipilih untuk kartu informasi
if isinstance(date_range, (tuple, list)) and len(date_range) == 2:
    period_start, period_end = date_range
    period_text = (
        f"{period_start:%d %b %Y} – {period_end:%d %b %Y}"
    )
else:
    period_text = "Pilih tanggal mulai dan akhir"

# Kartu informasi bagian bawah
st.sidebar.markdown(
    f"""
    <div class="sidebar-info-grid">
        <div class="sidebar-info-card">
            <div class="sidebar-info-icon">▤</div>
            <div class="sidebar-info-label">Dataset</div>
            <div class="sidebar-info-value">Multi-Site</div>
        </div>
        <div class="sidebar-info-card">
            <div class="sidebar-info-icon">◎</div>
            <div class="sidebar-info-label">Cakupan</div>
            <div class="sidebar-info-value">{len(stations)} stasiun</div>
        </div>
    </div>
    <div class="sidebar-period-note">
        <span>Sumber data</span>
        <strong>Beijing Multi-Site Air Quality</strong>
        <span>Periode dataset</span>
        <strong>{date_min:%d %b %Y} – {date_max:%d %b %Y}</strong>
    </div>
    """,
    unsafe_allow_html=True,
)

# Validasi filter
if not selected_stations:
    st.warning("Pilih minimal satu stasiun pada sidebar.")
    st.stop()

if not isinstance(date_range, (tuple, list)) or len(date_range) != 2:
    st.info("Pilih tanggal mulai dan tanggal akhir.")
    st.stop()

start_date, end_date = date_range

if start_date > end_date:
    st.warning("Tanggal mulai tidak boleh melewati tanggal akhir.")
    st.stop()

filtered = df[
    df["station"].isin(selected_stations)
    & df["datetime"].dt.date.between(start_date, end_date)
].copy()

if filtered.empty:
    st.warning("Tidak ada data untuk kombinasi filter yang dipilih.")
    st.stop()

# =========================================================
# 5. SHARED CHART STYLING
# =========================================================
plot_layout = dict(
    template="plotly_dark",
    paper_bgcolor="#111B2E",
    plot_bgcolor="#111B2E",
    font=dict(family="Inter, sans-serif", color="#DCE7F5"),
    title_font=dict(size=16, color="#F1F5F9"),
    margin=dict(l=20, r=20, t=55, b=35),
    legend=dict(
        bgcolor="rgba(0,0,0,0)",
        font=dict(color="#DCE7F5"),
    ),
    hoverlabel=dict(
        bgcolor="#1E293B",
        font=dict(color="#F8FAFC"),
    ),
)

pollutant_colors = {
    "PM2.5": "#22D3EE",
    "PM10": "#FBBF24",
}


# =========================================================
# 6. OVERVIEW
# =========================================================
st.markdown(
    '<div class="section-label">Overview</div>',
    unsafe_allow_html=True,
)

st.subheader("Ringkasan Pengamatan")

st.caption(
    f"Periode terpilih: {start_date:%d %b %Y} – "
    f"{end_date:%d %b %Y} · "
    f"{filtered['station'].nunique()} stasiun"
)

st.markdown(
    """
    <style>
    /* CSS dashboard yang sudah ada */
    .hero {
        border-radius: 18px;
    }

    /* TEMPEL CSS SIDEBAR BARU MULAI DI SINI */

    [data-testid="stSidebar"] {
        background: #111C30;
        border-right: 1px solid #263852;
    }

    [data-testid="stSidebar"] h2 {
        color: #F1F5F9;
        font-weight: 750;
        letter-spacing: -0.4px;
    }

    [data-testid="stSidebar"] hr {
        border-color: #334155;
        margin: 1.4rem 0;
    }

    [data-testid="stSidebar"] label,
    [data-testid="stSidebar"] p {
        color: #CBD5E1;
    }

    [data-testid="stSidebar"] [data-baseweb="select"] > div {
        background: #0B1424;
        border-color: #334155;
        border-radius: 12px;
    }

    [data-testid="stSidebar"] [data-baseweb="tag"] {
        background-color: #15374B !important;
        border: 1px solid #22647A !important;
        border-radius: 8px !important;
    }

    [data-testid="stSidebar"] [data-baseweb="tag"] span {
        color: #A5F3FC !important;
    }

    [data-testid="stSidebar"] [data-baseweb="tag"] svg {
        fill: #A5F3FC !important;
        color: #A5F3FC !important;
    }

    [data-testid="stSidebar"] [data-baseweb="tag"] span {
        color: #A5F3FC;
    }

    [data-testid="stSidebar"] input {
        color: #F1F5F9;
    }

    [data-testid="stSidebar"] [data-baseweb="select"]:focus-within,
    [data-testid="stSidebar"] [data-baseweb="input"]:focus-within {
        border-color: #22D3EE;
        box-shadow: 0 0 0 1px #22D3EE;
    }

    /* CSS SIDEBAR BARU SELESAI DI SINI */

    </style>
    """,
    unsafe_allow_html=True,
)

k1, k2, k3, k4 = st.columns(4)

k1.metric("Total observasi", f"{len(filtered):,}")
k2.metric(
    "Rata-rata PM2.5",
    f"{filtered['PM2.5'].mean():.1f} µg/m³"
)
k3.metric(
    "Rata-rata PM10",
    f"{filtered['PM10'].mean():.1f} µg/m³"
)
k4.metric("Stasiun terpilih", f"{filtered['station'].nunique():,}")


# =========================================================
# 7. KEY FINDINGS
# =========================================================
st.markdown("---")
st.markdown('<div class="section-label">At a glance</div>', unsafe_allow_html=True)
st.subheader("Key Findings")

station_means = filtered.groupby("station")[["PM2.5", "PM10"]].mean()
monthly_means = (
    filtered.assign(month_start=filtered["datetime"].dt.to_period("M").dt.to_timestamp())
    .groupby("month_start")[["PM2.5", "PM10"]]
    .mean()
)

ins1, ins2, ins3 = st.columns(3, gap="medium")

with ins1:
    station_pm25 = station_means["PM2.5"].dropna()
    if not station_pm25.empty:
        high_station = station_pm25.idxmax()
        low_station = station_pm25.idxmin()
        st.markdown(
            f"""<div class="insight-card">
                <div class="insight-kicker">Station signal</div>
                <div class="insight-title">{high_station}</div>
                <div class="insight-body">Rata-rata PM2.5 tertinggi: <b>{station_pm25.max():.1f} µg/m³</b>.</div>
                <div class="insight-body">Terendah: {low_station} ({station_pm25.min():.1f} µg/m³).</div>
            </div>""",
            unsafe_allow_html=True,
        )
    else:
        st.info("Data PM2.5 tidak tersedia pada filter ini.")

with ins2:
    monthly_pm25 = monthly_means["PM2.5"].dropna()
    if not monthly_pm25.empty:
        peak_month = monthly_pm25.idxmax()
        trough_month = monthly_pm25.idxmin()
        st.markdown(
            f"""<div class="insight-card">
                <div class="insight-kicker">Temporal signal</div>
                <div class="insight-title">{peak_month:%B %Y}</div>
                <div class="insight-body">Puncak rata-rata PM2.5: <b>{monthly_pm25.max():.1f} µg/m³</b>.</div>
                <div class="insight-body">Terendah: {trough_month:%B %Y} ({monthly_pm25.min():.1f} µg/m³).</div>
            </div>""",
            unsafe_allow_html=True,
        )
    else:
        st.info("Data bulanan tidak tersedia pada filter ini.")

with ins3:
    pairs = filtered[["PM2.5", "PM10"]].dropna()
    if len(pairs) >= 2 and pairs["PM2.5"].nunique() > 1 and pairs["PM10"].nunique() > 1:
        corr_value = pairs["PM2.5"].corr(pairs["PM10"])
        st.markdown(
            f"""<div class="insight-card">
                <div class="insight-kicker">Pollutant relationship</div>
                <div class="insight-title">PM2.5 ↔ PM10</div>
                <div class="insight-body">Korelasi Pearson: <b>{corr_value:.2f}</b>.</div>
                <div class="insight-body">Korelasi menunjukkan hubungan linear, bukan sebab-akibat.</div>
            </div>""",
            unsafe_allow_html=True,
        )
    else:
        st.info("Pasangan data PM2.5 dan PM10 belum cukup untuk menghitung korelasi.")


# =========================================================
# 8. MONTHLY TRENDS
# =========================================================
st.markdown("---")
st.markdown('<div class="section-label">01 / Temporal analysis</div>',
            unsafe_allow_html=True)
st.subheader("Tren Konsentrasi Partikulat")

st.markdown(
    '<div class="section-description">'
    'Rata-rata bulanan menunjukkan perubahan konsentrasi PM2.5 dan PM10.'
    '</div>',
    unsafe_allow_html=True,
)

monthly_long = (
    monthly_means.reset_index()
    .melt(
        id_vars="month_start",
        var_name="Polutan",
        value_name="Konsentrasi (µg/m³)",
    )
)

fig_trend = px.line(
    monthly_long,
    x="month_start",
    y="Konsentrasi (µg/m³)",
    color="Polutan",
    markers=True,
    color_discrete_map=pollutant_colors,
    labels={"month_start": "Bulan"},
)

fig_trend.update_layout(**plot_layout)
fig_trend.update_traces(line=dict(width=3), marker=dict(size=5))
fig_trend.update_xaxes(showgrid=False)
fig_trend.update_yaxes(gridcolor="#263852", zeroline=False)

st.plotly_chart(fig_trend, use_container_width=True)


# =========================================================
# 9. SEASONAL COMPARISON
# =========================================================
st.markdown("#### Perbandingan berdasarkan musim")

season_order = ["Spring", "Summer", "Autumn", "Winter"]

seasonal = (
    filtered.groupby("season", as_index=False)[["PM2.5", "PM10"]]
    .mean()
    .dropna(how="all")
)

if not seasonal.empty:
    seasonal["season"] = pd.Categorical(
        seasonal["season"],
        categories=season_order,
        ordered=True,
    )
    seasonal = seasonal.sort_values("season")

    season_long = seasonal.melt(
        id_vars="season",
        var_name="Polutan",
        value_name="Konsentrasi (µg/m³)",
    )

    left, right = st.columns([1.25, 1])

    with left:
        fig_season = px.bar(
            season_long,
            x="season",
            y="Konsentrasi (µg/m³)",
            color="Polutan",
            barmode="group",
            color_discrete_map=pollutant_colors,
            labels={"season": "Musim"},
        )

        fig_season.update_layout(**plot_layout)
        fig_season.update_xaxes(showgrid=False)
        fig_season.update_yaxes(gridcolor="#263852")

        st.plotly_chart(fig_season, use_container_width=True)

    with right:
        st.dataframe(
            seasonal.rename(
                columns={
                    "season": "Musim",
                    "PM2.5": "Rata-rata PM2.5",
                    "PM10": "Rata-rata PM10",
                }
            ),
            use_container_width=True,
            hide_index=True,
        )

        st.caption(
            "Perbedaan musiman bersifat deskriptif dan tidak menjelaskan penyebabnya."
        )


# =========================================================
# 10. STATION COMPARISON
# =========================================================
st.markdown("---")
st.markdown('<div class="section-label">02 / Station comparison</div>',
            unsafe_allow_html=True)
st.subheader("Perbandingan Konsentrasi Antarstasiun")

station_long = (
    station_means.reset_index()
    .melt(
        id_vars="station",
        var_name="Polutan",
        value_name="Konsentrasi (µg/m³)",
    )
    .dropna(subset=["Konsentrasi (µg/m³)"])
)

fig_station = px.bar(
    station_long,
    x="Konsentrasi (µg/m³)",
    y="station",
    color="Polutan",
    barmode="group",
    orientation="h",
    color_discrete_map=pollutant_colors,
    labels={"station": "Stasiun"},
)

fig_station.update_layout(**plot_layout)
fig_station.update_layout(yaxis=dict(autorange="reversed"))
fig_station.update_xaxes(gridcolor="#263852")
fig_station.update_yaxes(showgrid=False)

st.plotly_chart(fig_station, use_container_width=True)

with st.expander("Lihat ranking stasiun"):
    ranking = (
        station_means.sort_values("PM2.5", ascending=False)
        .reset_index()
    )
    ranking.index = ranking.index + 1
    ranking.index.name = "Peringkat"

    st.dataframe(
        ranking.rename(
            columns={
                "station": "Stasiun",
                "PM2.5": "Rata-rata PM2.5 (µg/m³)",
                "PM10": "Rata-rata PM10 (µg/m³)",
            }
        ),
        use_container_width=True,
    )


# =========================================================
# 11. POLLUTANT RELATIONSHIPS
# =========================================================
st.markdown("---")
st.markdown(
    '<div class="section-label">03 / Pollutant relationships</div>',
    unsafe_allow_html=True,
)
st.subheader("Hubungan Antarvariabel")

st.caption(
    "Korelasi menunjukkan arah dan kekuatan hubungan linear, "
    "bukan bukti sebab-akibat."
)

corr_cols = [
    "PM2.5", "PM10", "SO2", "NO2", "CO",
    "O3", "TEMP", "DEWP", "WSPM"
]

left_corr, right_corr = st.columns(2, gap="large")

with left_corr:
    st.markdown("#### Heatmap korelasi Pearson")

    corr = filtered[corr_cols].corr(numeric_only=True)

    fig_corr = px.imshow(
        corr,
        text_auto=".2f",
        color_continuous_scale="RdBu_r",
        zmin=-1,
        zmax=1,
        aspect="auto",
        labels={"color": "Korelasi"},
    )

    fig_corr.update_layout(**plot_layout)
    fig_corr.update_layout(
        coloraxis_colorbar=dict(title="Pearson r")
    )

    st.plotly_chart(fig_corr, use_container_width=True)


with right_corr:
    st.markdown("#### Eksplorasi hubungan antarvariabel")

    x_options = [
        "PM2.5", "PM10", "SO2", "NO2", "CO",
        "O3", "TEMP", "DEWP", "WSPM"
    ]

    x_variable = st.selectbox(
        "Pilih variabel pada sumbu X",
        options=x_options,
        index=0,
        key="scatter_x_variable",
    )

    y_options = [
        column for column in x_options
        if column != x_variable
    ]

    y_variable = st.selectbox(
        "Pilih variabel pada sumbu Y",
        options=y_options,
        index=0,
        key="scatter_y_variable",
    )

    scatter_data = filtered[
        [x_variable, y_variable]
    ].dropna()

    if len(scatter_data) >= 2:
        total_pairs = len(scatter_data)

        display_scatter = (
            scatter_data.sample(n=5000, random_state=42)
            if total_pairs > 5000
            else scatter_data
        )

        scatter_corr = scatter_data[x_variable].corr(
            scatter_data[y_variable]
        )

        fig_scatter = px.scatter(
            display_scatter,
            x=x_variable,
            y=y_variable,
            opacity=0.35,
            render_mode="svg",
            color_discrete_sequence=["#22D3EE"],
            labels={
                x_variable: x_variable,
                y_variable: y_variable,
            },
        )

        fig_scatter.update_layout(**plot_layout)
        fig_scatter.update_xaxes(gridcolor="#263852")
        fig_scatter.update_yaxes(gridcolor="#263852")

        st.plotly_chart(
            fig_scatter,
            use_container_width=True,
        )

        st.caption(
            f"Korelasi Pearson {x_variable} dan {y_variable}: "
            f"{scatter_corr:.2f}. "
            f"Total pasangan data: {total_pairs:,}; "
            f"titik yang ditampilkan: {len(display_scatter):,}. "
            "Korelasi tidak membuktikan sebab-akibat."
        )

    else:
        st.info(
            "Data berpasangan tidak cukup untuk menampilkan scatter plot."
        )

# =========================================================
# 12. RELATIVE PM2.5 CATEGORY / BINNING
# =========================================================
st.markdown("---")
st.markdown(
    '<div class="section-label">04 / Relative grouping</div>',
    unsafe_allow_html=True,
)
st.subheader("Distribusi Kategori Relatif PM2.5")

st.caption(
    "Kategori relatif dibentuk dari sepertiga dan dua pertiga kuantil PM2.5 "
    "pada dataset penuh agar perbandingan antarfilter tetap konsisten. "
    "Kategori ini bukan ambang resmi kualitas udara."
)

category_col = "PM2.5_relative_category"
valid_pm25 = df["PM2.5"].dropna()

if not valid_pm25.empty and valid_pm25.nunique() >= 3:
    # Ranking persentil menghindari error jika batas kuantil memiliki nilai sama.
    pm25_percentile = df["PM2.5"].rank(method="average", pct=True)
    df[category_col] = pd.cut(
        pm25_percentile,
        bins=[-float("inf"), 1 / 3, 2 / 3, float("inf")],
        labels=["Relatif rendah", "Relatif sedang", "Relatif tinggi"],
        include_lowest=True,
    )
    filtered[category_col] = df.loc[filtered.index, category_col]
else:
    filtered[category_col] = pd.NA


category_labels = {
    "rendah": "Relatif rendah",
    "low": "Relatif rendah",
    "relatif rendah": "Relatif rendah",
    "sedang": "Relatif sedang",
    "medium": "Relatif sedang",
    "moderate": "Relatif sedang",
    "relatif sedang": "Relatif sedang",
    "tinggi": "Relatif tinggi",
    "high": "Relatif tinggi",
    "relatif tinggi": "Relatif tinggi",
}

cat_source = (
    filtered[category_col]
    .astype("object")
    .fillna("Tidak diketahui")
    .astype(str)
    .map(
        lambda value: category_labels.get(
            value.strip().lower(), value
        )
    )
)

category_order = [
    "Relatif rendah",
    "Relatif sedang",
    "Relatif tinggi",
    "Tidak diketahui",
]

cat = (
    cat_source.value_counts()
    .rename_axis("Kategori")
    .reset_index(name="Jumlah observasi")
)

extra_categories = [
    value for value in cat["Kategori"].unique()
    if value not in category_order
]

full_order = category_order + extra_categories

cat["Kategori"] = pd.Categorical(
    cat["Kategori"],
    categories=full_order,
    ordered=True,
)

cat = cat.sort_values("Kategori")

fig_cat = px.bar(
    cat,
    x="Kategori",
    y="Jumlah observasi",
    color="Kategori",
    category_orders={"Kategori": full_order},
    color_discrete_map={
        "Relatif rendah": "#34D399",
        "Relatif sedang": "#FBBF24",
        "Relatif tinggi": "#FB7185",
        "Tidak diketahui": "#94A3B8",
    },
    text="Jumlah observasi",
)

fig_cat.update_traces(
    texttemplate="%{y:,.0f}",
    textposition="outside",
    cliponaxis=False,
)

fig_cat.update_layout(**plot_layout)
fig_cat.update_layout(showlegend=False)
fig_cat.update_xaxes(showgrid=False)
fig_cat.update_yaxes(gridcolor="#263852", rangemode="tozero")

st.plotly_chart(fig_cat, use_container_width=True)

st.markdown("#### Proporsi kategori pada data terpilih")

proportions = (
    cat_source.value_counts(normalize=True)
    .mul(100)
    .rename_axis("Kategori")
    .reset_index(name="Persentase (%)")
)

proportions["Persentase (%)"] = proportions["Persentase (%)"].round(2)

st.dataframe(
    proportions,
    use_container_width=True,
    hide_index=True,
)


# =========================================================
# 13. DATA EXPLORER AND DOWNLOAD
# =========================================================
st.markdown("---")
st.markdown(
    '<div class="section-label">05 / Data explorer</div>',
    unsafe_allow_html=True,
)
st.subheader("Jelajahi dan Unduh Data")

with st.expander("Buka tabel data"):
    display_cols = [
        column for column in [
            "datetime", "station", "PM2.5", "PM10", "SO2",
            "NO2", "CO", "O3", "TEMP", "DEWP", "WSPM",
            "season", category_col
        ]
        if column in filtered.columns
    ]

    st.dataframe(
        filtered[display_cols].head(1000),
        use_container_width=True,
        hide_index=True,
    )

    st.caption(
        f"Menampilkan maksimal 1.000 baris dari "
        f"{len(filtered):,} observasi hasil filter."
    )

    st.download_button(
        "⬇️ Unduh data sesuai filter (CSV)",
        data=filtered.to_csv(index=False).encode("utf-8"),
        file_name="air_quality_filtered.csv",
        mime="text/csv",
        use_container_width=True,
    )


# =========================================================
# 14. FOOTER
# =========================================================
st.markdown("---")

st.markdown(
    """
    <div class="footer">
        <b>Air Quality Explorer</b> · Beijing Multi-Site Air Quality Dataset
        <br>
        Nilai numerik yang hilang ditangani sesuai proses pembersihan
        pada notebook.
        <br>
        Analisis ini bersifat eksploratif. Korelasi tidak membuktikan
        sebab-akibat, dan kategori PM2.5 bukan ambang resmi kualitas udara.
    </div>
    """,
    unsafe_allow_html=True,
)