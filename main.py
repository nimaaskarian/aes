#!/bin/python3
from modules.dataprocessor import DataProcessorSentences, DataProcessor
from modules.cluster import ClusterDBSCAN, ClusterKmeans
from modules.argparser import parser

if __name__ == "__main__":
    args = parser.parse_args()

    if args.sentences:
        dp = DataProcessorSentences()
    else:
        dp = DataProcessor()

    if args.doc_count:
        dp.set_paths([f"data/document_{i}.txt" for i in range(args.doc_count)])

    if args.files:
        dp.set_paths(args.files)
    dp.generate()
    
    if args.query:
        similarities = dp.calculate_query_similarities(args.query)
        doc_index = dp.find_n_most_similar(similarities, 1)
        if args.sentences:
            sp = dp.sentence_index_to_position(doc_index)
            doc_index = sp.doc_index
        print(dp.document_at(doc_index))

        if args.sentences:
            print("This is the sentence in question:")
            print(dp.sentence_at(sp))

    else:
        # clusters = ClusterKmeans(dp.calculate_similarities(), args.clusters).clusters
        clusters = ClusterDBSCAN(dp.calculate_similarities(), eps=0.7).clusters
        print(clusters)
