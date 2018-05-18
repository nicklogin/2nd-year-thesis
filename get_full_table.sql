CREATE TABLE IF NOT EXISTS bigrams_with_freqs
AS SELECT bigrams.id,bigrams.bigram,bigrams.frequency,
bigrams.id_wordform1,bigrams.id_wordform2,wordforms.frequency,wordforms.lemma_id
FROM bigrams JOIN wordforms ON
bigrams.id_wordform1 = wordforms.id;

CREATE TABLE IF NOT EXISTS bigrams_with_freqs1
AS SELECT bigrams_with_freqs.id,bigrams_with_freqs.bigram,
bigrams_with_freqs.frequency,
bigrams_with_freqs."frequency:1",bigrams_with_freqs.id_wordform1,
bigrams_with_freqs.id_wordform2,lemmas.pos FROM bigrams_with_freqs JOIN
lemmas ON bigrams_with_freqs.lemma_id = lemmas.id;

CREATE TABLE IF NOT EXISTS bigrams_with_freqs2
AS SELECT bigrams_with_freqs1.id,bigrams_with_freqs1.bigram,
bigrams_with_freqs1.frequency,bigrams_with_freqs1."frequency:1",
bigrams_with_freqs1.id_wordform1,bigrams_with_freqs1.id_wordform2,
bigrams_with_freqs1.pos,
wordforms.frequency,wordforms.lemma_id FROM
bigrams_with_freqs1 JOIN wordforms ON
bigrams_with_freqs1.id_wordform2 = wordforms.id;

CREATE TABLE IF NOT EXISTS bigrams_with_freqs3
AS SELECT bigrams_with_freqs2.id,bigrams_with_freqs2.bigram,
bigrams_with_freqs2.frequency,bigrams_with_freqs2."frequency:1",
bigrams_with_freqs2."frequency:2",
bigrams_with_freqs2.id_wordform1,bigrams_with_freqs2.id_wordform2,
bigrams_with_freqs2.pos,lemmas.pos FROM bigrams_with_freqs2 JOIN
lemmas ON bigrams_with_freqs2.lemma_id = lemmas.id;

DROP TABLE IF EXISTS bigrams_with_freqs;

DROP TABLE IF EXISTS bigrams_with_freqs1;

DROP TABLE IF EXISTS bigrams_with_freqs2;

CREATE TABLE IF NOT EXISTS lemma_bigrams_with_freqs
AS SELECT lemma_bigrams.id,lemma_bigrams.lemma_bigram,lemma_bigrams.frequency,
lemma_bigrams.id_lemma1,lemma_bigrams.id_lemma2,lemmas.frequency,lemmas.pos
FROM lemma_bigrams JOIN lemmas ON
lemma_bigrams.id_lemma1 = lemmas.id;

CREATE TABLE IF NOT EXISTS lemma_bigrams_with_freqs1
AS SELECT lemma_bigrams_with_freqs.id,lemma_bigrams_with_freqs.lemma_bigram,
lemma_bigrams_with_freqs.frequency,lemma_bigrams_with_freqs."frequency:1",
lemma_bigrams_with_freqs.id_lemma1,lemma_bigrams_with_freqs.id_lemma2,
lemma_bigrams_with_freqs.pos,
lemmas.frequency,lemmas.pos FROM
lemma_bigrams_with_freqs JOIN lemmas ON
lemma_bigrams_with_freqs.id_lemma2 = lemmas.id;

DROP TABLE IF EXISTS lemma_bigrams_with_freqs;