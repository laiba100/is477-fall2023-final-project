rule prepare:
    output:
        "data/wine/wine.data"
    shell:
        "python scripts/prepare_data.py"

rule profile:
    input:
        "data/wine/wine.data"
    output:
        "profiling/report.html" 
    shell:
        "python scripts/profile.py"

rule analyze:
    input:
        "data/wine/wine.data"
    output:
        "results/wine_data_summary_statistics.csv",
        "results/classification_report.txt",
        "results/wine_data_analysis_histogram.png"
    shell:
        "python scripts/analysis.py"

rule reproduce:
    input:
        "profiling/report.html",
        "results/classification_report.txt",
        "results/wine_data_summary_statistics.csv",

