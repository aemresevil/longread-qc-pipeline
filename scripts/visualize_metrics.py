import argparse
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def visualize_and_summarize(input_csv, output_prefix):
    # Veriyi okuma
    df = pd.read_csv(input_csv)

    # İstatistikleri hesaplama ve terminale yazdırma
    print("--- Temel Özet İstatistikler ---")
    metrics = ['Read_Length', 'GC_Content_Pct', 'Mean_Quality_Score']
    for m in metrics:
        mean_val = df[m].mean()
        median_val = df[m].median()
        print(f"{m} - Ortalama (Mean): {mean_val:.2f}, Ortanca (Median): {median_val:.2f}")

    # Grafikleri çizdirme
    sns.set_theme(style="whitegrid")
    fig, axes = plt.subplots(1, 3, figsize=(18, 5))

    # 1. GC Content Dağılımı
    sns.histplot(df['GC_Content_Pct'], kde=True, ax=axes[0], color='skyblue')
    axes[0].set_title('GC Content Dağılımı')
    axes[0].set_xlabel('GC İçeriği (%)')

    # 2. Read Length Dağılımı
    sns.histplot(df['Read_Length'], kde=True, ax=axes[1], color='lightgreen')
    axes[1].set_title('Okuma Uzunluğu (Read Length) Dağılımı')
    axes[1].set_xlabel('Uzunluk (bp)')

    # 3. Mean Quality Score Dağılımı
    sns.histplot(df['Mean_Quality_Score'], kde=True, ax=axes[2], color='salmon')
    axes[2].set_title('Ortalama Kalite Skoru Dağılımı')
    axes[2].set_xlabel('Phred Skoru')

    plt.tight_layout()
    output_file = f"{output_prefix}_distributions.png"
    plt.savefig(output_file, dpi=300)
    print(f"\nGrafikler başarıyla oluşturuldu ve '{output_file}' olarak kaydedildi.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="QC metriklerini görselleştirir ve istatistikleri yazdırır.")
    parser.add_argument("-i", "--input", required=True, help="Girdi: analyze_reads.py çıktısı olan CSV dosyası")
    parser.add_argument("-p", "--prefix", required=True, default="qc_plot", help="Çıktı: Kaydedilecek grafik dosyasının öneki")
    
    args = parser.parse_args()
    visualize_and_summarize(args.input, args.prefix)
    