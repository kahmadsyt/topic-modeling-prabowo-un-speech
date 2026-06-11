# Ringkasan Laporan Akhir

## Judul

Analisis Komputasional Topik Pidato Presiden Prabowo pada Forum Nasional dan Internasional Menggunakan Manual Coding dan BERTopic

## Ringkasan Metode

Penelitian ini menggunakan dua pendekatan analisis topik, yaitu Manual Coding dan BERTopic. Manual Coding dilakukan melalui tahapan Open Coding, Axial Coding, dan Selective Coding. BERTopic digunakan sebagai pendekatan komputasional berbasis embedding dan clustering untuk menemukan pola topik secara otomatis dari data chunk pidato.

Dataset akhir terdiri dari chunk pidato yang telah melalui proses data inventory, text preprocessing, text chunking, manual coding, topic modeling, dan comparative analysis. Chunk yang berstatus EXCLUDED tidak digunakan dalam proses pemodelan BERTopic karena tidak mengandung substansi topik yang relevan.

## Temuan Kunci

- **Jumlah data analisis final**: Manual Coding mencakup 74 chunk, dengan 71 chunk berstatus REVIEWED dan 3 chunk berstatus EXCLUDED. BERTopic dijalankan pada 71 chunk substantif.
- **Tema manual paling dominan**: Tema manual paling dominan adalah 'Pembangunan manusia dan keadilan sosial' dengan 24 chunk.
- **Jumlah topik BERTopic**: BERTopic menghasilkan 15 label topik termasuk outlier. Jumlah topik non-outlier adalah 14, sedangkan jumlah dokumen pada topik outlier -1 adalah 2.
- **Topik BERTopic terbesar**: Topik BERTopic terbesar adalah Topic 0 dengan 13 chunk dan dominan berkaitan dengan tema manual 'Kedaulatan dan kemandirian nasional'.
- **Tema dengan alignment terkuat**: Alignment terkuat muncul pada tema manual 'Keberlanjutan lingkungan dan sumber daya' dengan dominant BERTopic Topic -1 dan theme concentration 0.5.
- **Kesesuaian Manual Coding dan BERTopic**: Metrik clustering menunjukkan NMI=0.334, AMI=0.1263, Homogeneity=0.45, Completeness=0.2656, dan V-measure=0.334. Nilai ini menunjukkan tingkat hubungan antara tema manual dan struktur topik BERTopic, bukan akurasi klasifikasi.

## Ringkasan Manual Coding

Manual Coding menghasilkan distribusi tema sebagai berikut:

                 manual_selective_theme_clean  document_count  unique_speech_count  unique_bertopic_topic_count  avg_bertopic_probability  document_percentage
      Pembangunan manusia dan keadilan sosial              24                    4                           12                    0.6661                33.80
          Kedaulatan dan kemandirian nasional              22                    5                            8                    0.7423                30.99
   Diplomasi, perdamaian, dan keadilan global              12                    3                            6                    0.8664                16.90
    Reformasi tata kelola dan penegakan hukum               6                    4                            5                    0.7384                 8.45
Transformasi ekonomi dan pembangunan nasional               5                    3                            5                    0.8337                 7.04
     Keberlanjutan lingkungan dan sumber daya               2                    2                            2                    0.5499                 2.82

## Ringkasan BERTopic

BERTopic menghasilkan ringkasan topik sebagai berikut:

 bertopic_topic_id            dominant_manual_selective_theme  dominant_theme_count  topic_document_count  topic_purity                                                 Name                                          auto_topic_label                                                                                    top_keywords topic_type
                 0        Kedaulatan dan kemandirian nasional                     8                    13        0.6154                       0_bupati_hadir_menteri_hormati            bupati / hadir / menteri / hormati / wali kota                             bupati, hadir, menteri, hormati, wali kota, wali, saudari, gubernur    Cluster
                 1 Diplomasi, perdamaian, dan keadilan global                     2                     7        0.2857            1_kampus_stability_growth_peace stability      kampus / stability / growth / peace stability / over                           kampus, stability, growth, peace stability, over, always, economy, it    Cluster
                 2        Kedaulatan dan kemandirian nasional                     4                     6        0.6667             2_energi_menghasilkan_kesulitan_hasilkan energi / menghasilkan / kesulitan / hasilkan / tergantung                     energi, menghasilkan, kesulitan, hasilkan, tergantung, tim, kemampuan, luar    Cluster
                 3        Kedaulatan dan kemandirian nasional                     3                     6        0.5000                           3_000_rice_years_000 murid                       000 / rice / years / 000 murid / 83                                      000, rice, years, 000 murid, 83, 83 000, sasaran, villages    Cluster
                 4    Pembangunan manusia dan keadilan sosial                     3                     5        0.6000                         4_kemerdekaan_dia_perang_mau                 kemerdekaan / dia / perang / mau / enggak                      kemerdekaan, dia, perang, mau, enggak, rakyat, perang kemerdekaan, tentara    Cluster
                 5        Kedaulatan dan kemandirian nasional                     3                     5        0.6000                       5_swasembada_amran_harga_tokoh             swasembada / amran / harga / tokoh / kulitnya                                swasembada, amran, harga, tokoh, kulitnya, jadi, petani, anaknya    Cluster
                 6    Pembangunan manusia dan keadilan sosial                     4                     4        1.0000                         6_anak_orang tuamu_tuamu_son                    anak / orang tuamu / tuamu / son / kau                                     anak, orang tuamu, tuamu, son, kau, ya, anak anak, dukungan    Cluster
                 7 Diplomasi, perdamaian, dan keadilan global                     4                     4        1.0000                7_united nations_nations_united_peace           united nations / nations / united / peace / all                              united nations, nations, united, peace, all, together, secure, may    Cluster
                 8    Pembangunan manusia dan keadilan sosial                     3                     4        0.7500                            8_koperasi_meals_day_guru                  koperasi / meals / day / guru / desember                              koperasi, meals, day, guru, desember, ribu, koperasi merah, panels    Cluster
                 9 Diplomasi, perdamaian, dan keadilan global                     2                     3        0.6667                           9_brics_best_danantara_now                  brics / best / danantara / now / biggest                             brics, best, danantara, now, biggest, fully support, fully, finance    Cluster
                10        Kedaulatan dan kemandirian nasional                     1                     3        0.3333                        10_sudah_proyek_mengerti_juta               sudah / proyek / mengerti / juta / sembilan                               sudah, proyek, mengerti, juta, sembilan, sita, singapura, siapkan    Cluster
                11    Pembangunan manusia dan keadilan sosial                     3                     3        1.0000                   11_akal_berjuang_masuk akal_leader     akal / berjuang / masuk akal / leader / negara begini           akal, berjuang, masuk akal, leader, negara begini, bagaimana negara, many them, masuk    Cluster
                12   Keberlanjutan lingkungan dan sumber daya                     1                     3        0.3333                12_persen_sekarang_jadi bangsa_selama         persen / sekarang / jadi bangsa / selama / petani                persen, sekarang, jadi bangsa, selama, petani, million hectares, hectares, mampu    Cluster
                13 Diplomasi, perdamaian, dan keadilan global                     1                     3        0.3333                      13_my_praktik_determined_markup               my / praktik / determined / markup / nature                                       my, praktik, determined, markup, nature, there, one, down    Cluster
                -1   Keberlanjutan lingkungan dan sumber daya                     1                     2        0.5000 -1_melindungi_ancaman_melindungi ancaman_pertumbuhan                                Outlier / tidak terklaster melindungi, ancaman, melindungi ancaman, pertumbuhan, merdeka, who save, berani melihat, tujuan    Outlier

## Metrik Perbandingan Manual Coding dan BERTopic

Metrik berikut digunakan karena BERTopic merupakan pendekatan unsupervised learning, sehingga tidak dievaluasi menggunakan accuracy klasifikasi biasa.

                       metric  value                                                                      interpretation
normalized_mutual_information 0.3340                  Mengukur hubungan informasi antara tema manual dan topik BERTopic.
  adjusted_mutual_information 0.1263                Mengukur hubungan informasi setelah dikoreksi terhadap peluang acak.
                  homogeneity 0.4500            Mengukur apakah setiap topik BERTopic cenderung berisi satu tema manual.
                 completeness 0.2656 Mengukur apakah dokumen dari tema manual yang sama cenderung masuk topik yang sama.
                    v_measure 0.3340                             Rata-rata harmonik antara homogeneity dan completeness.

## Interpretasi Komparatif

Berikut ringkasan hubungan antara tema manual dan topik BERTopic:

                 manual_selective_theme_clean  dominant_bertopic_topic_id  dominant_topic_count  theme_document_count  theme_concentration                         dominant_bertopic_topic_name                                     auto_topic_label alignment_level                                                                                                                                                                                                                                                                                                  interpretation_note
      Pembangunan manusia dan keadilan sosial                           6                     4                    24               0.1667                         6_anak_orang tuamu_tuamu_son               anak / orang tuamu / tuamu / son / kau           Lemah                                    Tema manual 'Pembangunan manusia dan keadilan sosial' paling sering dipetakan ke BERTopic Topic 6 dengan 4 dari 24 chunk. Tingkat alignment dikategorikan lemah (theme concentration=0.1667). Keyword topik dominan: anak, orang tuamu, tuamu, son, kau, ya, anak anak, dukungan.
          Kedaulatan dan kemandirian nasional                           0                     8                    22               0.3636                       0_bupati_hadir_menteri_hormati       bupati / hadir / menteri / hormati / wali kota           Lemah                                Tema manual 'Kedaulatan dan kemandirian nasional' paling sering dipetakan ke BERTopic Topic 0 dengan 8 dari 22 chunk. Tingkat alignment dikategorikan lemah (theme concentration=0.3636). Keyword topik dominan: bupati, hadir, menteri, hormati, wali kota, wali, saudari, gubernur.
   Diplomasi, perdamaian, dan keadilan global                           7                     4                    12               0.3333                7_united nations_nations_united_peace      united nations / nations / united / peace / all           Lemah                          Tema manual 'Diplomasi, perdamaian, dan keadilan global' paling sering dipetakan ke BERTopic Topic 7 dengan 4 dari 12 chunk. Tingkat alignment dikategorikan lemah (theme concentration=0.3333). Keyword topik dominan: united nations, nations, united, peace, all, together, secure, may.
    Reformasi tata kelola dan penegakan hukum                           1                     2                     6               0.3333            1_kampus_stability_growth_peace stability kampus / stability / growth / peace stability / over           Lemah                         Tema manual 'Reformasi tata kelola dan penegakan hukum' paling sering dipetakan ke BERTopic Topic 1 dengan 2 dari 6 chunk. Tingkat alignment dikategorikan lemah (theme concentration=0.3333). Keyword topik dominan: kampus, stability, growth, peace stability, over, always, economy, it.
Transformasi ekonomi dan pembangunan nasional                           1                     1                     5               0.2000            1_kampus_stability_growth_peace stability kampus / stability / growth / peace stability / over           Lemah                        Tema manual 'Transformasi ekonomi dan pembangunan nasional' paling sering dipetakan ke BERTopic Topic 1 dengan 1 dari 5 chunk. Tingkat alignment dikategorikan lemah (theme concentration=0.2). Keyword topik dominan: kampus, stability, growth, peace stability, over, always, economy, it.
     Keberlanjutan lingkungan dan sumber daya                          -1                     1                     2               0.5000 -1_melindungi_ancaman_melindungi ancaman_pertumbuhan                           Outlier / tidak terklaster          Sedang Tema manual 'Keberlanjutan lingkungan dan sumber daya' paling sering dipetakan ke BERTopic Topic -1 dengan 1 dari 2 chunk. Tingkat alignment dikategorikan sedang (theme concentration=0.5). Keyword topik dominan: melindungi, ancaman, melindungi ancaman, pertumbuhan, merdeka, who save, berani melihat, tujuan.

## Kesimpulan Sementara

Hasil Manual Coding memberikan interpretasi tematik berbasis pembacaan peneliti, sedangkan BERTopic memberikan pengelompokan topik berbasis pola semantik dalam teks. Perbedaan antara keduanya wajar terjadi karena Manual Coding berfokus pada makna konseptual, sementara BERTopic berfokus pada kedekatan representasi embedding dan distribusi kata kunci.

Secara umum, kombinasi kedua pendekatan memberikan analisis yang lebih kuat. Manual Coding membantu menjelaskan konteks substantif, sedangkan BERTopic membantu menemukan pola topik secara komputasional dan memberi pembanding terhadap hasil interpretasi manual.
