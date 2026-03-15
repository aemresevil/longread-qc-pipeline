import argparse
import csv
from Bio import SeqIO

def calculate_gc(seq):
    """DNA dizisindeki GC yüzdesini hesaplar."""
    g_count = seq.count('G')
    c_count = seq.count('C')
    total_len = len(seq)
    if total_len == 0:
        return 0.0
    return ((g_count + c_count) / total_len) * 100

def analyze_fastq(input_fastq, output_csv):
    """FASTQ dosyasını okur ve metrikleri CSV'ye yazar."""
    with open(output_csv, mode='w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(['Read_ID', 'Read_Length', 'GC_Content_Pct', 'Mean_Quality_Score'])

        for record in SeqIO.parse(input_fastq, "fastq"):
            read_id = record.id
            seq = str(record.seq).upper()
            
            read_length = len(seq)
            gc_content = calculate_gc(seq)
            
            quals = record.letter_annotations.get("phred_quality", [])
            mean_qual = sum(quals) / len(quals) if len(quals) > 0 else 0
            
            writer.writerow([read_id, read_length, round(gc_content, 2), round(mean_qual, 2)])
            
    print(f"Analiz tamamlandı! Sonuçlar '{output_csv}' dosyasına kaydedildi.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Uzun okuma FASTQ verileri için QC metriklerini hesaplar.")
    parser.add_argument("-i", "--input", required=True, help="Girdi: Ham FASTQ dosyası")
    parser.add_argument("-o", "--output", required=True, help="Çıktı: Sonuçların yazılacağı CSV dosyası")
    
    args = parser.parse_args()
    analyze_fastq(args.input, args.output)