# --- Yapılandırma ---
# Girdi dosyamızı ve çıktılarımızın nereye kaydedileceğini tanımlıyoruz
INPUT_FASTQ = "data/barcode77.fastq"
OUT_DIR = "results"

# Pipeline'ın nihai hedefi (bu dosyalar oluştuğunda işlem biter)
rule all:
    input:
        f"{OUT_DIR}/nanoplot_report/NanoPlot-report.html",
        f"{OUT_DIR}/custom_qc_metrics.csv",
        f"{OUT_DIR}/custom_qc_plot_distributions.png"

# --- Adım 1: Hazır QC Aracı (NanoPlot) ---
# Uzun okuma verileri için endüstri standardı olan NanoPlot'u çalıştırır
rule run_nanoplot:
    input:
        INPUT_FASTQ
    output:
        f"{OUT_DIR}/nanoplot_report/NanoPlot-report.html"
    log:
        "logs/nanoplot.log"
    shell:
        """
        NanoPlot --fastq {input} -o {OUT_DIR}/nanoplot_report > {log} 2>&1
        """

# --- Adım 2: Özel Analiz Scriptimiz ---
# Yazdığımız Python kodunu kullanarak her bir okumanın metriklerini hesaplar
rule analyze_reads:
    input:
        INPUT_FASTQ
    output:
        f"{OUT_DIR}/custom_qc_metrics.csv"
    log:
        "logs/analyze_reads.log"
    shell:
        """
        python scripts/analyze_reads.py -i {input} -o {output} > {log} 2>&1
        """

# --- Adım 3: Görselleştirme Scriptimiz ---
# İkinci adımda ürettiğimiz CSV dosyasını kullanarak grafikleri çizer
rule visualize_metrics:
    input:
        f"{OUT_DIR}/custom_qc_metrics.csv"
    output:
        f"{OUT_DIR}/custom_qc_plot_distributions.png"
    params:
        prefix=f"{OUT_DIR}/custom_qc_plot"
    log:
        "logs/visualize_metrics.log"
    shell:
        """
        python scripts/visualize_metrics.py -i {input} -p {params.prefix} > {log} 2>&1
        """