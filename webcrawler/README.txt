Data Structures Used:
Queue for URL frontier
Hash tables for indexing Documents and Urls
Bots and CNC type architecture
*md5 for detecting duplicates

------------------------------------------
Output Directory Structure:
------------------------------------------
collected_data/
    resolved_url_map.json
    url_id_map.json
    doc_hash_id_map.json

    "NAMED_OUTPUT_DIRECTORY"/
        log.txt
        response_summaries/
            response_summary_0.json
            ...
        documents/
            document_frequency_dict_0.json
            ...
output/
    output/document_term_frequency_matrix.csv
    output/output_log.txt
------------------------------------------
\Output Directory Structure
------------------------------------------
