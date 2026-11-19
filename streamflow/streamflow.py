# -*- coding: utf-8 -*-

from pathlib import Path
import csv

import matplotlib.pyplot as plt
import numpy as np


def load_streamflow(filename):
    """Load dates and one flow column per gauge from a CSV file."""
    csv_path = Path(filename)
    if not csv_path.is_absolute():
        csv_path = Path(__file__).resolve().parent / csv_path

    data_provo = np.genfromtxt(
        csv_path,
        delimiter=",",
        dtype=str,
        skip_header=1,
    )

    dates = data_provo[:, 0]
    flows = data_provo[:, 1:].astype(float)
    return dates, flows


def summarize(dates, flows, sites):
    """Print and save summary statistics for each streamflow gauge."""
    rows = []

    for column, site in enumerate(sites):
        gauge_flows = flows[:, column]
        max_index = int(np.argmax(gauge_flows))
        rows.append({
            "Gauge": site,
            "Max (cfs)": float(np.max(gauge_flows)),
            "Date of max": dates[max_index],
            "Min (cfs)": float(np.min(gauge_flows)),
            "Avg (cfs)": float(np.mean(gauge_flows)),
        })

    print(f"{'Gauge':<12}{'Max (cfs)':<12}{'Date of max':<22}"
          f"{'Min (cfs)':<12}{'Avg (cfs)':<12}")
    for row in rows:
        print(
            f"{row['Gauge']:<12}"
            f"{row['Max (cfs)']:>10.1f}"
            f"{row['Date of max']:>20}"
            f"{row['Min (cfs)']:>12.1f}"
            f"{row['Avg (cfs)']:>12.1f}"
        )

    output_path = Path(__file__).resolve().parent / "streamflow_summary.csv"
    with output_path.open("w", newline="", encoding="utf-8") as summary_file:
        writer = csv.DictWriter(
            summary_file,
            fieldnames=[
                "Gauge",
                "Max (cfs)",
                "Date of max",
                "Min (cfs)",
                "Avg (cfs)",
            ],
        )
        writer.writeheader()
        writer.writerows(rows)


def plot_streamflow(dates, flows, sites):
    """Plot each streamflow gauge against the date."""
    colors = ["purple", "blue", "green", "orange", "red"]

    plt.figure(figsize=(12, 6))
    for column, (site, color) in enumerate(zip(sites, colors)):
        plt.plot(
            dates,
            flows[:, column],
            label=f"Site {site}",
            color=color,
        )

    plt.title("Provo River Streamflow Rates (2021)")
    plt.xlabel("Date")
    plt.ylabel("Flowrate (cfs)")
    plt.xticks(dates[::200], rotation=45)
    plt.legend()
    plt.grid(True)
    output_path = Path(__file__).resolve().parent / "provo_streamflow.png"
    plt.savefig(output_path, dpi=150, bbox_inches="tight")
    plt.show()


# Main program
sites = ["10163000", "10155200", "10155500", "10154200", "10155000"]
dates, flows = load_streamflow(
    "June-2021-Provo-River-Streamflow-Rates.csv"
)
summarize(dates, flows, sites)
plot_streamflow(dates, flows, sites)