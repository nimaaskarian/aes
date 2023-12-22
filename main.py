#!/bin/python3
from modules.dataprocessor import DataProcessorSentences, DataProcessorDocs
from modules.cluster import ClusterKmeans
from modules.argparser import parser

if __name__ == "__main__":
    args = parser.parse_args()

    if args.type == "SENT":
        dp = DataProcessorSentences()
    else:
        dp = DataProcessorDocs()

    if args.doc_count:
        dp.set_paths([f"data/document_{i}.txt" for i in range(args.doc_count)])

    if args.files:
        dp.set_paths(args.files)
    dp.generate_tfidf()
    
    if args.query:
        similarities = dp.calculate_query_similarities(args.query)
        for i in dp.find_n_most_similar(similarities, 1):
            doc_index = i
            if args.type == "SENT":
                sp = dp.sentence_index_to_position(i)
                doc_index = sp.doc_index
                print(doc_index, sp.sentence_index)
            print(dp.document_at(doc_index))

            if args.type == "SENT":
                print("This is the sentence in question:")
                print(dp.sentence_at(sp))

    else:
        clusters = ClusterKmeans(dp.calculate_similarities(), args.clusters).clusters
        print(clusters)
